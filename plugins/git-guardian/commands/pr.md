---
allowed-tools: Bash(/usr/bin/git:*), Bash(gh:*), Task, WebSearch
description: Create a GitHub pull request with intelligent title and description generation
arguments:
  - name: branch
    description: Branch name for PR (defaults to current branch)
    required: false
  - name: base
    description: Base branch to merge into (defaults to main/master)
    required: false
  - name: draft
    description: Create as draft PR
    required: false
  - name: labels
    description: Comma-separated list of labels to add to the PR (e.g., "bug,urgent,backend")
    required: false
  - name: lang
    description: Description language ("en" or "es", defaults to "en")
    required: false
---

## Smart Pull Request Command

This command creates a GitHub PR by:
1. Analyzing the diff between branches
2. Reading commit messages to understand intent
3. Detecting Linear issues from session context, branch names, and commits
4. Automatically linking detected Linear issues
5. Generating an intelligent title and description
6. Creating the PR using GitHub CLI

### Task

Create a pull request following these steps:

#### 1. Gather Information

First, collect all necessary information:

```bash
# Get current branch if not specified
BRANCH="${branch:-$(git rev-parse --abbrev-ref HEAD)}"

# Get default base branch if not specified
BASE="${base:-$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')}"

# Get repository info
REPO_INFO=$(gh repo view --json owner,name)
REPO_OWNER=$(echo "$REPO_INFO" | jq -r '.owner.login')
REPO_NAME=$(echo "$REPO_INFO" | jq -r '.name')

# Get the diff
DIFF=$(git diff "$BASE...$BRANCH")

# Get commit messages
COMMITS=$(git log "$BASE..$BRANCH" --pretty=format:"- %s" --reverse)
```

#### 2. Detect Linear Issues

Analyze multiple sources to detect related Linear issues:

**Detection Sources (in priority order):**
1. **Session Context**: Scan the current conversation for Linear issue references (IA-XXX, ENG-XXX, etc.)
2. **Branch Name**: Extract issue IDs from branch name patterns:
   - `feature/IA-123-description`
   - `IA-456/fix-something`
   - `bugfix/IA-789`
3. **Commit Messages**: Look for issue references in commit messages:
   - `feat: add feature (IA-123)`
   - `Closes IA-456`
   - `Related to IA-789`

**Detection Logic:**
```bash
# Pattern for Linear issues (TEAM-NUMBER format)
LINEAR_PATTERN="[A-Z]{2,4}-[0-9]+"

# Extract from session context (highest priority)
# Note: This requires analyzing the conversation history for Linear issue mentions

# Extract from branch name
BRANCH_ISSUES=$(echo "$BRANCH" | grep -oE "$LINEAR_PATTERN" | head -1)

# Extract from commit messages
COMMIT_ISSUES=$(echo "$COMMITS" | grep -oE "$LINEAR_PATTERN" | sort -u)

# Combine all detected issues (session context takes priority)
DETECTED_ISSUES="$SESSION_ISSUES $BRANCH_ISSUES $COMMIT_ISSUES"
```

**Linear Issue Enrichment:**
For each detected issue, fetch details using Linear MCP:
- Issue title and description
- Current status
- Assignee information
- Labels and project context

#### 3. Analyze Changes

Based on the diff and commits, determine:
- **Type of change**: feat, fix, refactor, docs, test, build, ci, chore, style, perf
- **Main objective**: What the PR accomplishes
- **Context**: Why these changes were made

#### 4. Generate PR Content

Create title and description following these rules:

**Title Format (English, lowercase after type):**
```
<type>: <description>
```

Conventional Commit types:
- feat, fix, build, chore, ci, docs, style, refactor, perf, test

Examples:
- `feat: add user authentication with JWT tokens`
- `fix: resolve layout issues in mobile view`
- `refactor: optimize database query performance`

**Description Format (Markdown):**

The description language is controlled by the `lang` parameter (defaults to "en"):
- `lang=en`: English description (default)
- `lang=es`: Spanish description

**English Format (lang=en, default):**
```markdown
## What changes does this PR introduce?

- [x] <emoji> <Type>
<!-- ONLY include the ONE type that applies. Delete all others. Examples:
- [x] ✨ Feature
- [x] 🐛 Fix
- [x] 🔄 Refactor
- [x] 🔧 Chore
- [x] 📝 Docs
- [x] ✅ Test
-->

## Description
[High-level summary understandable by non-technical people]

## Linear Issues
[ONLY include this section if Linear issues are detected from any source]
<!-- Auto-generated section based on detected Linear issues -->
[For each detected Linear issue, include:]
- Closes IA-XXX: [Issue Title]
- [Brief context from the Linear issue if available]

[IF NO LINEAR ISSUES DETECTED - Skip this section entirely]

## Change Details

[Detailed technical description of changes, organized by conceptual blocks]

[For features: modules added/modified and functionality]
[For fixes: what was broken, how it was fixed, what tests prove it]
[For refactors: what was improved and benefits]
```

