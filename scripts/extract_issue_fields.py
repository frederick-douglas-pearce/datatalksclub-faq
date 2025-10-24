#!/usr/bin/env python3
"""
GitHub Actions helper script to extract fields from FAQ issue body

Reads issue body from stdin and outputs to GitHub Actions format.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to import faq_automation
sys.path.insert(0, str(Path(__file__).parent.parent))

from faq_automation.cli import parse_full_issue_body


def write_github_output(key: str, value: str) -> None:
    """Write output to GitHub Actions in multiline format"""
    github_output = os.environ.get('GITHUB_OUTPUT')

    if not github_output:
        # Local testing mode
        print(f"{key}: {value}")
        return

    with open(github_output, 'a') as f:
        # Use heredoc format for multiline values
        f.write(f"{key}<<EOF\n{value}\nEOF\n")


def main():
    """Main entry point"""
    try:
        # Read issue body from stdin
        issue_body = sys.stdin.read()

        if not issue_body.strip():
            print("Error: Empty issue body provided", file=sys.stderr)
            sys.exit(1)

        # Parse using Python function
        course, question, answer = parse_full_issue_body(issue_body)

        # Write to GitHub Actions output
        write_github_output('course', course)
        write_github_output('question', question)
        write_github_output('answer', answer)

        print("✅ Successfully extracted issue fields")
        print(f"   Course: {course}")
        print(f"   Question: {question[:50]}{'...' if len(question) > 50 else ''}")
        print(f"   Answer: {answer[:50]}{'...' if len(answer) > 50 else ''}")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        print("Please ensure the issue body has all required sections:", file=sys.stderr)
        print("  - ### Course", file=sys.stderr)
        print("  - ### Question", file=sys.stderr)
        print("  - ### Answer", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
