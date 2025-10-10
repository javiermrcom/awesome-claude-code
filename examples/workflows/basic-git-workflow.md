# Basic Git Workflow with Git Guardian

This example demonstrates a typical development workflow using the Git Guardian plugin.

## Scenario

You're working on a new feature that adds user authentication to your application. You need to:
1. Create a feature branch
2. Make changes
3. Commit your work
4. Create a pull request

## Step-by-Step Workflow

### 1. Create Feature Branch

Ask Claude Code to suggest a branch name:

```
User: I'm working on Linear issue IA-123 to add user authentication. Can you suggest a branch name?
Claude: /branch-name
```

Claude will analyze your uncommitted changes and suggest something like:
```
feat/jmr/add-user-authentication
```

Create the branch:
```bash
git checkout -b feat/jmr/add-user-authentication
```

### 2. Make Changes

Implement your feature using Claude Code's assistance:

```
User: Help me implement OAuth authentication with Google
Claude: [implements the feature]
```

### 3. Commit Your Work

Once ready, ask Claude to commit:

```
User: /commit
```

Claude will:
- Analyze all changes with `git status` and `git diff`
- Review recent commits to match your repo's style
- Generate a Conventional Commit message
- Detect Linear issue (IA-123) from branch name
- Create commit like:

```
feat(auth): add Google OAuth authentication

Implements OAuth 2.0 flow with Google provider including:
- OAuth configuration and redirect handling
- User profile fetching and session creation
- Token refresh and validation logic

Linear-Issue: IA-123
```

### 4. Create Pull Request

When ready to create a PR:

```
User: /pr
```

Claude will:
- Analyze all commits since branching from main
- Detect Linear issue IA-123 from branch/commits
- Generate bilingual PR:

**Title (English):**
```
feat(auth): add Google OAuth authentication
```

**Description (English by default):**
```markdown
## ¿Qué cambios introduce este PR?
✨ Nueva funcionalidad

## Descripción
Este PR implementa autenticación OAuth con Google, permitiendo a los usuarios
iniciar sesión usando sus cuentas de Google.

## Linear Issues
Closes IA-123

## Detalles de los cambios
- Configuración de OAuth 2.0 con Google provider
- Manejo de redirects y callbacks
- Obtención de perfil de usuario y creación de sesión
- Lógica de refresh y validación de tokens
```

## Advanced Scenarios

### Dry Run Before Committing

Preview the commit message first:

```
User: /commit --dry-run
```

### Breaking Changes

Mark breaking changes with `!`:

```
User: /commit --breaking
```

Results in:
```
feat(auth)!: refactor authentication API

BREAKING CHANGE: Authentication endpoints now require OAuth tokens
instead of username/password
```

### Draft Pull Requests

Create a draft PR for early feedback:

```
User: /pr --draft
```

### Multiple Commits

If you have multiple logical changes, commit them separately:

```
User: Commit the OAuth implementation first
Claude: /commit

User: Now commit the UI changes separately
Claude: /commit
```

## Security Features

Git Guardian's hooks will automatically protect you:

### Blocked Operations

These operations are automatically blocked:

```bash
# ❌ Direct push to main
git push origin main
# Hook blocks with: "Direct push to main/master branch is not allowed"

# ❌ Force push to protected branches
git push --force origin main
# Hook blocks with: "Force push to protected branches is dangerous"

# ❌ Dangerous rm commands
rm -rf /
# Hook blocks with: "Dangerous rm command detected"

# ❌ Accessing .env files
cat .env
# Hook blocks with: "Access to .env files is not allowed"
```

### Allowed Operations

These are safe and allowed:

```bash
# ✅ Push to feature branch
git push origin feat/jmr/add-user-authentication

# ✅ Force push to your own feature branch (after confirmation)
git push --force origin feat/jmr/add-user-authentication

# ✅ Access .env examples
cat .env.example
cat .env.sample
```

## Tips & Best Practices

1. **Use descriptive branch names** - They help Claude detect Linear issues
2. **Commit often** - Smaller commits are easier to review
3. **Use /commit --dry-run** - Preview before committing
4. **Let Claude detect context** - Mention Linear issues in conversation
5. **Review PR descriptions** - Claude generates them but you can edit

## Troubleshooting

### Claude can't find Linear issue

Make sure to:
- Mention the issue ID in conversation: "I'm working on IA-123"
- Use issue ID in branch name: `feat/IA-123-description`
- Reference in commit messages

### PR description is in wrong language

Git Guardian generates PRs in English by default. You can use `--lang es` to generate descriptions in Spanish.

### Hook blocks legitimate operation

If you need to override a hook (rare), you can temporarily disable it:
```bash
mv ~/.claude/hooks/pre_tool_use.py ~/.claude/hooks/pre_tool_use.py.disabled
# Perform operation
mv ~/.claude/hooks/pre_tool_use.py.disabled ~/.claude/hooks/pre_tool_use.py
```

**Note:** Only do this if you understand the security implications.
