// Bindings et secrets du Worker (miroir de wrangler.jsonc + `wrangler secret put`).
// Regénérable avec `npm run cf-typegen`, puis compléter les secrets ci-dessous.
interface Env {
  OAUTH_KV: KVNamespace;
  MCP_OBJECT: DurableObjectNamespace<import("./src/index").GbpMcp>;
  GOOGLE_CLIENT_ID: string;
  GOOGLE_CLIENT_SECRET: string;
  COOKIE_ENCRYPTION_KEY: string;
  /** Optionnel : liste d'e-mails Google autorisés, séparés par des virgules. */
  ALLOWED_EMAILS?: string;
}
