#!/usr/bin/env python3
"""
Agent Start - Initialize agent session

Usage:
    python3 agent_start.py --agent <agent_name>

Examples:
    python3 agent_start.py --agent claude_code
    python3 agent_start.py --agent gemini_cli
    python3 agent_start.py --agent openai_codex
"""

import sys
import argparse
from coordination_lib import CoordinationClient, ValidationError

def main():
    parser = argparse.ArgumentParser(description="Initialize agent session")
    parser.add_argument("--agent", required=True,
                       choices=["claude_code", "gemini_cli", "openai_codex"],
                       help="Agent name")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"🤖 Starting {args.agent} session")
    print(f"{'='*60}\n")

    try:
        # Initialize client
        client = CoordinationClient(args.agent)

        # Update heartbeat
        print("📡 Updating heartbeat...")
        client.update_heartbeat()

        # Get current tasks
        my_tasks = client.get_my_tasks()
        if my_tasks:
            print(f"\n✅ You have {len(my_tasks)} task(s) in progress:")
            for task in my_tasks:
                print(f"   • {task}")
        else:
            print("\n✅ No tasks currently in progress")

        # List available issues
        print("\n📋 Available issues to claim:\n")

        for severity in ["critical", "high", "medium", "low"]:
            issues = client.list_available_issues(severity=severity)
            if issues:
                print(f"  {severity.upper()}:")
                for issue in issues:
                    status_icon = "🔴" if severity == "critical" else "🟡" if severity == "high" else "🔵"
                    print(f"    {status_icon} {issue['issue_id']}: {issue['title']}")
                print()

        # Show next steps
        print(f"{'='*60}")
        print("📌 Next Steps:")
        print(f"{'='*60}\n")
        print("To claim an issue:")
        print(f"  python3 claim_issue.py --agent {args.agent} --issue <issue_id>")
        print("\nTo propose a fix:")
        print(f"  python3 propose_fix.py --agent {args.agent} --fix <fix_id> --issue <issue_id> --title \"Fix title\"")
        print("\nTo release an issue:")
        print(f"  python3 release_issue.py --agent {args.agent} --issue <issue_id>")
        print("\nTo regenerate reports:")
        print("  python3 generate_reports.py")
        print()

    except ValidationError as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you're registered in collaboration/coordination.json")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
