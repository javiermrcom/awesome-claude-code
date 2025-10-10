# Changelog

All notable changes to the Git Guardian plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-10

### 🎉 Initial Release

First public release of Git Guardian - Safe, intelligent Git workflow for AI-assisted coding.

### Added

#### Commands
- **`/commit`** - Intelligent commit creation with Conventional Commits format
  - Auto-groups related files (source + tests, docs)
  - Linear issue auto-detection from conversation context
  - Sentry error auto-detection from conversation context
  - Dry-run mode for preview (`--dry-run`)
  - Breaking change notation (`--breaking`)
  - Smart file staging/unstaging
  - Comprehensive commit message examples

- **`/pr`** - Smart pull request generation
  - Configurable language support (English by default, Spanish optional)
  - Linear issue detection (session > branch > commits priority)
  - Sentry error detection
  - Auto-generates comprehensive descriptions
  - Label management (`--labels`)
  - Draft PR support (`--draft`)
  - Base branch specification (`--base`)

- **`/branch-name`** - Auto-detecting branch name suggestions
  - Auto-detects developer initials from `git config user.name`
  - Format: `[type]/{initials}/{description}`
  - Supports all Conventional Commit types
  - Analyzes uncommitted changes for type suggestion
  - Fallback to GitHub PR/issue context if no local changes

- **`/git-status`** - Enhanced repository status
  - Structured output with clear sections
  - Repository status (branch, state, upstream)
  - Recent activity with commit history
  - Pending changes breakdown
  - Smart recommendations for next actions
  - Linear/Sentry context detection
  - README context inclusion

#### Hooks
- **`pre_tool_use.py`** - Comprehensive security hook
  - Git protection:
    - Blocks direct pushes to main/master branches
    - Prevents force pushes to protected branches
    - Blocks dangerous git operations (hard resets, branch deletions)
  - File system protection:
    - Prevents access to `.env` files (except `.env.sample`, `.env.example`)
    - Blocks dangerous `rm -rf` commands
    - Protects critical paths from deletion
  - Graceful error handling
  - Configurable via pattern lists
  - Python 3.8+ compatible

#### Agents
- **`reviewer`** - Comprehensive code review agent
  - Quality, security, performance, and architecture analysis
  - Validation-first approach (refuses if tests/linting fail)
  - Iterative refinement support
  - Clear APPROVE/REQUEST CHANGES decisions
  - Pragmatic approach (avoids bikeshedding)
  - Web search integration for best practices

#### Documentation
- Comprehensive README with usage examples
- Installation instructions (plugin system + manual)
- Configuration guide
- Troubleshooting section
- Best practices
- Roadmap
- Contributing guidelines

#### Metadata
- Plugin manifest (`plugin.json`)
- MIT License
- Changelog (this file)
- Examples directory structure

### Features

- ✅ **Universal Applicability** - Works for any developer (auto-detects git config)
- ✅ **Enterprise Safety** - Prevents costly Git mistakes
- ✅ **AI-Aware** - Designed for AI-assisted coding workflows
- ✅ **Integration-Rich** - Linear + Sentry auto-detection
- ✅ **Developer-Friendly** - Clear, actionable feedback
- ✅ **Production-Ready** - Battle-tested in real projects

### Technical Details

- **Requirements:**
  - Claude Code >= 0.9.0
  - Python >= 3.8
  - Git >= 2.0.0
  - GitHub CLI (optional, for `/pr`)

- **Components:**
  - 4 commands
  - 1 security hook
  - 1 review agent

- **Lines of Code:** ~2000+ (commands + hooks + agents)

---

## [Unreleased]

### Planned for v1.1
- [ ] Configurable branch name templates
- [ ] Large file size warnings in security hook
- [ ] Custom protected branch patterns
- [ ] Multi-developer team configuration file
- [ ] Enhanced git-status formatting options

### Planned for v1.2
- [ ] Git hooks integration (pre-commit, pre-push native hooks)
- [ ] Metrics and usage analytics
- [ ] Custom commit message templates
- [ ] Interactive commit staging mode
- [ ] Support for additional issue trackers (Jira, GitHub Issues)

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2025-10-10 | Initial public release |

---

## Migration Guide

### From Manual Git Workflows

If you're migrating from manual git workflows:

1. **Install the plugin** following the README instructions
2. **Configure git** with your name: `git config user.name "Your Name"`
3. **Start using commands:**
   - Replace `git commit` with `/commit`
   - Replace manual PR creation with `/pr`
   - Use `/branch-name` for branch naming
   - Use `/git-status` for repository overview

### From Custom Scripts

If you have custom git scripts:

1. **Review the security hook** patterns to ensure compatibility
2. **Test in a safe branch** before relying on automation
3. **Customize configuration** if needed (see README)

---

## Support & Feedback

- **Issues:** [GitHub Issues](https://github.com/javiermrcom/awesome-claude-code/issues)
- **Discussions:** [GitHub Discussions](https://github.com/javiermrcom/awesome-claude-code/discussions)
- **Email:** javiermrcom@gmail.com

---

**Thank you for using Git Guardian! 🛡️**
