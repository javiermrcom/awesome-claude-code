# Git Guardian - Workflow Examples

This document provides real-world workflow examples using Git Guardian.

## Example 1: Feature Development with Linear

### Scenario
You're working on Linear issue IA-456 to add payment integration.

### Workflow

```bash
# 1. Check current repository state
/git-status

# Output:
# 📊 Repository Status
# - Branch: main
# - Status: clean
# - Upstream: in sync

# 2. Mention the Linear issue in conversation
"I'm working on IA-456 to add Stripe payment integration"

# 3. Make your code changes
# ... edit files ...

# 4. Get branch name suggestion
/branch-name

# Output: feat/jmr/add-stripe-payment-integration

# 5. Create branch with suggested name
git checkout -b feat/jmr/add-stripe-payment-integration

# 6. Create intelligent commit (auto-detects IA-456)
/commit

# Output:
# Staging: payment_service.py, payment_test.py, README.md
#
# Commit created:
# feat: add stripe payment integration
#
# - Implement PaymentService class
# - Add Stripe API client wrapper
# - Add comprehensive unit tests
# - Update README with setup instructions
#
# Refs: IA-456

# 7. Push to remote
git push -u origin feat/jmr/add-stripe-payment-integration

# 8. Create pull request (auto-links Linear issue)
/pr --labels "feature,backend"

# Output:
# PR created: https://github.com/org/repo/pull/123
# Title: feat: add stripe payment integration
# Description includes: "Closes IA-456"
```

---

## Example 2: Bug Fix with Sentry

### Scenario
Sentry reported error SENTRY-456 about null user object in payment flow.

### Workflow

```bash
# 1. Mention Sentry error in conversation
"Investigating Sentry error SENTRY-456 about null user in payment service"

# 2. Check repository state
/git-status

# 3. Make the fix
# ... add null checks ...

# 4. Get branch name
/branch-name

# Output: fix/jmr/handle-null-user-payment

# 5. Create branch
git checkout -b fix/jmr/handle-null-user-payment

# 6. Commit with auto Sentry reference
/commit

# Output:
# Commit created:
# fix: handle null user object in payment flow
#
# - Add null check before accessing user.id
# - Return early with proper error message
# - Add defensive validation
# - Add test for null user scenario
#
# Fixes: SENTRY-456

# 7. Create PR
/pr --labels "bug,urgent"
```

---

## Example 3: Combined Linear + Sentry

### Scenario
Working on Linear issue IA-789 that also fixes Sentry error SENTRY-789.

### Workflow

```bash
# 1. Mention both in conversation
"Working on IA-789 to improve error handling, which should also fix SENTRY-789"

# 2. Make changes and commit
/commit

# Output:
# Commit created:
# fix: improve error handling in payment service
#
# - Add comprehensive error catching
# - Implement retry logic
# - Add detailed error logging
# - Improve user feedback messages
#
# Refs: IA-789
# Fixes: SENTRY-789

# 3. Create PR (auto-links both)
/pr
```

---

## Example 4: Protected Operations

### Scenario
Accidentally trying to push to main branch.

### Workflow

```bash
# Try to push to main
git push origin main

# Output (from security hook):
# BLOCKED: Direct push to main/master branch is not allowed
# You are currently on branch 'main'
# Please create a feature branch and submit a pull request instead
# Example: git checkout -b feature/your-feature-name
# Blocked command: git push origin main

# Safe workflow
git checkout -b feat/jmr/new-feature
# ... make changes ...
/commit
git push origin feat/jmr/new-feature  # ✅ Allowed
/pr
```

---

## Example 5: Breaking Changes

### Scenario
Refactoring API that introduces breaking changes.

### Workflow

```bash
# Make breaking changes
# ... refactor API ...

# Commit with breaking change notation
/commit --breaking

# Output:
# Commit created:
# refactor!: restructure payment API response format
#
# - Change from array to object structure
# - Add metadata field for pagination
# - Include timestamp in all responses
# - Update API documentation
#
# BREAKING CHANGE: Response format changed from array to object.
# Clients need to update parsing logic.

# Create PR
/pr --labels "breaking-change,api"
```

---

## Example 6: Dry Run Mode

### Scenario
Preview what will be committed before executing.

### Workflow

```bash
# Make various changes
# ... edit multiple files ...

# Preview commit without executing
/commit --dry-run

# Output:
# 📋 PREVIEW MODE - No changes will be made
#
# Would stage:
# - payment_service.py (modified)
# - payment_test.py (modified)
# - README.md (modified)
#
# Would NOT stage:
# - config.py (unrelated changes)
# - .env (sensitive file - automatically excluded)
#
# Suggested commit message:
# feat: add payment processing
#
# - Implement PaymentService
# - Add comprehensive tests
# - Update documentation
#
# Run /commit to execute this commit

# If happy with preview, execute
/commit
```

---

## Example 7: Multiple Commits

### Scenario
Changes span multiple logical units.

### Workflow

```bash
# Made changes to authentication AND payments

# First commit (authentication)
"Working on authentication improvements"
/commit
# Creates: refactor: improve authentication flow

# Second commit (payments)
"Now working on payment integration"
/commit
# Creates: feat: add payment integration

# Create PR for both
/pr
```

---

## Example 8: Status-Driven Workflow

### Scenario
Using /git-status to guide your workflow.

### Workflow

```bash
# Check status
/git-status

# Output:
# 📊 Repository Status
# - Branch: feat/jmr/payment-integration
# - Status: Uncommitted changes
# - Upstream: Ahead 2 commits
#
# 🔄 Pending Changes
# - Staged: 0 files
# - Unstaged: 5 files
# - Untracked: 2 files
#
# ⚠️ Recommendations
# - Run /commit to create a logical commit
# - After commit, run /pr to create pull request

# Follow recommendation
/commit

# Check status again
/git-status

# Output:
# ⚠️ Recommendations
# - Run /pr to create pull request (ahead 3 commits)

# Create PR
/pr
```

---

## Tips & Tricks

### 1. Conversation Context is Key

Git Guardian relies on conversation context for auto-detection. Always mention:
- Linear issues: "Working on IA-123"
- Sentry errors: "Fixing SENTRY-456"

### 2. Let Commands Auto-Group

Don't manually stage files. Let `/commit` intelligently group:
- Source + Tests together
- Docs separately
- Config separately

### 3. Use Branch Name Suggestions

Always use `/branch-name` for consistency:
- Format is automatic
- Initials auto-detected
- Type based on changes

### 4. Preview First

Use `--dry-run` when unsure:
```bash
/commit --dry-run  # Preview
/commit            # Execute
```

### 5. Security Hook is Active

Remember the hook protects you:
- ❌ Can't push to main/master
- ❌ Can't force push protected branches
- ❌ Can't access .env files
- ❌ Can't rm -rf dangerous paths

This is by design!

---

## Common Patterns

### Pattern 1: Quick Fix
```bash
"Fixing typo in README"
/branch-name → docs/jmr/fix-readme-typo
/commit → docs: fix typo in installation section
/pr → Quick PR with auto-generated description
```

### Pattern 2: Feature Development
```bash
"Working on IA-456"
/branch-name → feat/jmr/payment-integration
# ... develop feature ...
/commit → feat: add payment integration (Refs: IA-456)
/pr → PR with "Closes IA-456"
```

### Pattern 3: Bug Investigation
```bash
"Investigating SENTRY-789"
# ... find and fix bug ...
/commit → fix: resolve payment timeout (Fixes: SENTRY-789)
/pr --labels "bug,urgent" → Quick hotfix PR
```

---

**These examples demonstrate real-world usage of Git Guardian in daily development workflows.**
