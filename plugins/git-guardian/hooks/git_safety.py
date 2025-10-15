#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///

"""
Git Safety Hook for Claude Code

This hook provides Git-specific security protection by intercepting and validating
Git operations before execution. It prevents dangerous operations that could harm
your repository or workflow.

SECURITY FEATURES:
1. Push Protection:
   - Blocks direct pushes to main/master branches
   - Prevents force pushes to protected branches

2. Dangerous Operations:
   - Blocks hard resets to main/master
   - Prevents branch deletions of main/master
   - Blocks force-with-lease to protected branches

HOOK MECHANICS:
- Exit code 0: Allow tool execution
- Exit code 2: Block tool execution and show error to Claude
- Errors are gracefully handled to prevent blocking on hook failures

CUSTOMIZATION:
Modify PROTECTED_BRANCHES to add/remove protected branch names.

REQUIREMENTS:
- Python 3.8+
- uv package manager (for script execution)
- Executable permissions on the hook file
"""

import json
import re
import subprocess
import sys

# Configuration
PROTECTED_BRANCHES = ["main", "master"]


def get_current_git_branch():
    """
    Get the current git branch name.
    Returns None if not in a git repository or if there's an error.
    """
    try:
        result = subprocess.run(
            ["/usr/bin/git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, subprocess.SubprocessError, FileNotFoundError):
        pass
    return None


def is_dangerous_git_push(command):
    """
    Detect dangerous git push operations to protected branches.
    Checks both current branch and explicit branch specifications in command.
    """
    normalized = " ".join(command.lower().split())

    # Check if this is a git push command
    is_push_command = bool(re.search(r"^(git|/usr/bin/git)\s+push\b", normalized))

    if not is_push_command:
        return False

    # Get current branch
    current_branch = get_current_git_branch()

    # Block any push from protected branches
    if current_branch in PROTECTED_BRANCHES:
        return True

    # Build patterns for protected branches
    protected_patterns = []
    for branch in PROTECTED_BRANCHES:
        protected_patterns.extend([
            rf"\bgit\s+push.*\b{branch}\b",
            rf"/usr/bin/git\s+push.*\b{branch}\b",
            rf"\bgit\s+push\s+origin\s+{branch}\b",
            rf"/usr/bin/git\s+push\s+origin\s+{branch}\b",
            rf"\bgit\s+push.*--force.*\b{branch}\b",
            rf"\bgit\s+push.*-f.*\b{branch}\b",
            rf"/usr/bin/git\s+push.*--force.*\b{branch}\b",
            rf"/usr/bin/git\s+push.*-f.*\b{branch}\b",
        ])

    for pattern in protected_patterns:
        if re.search(pattern, normalized):
            return True

    return False


def is_dangerous_git_operation(command):
    """
    Detect other dangerous git operations on protected branches.
    """
    normalized = " ".join(command.lower().split())

    # Build patterns for each protected branch
    dangerous_patterns = []
    for branch in PROTECTED_BRANCHES:
        dangerous_patterns.extend([
            rf"\bgit\s+reset\s+--hard\s+origin/{branch}",
            rf"/usr/bin/git\s+reset\s+--hard\s+origin/{branch}",
            rf"\bgit\s+push\s+--force-with-lease.*\b{branch}\b",
            rf"/usr/bin/git\s+push\s+--force-with-lease.*\b{branch}\b",
            rf"\bgit\s+push.*--delete.*\b{branch}\b",
            rf"/usr/bin/git\s+push.*--delete.*\b{branch}\b",
        ])

    for pattern in dangerous_patterns:
        if re.search(pattern, normalized):
            return True

    return False


def main():
    try:
        # Read input from stdin
        raw_input = sys.stdin.read()

        # Try to parse JSON
        try:
            input_data = json.loads(raw_input)
        except json.JSONDecodeError as e:
            print(f"JSON decode error in git safety hook: {e}", file=sys.stderr)
            sys.exit(0)  # Don't block execution on JSON errors

        tool_name = input_data.get("tool_name", "")
        tool_input = input_data.get("tool_input", {})

        # Only check Bash commands for Git operations
        if tool_name == "Bash":
            command = tool_input.get("command", "")

            # Block dangerous git push operations to protected branches
            if is_dangerous_git_push(command):
                current_branch = get_current_git_branch()
                print(
                    f"BLOCKED: Direct push to protected branch ({', '.join(PROTECTED_BRANCHES)}) is not allowed",
                    file=sys.stderr,
                )
                if current_branch in PROTECTED_BRANCHES:
                    print(
                        f"You are currently on branch '{current_branch}'",
                        file=sys.stderr,
                    )
                    print(
                        "Please create a feature branch and submit a pull request instead",
                        file=sys.stderr,
                    )
                    print(
                        "Example: git checkout -b feature/your-feature-name",
                        file=sys.stderr,
                    )
                else:
                    print(
                        "Please create a feature branch and submit a pull request instead",
                        file=sys.stderr,
                    )
                print(f"Blocked command: {command}", file=sys.stderr)
                sys.exit(2)  # Exit code 2 blocks tool call and shows error to Claude

            # Block other dangerous git operations
            if is_dangerous_git_operation(command):
                print(
                    "BLOCKED: Dangerous git operation on protected branch detected and prevented",
                    file=sys.stderr,
                )
                print(f"Protected branches: {', '.join(PROTECTED_BRANCHES)}", file=sys.stderr)
                print(f"Command: {command}", file=sys.stderr)
                sys.exit(2)  # Exit code 2 blocks tool call and shows error to Claude

        sys.exit(0)  # Allow execution

    except Exception as e:
        # Handle any other errors gracefully - don't block execution
        print(f"Git safety hook error (allowing execution): {e}", file=sys.stderr)
        sys.exit(0)


if __name__ == "__main__":
    main()
