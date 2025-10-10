# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## What is awesome-claude-code?

This is a **curated collection of production-ready Claude Code plugins and resources**. Think of it like [awesome lists](https://github.com/sindresorhus/awesome) but specifically for Claude Code.

**Think of it as:** A showcase of what's possible with Claude Code, with ready-to-install plugins.

## Repository Structure

```
awesome-claude-code/
├── plugins/                    # Installable plugins
│   └── git-guardian/          # Git workflow automation
│       ├── .claude-plugin/
│       │   └── plugin.json    # Plugin metadata
│       ├── commands/          # Slash commands
│       ├── agents/            # Subagents
│       ├── hooks/             # Security hooks
│       ├── README.md
│       └── CHANGELOG.md
│
├── examples/                   # Usage examples & patterns
│   └── workflows/
│
└── README.md                   # Main documentation
```

## How Users Should Use This

### Installing Plugins

Users can install plugins directly using Claude Code's plugin system:

```bash
# Add the marketplace
/plugin marketplace add javiermrcom/awesome-claude-code

# Install a plugin
/plugin install git-guardian@awesome-claude-code
```

Claude Code will automatically:
- Read the `plugin.json` metadata
- Copy commands to `~/.claude/commands/`
- Copy agents to `~/.claude/agents/`
- Copy hooks to `~/.claude/hooks/`
- Make hooks executable
- Register the plugin

### Browsing Resources

Users can also:
- Browse the source code to learn patterns
- Copy individual components if they prefer manual installation
- Fork and customize plugins for their needs
- Use examples as templates for their own plugins

## Available Plugins

### Git Guardian v1.0.0
**Complete Git workflow automation with safety guardrails**

**Features:**
- Smart commits with Conventional Commits format
- Intelligent PR generation (bilingual: English titles, Spanish descriptions)
- Auto-detecting branch names
- Enhanced repository status
- Security validation (blocks dangerous operations)
- Linear issue integration
- Sentry error integration

**Installation:**
```bash
claude-code plugin install awesome-claude-code/plugins/git-guardian
```

**Components:**
- Commands: `/commit`, `/pr`, `/branch-name`, `/git-status`
- Hooks: `pre_tool_use.py` (security guardrails)
- Agents: `reviewer` (code review)

See: `plugins/git-guardian/README.md`

## Development Guidelines

### Creating a New Plugin

When adding a new plugin to this collection:

1. **Plugin Structure:**
   ```
   plugins/your-plugin/
   ├── .claude-plugin/
   │   └── plugin.json       # Required
   ├── commands/             # Optional
   ├── agents/               # Optional
   ├── hooks/                # Optional
   ├── README.md             # Required
   └── CHANGELOG.md          # Required
   ```

2. **Plugin Metadata (`plugin.json`):**
   ```json
   {
     "name": "your-plugin",
     "version": "1.0.0",
     "description": "Brief description",
     "author": {
       "name": "Your Name",
       "email": "your.email@company.com"
     },
     "components": {
       "commands": ["command1", "command2"],
       "hooks": ["hook.py"],
       "agents": ["agent1"]
     },
     "tags": ["category1", "category2"]
   }
   ```

3. **Quality Standards:**
   - Battle-tested in production
   - Comprehensive documentation
   - Clear installation instructions
   - Examples of usage
   - Proper error handling

### Component Guidelines

#### Commands (Slash Commands)
- File format: `command-name.md`
- Location: `plugins/{name}/commands/`
- Must include frontmatter:
  ```yaml
  ---
  allowed-tools: Bash, Task, Read
  description: Brief command description
  arguments:
    - name: arg_name
      description: Argument description
      required: false
  ---
  ```

#### Agents (Subagents)
- File format: `agent-name.md`
- Location: `plugins/{name}/agents/`
- Must include frontmatter with `allowed-tools` and clear task description
- Agents analyze, main Claude executes

#### Hooks
- Configuration: Define in `plugin.json` under `"hooks"` key
- Scripts: Python/shell scripts referenced by the hooks configuration
- Must be executable (chmod +x)
- Available events: `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, etc.
- Must fail open (exit 0 on errors, don't block Claude)
- Example in `plugin.json`:
  ```json
  "hooks": {
    "PreToolUse": [{
      "matcher": ".*",
      "hooks": [{"type": "command", "command": "../../hooks/pre_tool_use.py"}]
    }]
  }
  ```

### Testing Plugins

Before adding to the collection:

```bash
# Test plugin installation
claude-code plugin install plugins/your-plugin

# Verify components are installed
ls -la ~/.claude/commands/
ls -la ~/.claude/agents/
ls -la ~/.claude/hooks/

# Test functionality
# Try using the commands, agents, hooks in Claude Code
```

## Key Patterns & Best Practices

### Common Integrations

Plugins in this collection support popular development tools:

**Linear Issues:**
- Auto-detection from branch names (e.g., `feat/PROJ-123-description`)
- Session context analysis (conversation mentions)
- Auto-linking in PRs and commits

**Sentry Errors:**
- Pattern detection (Sentry URLs and issue IDs like PROJ-123, SENTRY-456)
- Auto-linking in commit footers

**Configurable PR Format:**
- Titles in English (lowercase after type)
- Descriptions with structured sections
- Customizable language and format

### Security Patterns

**Protected Operations (via hooks):**
- Block direct pushes to `main`/`master`
- Prevent force pushes to protected branches
- Block dangerous `rm -rf` commands
- Protect `.env` files (allow `.env.sample`/`.env.example`)

**Git Command Safety:**
- Always use `/usr/bin/git` instead of `git`
- Require explicit confirmation for destructive operations
- Fail open on hook errors (don't block Claude entirely)

### Conventional Commits

All commit-related commands use Conventional Commits v1.0.0:
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`
- Format: `<type>[scope][!]: <description>`
- Breaking changes marked with `!`

## Support & Contributing

**Documentation:** Each plugin has its own README with detailed usage

**Issues:** https://github.com/javiermrcom/awesome-claude-code/issues

**Contributing:**
1. Fork the repository
2. Create your plugin following the guidelines above
3. Test thoroughly in production
4. Submit a PR with your plugin

**Contact:** javiermrcom@gmail.com

## Notes for Claude Code

When working in this repository:

1. **This is a plugin collection** - Each plugin should be self-contained and installable via `claude-code plugin install`
2. **Plugin metadata is key** - Every plugin needs a valid `.claude-plugin/plugin.json`
3. **Quality over quantity** - Only add battle-tested, production-ready plugins
4. **Documentation matters** - Clear READMEs, examples, and installation instructions are essential
5. **Follow existing patterns** - Use Git Guardian as a reference for structure and quality
