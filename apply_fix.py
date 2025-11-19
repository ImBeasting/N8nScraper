#!/usr/bin/env python3
"""
Apply Fix - Mark a fix as applied and resolve the issue

Usage:
    python3 apply_fix.py --agent <agent_name> --fix <fix_id>

Examples:
    python3 apply_fix.py --agent claude_code --fix fix_011
    python3 apply_fix.py --agent gemini_cli --fix fix_012
"""

import sys
import argparse
from coordination_lib import CoordinationClient, ValidationError, CoordinationError

def main():
    parser = argparse.ArgumentParser(description="Mark a fix as applied")
    parser.add_argument("--agent", required=True,
                       choices=["claude_code", "gemini_cli", "openai_codex"],
                       help="Agent name")
    parser.add_argument("--fix", required=True,
                       help="Fix ID (e.g., fix_011)")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"✅ Applying {args.fix} by {args.agent}")
    print(f"{'='*60}\n")

    try:
        # Initialize client
        client = CoordinationClient(args.agent)

        # Update heartbeat
        client.update_heartbeat()

        # Apply fix
        success = client.apply_fix(args.fix)

        if success:
            print(f"\n{'='*60}")
            print("✅ Fix successfully applied!")
            print(f"{'='*60}\n")
            print(f"• {args.fix} moved from proposed/ to applied/")
            print(f"• Related issue marked as resolved")
            print(f"• {args.agent} added as verifier")
            print("\nNext steps:")
            print("  1. Regenerate reports to reflect changes:")
            print("     python3 generate_reports.py")
            print("\n  2. Check system status:")
            print("     ./health_check.sh")
            print()

    except ValidationError as e:
        print(f"\n❌ Validation Error: {e}")
        print("\nMake sure the fix exists in fixes/proposed/")
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
