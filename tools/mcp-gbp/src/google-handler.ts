// Flux OAuth Google (autorisation, consentement, callback). Adapté du modèle
// cloudflare/ai demos/remote-mcp-google-oauth/src/google-handler.ts (MIT) :
// périmètre business.manage, refresh token conservé dans les props, liste
// d'e-mails autorisés (ALLOWED_EMAILS).

import type { AuthRequest, OAuthHelpers } from "@cloudflare/workers-oauth-provider";
import { Hono } from "hono";
import { fetchUpstreamAuthToken, getUpstreamAuthorizeUrl, GOOGLE_SCOPES, type Props } from "./utils";
import {
	addApprovedClient,
	bindStateToSession,
	createOAuthState,
	generateCSRFProtection,
	isClientApproved,
	OAuthError,
	renderApprovalDialog,
	validateCSRFToken,
	validateOAuthState,
} from "./workers-oauth-utils";

const app = new Hono<{ Bindings: Env & { OAUTH_PROVIDER: OAuthHelpers } }>();

const SERVER_INFO = {
	name: "RUSHITI Rénovation — Google Business Profile",
	description:
		"Connecteur privé : Claude lit la fiche Google Business de RUSHITI Rénovation " +
		"(avis, statistiques, posts, questions) et ne publie qu'après validation.",
};

app.get("/", (c) =>
	c.text(
		"rushiti-mcp-gbp — serveur MCP privé de RUSHITI Rénovation.\n" +
			"Point d'entrée MCP : /mcp (OAuth requis).",
	),
);

app.get("/authorize", async (c) => {
	const oauthReqInfo = await c.env.OAUTH_PROVIDER.parseAuthRequest(c.req.raw);
	const { clientId } = oauthReqInfo;
	if (!clientId) {
		return c.text("Requête invalide", 400);
	}

	// Client déjà approuvé : on saute l'écran de consentement mais on garde
	// la protection d'état liée à la session.
	if (await isClientApproved(c.req.raw, clientId, c.env.COOKIE_ENCRYPTION_KEY)) {
		const { stateToken } = await createOAuthState(oauthReqInfo, c.env.OAUTH_KV);
		const { setCookie: sessionBindingCookie } = await bindStateToSession(stateToken);
		return redirectToGoogle(c.req.raw, c.env, stateToken, {
			"Set-Cookie": sessionBindingCookie,
		});
	}

	const { token: csrfToken, setCookie } = generateCSRFProtection();

	return renderApprovalDialog(c.req.raw, {
		client: await c.env.OAUTH_PROVIDER.lookupClient(clientId),
		csrfToken,
		server: SERVER_INFO,
		setCookie,
		state: { oauthReqInfo },
	});
});

app.post("/authorize", async (c) => {
	try {
		const formData = await c.req.raw.formData();
		validateCSRFToken(formData, c.req.raw);

		const encodedState = formData.get("state");
		if (!encodedState || typeof encodedState !== "string") {
			return c.text("État manquant dans le formulaire", 400);
		}

		let state: { oauthReqInfo?: AuthRequest };
		try {
			state = JSON.parse(atob(encodedState));
		} catch (_e) {
			return c.text("État invalide", 400);
		}

		if (!state.oauthReqInfo || !state.oauthReqInfo.clientId) {
			return c.text("Requête invalide", 400);
		}

		const approvedClientCookie = await addApprovedClient(
			c.req.raw,
			state.oauthReqInfo.clientId,
			c.env.COOKIE_ENCRYPTION_KEY,
		);

		const { stateToken } = await createOAuthState(state.oauthReqInfo, c.env.OAUTH_KV);
		const { setCookie: sessionBindingCookie } = await bindStateToSession(stateToken);

		const headers = new Headers();
		headers.append("Set-Cookie", approvedClientCookie);
		headers.append("Set-Cookie", sessionBindingCookie);

		return redirectToGoogle(c.req.raw, c.env, stateToken, Object.fromEntries(headers));
	} catch (error: any) {
		console.error("POST /authorize error:", error);
		if (error instanceof OAuthError) {
			return error.toResponse();
		}
		return c.text(`Erreur interne : ${error.message}`, 500);
	}
});

