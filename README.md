# Awesome Claude Code

> Curated collection of production-ready Claude Code components and plugins

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Components](https://img.shields.io/badge/components-shared-blue.svg)](#components)
[![Plugins](https://img.shields.io/badge/plugins-1-orange.svg)](#plugins)

---

## Overview

**Awesome Claude Code** is a curated collection of reusable Claude Code components (commands, agents, hooks) and complete plugins. All components are production-tested and designed with a "share-first" philosophy.

### What Makes This Different?

**Shared Component Architecture:**
- **Root-level components** that can be used standalone OR by plugins
- **Plugin references** instead of duplication
- **Mix and match** - copy individual components or install complete plugins
- **Plugin composition** - multiple plugins can share the same components

### Use Cases

**Individual Developers:**
```bash
# Copy a single command
cp commands/commit.md ~/.claude/commands/

# Copy a security hook
cp hooks/pre_tool_use.py ~/.claude/hooks/
chmod +x ~/.claude/hooks/pre_tool_use.py
```

**Teams Using Plugins:**
```bash
# Add marketplace and install
/plugin marketplace add javiermrcom/awesome-claude-code
/plugin install git-guardian@awesome-claude-code
```

**Plugin Developers:**
- Browse components for inspiration
- Reference shared components in your plugins
- Contribute new reusable components

---

## Repository Structure

```
awesome-claude-code/
├── commands/              # Shared slash commands
│   ├── commit.md         # Smart commits with Conventional Commits
│   ├── pr.md             # Intelligent PR generation
│   ├── branch-name.md    # Auto-detecting branch names
│   └── git-status.md     # Enhanced repository status
│
├── agents/               # Shared subagents
│   └── reviewer.md       # Comprehensive code review
│
├── hooks/                # Shared event hooks
│   └── git_safety.py     # Git-specific safety validations
│
├── mcps/                 # MCP server configurations
│   ├── linear.json       # Linear integration
│   └── sentry.json       # Sentry integration
│
├── plugins/              # Complete bundled solutions
│   └── git-guardian/     # Git workflow automation (references shared components)
│
└── examples/             # Usage patterns and workflows
    └── workflows/
```

---

## Components

### 📝 Commands (Slash Commands)

#### `/commit` - Smart Commit Creation
Intelligent commits with Conventional Commits format, Linear issue detection, and Sentry error integration.

**Usage:**
```bash
/commit                  # Create intelligent commit
/commit --dry-run       # Preview without committing
/commit --breaking      # Mark as breaking change
```

**Features:**
- Conventional Commits v1.0.0 format
- Auto-detects Linear issues from branch names and conversation
- Auto-detects Sentry errors from conversation
- Analyzes git diff and recent commits
- Bilingual support (optional)

[📖 View Source](commands/commit.md)

---

#### `/pr` - Intelligent PR Generation
Smart pull request creation with context detection and bilingual descriptions.

**Usage:**
```bash
/pr                     # Create PR with English description (default)
/pr --lang es          # Create PR with Spanish description
/pr --draft            # Create draft PR
/pr --base develop     # Target different base branch
/pr --labels bug,urgent # Add labels
```

**Features:**
- Auto-detects Linear issues (session context → branch → commits)
- Auto-generates titles (English, lowercase after type)
- Auto-generates descriptions (English by default, Spanish with --lang es)
- Includes commit history analysis
- Links issues automatically

[📖 View Source](commands/pr.md)

---

#### `/branch-name` - Auto-Detecting Branch Names
Suggests branch names based on uncommitted changes and git config.

**Usage:**
```bash
/branch-name
```

**Features:**
- Analyzes uncommitted changes
- Auto-detects developer initials from git config
- Follows format: `[type]/{initials}/{description}`
- Developer-agnostic (no hardcoded names)

[📖 View Source](commands/branch-name.md)

---

#### `/git-status` - Enhanced Repository Status
Git status with actionable recommendations and insights.

**Usage:**
```bash
/git-status
```

**Features:**
- Shows working tree status
- Analyzes branches and upstream
- Provides actionable recommendations
- Detects common issues

[📖 View Source](commands/git-status.md)

---

### 🤖 Agents (Subagents)

#### `reviewer` - Code Review Agent
Comprehensive code review before commits with quality checks.

**Features:**
- Multi-pass analysis (security, performance, quality)
- Actionable feedback
- Best practices validation
- Integration with `/commit` command

[📖 View Source](agents/reviewer.md)

---

### 🔌 MCP Integrations

#### Linear Integration
Connect to Linear for issue tracking and project management.

**Configuration:** `mcps/linear.json`

**Authentication:** OAuth (automatic on first use)

**Setup:** Install the plugin and authenticate when prompted - no manual API keys needed!

**Features:**
- Official Linear MCP server (`https://mcp.linear.app/sse`)
- OAuth 2.1 authentication
- Centrally hosted and managed

[📖 View Config](mcps/linear.json) | [📖 Setup Guide](mcps/README.md)

---

#### Sentry Integration
Connect to Sentry for error tracking and monitoring.

**Configuration:** `mcps/sentry.json`

**Authentication:** OAuth (automatic on first use)

**Setup:** Install the plugin and authenticate when prompted - no manual tokens needed!

**Features:**
- Official Sentry MCP server (`https://mcp.sentry.dev/mcp`)
- OAuth authentication
- 16+ MCP tools
- Centrally hosted and managed

[📖 View Config](mcps/sentry.json) | [📖 Setup Guide](mcps/README.md)

---

### 🔒 Hooks

#### Git Safety Hook
Prevents dangerous Git operations on protected branches.

**Script:** `git_safety.py`

**Protected Operations:**
- ❌ Direct pushes to `main`/`master`
- ❌ Force pushes to protected branches
- ❌ Hard resets to `main`/`master`
- ❌ Branch deletions of protected branches

**Features:**
- Git-specific validations only
- Configurable protected branches
- Fails open (errors don't block Claude)
- Clear, actionable error messages

**Why Git-specific?** Each hook focuses on one concern. Future hooks can handle file system, environment, or other validations independently.

[📖 View Script](hooks/git_safety.py)

---

## Plugins

### 🛡️ Git Guardian v1.0.0

**Complete Git workflow automation with safety guardrails**

Git Guardian bundles all Git-related components into a cohesive workflow. Instead of duplicating components, it **references** shared components from the root.

**Installation:**
```bash
# Add marketplace
/plugin marketplace add javiermrcom/awesome-claude-code

# Install plugin
/plugin install git-guardian@awesome-claude-code
```

**What's Included:**
- Commands: `/commit`, `/pr`, `/branch-name`, `/git-status`
- Agents: `reviewer`
- Hooks: Git safety validations
- MCPs: Linear & Sentry integrations

**Features:**
- Conventional Commits format
- Linear issue integration
- Sentry error integration
- Security guardrails
- Configurable PR language (English by default, Spanish optional)
- Developer-agnostic workflows

[📖 Full Documentation](plugins/git-guardian/README.md) | [📋 Changelog](plugins/git-guardian/CHANGELOG.md)

---

## Installation

### Option 1: Individual Components (Copy & Paste)

**Copy what you need:**
```bash
# Commands
cp commands/commit.md ~/.claude/commands/
cp commands/pr.md ~/.claude/commands/

# Agents
cp agents/reviewer.md ~/.claude/agents/

# Hooks (don't forget chmod)
cp hooks/pre_tool_use.py ~/.claude/hooks/
chmod +x ~/.claude/hooks/pre_tool_use.py
```

### Option 2: Complete Plugin

**Install via Claude Code plugin system:**
```bash
# Add this repository as a marketplace
/plugin marketplace add javiermrcom/awesome-claude-code

# Install Git Guardian plugin
/plugin install git-guardian@awesome-claude-code
```

Claude Code will automatically:
- Copy all referenced components to `~/.claude/`
- Make hooks executable
- Register the plugin

---

## Quick Start

### Git Workflow Example

```bash
# 1. Check status
/git-status

# 2. Get branch name suggestion
/branch-name
# Output: feat/jmr/add-oauth-authentication

# 3. Create branch
git checkout -b feat/jmr/add-oauth-authentication

# 4. Make changes
# ... edit files ...

# 5. Preview commit
/commit --dry-run

# 6. Create commit
/commit

# 7. Create PR
/pr
```

[📖 Complete Workflow Example](examples/workflows/basic-git-workflow.md)

---

## Plugin Development

### Creating Plugins That Reference Shared Components

**Plugin Structure:**
```
plugins/your-plugin/
├── .claude-plugin/
│   └── plugin.json       # References shared components
├── README.md
└── CHANGELOG.md
```

**Example `plugin.json`:**
```json
{
  "name": "your-plugin",
  "version": "1.0.0",
  "description": "Your plugin description",
  "components": {
    "commands": [
      "../../commands/commit.md",
      "../../commands/pr.md"
    ],
    "hooks": [
      "../../hooks/pre_tool_use.py"
    ],
    "agents": [
      "../../agents/reviewer.md"
    ]
  }
}
```

**Benefits:**
- No component duplication
- Automatic updates when shared components improve
- Smaller plugin size
- Consistent behavior across plugins

[📖 Plugin Development Guide](CLAUDE.md#plugin-development)

---

## Requirements

**General:**
- Claude Code >= 0.9.0
- Git >= 2.0.0

**Component-Specific:**
- **Hooks:** Python >= 3.8
- **MCPs:** Node.js >= 18 (for npx)
- **Linear MCP:** OAuth authentication (automatic)
- **Sentry MCP:** OAuth authentication (automatic)

---

## Examples & Patterns

- [Basic Git Workflow](examples/workflows/basic-git-workflow.md)
- [More examples coming soon...]

---

## Contributing

We welcome contributions of new components and plugins!

### Contributing Components

1. **Create your component** (command, agent, or hook)
2. **Test thoroughly** in production
3. **Add documentation** with usage examples
4. **Submit a PR** with:
   - Component file(s)
   - README updates
   - Usage examples

### Contributing Plugins

1. **Build your plugin** referencing shared components
2. **Create plugin.json** with relative paths
3. **Test installation** locally
4. **Submit a PR** with:
   - Plugin directory
   - README.md
   - CHANGELOG.md
   - Examples

[📖 Development Guidelines](CLAUDE.md#development-guidelines)

---

## Support

**Documentation:**
- [CLAUDE.md](CLAUDE.md) - Development guide
- [Git Guardian README](plugins/git-guardian/README.md)
- [Workflow Examples](examples/workflows/)

**Getting Help:**
- 🐛 [Report Issues](https://github.com/javiermrcom/awesome-claude-code/issues)
- 📧 Email: javiermrcom@gmail.com

---

## Roadmap

### Current (Q4 2025)
- ✅ Git Guardian v1.0.0
- ✅ Shared component architecture
- ✅ Example workflows

### Planned
- 🔄 Linear Workflow Plugin
- 📊 Code Quality Components
- 🐍 Python Dev Components
- 🧪 Testing Utilities

---

## About

**Awesome Claude Code** is maintained by [Javier Martinez](https://github.com/javiermrcom). A curated collection of production-ready components for AI-assisted development.

---

## License

All components and plugins are licensed under the MIT License unless otherwise specified.

See [LICENSE](LICENSE) for details.

---

## Acknowledgments

- **Anthropic** for Claude Code
- **Open Source Community** for inspiration and tools

---

**Made with ❤️ by [Javier Martinez](https://github.com/javiermrcom)**

[⬆ Back to top](#awesome-claude-code)
