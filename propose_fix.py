#!/usr/bin/env python3
"""
Propose Fix - Propose a fix for an issue

Usage:
    python3 propose_fix.py --agent <agent_name> --fix <fix_id> --issue <issue_id> --title "Fix title" --approach "Description" --files "file1.py,file2.py" --lines "100-150"

Examples:
    python3 propose_fix.py --agent claude_code --fix fix_011 --issue _claude_issue_007 \\
        --title "Fixed template variable resolution" \\
        --approach "Modified TypeScriptParser to resolve template literals" \\
        --files "n8n_node_extractor.py" \\
        --lines "450-480"
"""

import sys
import argparse
from coordination_lib import CoordinationClient, ValidationError, CoordinationError

def main():
    parser = argparse.ArgumentParser(description="Propose a fix for an issue")
    parser.add_argument("--agent", required=True,
                       choices=["claude_code", "gemini_cli", "openai_codex"],
                       help="Agent name")
    parser.add_argument("--fix", required=True,
                       help="Fix ID (e.g., fix_011)")
    parser.add_argument("--issue", required=True,
                       help="Issue ID being fixed (e.g., _claude_issue_007, _gemini_issue_001)")
    parser.add_argument("--title", required=True,
                       help="Fix title")
    parser.add_argument("--approach", required=True,
                       help="Implementation approach description")
    parser.add_argument("--files", required=True,
                       help="Comma-separated list of files modified")
    parser.add_argument("--lines", required=False, default="",
                       help="Lines changed (e.g., '100-150' or '100-150,200-210')")
    parser.add_argument("--tested", action="store_true",
                       help="Mark as tested")
    parser.add_argument("--test-notes", default="",
                       help="Test results/notes")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"📝 Proposing {args.fix} for {args.issue}")
    print(f"{'='*60}\n")

    try:
        # Initialize client
        client = CoordinationClient(args.agent)

        # Update heartbeat
        client.update_heartbeat()

        # Parse files
        files_modified = [f.strip() for f in args.files.split(",")]

        # Build implementation dict
        implementation = {
            "approach": args.approach,
            "files_modified": files_modified,
            "lines_changed": args.lines if args.lines else "See git diff"
        }

        # Build test results
        test_results = {}
        if args.tested:
            test_results = {
                "tested": True,
                "notes": args.test_notes if args.test_notes else "Manual testing completed"
            }
        else:
            test_results = {
                "tested": False,
                "notes": "Testing pending"
            }

        # Propose fix
        success = client.propose_fix(
            fix_id=args.fix,
            issue_id=args.issue,
            title=args.title,
            implementation=implementation,
            test_results=test_results
        )

        if success:
            print(f"\n{'='*60}")
            print("✅ Fix successfully proposed!")
            print(f"{'='*60}\n")
            print(f"Fix ID: {args.fix}")
            print(f"Title: {args.title}")
            print(f"Status: proposed")
            print(f"Resolves: {args.issue}")
            print(f"Files: {', '.join(files_modified)}")
            print(f"Tested: {'✅ Yes' if args.tested else '❌ No'}")
            print("\nNext steps:")
            print("  1. Test the fix if not already done")
            print("  2. Request peer review from another agent")
            print("  3. Once verified, apply the fix:")
            print(f"     python3 apply_fix.py --agent {args.agent} --fix {args.fix}")
            print("\n  4. Regenerate reports:")
            print("     python3 generate_reports.py")
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
