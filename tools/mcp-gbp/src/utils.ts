// Utilitaires OAuth amont (Google). Adapté du modèle cloudflare/ai
// demos/remote-mcp-google-oauth/src/utils.ts (licence MIT) : ajout de l'accès
// hors ligne (refresh token) indispensable pour interroger l'API GBP durablement.

/** Périmètre Google demandé : gestion de la fiche + identité de l'utilisateur. */
export const GOOGLE_SCOPES = [
	"openid",
	"email",
	"profile",
	"https://www.googleapis.com/auth/business.manage",
].join(" ");

/**
 * Construit l'URL d'autorisation Google.
 * `access_type=offline` + `prompt=consent` garantissent qu'un refresh token
 * est renvoyé à chaque autorisation (sinon Google ne le fournit qu'une fois).
 */
export function getUpstreamAuthorizeUrl({
	upstreamUrl,
	clientId,
	scope,
	redirectUri,
	state,
}: {
	upstreamUrl: string;
	clientId: string;
	scope: string;
	redirectUri: string;
	state?: string;
}) {
	const upstream = new URL(upstreamUrl);
	upstream.searchParams.set("client_id", clientId);
	upstream.searchParams.set("redirect_uri", redirectUri);
	upstream.searchParams.set("scope", scope);
	upstream.searchParams.set("response_type", "code");
	upstream.searchParams.set("access_type", "offline");
	upstream.searchParams.set("prompt", "consent");
	upstream.searchParams.set("include_granted_scopes", "true");
	if (state) upstream.searchParams.set("state", state);
	return upstream.href;
}

export interface UpstreamTokens {
	accessToken: string;
	refreshToken: string;
	expiresIn: number;
}

/**
 * Échange le code d'autorisation contre les jetons Google.
 * Retourne [jetons, null] ou [null, Response d'erreur].
 */
export async function fetchUpstreamAuthToken({
	clientId,
	clientSecret,
	code,
	redirectUri,
	upstreamUrl,
}: {
	code: string | undefined;
	upstreamUrl: string;
	clientSecret: string;
	redirectUri: string;
	clientId: string;
}): Promise<[UpstreamTokens, null] | [null, Response]> {
	if (!code) {
		return [null, new Response("Code d'autorisation manquant", { status: 400 })];
	}

	const resp = await fetch(upstreamUrl, {
		body: new URLSearchParams({
			client_id: clientId,
			client_secret: clientSecret,
			code,
			grant_type: "authorization_code",
			redirect_uri: redirectUri,
		}).toString(),
		headers: { "Content-Type": "application/x-www-form-urlencoded" },
		method: "POST",
	});
	if (!resp.ok) {
		console.log(await resp.text());
		return [null, new Response("Échec de l'échange du code contre un jeton Google", { status: 500 })];
	}

	const body = (await resp.json()) as {
		access_token?: string;
		refresh_token?: string;
		expires_in?: number;
	};
	if (!body.access_token) {
		return [null, new Response("Jeton d'accès Google absent de la réponse", { status: 400 })];
	}
	if (!body.refresh_token) {
		return [
			null,
			new Response(
				"Google n'a pas renvoyé de refresh token. Retirez l'accès de l'application dans " +
					"https://myaccount.google.com/permissions puis recommencez l'autorisation.",
				{ status: 400 },
			),
		];
	}
	return [
		{
			accessToken: body.access_token,
			refreshToken: body.refresh_token,
			expiresIn: body.expires_in ?? 3600,
		},
		null,
	];
}

/**
 * Contexte issu de l'autorisation, chiffré dans le jeton remis au client MCP
 * (claude.ai) et exposé au serveur via `this.props`.
 */
export type Props = {
	name: string;
	email: string;
	googleUserId: string;
	/** Refresh token Google : permet d'obtenir un jeton d'accès à la demande. */
	refreshToken: string;
};
