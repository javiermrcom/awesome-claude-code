---
allowed-tools: Bash(/usr/bin/git status:*), Bash(/usr/bin/git add:*), Bash(/usr/bin/git reset:*), Bash(/usr/bin/git diff:*), Bash(/usr/bin/git show:*), Bash(/usr/bin/git log:*), Bash(/usr/bin/git commit:*)
description: Intelligently stage and commit changes based on logical groupings with Linear and Sentry issue detection
argument-hint: "[--dry-run] [--breaking]"
arguments:
  - name: dry_run
    description: Preview what would be staged and committed without making changes
    required: false
  - name: breaking
    description: Mark this commit as a breaking change (adds ! to commit type)
    required: false
---

## Smart Commit Command

This command enhances Claude Code's native commit abilities by:
1. Analyzing ALL changes (staged + unstaged) to find logical groupings
2. Intelligently staging/unstaging files to create atomic commits
3. Generating Conventional Commits format messages WITHOUT attribution
4. Auto-detecting and referencing Linear issues and Sentry errors from context

### Core Logic

The command will:
1. Assess what's currently staged vs unstaged
2. Use conversation context OR change analysis to group related files
3. Detect Linear issues and Sentry errors from session context
4. Stage the right files for a single logical commit
5. Generate a proper Conventional Commits message with issue references

### Task

Analyze the current git state and conversation context. Based on this:

1. **Analyze Git State:**
   - Run `git status --porcelain` to see all changes
   - Determine what forms a logical unit based on:
     - Conversation context (if available)
     - File relationships (source + tests, docs together, etc.)

2. **Detect Issue References:**
   - **Linear Issues:** Scan conversation for Linear issue IDs (e.g., IA-123, ENG-456)
   - **Sentry Issues:** Detect Sentry error references (e.g., ABCD-7S, issue IDs, URLs)
   - Priority: Use the most relevant issue mentioned in current conversation context

3. **Stage Changes:**
   - Unstage files that don't belong in this commit
   - Stage files that complete the logical change

4. **Generate Commit Message:**
   - Follow Conventional Commits format
   - Include issue references in footer when detected
   - Format: `Refs: IA-123` (Linear) or `Fixes: ABCD-7S` (Sentry) or both

5. **Execute Commit**

**Commit Message Format (Conventional Commits v1.0.0):**
```
<type>[optional scope][!]: <description>

[optional body]

[optional footer(s)]
```

**Body Guidelines:**
- Include a body for non-trivial changes (most commits should have one)
- Use bullet points with `- ` prefix (3-5 lines typical)
- Each bullet should describe a specific aspect of the change
- Keep each bullet concise and focused

**Breaking Changes:**
- If breaking argument is provided, add exclamation mark after the type/scope: feat!: or feat(api)!:
- Only the user can determine if a change is breaking

**Types:**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that don't affect meaning (formatting, missing semi-colons, etc)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `build`: Changes to build system or external dependencies
- `ci`: Changes to CI configuration files and scripts
- `chore`: Other changes that don't modify src or test files
- `revert`: Reverts a previous commit

**Important Rules:**
- NEVER stage sensitive files (.env, secrets, passwords, tokens)
- NEVER stage temporary files (.tmp, .cache, logs)
- Group related changes (feature + tests, docs updates together)
- Use lowercase for type and description
- Don't end the subject line with a period
- Use imperative mood in subject line ("add" not "added")
- Keep subject line under 50 characters when possible
- If dry_run argument is provided, show what would be done without executing
- If breaking argument is provided, add exclamation mark after the type (e.g., feat! or feat(scope)!)

**Example commit messages:**

Simple (without body):
```
docs: update README installation instructions
```

Typical (with body):
```
feat: add user authentication module

- Implement JWT-based authentication
- Add login and logout endpoints
- Include session management
- Add password hashing with bcrypt
```

Breaking change:
```
refactor!: restructure API response format

- Change from array to object structure
- Add metadata field for pagination
- Include timestamp in all responses
```

With Linear issue reference:
```
fix: resolve authentication timeout issue

- Increase JWT token expiration to 24h
- Add refresh token mechanism
- Improve session cleanup

Refs: IA-123
```

With Sentry issue reference:
```
fix: handle null user object in payment flow

- Add null check before accessing user.id
- Return early with proper error message
- Add defensive validation

Fixes: ABCD-7S
```

With both Linear and Sentry references:
```
fix: resolve critical payment processing error

- Add null check for user object
- Improve error handling in payment service
- Add integration tests for edge cases

Refs: IA-456
Fixes: ABCD-7S
```

**Footer Format for Issue References:**
- Use `Refs: IA-XXX` for Linear issues (general reference)
- Use `Fixes: SENTRY-ID` for Sentry errors (indicates bug fix)
- Include both if applicable (Linear on first line, Sentry on second)

The goal is to make ONE atomic, logical commit from the available changes following Conventional Commits format with automatic issue detection and referencing.