**Spanish Format (lang=es):**
```markdown
## ¿Qué cambios introduce este PR?

- [x] <emoji> <Type>
<!-- ONLY include the ONE type that applies. Delete all others. Examples:
- [x] ✨ Feature
- [x] 🐛 Fix
- [x] 🔄 Refactor
- [x] 🔧 Chore
- [x] 📝 Docs
- [x] ✅ Test
-->

## Descripción
[High-level summary understandable by non-technical people]

## Linear Issues
[ONLY include this section if Linear issues are detected from any source]
<!-- Auto-generated section based on detected Linear issues -->
[For each detected Linear issue, include:]
- Closes IA-XXX: [Issue Title]
- [Brief context from the Linear issue if available]

[IF NO LINEAR ISSUES DETECTED - Skip this section entirely]

## Detalles de los cambios

[Detailed technical description of changes, organized by conceptual blocks]

[For features: modules added/modified and functionality]
[For fixes: what was broken, how it was fixed, what tests prove it]
[For refactors: what was improved and benefits]
```

#### 5. Create the PR

Use gh CLI to create the PR:

```bash
# Create PR (add --draft flag if requested)
gh pr create \
  --base "$BASE" \
  --head "$BRANCH" \
  --title "$TITLE" \
  --body "$DESCRIPTION" \
  [--draft if requested]

# Add labels if provided
if [ -n "$labels" ]; then
  # Convert comma-separated labels to individual labels
  IFS=',' read -ra LABEL_ARRAY <<< "$labels"
  for label in "${LABEL_ARRAY[@]}"; do
    # Trim whitespace and add label
    label=$(echo "$label" | xargs)
    gh pr edit --add-label "$label"
  done
fi
```

### Important Guidelines

1. **Use commits as primary source** - They contain the developer's intent
2. **Title in English** - Always lowercase after the type
3. **Description language** - Defaults to English, use `--lang es` for Spanish
4. **Focus on the main objective** - Don't get lost in auxiliary changes
5. **Mark ONLY ONE type** - Include only `[x] ✨ Feature` (or whatever applies), delete all others
6. **Be non-technical in Description** - Should be understood by PMs, clients, marketing
7. **Be technical in Details** - Include implementation details

### Implementation Steps

#### Session Context Analysis for Linear Issues

**CRITICAL**: Before analyzing git history, scan the current conversation for Linear issue references:

1. **Extract Session Context**:
   ```bash
   # This step requires the agent to analyze the conversation history
   # Look for patterns like:
   # - "working on IA-123"
   # - "this fixes IA-456"
   # - "related to Linear issue IA-789"
   # - "implementing IA-321"
   ```

2. **Use Linear MCP Integration**:
   ```bash
   # For each detected issue ID, fetch details:
   # mcp__linear__get_issue with the issue ID
   # Extract: title, description, status, assignee
   ```

3. **Priority Logic**:
   - Session context issues take highest priority
   - Branch name issues are secondary
   - Commit message issues are tertiary
   - If multiple issues detected, include all but prioritize session context for main linking

#### Full Execution Flow

Analyze the current repository state and create a PR following all the guidelines above:

1. **Scan session context** for Linear issue mentions (HIGHEST PRIORITY)
2. **Extract branch and commit references** for additional context
3. **Fetch Linear issue details** using MCP integration for detected issues
4. **Generate PR content** with automatic Linear issue linking
5. **Create GitHub PR** with enhanced description

The PR should:
- Have a clear, conventional commit formatted title
- Include a comprehensive description (English by default, Spanish if --lang es specified)
- **Automatically link detected Linear issues** with "Closes IA-XXX" syntax
- Include Linear issue context when available
- Properly categorize the type of change
- Be understandable by both technical and non-technical stakeholders

#### Session Context Examples

The agent should recognize these patterns in conversation:
- "Let's implement the user authentication feature for IA-123"
- "This PR fixes the bug reported in IA-456"
- "Working on Linear issue IA-789"
- "Addressing the requirements from IA-321"
- "This relates to IA-111 and IA-222"

**Non-Linear Workflows**: When no Linear issues are detected, the PR command should:
- Focus on commit messages and branch names for context
- Create comprehensive PR descriptions based purely on code changes
- Skip the Linear Issues section entirely
- Use session context for commit type detection (feat/fix/refactor/etc.)
