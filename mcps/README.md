# MCP Integrations

Model Context Protocol (MCP) servers enable Claude Code to interact with external services. Git Guardian includes pre-configured integrations for Linear and Sentry.

## Available Integrations

### Linear Integration

**Purpose:** Issue tracking and project management

**Configuration:** `linear.json`

**Authentication:** OAuth (automatic on first use)

**Setup:**
1. Install the plugin (MCPs included automatically)
2. On first use, you'll be prompted to authenticate with Linear
3. Authorize Claude Code to access your Linear workspace
4. No manual API keys needed!

**Technical Details:**
- Uses official Linear MCP server: `https://mcp.linear.app/sse`
- Server-Sent Events (SSE) transport
- OAuth 2.1 with dynamic client registration
- Centrally hosted and managed by Linear

**What it enables:**
- Auto-detection of Linear issues in conversation
- Fetching issue details (title, description, status, assignee)
- Linking issues in commits and PRs
- Issue metadata in PR descriptions

---

### Sentry Integration

**Purpose:** Error tracking and monitoring

**Configuration:** `sentry.json`

**Authentication:** OAuth (automatic on first use)

**Setup:**
1. Install the plugin (MCPs included automatically)
2. On first use, you'll be prompted to authenticate with Sentry
3. Authorize Claude Code to access your Sentry organization
4. No manual API tokens needed!

**Technical Details:**
- Uses official Sentry MCP server: `https://mcp.sentry.dev/mcp`
- HTTP transport with SSE fallback
- OAuth authentication
- Centrally hosted and managed by Sentry

**What it enables:**
- Auto-detection of Sentry errors in conversation
- Fetching error details and stack traces
- Linking errors in commits with "Fixes: SENTRY-ID"
- Error context in commit messages
- Access to 16+ Sentry MCP tools

---

## Installation

MCPs are automatically configured when you install the Git Guardian plugin:

```bash
/plugin marketplace add javiermrcom/awesome-claude-code
/plugin install git-guardian@javiermrcom
```

The plugin will:
1. Copy MCP configuration files
2. Register them with Claude Code
3. Attempt to connect using your environment variables

---

## Manual Configuration

If you want to configure MCPs manually in Claude Code:

```bash
# Add Linear MCP
claude mcp add linear https://mcp.linear.app/sse

# Add Sentry MCP
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
```

Then restart Claude Code to load the configurations.

---

## Verifying Installation

Check if MCPs are active:

```bash
# In Claude Code, run:
/help
```

Look for these tools being available:
- `mcp__linear__*` (Linear tools)
- `mcp__sentry__*` (Sentry tools)

---

## Troubleshooting

### MCP not connecting

**Authentication Required:**
- First time using a tool, you'll be prompted to authenticate via OAuth
- Click the authorization link and sign in to Linear/Sentry
- Grant permissions to Claude Code

**Re-authenticate if needed:**
```bash
# For Claude Code
claude mcp remove linear
claude mcp add linear https://mcp.linear.app/sse
```

### MCPs not appearing in Claude Code

1. Ensure Node.js >= 18 is installed: `node --version`
2. Check `npx` is available: `npx --version`
3. Restart Claude Code
4. Try manual authentication: Use a Linear/Sentry MCP tool and follow OAuth flow

### OAuth Issues

- **Browser doesn't open:** Check if your system can open URLs from terminal
- **Permission denied:** Ensure you have access to the Linear workspace or Sentry organization
- **Token expired:** Re-authenticate using the MCP tool again

---

## Notes

These MCPs are pre-configured for Claude Code CLI. They use the official, centrally-managed MCP servers from Linear and Sentry, which handle OAuth authentication automatically on first use.

---

## Learn More

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Linear API Docs](https://developers.linear.app/)
- [Sentry API Docs](https://docs.sentry.io/api/)
