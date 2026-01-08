#!/usr/bin/env python3
"""
Issue Naming System Migration Script
=====================================
Migrates from global issue numbering (issue_NNN) to per-agent sequential numbering (_agent_issue_NNN)

Usage:
    python3 migrate_issue_naming.py [--dry-run]
"""

import json
import os
import shutil
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Tuple
from collections import defaultdict

# Configuration
BASE_DIR = Path(__file__).parent.resolve()
ISSUES_DIR = BASE_DIR / "issues"
BACKUP_DIR = BASE_DIR / "issues_backup_20251106"
MAPPING_FILE = BASE_DIR / "issue_migration_mapping.json"

# Agent name mappings
AGENT_SHORT_NAMES = {
    "claude_code": "claude",
    "gemini_cli": "gemini",
    "openai_codex": "openai"
}

class IssueMigrator:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.issues = []
        self.mapping = defaultdict(list)
        self.stats = {
            "total_issues": 0,
            "by_agent": defaultdict(int),
            "renamed_files": 0,
            "updated_contents": 0,
            "errors": []
        }

    def load_all_issues(self):
        """Load all issue JSON files from all severity directories"""
        print("=" * 70)
        print("STEP 1: Loading all issue files...")
        print("=" * 70)

        severities = ["critical", "high", "medium", "low"]
        for severity in severities:
            severity_dir = ISSUES_DIR / severity
            if not severity_dir.exists():
                continue

            for json_file in severity_dir.glob("*.json"):
                try:
                    with open(json_file, 'r') as f:
                        data = json.load(f)

                    # Extract metadata
                    issue_info = {
                        "old_file_path": json_file,
                        "old_filename": json_file.name,
                        "severity": severity,
                        "issue_id": data.get("issue_id", "unknown"),
                        "title": data.get("title", ""),
                        "created_by": data.get("metadata", {}).get("created_by", "unknown"),
                        "created_at": data.get("metadata", {}).get("created_at", ""),
                        "data": data
                    }

                    self.issues.append(issue_info)
                    self.stats["total_issues"] += 1

                except Exception as e:
                    error_msg = f"Error loading {json_file}: {e}"
                    print(f"  ❌ {error_msg}")
                    self.stats["errors"].append(error_msg)

        print(f"✅ Loaded {self.stats['total_issues']} issue files")
        print()

    def build_migration_mapping(self):
        """Group issues by creator and assign sequential numbers"""
        print("=" * 70)
        print("STEP 2: Building migration mapping...")
        print("=" * 70)

        # Group by creator
        by_creator = defaultdict(list)
        for issue in self.issues:
            creator = issue["created_by"]
            by_creator[creator].append(issue)

        # Sort each group by creation timestamp and assign new sequential IDs
        for creator, creator_issues in by_creator.items():
            # Sort by created_at timestamp
            creator_issues.sort(key=lambda x: x["created_at"])

            short_name = AGENT_SHORT_NAMES.get(creator, creator)

            for idx, issue in enumerate(creator_issues, start=1):
                new_issue_id = f"_{short_name}_issue_{idx:03d}"

                # Build new filename
                old_filename = issue["old_filename"]
                # Remove old issue_id pattern and add new one
                # Pattern: issue_XXX_description.json -> _agent_issue_XXX_description.json
                desc_match = re.search(r'issue_\d+_(.*?)\.json$', old_filename)
                if desc_match:
                    description = desc_match.group(1)
                    new_filename = f"{new_issue_id}_{description}.json"
                else:
                    # Fallback: just prepend new ID
                    new_filename = f"{new_issue_id}_{old_filename}"

                new_file_path = ISSUES_DIR / issue["severity"] / new_filename

                mapping_entry = {
                    "old_issue_id": issue["issue_id"],
                    "new_issue_id": new_issue_id,
                    "old_filename": old_filename,
                    "new_filename": new_filename,
                    "old_file_path": str(issue["old_file_path"]),
                    "new_file_path": str(new_file_path),
                    "severity": issue["severity"],
                    "title": issue["title"],
                    "created_at": issue["created_at"],
                    "sequential_number": idx
                }

                self.mapping[creator].append(mapping_entry)
                self.stats["by_agent"][creator] += 1

                # Update issue object with new info
                issue["new_issue_id"] = new_issue_id
                issue["new_filename"] = new_filename
                issue["new_file_path"] = new_file_path

        # Print summary
        for creator, entries in self.mapping.items():
            short_name = AGENT_SHORT_NAMES.get(creator, creator)
            print(f"  {creator} → {len(entries)} issues ({short_name}_issue_001 to {short_name}_issue_{len(entries):03d})")

        print()

        # Save mapping to file
        with open(MAPPING_FILE, 'w') as f:
            json.dump(dict(self.mapping), f, indent=2)

        print(f"✅ Migration mapping saved to: {MAPPING_FILE}")
        print()

    def rename_files_and_update_contents(self):
        """Rename all issue files and update their internal issue_id"""
        print("=" * 70)
        print("STEP 3: Renaming files and updating contents...")
        print("=" * 70)

        if self.dry_run:
            print("🔍 DRY RUN MODE - No files will be modified")
            print()

        for issue in self.issues:
            old_path = issue["old_file_path"]
            new_path = issue["new_file_path"]
            old_id = issue["issue_id"]
            new_id = issue["new_issue_id"]

            try:
                # Update JSON content
                data = issue["data"]
                data["issue_id"] = new_id

                if self.dry_run:
                    print(f"  [DRY RUN] Would rename: {old_path.name} → {new_path.name}")
                    print(f"            Would update issue_id: {old_id} → {new_id}")
                else:
                    # Write updated content to new file
                    with open(new_path, 'w') as f:
                        json.dump(data, f, indent=2)

                    # Remove old file if different from new file
                    if old_path != new_path:
                        old_path.unlink()

                    print(f"  ✅ {old_id} → {new_id}: {new_path.name}")
                    self.stats["renamed_files"] += 1
                    self.stats["updated_contents"] += 1

            except Exception as e:
                error_msg = f"Error migrating {old_path.name}: {e}"
                print(f"  ❌ {error_msg}")
                self.stats["errors"].append(error_msg)

        print()
        if not self.dry_run:
            print(f"✅ Renamed {self.stats['renamed_files']} files")
            print(f"✅ Updated {self.stats['updated_contents']} issue IDs")
        print()

    def update_index_json(self):
        """Update issues/index.json with new issue IDs and file paths"""
        print("=" * 70)
        print("STEP 4: Updating issues/index.json...")
        print("=" * 70)

        index_path = ISSUES_DIR / "index.json"

        try:
            with open(index_path, 'r') as f:
                index_data = json.load(f)

            # Create mapping from old issue_id to new issue_id
            old_to_new = {}
            for creator_entries in self.mapping.values():
                for entry in creator_entries:
                    old_to_new[entry["old_issue_id"]] = {
                        "new_issue_id": entry["new_issue_id"],
                        "new_file_path": entry["new_file_path"].replace(str(BASE_DIR) + "/", "")
                    }

            # Update each issue entry in index
            updated_count = 0
            for issue_entry in index_data["issues"]:
                old_id = issue_entry["issue_id"]
                if old_id in old_to_new:
                    issue_entry["issue_id"] = old_to_new[old_id]["new_issue_id"]
                    issue_entry["file_path"] = old_to_new[old_id]["new_file_path"]
                    updated_count += 1

            # Update timestamp
            index_data["last_updated"] = datetime.now().isoformat() + "Z"

            if self.dry_run:
                print(f"  [DRY RUN] Would update {updated_count} entries in index.json")
            else:
                with open(index_path, 'w') as f:
                    json.dump(index_data, f, indent=4)
                print(f"  ✅ Updated {updated_count} entries in index.json")

        except Exception as e:
            error_msg = f"Error updating index.json: {e}"
            print(f"  ❌ {error_msg}")
            self.stats["errors"].append(error_msg)

        print()

    def update_fix_references(self):
        """Update any issue_id references in fixes/*.json files"""
        print("=" * 70)
        print("STEP 5: Updating fix file references...")
        print("=" * 70)

        fixes_dir = BASE_DIR / "fixes"
        if not fixes_dir.exists():
            print("  ℹ️  No fixes directory found, skipping")
            print()
            return

        # Create mapping from old to new issue IDs
        old_to_new = {}
        for creator_entries in self.mapping.values():
            for entry in creator_entries:
                old_to_new[entry["old_issue_id"]] = entry["new_issue_id"]

        updated_count = 0
        for fix_dir in ["applied", "proposed"]:
            fix_subdir = fixes_dir / fix_dir
            if not fix_subdir.exists():
                continue

            for fix_file in fix_subdir.glob("*.json"):
                try:
                    with open(fix_file, 'r') as f:
                        fix_data = json.load(f)

                    # Update issue_id if it references an old issue
                    if "issue_id" in fix_data and fix_data["issue_id"] in old_to_new:
                        old_id = fix_data["issue_id"]
                        new_id = old_to_new[old_id]
                        fix_data["issue_id"] = new_id

                        if not self.dry_run:
                            with open(fix_file, 'w') as f:
                                json.dump(fix_data, f, indent=2)
                            print(f"  ✅ Updated {fix_file.name}: {old_id} → {new_id}")
                            updated_count += 1
                        else:
                            print(f"  [DRY RUN] Would update {fix_file.name}: {old_id} → {new_id}")

                except Exception as e:
                    error_msg = f"Error updating {fix_file}: {e}"
                    print(f"  ❌ {error_msg}")
                    self.stats["errors"].append(error_msg)

        if updated_count == 0:
            print("  ℹ️  No fix files needed updates")

        print()

    def print_summary(self):
        """Print migration summary"""
        print("=" * 70)
        print("MIGRATION SUMMARY")
        print("=" * 70)
        print()
        print(f"Total Issues Migrated: {self.stats['total_issues']}")
        print()
        print("By Agent:")
        for agent, count in self.stats["by_agent"].items():
            short_name = AGENT_SHORT_NAMES.get(agent, agent)
            print(f"  {agent}: {count} issues ({short_name}_issue_001 to {short_name}_issue_{count:03d})")
        print()

        if not self.dry_run:
            print(f"Files Renamed: {self.stats['renamed_files']}")
            print(f"Contents Updated: {self.stats['updated_contents']}")
            print()

        if self.stats["errors"]:
            print(f"⚠️  Errors: {len(self.stats['errors'])}")
            for error in self.stats["errors"]:
                print(f"  - {error}")
            print()
        else:
            print("✅ No errors encountered")
            print()

        print("=" * 70)
        if self.dry_run:
            print("DRY RUN COMPLETE - No files were modified")
        else:
            print("✅ MIGRATION COMPLETE")
        print("=" * 70)

    def run(self):
        """Execute full migration process"""
        self.load_all_issues()
        self.build_migration_mapping()
        self.rename_files_and_update_contents()
        self.update_index_json()
        self.update_fix_references()
        self.print_summary()


def main():
    import sys

    dry_run = "--dry-run" in sys.argv

    print()
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "ISSUE NAMING SYSTEM MIGRATION" + " " * 24 + "║")
    print("╚" + "═" * 68 + "╝")
    print()

    if dry_run:
        print("🔍 Running in DRY RUN mode - no files will be modified")
        print()

    # Verify backup exists
    if not BACKUP_DIR.exists():
        print("❌ ERROR: Backup directory not found!")
        print(f"   Expected: {BACKUP_DIR}")
        print("   Please create backup before running migration.")
        sys.exit(1)

    print(f"✅ Backup verified: {BACKUP_DIR}")
    print()

    # Run migration
    migrator = IssueMigrator(dry_run=dry_run)
    migrator.run()

    print()
    print("Next Steps:")
    if dry_run:
        print("  1. Review the dry run output above")
        print("  2. Run without --dry-run to execute migration:")
        print("     python3 migrate_issue_naming.py")
    else:
        print("  1. Update Python scripts (coordination_lib.py, etc.)")
        print("  2. Validate migration with test claims")
        print("  3. Regenerate reports")
        print("  4. Update documentation")
    print()


if __name__ == "__main__":
    main()
