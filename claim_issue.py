#!/usr/bin/env python3
"""
Claim Issue - Claim an issue for work

Usage:
    python3 claim_issue.py --agent <agent_name> --issue <issue_id>

Examples:
    python3 claim_issue.py --agent claude_code --issue _claude_issue_007
    python3 claim_issue.py --agent gemini_cli --issue _gemini_issue_001
"""

import sys
import argparse
from coordination_lib import CoordinationClient, ValidationError, CoordinationError, LockAcquisitionError

def main():
    parser = argparse.ArgumentParser(description="Claim an issue for work")
    parser.add_argument("--agent", required=True,
                       choices=["claude_code", "gemini_cli", "openai_codex"],
                       help="Agent name")
    parser.add_argument("--issue", required=True,
                       help="Issue ID (e.g., _claude_issue_007, _gemini_issue_001)")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"🔒 Claiming {args.issue} for {args.agent}")
    print(f"{'='*60}\n")

    try:
        # Initialize client
        client = CoordinationClient(args.agent)

        # Update heartbeat
        client.update_heartbeat()

        # Claim issue
        success = client.claim_issue(args.issue)

        if success:
            print(f"\n{'='*60}")
            print("✅ Issue successfully claimed!")
            print(f"{'='*60}\n")
            print(f"You can now work on {args.issue}")
            print("\nNext steps:")
            print("  1. Investigate the issue")
            print("  2. Develop a fix")
            print("  3. Test the fix")
            print("  4. Propose the fix:")
            print(f"     python3 propose_fix.py --agent {args.agent} --fix fix_XXX --issue {args.issue} --title \"Fix title\"")
            print("\nOr release the issue if you can't complete it:")
            print(f"  python3 release_issue.py --agent {args.agent} --issue {args.issue}")
            print()

    except ValidationError as e:
        print(f"\n❌ Validation Error: {e}")
        sys.exit(1)
    except CoordinationError as e:
        print(f"\n❌ Coordination Error: {e}")
        sys.exit(1)
    except LockAcquisitionError as e:
        print(f"\n❌ Lock Error: {e}")
        print("\nThe issue may be locked by another agent.")
        print("Try again in a few seconds, or check health_check.sh for stale locks.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
