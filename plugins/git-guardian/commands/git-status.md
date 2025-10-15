---
allowed-tools: Bash(/usr/bin/git:*)
description: Understand the current state of the git repository
argument-hint: ""
---

# Git Status

Analyze the current state of the git repository and provide a structured, actionable summary.

## Commands to Execute

- Current Status: !`/usr/bin/git status`
- Current branch: !`/usr/bin/git branch --show-current`
- Current diff: !`/usr/bin/git diff HEAD origin/main`
- Recent commits: !`/usr/bin/git log --oneline -5 --pretty=format:"%h - %s"`
- Upstream status: !`/usr/bin/git status -sb`

## Files to Read
@README.md

## Task

Based on the git commands output above, provide a structured summary in the following format:

### 📊 Repository Status
- **Branch:** {current_branch}
- **Status:** {clean/uncommitted changes/untracked files/conflicts}
- **Upstream:** {ahead X commits/behind Y commits/in sync/not tracking remote}

### 📝 Recent Activity
{List last 5 commits with commit hash and message}
{Highlight any Linear issue references (IA-XXX) or Sentry references if present}

### 🔄 Pending Changes
- **Staged:** {count} files {list if < 5 files}
- **Unstaged:** {count} files {list if < 5 files}
- **Untracked:** {count} files {list if < 3 files}

### 📋 Summary of Changes
{Brief description of what's being worked on based on file changes and commit messages}
{Identify the main area: feature, fix, refactor, docs, etc.}

### ⚠️ Recommendations
{Suggest next actions based on current state:}
- If uncommitted changes: "Run `/commit` to create a logical commit"
- If ahead of origin: "Consider creating a PR with `/pr`"
- If clean state: "Ready to start new work or switch branches"
- If behind origin: "Pull latest changes before continuing"
- If untracked files: "Review and stage relevant files"

### 🔗 Related Context
{If Linear issues or Sentry errors detected in commits/branch, mention them}

Make the summary concise, actionable, and easy to scan.
