# Awesome Claude Code

> Curated collection of production-ready Claude Code components and plugins

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Components](https://img.shields.io/badge/components-shared-blue.svg)](#components)
[![Plugins](https://img.shields.io/badge/plugins-1-orange.svg)](#plugins)

---

## Overview

**Awesome Claude Code** is a curated collection of production-ready Claude Code plugins. Each plugin is battle-tested, self-contained, and ready to enhance your AI-assisted development workflow.

### What Makes This Different?

**Plugin-First Architecture:**
- **Complete, self-contained plugins** ready to install
- **Production-tested** in real development workflows
- **Easy installation** via Claude Code plugin system
- **Battle-tested components** that work together seamlessly

### Use Cases

**Teams & Individual Developers:**
```bash
# Add marketplace and install
/plugin marketplace add javiermrcom/awesome-claude-code
/plugin install git-guardian@awesome-claude-code
```

**Plugin Developers:**
- Browse plugin source code for inspiration
- Learn best practices from production plugins
- Contribute new plugins to the collection

---

## Repository Structure

```
awesome-claude-code/
├── .claude-plugin/
│   └── marketplace.json   # Marketplace configuration
│
├── plugins/               # Production-ready plugins
│   └── git-guardian/      # Git workflow automation
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── commands/      # Slash commands
│       ├── agents/        # Subagents
│       ├── hooks/         # Security hooks
│       ├── README.md
│       └── CHANGELOG.md
│
└── README.md              # This file
```

---

## Plugins

### 🛡️ Git Guardian v1.0.0

**Complete Git workflow automation with safety guardrails**

Transform your Git workflow with intelligent automation and enterprise-grade safety features.

**Installation:**
```bash
/plugin install git-guardian@awesome-claude-code
```

**Features:**
- ✅ Intelligent commits with Conventional Commits format
- ✅ Smart PR generation (bilingual: EN/ES)
- ✅ Auto-detection of Linear issues and Sentry errors
- ✅ Branch name suggestions
- ✅ Enhanced git status
- ✅ Security guardrails (blocks dangerous operations)
- ✅ Code review before commits

**Commands:**
- `/commit` - Create intelligent commits
- `/pr` - Generate smart pull requests
- `/branch-name` - Get branch name suggestions
- `/git-status` - Enhanced repository status

[📖 Full Documentation](plugins/git-guardian/README.md) | [📋 Changelog](plugins/git-guardian/CHANGELOG.md)

---

## Installation

### Quick Start

```bash
# Add the marketplace (first time only)
/plugin marketplace add javiermrcom/awesome-claude-code

# Install Git Guardian
/plugin install git-guardian@awesome-claude-code
```

That's it! Claude Code automatically installs all commands, agents, hooks, and configurations.

---

## Quick Examples

### Git Workflow with Git Guardian

```bash
# 1. Check status
/git-status

# 2. Get branch name suggestion
/branch-name
# Output: feat/jmr/add-oauth-authentication

# 3. Create branch and make changes
git checkout -b feat/jmr/add-oauth-authentication
# ... edit files ...

# 4. Create commit
/commit

# 5. Create PR
/pr
```

[📖 More Examples](plugins/git-guardian/README.md#usage-examples)

---

## Contributing

We welcome contributions of new plugins!

### Creating a New Plugin

1. **Create plugin structure:**
   ```
   plugins/your-plugin/
   ├── .claude-plugin/
   │   └── plugin.json
   ├── commands/
   ├── agents/
   ├── hooks/
   ├── README.md
   └── CHANGELOG.md
   ```

2. **Test thoroughly** in production

3. **Submit a PR** with:
   - Complete plugin directory
   - Comprehensive README
   - CHANGELOG
   - Usage examples

[📖 Plugin Development Guide](CLAUDE.md#creating-a-new-plugin)

---

## Requirements

**General:**
- Claude Code >= 0.9.0
- Git >= 2.0.0

**Plugin-Specific:**
See individual plugin READMEs for specific requirements.

---

## Support

**Documentation:**
- [CLAUDE.md](CLAUDE.md) - Development guide
- [Git Guardian README](plugins/git-guardian/README.md)

**Getting Help:**
- 🐛 [Report Issues](https://github.com/javiermrcom/awesome-claude-code/issues)
- 💬 [Discussions](https://github.com/javiermrcom/awesome-claude-code/discussions)
- 📧 Email: javiermrcom@gmail.com

---

## Roadmap

### Current (Q4 2025)
- ✅ Git Guardian v1.0.0
- ✅ Plugin marketplace

### Planned
- 🔄 Linear Workflow Plugin
- 📊 Code Quality Plugin
- 🐍 Python Dev Plugin
- 🧪 Testing Utilities Plugin

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
