// Outils MCP exposés à Claude. Convention : préfixe `gbp_`, descriptions en
// français, lecture seule par défaut. Les trois outils qui publient quelque
// chose sur la fiche (réponse à un avis, post, réponse à une question) exigent
// `valide_par_isuf: true` : Claude ne doit les appeler qu'après validation
// explicite du texte exact par Isuf ou Yll.

import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import type { CallToolResult } from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";
import {
	API,
	GbpApiError,
	type GbpClient,
	locationId,
	toGoogleDate,
	toGoogleMonth,
	v4LocationPath,
} from "./gbp-client";

// ------------------------------------------------------------- helpers

function ok(data: unknown): CallToolResult {
	return {
		content: [{ type: "text", text: JSON.stringify(data, null, 2) }],
		structuredContent: typeof data === "object" && data !== null ? (data as Record<string, unknown>) : { value: data },
	};
}

function fail(message: string): CallToolResult {
	return { content: [{ type: "text", text: message }], isError: true };
}

/** Enrobe un outil : erreurs Google → message actionnable, jamais d'exception brute. */
function guard<A>(fn: (args: A) => Promise<CallToolResult>) {
	return async (args: A): Promise<CallToolResult> => {
		try {
			return await fn(args);
		} catch (error) {
			if (error instanceof GbpApiError) return fail(error.message);
			return fail(`Erreur inattendue : ${error instanceof Error ? error.message : String(error)}`);
		}
	};
}

const READ_ONLY = { readOnlyHint: true, destructiveHint: false, idempotentHint: true, openWorldHint: true };
const WRITE = { readOnlyHint: false, destructiveHint: false, idempotentHint: false, openWorldHint: true };

const LOCATION_READ_MASK =
	"name,title,storeCode,languageCode,categories,storefrontAddress,phoneNumbers,websiteUri," +
	"regularHours,specialHours,moreHours,serviceArea,labels,latlng,openInfo,metadata,profile,serviceItems";

const locationParam = z
	.string()
	.describe("Nom de l'établissement : locations/{id} ou accounts/{id}/locations/{id} (champ `name` ou `v4Path` de gbp_list_locations).");
const accountParam = z
	.string()
	.optional()
	.describe("Compte accounts/{id}. Requis pour les API avis/posts/médias si `location` ne contient pas déjà le compte.");
const pageSize = (max: number, def: number) =>
	z.number().int().min(1).max(max).default(def).describe(`Taille de page (1–${max}).`);
const pageToken = z.string().optional().describe("Jeton de page renvoyé par l'appel précédent (nextPageToken).");
const valideParIsuf = z
	.boolean()
	.describe(
		"Doit valoir true. Confirme qu'Isuf ou Yll a validé mot pour mot le texte à publier sur la fiche Google. " +
			"Sans validation explicite dans la conversation, ne pas appeler cet outil : proposer un brouillon.",
	);

const DAILY_METRICS = [
	"BUSINESS_IMPRESSIONS_DESKTOP_MAPS",
	"BUSINESS_IMPRESSIONS_DESKTOP_SEARCH",
	"BUSINESS_IMPRESSIONS_MOBILE_MAPS",
	"BUSINESS_IMPRESSIONS_MOBILE_SEARCH",
	"BUSINESS_CONVERSATIONS",
	"BUSINESS_DIRECTION_REQUESTS",
	"CALL_CLICKS",
	"WEBSITE_CLICKS",
	"BUSINESS_BOOKINGS",
] as const;

// ------------------------------------------------------- types Google

interface Review {
	name: string;
	reviewId: string;
	reviewer?: { displayName?: string; isAnonymous?: boolean };
	starRating?: string;
	comment?: string;
	createTime?: string;
	updateTime?: string;
	reviewReply?: { comment?: string; updateTime?: string };
}

interface LocalPost {
	name: string;
	languageCode?: string;
	summary?: string;
	callToAction?: { actionType?: string; url?: string };
	state?: string;
	topicType?: string;
	createTime?: string;
	updateTime?: string;
	searchUrl?: string;
	media?: Array<{ mediaFormat?: string; sourceUrl?: string; googleUrl?: string }>;
}

