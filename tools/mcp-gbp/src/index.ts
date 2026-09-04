// Point d'entrée du Worker : serveur OAuth 2.1 (côté claude.ai) + agent MCP
// (Durable Object) qui expose les outils Google Business Profile.
//
// Architecture (identique au modèle Cloudflare remote-mcp-google-oauth) :
//   claude.ai ──OAuth──▶ ce Worker ──OAuth Google──▶ accounts.google.com
//   claude.ai ──MCP (/mcp)──▶ GbpMcp (Durable Object) ──▶ API Business Profile
// Le refresh token Google voyage chiffré dans le jeton remis à claude.ai
// (props) ; aucun secret Google n'est stocké en clair côté Cloudflare.

import OAuthProvider from "@cloudflare/workers-oauth-provider";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { McpAgent } from "agents/mcp";
import { GbpClient } from "./gbp-client";
import { GoogleHandler } from "./google-handler";
import { registerTools } from "./tools";
import type { Props } from "./utils";

export class GbpMcp extends McpAgent<Env, Record<string, never>, Props> {
	server = new McpServer({
		name: "rushiti-gbp",
		version: "0.1.0",
	});

	async init() {
		const client = new GbpClient(this.env, () => this.props?.refreshToken);
		registerTools(this.server, client);
	}
}

export default new OAuthProvider({
	apiHandler: GbpMcp.serve("/mcp"),
	apiRoute: "/mcp",
	authorizeEndpoint: "/authorize",
	clientRegistrationEndpoint: "/register",
	defaultHandler: GoogleHandler as any,
	tokenEndpoint: "/token",
});
