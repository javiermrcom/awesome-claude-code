# Git Guardian 🛡️

> Safe, intelligent Git workflow for AI-assisted coding with enterprise-grade safety guardrails

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/javiermrcom/awesome-claude-code)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-%3E%3D0.9.0-purple.svg)](https://claude.com/code)

## Overview

Git Guardian is a Claude Code plugin that transforms your Git workflow with intelligent automation and enterprise-grade safety features. It prevents costly mistakes while maintaining development velocity through smart commit creation, PR generation, and comprehensive safety guardrails.

### Key Features

- ✅ **Intelligent Commits** - Auto-grouped staging with Conventional Commits format
- ✅ **Smart PR Generation** - Bilingual (EN/ES) with auto Linear/Sentry linking
- ✅ **Safety Guardrails** - Prevents dangerous Git operations and sensitive file exposure
- ✅ **Auto-Detection** - Linear issues and Sentry errors from conversation context
- ✅ **Developer-Agnostic** - Works for any developer (auto-detects git config)
- ✅ **Code Review** - Comprehensive quality checks before commits

---

## Installation

### Using Claude Code Plugin System (Recommended)

```bash
# Add the marketplace (first time only)
/plugin marketplace add javiermrcom/awesome-claude-code

# Install Git Guardian
/plugin install git-guardian@awesome-claude-code
```

### Manual Installation (Alternative)

```bash
# Clone the repository
git clone https://github.com/javiermrcom/awesome-claude-code.git
cd awesome-claude-code

# Copy shared components to your .claude directory
cp commands/* ~/.claude/commands/
cp hooks/* ~/.claude/hooks/
cp agents/* ~/.claude/agents/

# Make hooks executable
chmod +x ~/.claude/hooks/pre_tool_use.py
```

### Optional MCP Configuration

For enhanced Linear and Sentry integrations, configure MCPs in `~/.claude/mcp.json`:

```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-linear"],
      "env": {
        "LINEAR_API_KEY": "your-linear-api-key"
      }
    },
    "sentry": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sentry"],
      "env": {
        "SENTRY_AUTH_TOKEN": "your-sentry-auth-token"
      }
    }
  }
}
```

**Without MCP configuration:**
- Commands work normally
- No automatic Linear/Sentry linking
- Manual issue references still work in commit messages

**With MCP configuration:**
- Auto-detection of Linear issues from conversation
- Auto-linking in commits and PRs
- Rich context from Linear/Sentry in PR descriptions

---

## Components

### Commands (4)

#### `/commit` - Intelligent Commit Creation

Creates atomic, logical commits with Conventional Commits format and automatic issue detection.

**Features:**
- Auto-groups related files (source + tests, docs together)
- Generates proper commit messages
- Detects Linear issues and Sentry errors from context
- Dry-run mode for preview
- Breaking change notation

**Usage:**
```bash
# Basic commit
/commit

# Preview without committing
/commit --dry-run

# Mark as breaking change
/commit --breaking
```

**Example Output:**
```
fix: resolve authentication timeout issue

- Increase JWT token expiration to 24h
- Add refresh token mechanism
- Improve session cleanup

Refs: IA-123
Fixes: PROJ-123
```

---

#### `/pr` - Smart Pull Request Generation

Creates GitHub PRs with intelligent titles, descriptions, and automatic Linear/Sentry linking.

**Features:**
- Detects Linear issues from session > branch > commits
- Configurable language (English by default, Spanish with --lang es)
- Auto-generates comprehensive descriptions
- Label management
- Draft PR support

**Usage:**
```bash
# Create PR from current branch
/pr

# Create draft PR
/pr --draft

# Specify base branch and labels
/pr --base develop --labels "bug,urgent"
```

**Detection Priority:**
1. Session context (conversation mentions)
2. Branch name (e.g., `feat/IA-123-description`)
3. Commit messages

---

#### `/branch-name` - Auto-Detecting Branch Names

Suggests proper branch names based on uncommitted changes with auto-detected developer initials.

**Features:**
- Auto-detects initials from `git config user.name`
- Follows format: `[type]/{initials}/{description}`
- Analyzes changes to suggest appropriate type
- Supports all Conventional Commit types

**Usage:**
```bash
/branch-name
```

**Example Output:**
```
feat/jmr/add-payment-integration
```

**Initials Detection:**
- "Javier Martinez" → `jmr`
- "John Doe" → `jd`
- "Maria Lopez Garcia" → `mlg`

---

#### `/git-status` - Enhanced Repository Status

Provides structured, actionable git status with recommendations.

**Features:**
- Structured output with clear sections
- Recent activity with issue detection
- Pending changes breakdown
- Smart recommendations for next actions
- Related Linear/Sentry context

**Usage:**
```bash
/git-status
```

**Example Output:**
```markdown
### 📊 Repository Status
- **Branch:** feat/jmr/add-payment-integration
- **Status:** Uncommitted changes
- **Upstream:** Ahead 2 commits

### 📝 Recent Activity
- a1b2c3d - fix: resolve payment timeout (Fixes: PROJ-123)
- d4e5f6g - feat: add payment gateway (Refs: IA-456)

### 🔄 Pending Changes
- **Staged:** 3 files
- **Unstaged:** 1 file

### ⚠️ Recommendations
- Run `/commit` to create a logical commit
```

---

### Hooks (1)

#### `pre_tool_use.py` - Security Hook

Comprehensive security protection that prevents dangerous operations.

**Protection Features:**

**Git Safety:**
- ✅ Blocks direct pushes to main/master
- ✅ Prevents force pushes to protected branches
- ✅ Blocks dangerous git operations (hard resets, deletions)

**File System Safety:**
- ✅ Prevents access to `.env` files
- ✅ Blocks dangerous `rm -rf` commands
- ✅ Protects critical paths from deletion

**Configuration:**

The hook is automatically configured when you install the plugin. For custom protected branches:

```python
# Edit hooks/pre_tool_use.py
PLUGIN_CONFIG = {
    "protected_branches": ["main", "master", "production"],
    "allow_force_push": False
}
```

**Example Protection:**
```bash
# This will be blocked
git push origin main
# Output: BLOCKED: Direct push to main/master branch is not allowed

# This will be allowed
git push origin feat/jmr/my-feature
```

---

### Agents (1)

#### `reviewer` - Code Review Agent

Comprehensive code quality review before commits.

**Review Dimensions:**
- Code quality and readability
- Security vulnerabilities
- Performance bottlenecks
- Architecture and design
- Testing coverage
- Best practices

**Prerequisites:**
- All tests passing
- All linting issues resolved
- Type checking passed
- Project builds successfully

**Decision:** APPROVE or REQUEST CHANGES with specific, actionable feedback.

---

## Usage Examples

### Scenario 1: Feature Development with Linear

```bash
# 1. Get repository status
/git-status

# 2. Start working on Linear issue IA-456
# Make your changes...

# 3. Get branch name suggestion
/branch-name
# Output: feat/jmr/payment-integration

# 4. Create branch
git checkout -b feat/jmr/payment-integration

# 5. Commit changes (auto-detects IA-456 from conversation)
/commit
# Creates: feat: add payment integration
#          Refs: IA-456

# 6. Create PR (auto-links Linear issue)
/pr
# PR includes: "Closes IA-456"
```

---

### Scenario 2: Bug Fix with Sentry

```bash
# 1. Investigating Sentry error PROJ-123
# Fix the issue...

# 2. Commit with auto Sentry reference
/commit
# Creates: fix: handle null user object
#          Fixes: PROJ-123

# 3. Create PR
/pr --labels "bug,urgent"
```

---

### Scenario 3: Protected Operations

```bash
# Accidentally try to push to main
git push origin main
# BLOCKED: Direct push to main/master branch is not allowed
# Please create a feature branch and submit a pull request instead

# Safe workflow
git checkout -b feat/jmr/new-feature
git push origin feat/jmr/new-feature  # ✅ Allowed
```

---

## Configuration

### Optional Plugin Configuration

Create `~/.claude/git-guardian.config.json` (optional):

```json
{
  "developer": {
    "initials": "auto"
  },
  "security": {
    "protected_branches": ["main", "master", "production"],
    "allow_force_push": false
  },
  "pr_defaults": {
    "labels": ["ai-agent"],
    "draft": false,
    "description_language": "es",
    "title_language": "en"
  },
  "commit": {
    "require_body": false,
    "max_subject_length": 50
  }
}
```

### Git Integration

The plugin respects your git configuration:

```bash
# Set your name (used for branch initials)
git config user.name "Javier Martinez"

# Set your email
git config user.email "javi.martinez@company.com"
```

---

## Requirements

### Required
- **Claude Code:** >= 0.9.0
- **Python:** >= 3.8 (for security hook)
- **Git:** >= 2.0.0

### Optional
- **GitHub CLI (`gh`):** Required for `/pr` command
- **Linear MCP:** Enables auto-detection and linking of Linear issues in commits and PRs
- **Sentry MCP:** Enables auto-detection and linking of Sentry errors in commits

**Note:** All commands work without MCP servers configured. Linear and Sentry integrations gracefully degrade when MCPs are not available.

---

## Troubleshooting

### Hook Not Working

```bash
# Ensure hook is executable
chmod +x ~/.claude/hooks/pre_tool_use.py

# Test hook manually
echo '{"tool_name":"Bash","tool_input":{"command":"git push origin main"}}' | ~/.claude/hooks/pre_tool_use.py
```

### Branch Name Not Auto-Detecting

```bash
# Check git config
git config user.name

# If empty, set it
git config user.name "Your Name"
```

### Commits Not Detecting Linear Issues

Ensure you mention the Linear issue in the conversation:
```
"Working on IA-123 to add payment integration"
```

Then run `/commit` - it will auto-detect IA-123.

---

## Best Practices

### 1. Use Conversation Context

Mention Linear issues and Sentry errors in your conversation with Claude:
```
"Fixing the timeout bug reported in IA-456 and Sentry error PROJ-123"
```

### 2. Logical Commits

Let `/commit` auto-group related files:
- Source + Tests together
- Docs separately
- Config changes separately

### 3. Review Before PR

Use the reviewer agent (automatically invoked by `/build`) before creating PRs.

### 4. Branch Naming

Use `/branch-name` for consistent branch naming across your team.

---

## Roadmap

### v1.1 (Planned)
- [ ] Configurable branch name templates
- [ ] Large file size warnings
- [ ] Custom protected branch patterns
- [ ] Multi-developer team configuration

### v1.2 (Future)
- [ ] Git hooks integration (pre-commit, pre-push)
- [ ] Metrics and usage analytics
- [ ] Custom commit message templates
- [ ] Interactive commit staging

---

## Contributing

Contributions are welcome! This plugin is part of the [Claude Code Marketplace](https://github.com/javiermrcom/awesome-claude-code).

### Development Setup

```bash
# Clone the repository
git clone https://github.com/javiermrcom/awesome-claude-code.git
cd claude-code-marketplace/git-guardian

# Make changes and test locally
cp -r commands ~/.claude/
cp -r hooks ~/.claude/
cp -r agents ~/.claude/
```

### Reporting Issues

Please report issues on [GitHub Issues](https://github.com/javiermrcom/awesome-claude-code/issues).

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Credits

**Author:** [Javier Martinez](https://github.com/javiermrcom)

**Inspired by:** Real-world AI-assisted development workflows

---

## Support

- 📚 [Documentation](https://github.com/javiermrcom/awesome-claude-code)
- 💬 [Discussions](https://github.com/javiermrcom/awesome-claude-code/discussions)
- 🐛 [Issues](https://github.com/javiermrcom/awesome-claude-code/issues)
- 📧 Email: javiermrcom@gmail.com

---

**Made with ❤️ for the Claude Code community**
