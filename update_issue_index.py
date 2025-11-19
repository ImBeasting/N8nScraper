
import json
from pathlib import Path

BASE_DIR = Path("/media/tyler/fastraid/Projects/n8n Node Scrapper")
ISSUES_DIR = BASE_DIR / "issues"
INDEX_FILE = ISSUES_DIR / "index.json"

def update_issue_index():
    """Update the issue index with all issues from the issues directory."""
    issues = []
    for severity in ["critical", "high", "medium", "low"]:
        severity_dir = ISSUES_DIR / severity
        if not severity_dir.exists():
            continue
        for issue_file in severity_dir.glob("*.json"):
            try:
                with open(issue_file, "r", encoding="utf-8") as f:
                    issue_data = json.load(f)
                    issues.append({
                        "issue_id": issue_data["issue_id"],
                        "file_path": str(issue_file.relative_to(BASE_DIR)),
                    })
            except json.JSONDecodeError as e:
                print(f"⚠️  Skipping malformed JSON: {issue_file.name} - {e}")
                continue

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        index_data = json.load(f)

    index_data["issues"] = issues
    index_data["total_issues"] = len(issues)
    index_data["last_updated"] = "2025-11-06T22:00:00.000000"

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=4)

if __name__ == "__main__":
    update_issue_index()
    print(f"Successfully updated {INDEX_FILE}")
