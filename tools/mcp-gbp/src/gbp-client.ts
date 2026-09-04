// Client HTTP des API Google Business Profile.
// Gère le rafraîchissement du jeton d'accès à partir du refresh token, la
// normalisation des noms de ressources et la traduction des erreurs Google en
// messages actionnables (en français).

export const API = {
	accounts: "https://mybusinessaccountmanagement.googleapis.com/v1",
	info: "https://mybusinessbusinessinformation.googleapis.com/v1",
	perf: "https://businessprofileperformance.googleapis.com/v1",
	qanda: "https://mybusinessqanda.googleapis.com/v1",
	/** API historique (v4) : avis, posts, médias. */
	v4: "https://mybusiness.googleapis.com/v4",
} as const;

export class GbpApiError extends Error {
	constructor(
		message: string,
		public status: number,
		public details?: unknown,
	) {
		super(message);
		this.name = "GbpApiError";
	}
}

type Query = Record<string, string | number | boolean | string[] | undefined>;

export class GbpClient {
	private accessToken: string | null = null;
	/** Horodatage (ms) d'expiration du jeton d'accès en cache. */
	private expiresAt = 0;

	constructor(
		private readonly env: Pick<Env, "GOOGLE_CLIENT_ID" | "GOOGLE_CLIENT_SECRET">,
		private readonly getRefreshToken: () => string | undefined,
	) {}

	// ---------------------------------------------------------------- jetons

	private async token(force = false): Promise<string> {
		if (!force && this.accessToken && Date.now() < this.expiresAt - 60_000) {
			return this.accessToken;
		}
		const refreshToken = this.getRefreshToken();
		if (!refreshToken) {
			throw new GbpApiError(
				"Aucun refresh token Google dans la session : reconnectez le connecteur dans claude.ai.",
				401,
			);
		}
		const resp = await fetch("https://oauth2.googleapis.com/token", {
			method: "POST",
			headers: { "Content-Type": "application/x-www-form-urlencoded" },
			body: new URLSearchParams({
				client_id: this.env.GOOGLE_CLIENT_ID,
				client_secret: this.env.GOOGLE_CLIENT_SECRET,
				grant_type: "refresh_token",
				refresh_token: refreshToken,
			}).toString(),
		});
		if (!resp.ok) {
			const text = await resp.text();
			throw new GbpApiError(
				"Google refuse de renouveler le jeton (refresh token expiré ou révoqué). " +
					"Reconnectez le connecteur dans claude.ai. Détail : " +
					text.slice(0, 300),
				401,
			);
		}
		const body = (await resp.json()) as { access_token: string; expires_in?: number };
		this.accessToken = body.access_token;
		this.expiresAt = Date.now() + (body.expires_in ?? 3600) * 1000;
		return this.accessToken;
	}

	// -------------------------------------------------------------- requêtes

	private buildUrl(base: string, path: string, query?: Query): string {
		const url = new URL(`${base}/${path.replace(/^\//, "")}`);
		for (const [key, value] of Object.entries(query ?? {})) {
			if (value === undefined) continue;
			if (Array.isArray(value)) {
				for (const v of value) url.searchParams.append(key, v);
			} else {
				url.searchParams.set(key, String(value));
			}
		}
		return url.href;
	}

	async request<T>(
		method: "GET" | "POST" | "PUT" | "PATCH" | "DELETE",
		base: string,
		path: string,
		options: { query?: Query; body?: unknown } = {},
	): Promise<T> {
		const url = this.buildUrl(base, path, options.query);
		const doFetch = async (token: string) =>
			fetch(url, {
				method,
				headers: {
					Authorization: `Bearer ${token}`,
					Accept: "application/json",
					...(options.body !== undefined ? { "Content-Type": "application/json" } : {}),
				},
				body: options.body !== undefined ? JSON.stringify(options.body) : undefined,
			});

		let resp = await doFetch(await this.token());
		if (resp.status === 401) {
			// Jeton périmé côté Google : on force un renouvellement puis on rejoue une fois.
			resp = await doFetch(await this.token(true));
		}
		if (!resp.ok) {
			throw await this.toError(resp, url);
		}
		if (resp.status === 204) return {} as T;
		const text = await resp.text();
		return (text ? JSON.parse(text) : {}) as T;
	}

	get<T>(base: string, path: string, query?: Query) {
		return this.request<T>("GET", base, path, { query });
	}