interface MediaItem {
	name: string;
	mediaFormat?: string;
	locationAssociation?: { category?: string };
	googleUrl?: string;
	createTime?: string;
	description?: string;
	insights?: { viewCount?: string };
}

interface Question {
	name: string;
	author?: { displayName?: string; type?: string };
	upvoteCount?: number;
	text?: string;
	createTime?: string;
	updateTime?: string;
	totalAnswerCount?: number;
	topAnswers?: Array<{ name: string; author?: { displayName?: string; type?: string }; text?: string; updateTime?: string }>;
}

const STARS: Record<string, number> = { ONE: 1, TWO: 2, THREE: 3, FOUR: 4, FIVE: 5 };

function compactReview(r: Review) {
	return {
		name: r.name,
		reviewId: r.reviewId,
		auteur: r.reviewer?.isAnonymous ? "(anonyme)" : (r.reviewer?.displayName ?? ""),
		note: STARS[r.starRating ?? ""] ?? null,
		commentaire: r.comment ?? "",
		creeLe: r.createTime,
		modifieLe: r.updateTime,
		reponse: r.reviewReply ? { texte: r.reviewReply.comment ?? "", modifieLe: r.reviewReply.updateTime } : null,
	};
}

// --------------------------------------------------------- registre

export function registerTools(server: McpServer, client: GbpClient) {
	// ---------------------------------------------------- comptes / fiches

	server.registerTool(
		"gbp_list_accounts",
		{
			title: "Comptes Google Business accessibles",
			description:
				"Liste les comptes Business Profile (personnel, groupe d'établissements, organisation) auxquels " +
				"l'utilisateur connecté a accès. Point de départ : fournit accounts/{id} pour gbp_list_locations.",
			inputSchema: {},
			annotations: READ_ONLY,
		},
		guard(async () => {
			const { items } = await client.listAll<Record<string, unknown>>(API.accounts, "accounts", "accounts");
			return ok({
				comptes: items.map((a) => ({
					name: a.name,
					nom: a.accountName,
					type: a.type,
					role: a.role,
					verification: a.verificationState,
				})),
			});
		}),
	);

	server.registerTool(
		"gbp_list_locations",
		{
			title: "Établissements d'un compte",
			description:
				"Liste les fiches (établissements) d'un compte, ou de tous les comptes si `account` est omis. " +
				"Renvoie pour chaque fiche `name` (locations/{id}) et `v4Path` (accounts/{id}/locations/{id}) à réutiliser " +
				"dans les autres outils, plus titre, adresse, téléphone, site, catégorie principale et état de vérification.",
			inputSchema: {
				account: z.string().optional().describe("accounts/{id} ; omis = parcourir tous les comptes."),
			},
			annotations: READ_ONLY,
		},
		guard(async ({ account }) => {
			let accounts: string[];
			if (account) {
				accounts = [account];
			} else {
				const { items } = await client.listAll<{ name: string }>(API.accounts, "accounts", "accounts");
				accounts = items.map((a) => a.name);
			}
			const readMask =
				"name,title,storeCode,categories,storefrontAddress,phoneNumbers,websiteUri,metadata,openInfo";
			const fiches: unknown[] = [];
			for (const acc of accounts) {
				const { items } = await client.listAll<Record<string, any>>(
					API.info,
					`${acc}/locations`,
					"locations",
					{ readMask, pageSize: 100 },
				);
				for (const l of items) {
					fiches.push({
						name: l.name,
						v4Path: `${acc}/${l.name}`,
						compte: acc,
						titre: l.title,
						codeMagasin: l.storeCode,
						categoriePrincipale: l.categories?.primaryCategory?.displayName,
						adresse: l.storefrontAddress
							? [
									...(l.storefrontAddress.addressLines ?? []),
									l.storefrontAddress.postalCode,
									l.storefrontAddress.locality,
								]
									.filter(Boolean)
									.join(", ")
							: null,
						telephone: l.phoneNumbers?.primaryPhone,
						site: l.websiteUri,
						statut: l.openInfo?.status,
						placeId: l.metadata?.placeId,
						urlMaps: l.metadata?.mapsUri,
						urlNouvelAvis: l.metadata?.newReviewUri,
						verifieeEtActive: l.metadata?.hasVoiceOfMerchant,
						modificationsEnAttente: l.metadata?.hasPendingEdits,
						miseAJourGoogleEnAttente: l.metadata?.hasGoogleUpdated,
					});
				}
			}
			return ok({ nombre: fiches.length, fiches });
		}),
	);

	server.registerTool(
		"gbp_get_location",
		{
			title: "Détail complet d'une fiche",
			description:
				"Renvoie la fiche complète : titre, catégories, adresse, téléphones, site, description (profile.description), " +
				"horaires réguliers et exceptionnels, zone desservie, services déclarés, attributs de métadonnées. " +
				"Utile pour contrôler le NAP, la description officielle et les horaires face au site.",
			inputSchema: {
				location: locationParam,
				readMask: z
					.string()
					.optional()
					.describe("Champs à lire, séparés par des virgules (défaut : tous les champs utiles)."),
			},
			annotations: READ_ONLY,
		},
		guard(async ({ location, readMask }) => {
			const data = await client.get<Record<string, unknown>>(API.info, `locations/${locationId(location)}`, {
				readMask: readMask ?? LOCATION_READ_MASK,
			});
			return ok(data);
		}),
	);

	server.registerTool(
		"gbp_get_google_updates",
		{
			title: "Modifications suggérées par Google",
			description:
				"Renvoie la version de la fiche telle que Google l'a modifiée ou propose de la modifier (mises à jour " +
				"« suggérées par Google » et diffMask des champs concernés). Permet de repérer un changement d'horaires, " +
				"de catégorie ou de site que Google a appliqué sans validation.",
			inputSchema: { location: locationParam },
			annotations: READ_ONLY,
		},
		guard(async ({ location }) => {
			const data = await client.get<Record<string, unknown>>(
				API.info,
				`locations/${locationId(location)}:getGoogleUpdated`,
				{ readMask: LOCATION_READ_MASK },
			);
			return ok(data);
		}),
	);

	server.registerTool(
		"gbp_update_location",
		{
			title: "Modifier des champs de la fiche (après validation)",
			description:
				"Met à jour des champs de la fiche (ex. profile.description, websiteUri, regularHours, phoneNumbers). " +
				"`updateMask` liste les champs modifiés ; `fields` contient l'objet Location partiel correspondant. " +
				"Avec `validateOnly: true`, Google vérifie sans rien enregistrer : à utiliser d'abord. " +
				"Nécessite `valide_par_isuf: true`.",
			inputSchema: {
				location: locationParam,
				updateMask: z.string().describe("Champs modifiés, séparés par des virgules. Ex. : profile.description,websiteUri"),
				fields: z.record(z.string(), z.unknown()).describe("Objet Location partiel. Ex. : {\"profile\":{\"description\":\"…\"}}"),
				validateOnly: z.boolean().default(false).describe("true = simulation sans enregistrement."),
				valide_par_isuf: valideParIsuf,
			},
			annotations: { ...WRITE, idempotentHint: true },
		},
		guard(async ({ location, updateMask, fields, validateOnly, valide_par_isuf }) => {
			if (!valide_par_isuf) return fail("Refusé : la modification doit être validée par Isuf ou Yll (valide_par_isuf: true).");
			const data = await client.request<Record<string, unknown>>("PATCH", API.info, `locations/${locationId(location)}`, {
				query: { updateMask, validateOnly },
				body: fields,
			});
			return ok({ simulation: validateOnly, resultat: data });
		}),
	);

	// ------------------------------------------------------------- avis

	server.registerTool(
		"gbp_list_reviews",
		{
			title: "Avis Google de la fiche",
			description:
				"Liste les avis (note, auteur, commentaire, dates, réponse existante) avec la note moyenne et le total. " +
				"Par défaut les plus récents d'abord. Sert à repérer les avis sans réponse et à préparer des brouillons de " +
				"réponse (skill rushiti-avis-google) — jamais à publier sans validation.",
			inputSchema: {
				location: locationParam,
				account: accountParam,
				pageSize: pageSize(50, 50),
				pageToken,
				orderBy: z
					.enum(["updateTime desc", "rating", "rating desc"])
					.default("updateTime desc")
					.describe("Tri : plus récents (défaut), note croissante, note décroissante."),
				sansReponseSeulement: z.boolean().default(false).describe("true = ne renvoyer que les avis sans réponse."),
			},
			annotations: READ_ONLY,
		},
		guard(async ({ location, account, pageSize, pageToken, orderBy, sansReponseSeulement }) => {
			const path = `${v4LocationPath(location, account)}/reviews`;
			const data = await client.get<{
				reviews?: Review[];
				averageRating?: number;
				totalReviewCount?: number;
				nextPageToken?: string;
			}>(API.v4, path, { pageSize, pageToken, orderBy });
			let avis = (data.reviews ?? []).map(compactReview);
			if (sansReponseSeulement) avis = avis.filter((a) => !a.reponse);
			return ok({
				noteMoyenne: data.averageRating ?? null,
				totalAvis: data.totalReviewCount ?? null,
				nombreRenvoye: avis.length,
				nextPageToken: data.nextPageToken ?? null,
				avis,
			});
		}),
	);

	server.registerTool(
		"gbp_get_review",
		{
			title: "Un avis précis",
			description: "Renvoie un avis à partir de son nom complet accounts/{a}/locations/{l}/reviews/{id}.",
			inputSchema: {
				review: z.string().describe("Nom complet de l'avis (champ `name` de gbp_list_reviews)."),
			},
			annotations: READ_ONLY,
		},
		guard(async ({ review }) => {
			const data = await client.get<Review>(API.v4, review);
			return ok(compactReview(data));
		}),
	);

	server.registerTool(
		"gbp_reply_review",
		{
			title: "Publier une réponse à un avis (après validation)",
			description:
				"Publie (ou remplace) la réponse de l'établissement à un avis. Texte signé « L'équipe RUSHITI Rénovation », " +
				"sans détail client ni promesse commerciale (voir skill rushiti-avis-google). " +
				"Nécessite `valide_par_isuf: true` : ne jamais publier un brouillon non validé.",
			inputSchema: {
				review: z.string().describe("Nom complet de l'avis accounts/{a}/locations/{l}/reviews/{id}."),
				comment: z.string().min(1).max(4096).describe("Texte exact validé de la réponse."),
				valide_par_isuf: valideParIsuf,
			},
			annotations: { ...WRITE, idempotentHint: true },
		},
		guard(async ({ review, comment, valide_par_isuf }) => {
			if (!valide_par_isuf) return fail("Refusé : la réponse doit être validée par Isuf ou Yll (valide_par_isuf: true).");
			const data = await client.request<Record<string, unknown>>("PUT", API.v4, `${review}/reply`, {
				body: { comment },
			});
			return ok({ publie: true, reponse: data });
		}),
	);

	// ------------------------------------------------------- statistiques

	server.registerTool(
		"gbp_performance",
		{
			title: "Statistiques de la fiche (impressions, appels, clics, itinéraires)",
			description:
				"Séries quotidiennes de performance sur une plage de dates (max ~18 mois d'historique, données disponibles " +
				"avec 2 à 3 jours de décalage) : impressions Maps/Recherche sur mobile et ordinateur, appels, clics vers le site, " +
				"demandes d'itinéraire, conversations. Renvoie le total par métrique et, si demandé, le détail par jour.",
			inputSchema: {
				location: locationParam,
				startDate: z.string().describe("Début AAAA-MM-JJ."),
				endDate: z.string().describe("Fin AAAA-MM-JJ (incluse)."),
				metrics: z
					.array(z.enum(DAILY_METRICS))
					.default([
						"BUSINESS_IMPRESSIONS_DESKTOP_MAPS",
						"BUSINESS_IMPRESSIONS_DESKTOP_SEARCH",
						"BUSINESS_IMPRESSIONS_MOBILE_MAPS",
						"BUSINESS_IMPRESSIONS_MOBILE_SEARCH",
						"CALL_CLICKS",
						"WEBSITE_CLICKS",
						"BUSINESS_DIRECTION_REQUESTS",
					])
					.describe("Métriques à récupérer."),
				detailParJour: z.boolean().default(false).describe("true = inclure la série jour par jour."),
			},
			annotations: READ_ONLY,
		},
		guard(async ({ location, startDate, endDate, metrics, detailParJour }) => {
			const s = toGoogleDate(startDate);
			const e = toGoogleDate(endDate);
			const data = await client.get<{
				multiDailyMetricTimeSeries?: Array<{
					dailyMetricTimeSeries?: Array<{
						dailyMetric: string;
						timeSeries?: { datedValues?: Array<{ date: { year: number; month: number; day?: number }; value?: string }> };
					}>;
				}>;
			}>(API.perf, `locations/${locationId(location)}:fetchMultiDailyMetricsTimeSeries`, {
				dailyMetrics: metrics,
				"dailyRange.startDate.year": s.year,
				"dailyRange.startDate.month": s.month,
				"dailyRange.startDate.day": s.day,
				"dailyRange.endDate.year": e.year,
				"dailyRange.endDate.month": e.month,
				"dailyRange.endDate.day": e.day,
			});
			const totaux: Record<string, number> = {};
			const series: Record<string, Array<{ date: string; valeur: number }>> = {};
			for (const group of data.multiDailyMetricTimeSeries ?? []) {
				for (const ts of group.dailyMetricTimeSeries ?? []) {
					let total = 0;
					const points: Array<{ date: string; valeur: number }> = [];
					for (const dv of ts.timeSeries?.datedValues ?? []) {
						const v = Number(dv.value ?? 0);
						total += v;
						const d = dv.date;
						points.push({
							date: `${d.year}-${String(d.month).padStart(2, "0")}-${String(d.day ?? 1).padStart(2, "0")}`,
							valeur: v,
						});
					}
					totaux[ts.dailyMetric] = total;
					if (detailParJour) series[ts.dailyMetric] = points;
				}
			}
			const impressions =
				(totaux.BUSINESS_IMPRESSIONS_DESKTOP_MAPS ?? 0) +
				(totaux.BUSINESS_IMPRESSIONS_DESKTOP_SEARCH ?? 0) +
				(totaux.BUSINESS_IMPRESSIONS_MOBILE_MAPS ?? 0) +
				(totaux.BUSINESS_IMPRESSIONS_MOBILE_SEARCH ?? 0);
			return ok({
				periode: { debut: startDate, fin: endDate },
				totaux,
				impressionsTotales: impressions,
				...(detailParJour ? { series } : {}),
			});
		}),
	);

	server.registerTool(
		"gbp_search_keywords",
		{
			title: "Requêtes de recherche ayant affiché la fiche",
			description:
				"Mots-clés tapés par les internautes qui ont fait apparaître la fiche, avec le nombre d'utilisateurs uniques " +
				"par mois (ou un seuil « < N » quand Google masque la valeur exacte). Plage en mois AAAA-MM. " +
				"Complète Search Console pour le SEO local (skill rushiti-keyword-map).",
			inputSchema: {
				location: locationParam,
				startMonth: z.string().describe("Premier mois AAAA-MM."),
				endMonth: z.string().describe("Dernier mois AAAA-MM (inclus)."),
				pageSize: pageSize(100, 100),
				pageToken,
			},
			annotations: READ_ONLY,
		},
		guard(async ({ location, startMonth, endMonth, pageSize, pageToken }) => {
			const s = toGoogleMonth(startMonth);
			const e = toGoogleMonth(endMonth);
			const data = await client.get<{
				searchKeywordsCounts?: Array<{ searchKeyword: string; insightsValue?: { value?: string; threshold?: string } }>;
				nextPageToken?: string;
			}>(API.perf, `locations/${locationId(location)}/searchkeywords/impressions/monthly`, {
				"monthlyRange.startMonth.year": s.year,
				"monthlyRange.startMonth.month": s.month,
				"monthlyRange.endMonth.year": e.year,
				"monthlyRange.endMonth.month": e.month,
				pageSize,
				pageToken,
			});
			return ok({
				periode: { debut: startMonth, fin: endMonth },
				nextPageToken: data.nextPageToken ?? null,
				motsCles: (data.searchKeywordsCounts ?? []).map((k) => ({
					requete: k.searchKeyword,
					utilisateurs: k.insightsValue?.value ? Number(k.insightsValue.value) : null,
					seuilInferieurA: k.insightsValue?.threshold ? Number(k.insightsValue.threshold) : null,
				})),
			});
		}),
	);

	// ------------------------------------------------------------ posts

	server.registerTool(
		"gbp_list_posts",
		{
			title: "Posts Google publiés",
			description:
				"Liste les posts (actualités, offres, événements) de la fiche : résumé, bouton d'action, état, dates, " +
				"lien de recherche, médias. Permet de voir la fréquence de publication et les posts encore en ligne.",
			inputSchema: { location: locationParam, account: accountParam, pageSize: pageSize(100, 20), pageToken },
			annotations: READ_ONLY,
		},
		guard(async ({ location, account, pageSize, pageToken }) => {
			const data = await client.get<{ localPosts?: LocalPost[]; nextPageToken?: string; totalSize?: number }>(
				API.v4,
				`${v4LocationPath(location, account)}/localPosts`,
				{ pageSize, pageToken },
			);
			return ok({
				total: data.totalSize ?? null,
				nextPageToken: data.nextPageToken ?? null,
				posts: (data.localPosts ?? []).map((p) => ({
					name: p.name,
					type: p.topicType,
					etat: p.state,
					resume: p.summary,
					bouton: p.callToAction ?? null,
					creeLe: p.createTime,
					modifieLe: p.updateTime,
					urlRecherche: p.searchUrl,
					medias: (p.media ?? []).map((m) => m.googleUrl ?? m.sourceUrl).filter(Boolean),
				})),
			});
		}),
	);

	server.registerTool(
		"gbp_create_post",
		{
			title: "Publier un post Google (après validation)",
			description:
				"Publie un post « Nouveautés » (STANDARD) : texte court orienté SEO local (service + quartier ou commune), " +
				"bouton d'action facultatif (LEARN_MORE vers une page du site, CALL, BOOK…), photo facultative par URL publique. " +
				"0 à 2 hashtags maximum. Nécessite `valide_par_isuf: true`.",
			inputSchema: {
				location: locationParam,
				account: accountParam,
				summary: z.string().min(1).max(1500).describe("Texte du post validé (max 1 500 caractères)."),
				languageCode: z.string().default("fr").describe("Langue (défaut fr)."),
				callToAction: z
					.object({
						actionType: z.enum(["BOOK", "ORDER", "SHOP", "LEARN_MORE", "SIGN_UP", "CALL"]),
						url: z.string().url().optional().describe("URL cible (inutile pour CALL)."),
					})
					.optional(),
				photoUrl: z.string().url().optional().describe("URL publique d'une photo (accord RGPD du client vérifié)."),
				valide_par_isuf: valideParIsuf,
			},
			annotations: WRITE,
		},
		guard(async ({ location, account, summary, languageCode, callToAction, photoUrl, valide_par_isuf }) => {
			if (!valide_par_isuf) return fail("Refusé : le post doit être validé par Isuf ou Yll (valide_par_isuf: true).");
			const body: Record<string, unknown> = { languageCode, summary, topicType: "STANDARD" };
			if (callToAction) body.callToAction = callToAction;
			if (photoUrl) body.media = [{ mediaFormat: "PHOTO", sourceUrl: photoUrl }];
			const data = await client.request<LocalPost>("POST", API.v4, `${v4LocationPath(location, account)}/localPosts`, {
				body,
			});
			return ok({ publie: true, name: data.name, etat: data.state, urlRecherche: data.searchUrl });
		}),
	);

	// ----------------------------------------------------------- médias

	server.registerTool(
		"gbp_list_media",
		{
			title: "Photos et vidéos de la fiche",
			description:
				"Liste les médias publiés par l'établissement (catégorie : couverture, logo, intérieur, extérieur, équipe, " +
				"chantier…), avec date et nombre de vues quand Google le fournit. Sert à mesurer le rythme d'ajout de photos.",
			inputSchema: { location: locationParam, account: accountParam, pageSize: pageSize(100, 50), pageToken },
			annotations: READ_ONLY,
		},
		guard(async ({ location, account, pageSize, pageToken }) => {
			const data = await client.get<{ mediaItems?: MediaItem[]; totalMediaItemCount?: number; nextPageToken?: string }>(
				API.v4,
				`${v4LocationPath(location, account)}/media`,
				{ pageSize, pageToken },
			);
			return ok({
				total: data.totalMediaItemCount ?? null,
				nextPageToken: data.nextPageToken ?? null,
				medias: (data.mediaItems ?? []).map((m) => ({
					name: m.name,
					format: m.mediaFormat,
					categorie: m.locationAssociation?.category,
					url: m.googleUrl,
					creeLe: m.createTime,
					description: m.description,
					vues: m.insights?.viewCount ? Number(m.insights.viewCount) : null,
				})),
			});
		}),
	);

	// ------------------------------------------------- questions-réponses

	server.registerTool(
		"gbp_list_questions",
		{
			title: "Questions-réponses publiques de la fiche",
			description:
				"Liste les questions posées sur la fiche avec leurs meilleures réponses (auteur, type MERCHANT si c'est " +
				"l'établissement). Permet de repérer les questions sans réponse de l'établissement.",
			inputSchema: {
				location: locationParam,
				pageSize: pageSize(100, 20),
				pageToken,
				answersPerQuestion: z.number().int().min(0).max(10).default(3).describe("Réponses renvoyées par question."),
			},
			annotations: READ_ONLY,
		},
		guard(async ({ location, pageSize, pageToken, answersPerQuestion }) => {
			const data = await client.get<{ questions?: Question[]; nextPageToken?: string; totalSize?: number }>(
				API.qanda,
				`locations/${locationId(location)}/questions`,
				{ pageSize, pageToken, answersPerQuestion },
			);
			return ok({
				total: data.totalSize ?? null,
				nextPageToken: data.nextPageToken ?? null,
				questions: (data.questions ?? []).map((q) => ({
					name: q.name,
					auteur: q.author?.displayName,
					typeAuteur: q.author?.type,
					texte: q.text,
					votes: q.upvoteCount ?? 0,
					creeLe: q.createTime,
					nombreReponses: q.totalAnswerCount ?? 0,
					reponduParEtablissement: (q.topAnswers ?? []).some((a) => a.author?.type === "MERCHANT"),
					reponses: (q.topAnswers ?? []).map((a) => ({
						name: a.name,
						auteur: a.author?.displayName,
						typeAuteur: a.author?.type,
						texte: a.text,
						modifieLe: a.updateTime,
					})),
				})),
			});
		}),
	);

	server.registerTool(
		"gbp_answer_question",
		{
			title: "Répondre à une question publique (après validation)",
			description:
				"Publie ou remplace la réponse de l'établissement à une question de la fiche. " +
				"Nécessite `valide_par_isuf: true`.",
			inputSchema: {
				question: z.string().describe("Nom complet de la question locations/{id}/questions/{id}."),
				text: z.string().min(1).max(4096).describe("Texte exact validé de la réponse."),
				valide_par_isuf: valideParIsuf,
			},
			annotations: { ...WRITE, idempotentHint: true },
		},
		guard(async ({ question, text, valide_par_isuf }) => {
			if (!valide_par_isuf) return fail("Refusé : la réponse doit être validée par Isuf ou Yll (valide_par_isuf: true).");
			const data = await client.request<Record<string, unknown>>("POST", API.qanda, `${question}/answers:upsert`, {
				body: { answer: { text } },
			});
			return ok({ publie: true, reponse: data });
		}),
	);
}
