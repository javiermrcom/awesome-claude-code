---
allowed-tools: Bash(/usr/bin/git status:*), Bash(/usr/bin/git diff:*), Bash(/usr/bin/git log:*), Bash(/usr/bin/git branch:*), Bash(gh pr view:*), Bash(gh issue view:*)
description: Suggest branch names based on uncommitted changes with format [type]/{initials}/snake-case-name
argument-hint: ""
---

## Context
- Current git status: !`/usr/bin/git status --porcelain`
- Unstaged changes: !`/usr/bin/git diff --stat`
- Staged changes: !`/usr/bin/git diff --cached --stat`
- Current branch: !`/usr/bin/git branch --show-current`
- Recent commits: !`/usr/bin/git log --oneline -5 --pretty=format:"%s"`
- Git user name: !`/usr/bin/git config user.name`

## Requirements for branch name suggestions

1. **Format**
   - MUST be: `[type]/{initials}/descriptive-name`
   - Auto-detect developer initials from git config user.name
   - Use kebab-case (hyphens) for descriptive part

2. **Developer Initials Detection**
   - Extract from git config user.name
   - Generate initials from full name:
     - "Javier Martinez Ruiz" → "jmr" (first letters of each word, lowercase)
     - "John Doe" → "jd"
     - "Maria Lopez Garcia" → "mlg"
   - If name is not available, use git username or fallback to "dev"

3. **Branch types**
   - `fix`: Bug fixes
   - `feat`: New features
   - `chore`: Maintenance, dependencies, tooling
   - `docs`: Documentation only changes
   - `refactor`: Code restructuring without behavior change
   - `test`: Adding or modifying tests
   - `perf`: Performance improvements
   - `style`: Code formatting, no logic change
   - `build`: Build system or external dependencies
   - `ci`: CI/CD configuration changes

4. **Naming rules**
   - Keep descriptive part concise (2-5 words)
   - Use clear, specific terms from the changes
   - Match type to primary purpose of changes
   - All lowercase, no special characters except hyphens

5. **Output requirements**
   - Provide exactly ONE branch name suggestion
   - Choose the most appropriate based on the changes
   - No explanations, just the single branch name

## Task

Based on the uncommitted changes and git user context above:

1. **Detect developer initials:**
   - Parse the git user.name value
   - Generate initials from the full name (first letter of each word, lowercase)
   - Example: "Javier Martinez Ruiz" → "jmr", "John Doe" → "jd"

2. **Suggest branch name:**
   - Format: `[type]/{detected-initials}/descriptive-name`
   - If no changes are present, check for associated PR or issue using gh
   - Choose the most appropriate type based on changes

Output only ONE branch name suggestion, nothing else.