async function redirectToGoogle(
	request: Request,
	env: Env,
	stateToken: string,
	headers: Record<string, string> = {},
) {
	return new Response(null, {
		headers: {
			...headers,
			location: getUpstreamAuthorizeUrl({
				clientId: env.GOOGLE_CLIENT_ID,
				redirectUri: new URL("/callback", request.url).href,
				scope: GOOGLE_SCOPES,
				state: stateToken,
				upstreamUrl: "https://accounts.google.com/o/oauth2/v2/auth",
			}),
		},
		status: 302,
	});
}

/** Vérifie la liste blanche ALLOWED_EMAILS (vide = tout le monde). */
function isEmailAllowed(env: Env, email: string): boolean {
	const list = (env.ALLOWED_EMAILS ?? "")
		.split(",")
		.map((e) => e.trim().toLowerCase())
		.filter(Boolean);
	return list.length === 0 || list.includes(email.toLowerCase());
}

/**
 * Callback Google : vérifie l'état (KV + cookie de session), échange le code,
 * lit l'identité, puis remet au client MCP un jeton dont les props contiennent
 * le refresh token Google.
 */
app.get("/callback", async (c) => {
	let oauthReqInfo: AuthRequest;
	let clearSessionCookie: string;

	try {
		const result = await validateOAuthState(c.req.raw, c.env.OAUTH_KV);
		oauthReqInfo = result.oauthReqInfo;
		clearSessionCookie = result.clearCookie;
	} catch (error: any) {
		if (error instanceof OAuthError) {
			return error.toResponse();
		}
		return c.text("Erreur interne", 500);
	}

	if (!oauthReqInfo.clientId) {
		return c.text("Données OAuth invalides", 400);
	}

	const googleError = c.req.query("error");
	if (googleError) {
		return c.text(`Autorisation Google refusée : ${googleError}`, 400);
	}

	const [tokens, googleErrResponse] = await fetchUpstreamAuthToken({
		clientId: c.env.GOOGLE_CLIENT_ID,
		clientSecret: c.env.GOOGLE_CLIENT_SECRET,
		code: c.req.query("code"),
		redirectUri: new URL("/callback", c.req.url).href,
		upstreamUrl: "https://oauth2.googleapis.com/token",
	});
	if (googleErrResponse) {
		return googleErrResponse;
	}

	const userResponse = await fetch("https://www.googleapis.com/oauth2/v2/userinfo", {
		headers: { Authorization: `Bearer ${tokens.accessToken}` },
	});
	if (!userResponse.ok) {
		return c.text(`Impossible de lire l'identité Google : ${await userResponse.text()}`, 500);
	}

	const { id, name, email } = (await userResponse.json()) as {
		id: string;
		name?: string;
		email: string;
	};

	if (!isEmailAllowed(c.env, email)) {
		return c.text(
			`Le compte ${email} n'est pas autorisé sur ce connecteur (secret ALLOWED_EMAILS).`,
			403,
		);
	}

	const { redirectTo } = await c.env.OAUTH_PROVIDER.completeAuthorization({
		metadata: { label: name ?? email },
		props: {
			name: name ?? email,
			email,
			googleUserId: id,
			refreshToken: tokens.refreshToken,
		} satisfies Props,
		request: oauthReqInfo,
		scope: oauthReqInfo.scope,
		userId: id,
	});

	const headers = new Headers({ Location: redirectTo });
	if (clearSessionCookie) {
		headers.set("Set-Cookie", clearSessionCookie);
	}
	return new Response(null, { status: 302, headers });
});

export { app as GoogleHandler };
