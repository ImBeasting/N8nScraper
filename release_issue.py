#!/usr/bin/env python3
"""
Release Issue - Release claim on an issue

Usage:
    python3 release_issue.py --agent <agent_name> --issue <issue_id>

Examples:
    python3 release_issue.py --agent claude_code --issue _claude_issue_007
    python3 release_issue.py --agent gemini_cli --issue _gemini_issue_001
"""

import sys
import argparse
from coordination_lib import CoordinationClient, ValidationError, CoordinationError

def main():
    parser = argparse.ArgumentParser(description="Release claim on an issue")
    parser.add_argument("--agent", required=True,
                       choices=["claude_code", "gemini_cli", "openai_codex"],
                       help="Agent name")
    parser.add_argument("--issue", required=True,
                       help="Issue ID (e.g., _claude_issue_007, _gemini_issue_001)")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"🔓 Releasing {args.issue} by {args.agent}")
    print(f"{'='*60}\n")

    try:
        # Initialize client
        client = CoordinationClient(args.agent)

        # Update heartbeat
        client.update_heartbeat()

        # Release issue
        success = client.release_issue(args.issue)

        if success:
            print(f"\n{'='*60}")
            print("✅ Issue successfully released!")
            print(f"{'='*60}\n")
            print(f"{args.issue} is now available for other agents to claim")
            print()

    except ValidationError as e:
        print(f"\n❌ Validation Error: {e}")
        sys.exit(1)
    except CoordinationError as e:
        print(f"\n❌ Coordination Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