	/** Suit `nextPageToken` jusqu'à `maxPages` pages et concatène `key`. */
	async listAll<T>(
		base: string,
		path: string,
		key: string,
		query: Query = {},
		maxPages = 10,
	): Promise<{ items: T[]; pages: number; truncated: boolean }> {
		const items: T[] = [];
		let pageToken: string | undefined;
		let pages = 0;
		do {
			const page = await this.get<Record<string, unknown>>(base, path, { ...query, pageToken });
			items.push(...((page[key] as T[] | undefined) ?? []));
			pageToken = page.nextPageToken as string | undefined;
			pages++;
		} while (pageToken && pages < maxPages);
		return { items, pages, truncated: Boolean(pageToken) };
	}

	// ---------------------------------------------------------------- erreurs

	private async toError(resp: Response, url: string): Promise<GbpApiError> {
		let details: unknown;
		let googleMessage = "";
		try {
			details = await resp.json();
			googleMessage = (details as { error?: { message?: string } })?.error?.message ?? "";
		} catch {
			details = undefined;
		}
		const host = new URL(url).host;
		const lower = googleMessage.toLowerCase();
		let hint: string;
		switch (resp.status) {
			case 400:
				hint = "Requête refusée par Google (paramètre ou nom de ressource invalide).";
				break;
			case 401:
				hint = "Jeton Google invalide : reconnectez le connecteur dans claude.ai.";
				break;
			case 403:
				if (lower.includes("quota") || lower.includes("rate")) {
					hint =
						"Quota à 0 : le projet Google Cloud n'a probablement pas encore reçu l'accès aux API " +
						"Business Profile (formulaire de demande d'accès, voir README) — ou la limite par minute est atteinte.";
				} else if (lower.includes("not been used") || lower.includes("disabled") || lower.includes("enable")) {
					hint = `API ${host} non activée dans le projet Google Cloud : l'activer dans la console (voir README).`;
				} else {
					hint =
						"Accès refusé : le compte Google connecté n'est pas propriétaire ou gestionnaire de cette fiche, " +
						"ou le périmètre business.manage n'a pas été accordé.";
				}
				break;
			case 404:
				hint = "Ressource introuvable : vérifiez le nom exact (accounts/…, locations/…, reviews/…).";
				break;
			case 429:
				hint = "Limite de requêtes Google atteinte : patienter une minute puis réessayer.";
				break;
			default:
				hint = `Erreur Google ${resp.status}.`;
		}
		return new GbpApiError(
			`${hint}${googleMessage ? ` Message Google : ${googleMessage}` : ""}`,
			resp.status,
			details,
		);
	}
}

// -------------------------------------------------- noms de ressources

/** Extrait l'identifiant numérique d'un nom `locations/123` ou `accounts/4/locations/123`. */
export function locationId(name: string): string {
	const m = name.trim().match(/locations\/(\d+)/);
	if (!m) {
		throw new GbpApiError(
			`Nom d'établissement invalide « ${name} » : attendu locations/{id} ou accounts/{id}/locations/{id}.`,
			400,
		);
	}
	return m[1];
}

/** Extrait l'identifiant numérique d'un nom `accounts/123` ou `accounts/123/locations/…`. */
export function accountId(name: string | undefined): string | undefined {
	const m = name?.trim().match(/accounts\/(\d+)/);
	return m?.[1];
}

/**
 * Chemin v4 `accounts/{a}/locations/{l}` requis par les API avis / posts / médias.
 * `location` peut déjà contenir le compte ; sinon `account` est obligatoire.
 */
export function v4LocationPath(location: string, account?: string): string {
	const acc = accountId(location) ?? accountId(account);
	if (!acc) {
		throw new GbpApiError(
			"Le compte est requis pour cette API : passez `location` sous la forme accounts/{id}/locations/{id} " +
				"ou renseignez `account` (voir gbp_list_locations, champ v4Path).",
			400,
		);
	}
	return `accounts/${acc}/locations/${locationId(location)}`;
}

/** Convertit « AAAA-MM-JJ » en objet Date Google. */
export function toGoogleDate(iso: string): { year: number; month: number; day: number } {
	const m = iso.trim().match(/^(\d{4})-(\d{2})-(\d{2})$/);
	if (!m) throw new GbpApiError(`Date invalide « ${iso} » : format attendu AAAA-MM-JJ.`, 400);
	return { year: Number(m[1]), month: Number(m[2]), day: Number(m[3]) };
}

/** Convertit « AAAA-MM » en objet mois Google. */
export function toGoogleMonth(iso: string): { year: number; month: number } {
	const m = iso.trim().match(/^(\d{4})-(\d{2})$/);
	if (!m) throw new GbpApiError(`Mois invalide « ${iso} » : format attendu AAAA-MM.`, 400);
	return { year: Number(m[1]), month: Number(m[2]) };
}
