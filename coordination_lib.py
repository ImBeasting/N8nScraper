#!/usr/bin/env python3
"""
Multi-Agent Coordination Library

Provides atomic operations for coordinating work between multiple AI agents.
Handles locking, issue claiming, fix proposals, and consistency validation.
"""

import json
import os
import time
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import fcntl
import errno

# Project paths - use relative path from script location
PROJECT_ROOT = Path(__file__).parent.resolve()
COLLABORATION_DIR = PROJECT_ROOT / "collaboration"
ISSUES_DIR = PROJECT_ROOT / "issues"
FIXES_DIR = PROJECT_ROOT / "fixes"
REPORTS_DIR = PROJECT_ROOT / "reports"

# Lock timeout
LOCK_TIMEOUT_MINUTES = 60

class CoordinationError(Exception):
    """Base exception for coordination errors"""
    pass

class LockAcquisitionError(CoordinationError):
    """Failed to acquire lock"""
    pass

class ValidationError(CoordinationError):
    """Validation failed"""
    pass


class CoordinationClient:
    """Main coordination client for multi-agent collaboration"""

    def __init__(self, agent_name: str):
        """
        Initialize coordination client for an agent.

        Args:
            agent_name: Name of the agent (claude_code, gemini_cli, openai_codex)
        """
        self.agent_name = agent_name
        self.coordination_file = COLLABORATION_DIR / "coordination.json"
        self.heartbeat_file = COLLABORATION_DIR / "agent_heartbeats.json"
        self.audit_log = COLLABORATION_DIR / "audit_log.jsonl"

        # Validate agent is registered
        self._validate_agent()

    def _validate_agent(self):
        """Ensure agent is registered in coordination.json"""
        coord = self._load_coordination()
        if self.agent_name not in coord.get("agents", {}):
            raise ValidationError(f"Agent '{self.agent_name}' not registered in coordination.json")

    def _load_coordination(self) -> Dict[str, Any]:
        """Load coordination.json with file locking"""
        with open(self.coordination_file, 'r') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_SH)
            data = json.load(f)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
        return data

    def _save_coordination(self, data: Dict[str, Any]):
        """Save coordination.json with file locking"""
        with open(self.coordination_file, 'w') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            json.dump(data, f, indent=2)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)

    def _log_audit(self, action: str, success: bool, message: str, **kwargs):
        """Append to audit log"""
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "agent": self.agent_name,
            "action": action,
            "success": success,
            "message": message,
            **kwargs
        }
        with open(self.audit_log, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    def update_heartbeat(self):
        """Update agent heartbeat timestamp"""
        try:
            if self.heartbeat_file.exists():
                with open(self.heartbeat_file, 'r') as f:
                    heartbeats = json.load(f)
            else:
                heartbeats = {}

            heartbeats[self.agent_name] = {
                "last_seen": datetime.utcnow().isoformat() + "Z",
                "status": "active"
            }

            with open(self.heartbeat_file, 'w') as f:
                json.dump(heartbeats, f, indent=2)

            return True
        except Exception as e:
            print(f"⚠️  Failed to update heartbeat: {e}")
            return False

    def acquire_lock(self, resource_id: str, timeout_seconds: int = 30) -> bool:
        """
        Acquire atomic lock for a resource (issue or fix).

        Args:
            resource_id: ID of resource to lock (e.g., '_claude_issue_007')
            timeout_seconds: How long to wait for lock

        Returns:
            True if lock acquired, False otherwise

        Raises:
            LockAcquisitionError: If lock cannot be acquired
        """
        lock_path = COLLABORATION_DIR / f"{resource_id}.lock"
        start_time = time.time()

        while True:
            try:
                # Atomic operation: create directory only if it doesn't exist
                lock_path.mkdir(exist_ok=False)

                # Write lock metadata
                lock_info = {
                    "locked_by": self.agent_name,
                    "locked_at": datetime.utcnow().isoformat() + "Z",
                    "expires_at": (datetime.utcnow() + timedelta(minutes=LOCK_TIMEOUT_MINUTES)).isoformat() + "Z"
                }
                with open(lock_path / "lock_info.json", 'w') as f:
                    json.dump(lock_info, f, indent=2)

                self._log_audit("acquire_lock", True, f"Acquired lock for {resource_id}", resource_id=resource_id)
                return True

            except FileExistsError:
                # Lock exists, check if stale
                if self._is_lock_stale(lock_path):
                    print(f"🔓 Found stale lock on {resource_id}, removing...")
                    self.release_lock(resource_id, force=True)
                    continue

                # Lock held by another agent
                elapsed = time.time() - start_time
                if elapsed >= timeout_seconds:
                    raise LockAcquisitionError(f"Could not acquire lock for {resource_id} after {timeout_seconds}s")

                print(f"⏳ Waiting for lock on {resource_id}... ({int(elapsed)}s)")
                time.sleep(2)

    def _is_lock_stale(self, lock_path: Path) -> bool:
        """Check if a lock has expired"""
        lock_info_file = lock_path / "lock_info.json"
        if not lock_info_file.exists():
            return True  # No metadata = stale

        try:
            with open(lock_info_file, 'r') as f:
                lock_info = json.load(f)

            expires_at = datetime.fromisoformat(lock_info["expires_at"].replace("Z", "+00:00"))
            return datetime.utcnow().replace(tzinfo=expires_at.tzinfo) > expires_at
        except:
            return True  # Error reading = stale

    def release_lock(self, resource_id: str, force: bool = False):
        """
        Release lock for a resource.

        Args:
            resource_id: ID of resource to unlock
            force: Force unlock even if held by another agent
        """
        lock_path = COLLABORATION_DIR / f"{resource_id}.lock"

        if not lock_path.exists():
            return  # Already unlocked

        # Verify we own the lock (unless force)
        if not force:
            lock_info_file = lock_path / "lock_info.json"
            if lock_info_file.exists():
                with open(lock_info_file, 'r') as f:
                    lock_info = json.load(f)
                if lock_info.get("locked_by") != self.agent_name:
                    raise CoordinationError(f"Cannot release lock held by {lock_info.get('locked_by')}")

        # Remove lock directory
        if lock_info_file.exists():
            lock_info_file.unlink()
        lock_path.rmdir()

        self._log_audit("release_lock", True, f"Released lock for {resource_id}", resource_id=resource_id, force=force)

    def claim_issue(self, issue_id: str) -> bool:
        """
        Claim an issue for work.

        Args:
            issue_id: ID of issue to claim (e.g., '_claude_issue_007')

        Returns:
            True if claimed successfully
        """
        # Find issue file
        issue_file = self._find_issue_file(issue_id)
        if not issue_file:
            raise ValidationError(f"Issue {issue_id} not found")

        # Acquire lock
        self.acquire_lock(issue_id)

        try:
            # Load issue
            with open(issue_file, 'r') as f:
                issue = json.load(f)

            # Check if already claimed
            if issue.get("ownership", {}).get("assigned_to"):
                assigned = issue["ownership"]["assigned_to"]
                if assigned != self.agent_name:
                    raise CoordinationError(f"Issue already claimed by {assigned}")
                print(f"✅ Issue {issue_id} already claimed by you")
                return True

            # Claim issue
            if "ownership" not in issue:
                issue["ownership"] = {}

            issue["ownership"]["assigned_to"] = self.agent_name
            issue["ownership"]["claimed_at"] = datetime.utcnow().isoformat() + "Z"
            issue["status"] = "in_progress"

            # Save issue
            with open(issue_file, 'w') as f:
                json.dump(issue, f, indent=2)

            # Update coordination.json
            coord = self._load_coordination()
            if self.agent_name not in coord["agents"]:
                coord["agents"][self.agent_name] = {}
            if "current_tasks" not in coord["agents"][self.agent_name]:
                coord["agents"][self.agent_name]["current_tasks"] = []

            coord["agents"][self.agent_name]["current_tasks"].append(issue_id)
            self._save_coordination(coord)

            # Update indexes
            self._update_issue_index()

            # Log
            self._log_audit("claim_issue", True, f"Claimed {issue_id}", issue_id=issue_id)

            print(f"✅ Successfully claimed {issue_id}")
            return True

        finally:
            self.release_lock(issue_id)

    def propose_fix(self, fix_id: str, issue_id: str, title: str,
                    implementation: Dict[str, Any], test_results: Optional[Dict[str, Any]] = None) -> bool:
        """
        Propose a fix for an issue.

        Args:
            fix_id: ID for the fix (e.g., 'fix_011')
            issue_id: ID of issue being fixed
            title: Fix title
            implementation: Dict with approach, files_modified, lines_changed
            test_results: Optional test results

        Returns:
            True if fix created successfully
        """
        # Verify issue exists
        issue_file = self._find_issue_file(issue_id)
        if not issue_file:
            raise ValidationError(f"Issue {issue_id} not found")

        # Acquire lock
        self.acquire_lock(fix_id)

        try:
            # Create fix JSON
            fix = {
                "fix_id": fix_id,
                "title": title,
                "status": "proposed",
                "resolves_issue": issue_id,
                "metadata": {
                    "implemented_by": self.agent_name,
                    "implemented_at": datetime.utcnow().isoformat() + "Z",
                    "verified_by": []
                },
                "implementation": implementation,
                "test_results": test_results or {}
            }

            # Determine fix directory (proposed vs applied)
            fix_dir = FIXES_DIR / "proposed"
            fix_file = fix_dir / f"{fix_id}_{self._slugify(title)}.json"

            # Save fix
            with open(fix_file, 'w') as f:
                json.dump(fix, f, indent=2)

            # Update fix index
            self._update_fix_index()

            # Log
            self._log_audit("propose_fix", True, f"Proposed {fix_id} for {issue_id}",
                          fix_id=fix_id, issue_id=issue_id)

            print(f"✅ Successfully proposed {fix_id}")
            print(f"   File: {fix_file}")
            return True

        finally:
            self.release_lock(fix_id)

    def apply_fix(self, fix_id: str) -> bool:
        """
        Mark a fix as applied and move from proposed/ to applied/.

        Args:
            fix_id: ID of fix to apply

        Returns:
            True if applied successfully
        """
        # Find fix file in proposed/
        fix_file = self._find_fix_file(fix_id, "proposed")
        if not fix_file:
            raise ValidationError(f"Fix {fix_id} not found in proposed/")

        # Acquire lock
        self.acquire_lock(fix_id)

        try:
            # Load fix
            with open(fix_file, 'r') as f:
                fix = json.load(f)

            # Update status
            fix["status"] = "applied"
            if self.agent_name not in fix["metadata"].get("verified_by", []):
                fix["metadata"]["verified_by"].append(self.agent_name)

            # Move to applied/
            applied_dir = FIXES_DIR / "applied"
            new_file = applied_dir / fix_file.name

            with open(new_file, 'w') as f:
                json.dump(fix, f, indent=2)

            # Remove from proposed/
            fix_file.unlink()

            # Update related issue
            issue_id = fix.get("resolves_issue")
            if issue_id:
                issue_file = self._find_issue_file(issue_id)
                if issue_file:
                    with open(issue_file, 'r') as f:
                        issue = json.load(f)
                    issue["status"] = "resolved"
                    issue["resolved_by"] = self.agent_name
                    issue["resolved_at"] = datetime.utcnow().isoformat() + "Z"
                    with open(issue_file, 'w') as f:
                        json.dump(issue, f, indent=2)

            # Update indexes
            self._update_fix_index()
            self._update_issue_index()

            # Log
            self._log_audit("apply_fix", True, f"Applied {fix_id}", fix_id=fix_id)

            print(f"✅ Successfully applied {fix_id}")
            return True

        finally:
            self.release_lock(fix_id)

    def release_issue(self, issue_id: str) -> bool:
        """
        Release claim on an issue.

        Args:
            issue_id: ID of issue to release

        Returns:
            True if released successfully
        """
        # Find issue file
        issue_file = self._find_issue_file(issue_id)
        if not issue_file:
            raise ValidationError(f"Issue {issue_id} not found")

        # Acquire lock
        self.acquire_lock(issue_id)

        try:
            # Load issue
            with open(issue_file, 'r') as f:
                issue = json.load(f)

            # Verify we own it
            assigned = issue.get("ownership", {}).get("assigned_to")
            if assigned != self.agent_name:
                raise CoordinationError(f"Cannot release issue assigned to {assigned}")

            # Release ownership
            issue["ownership"]["assigned_to"] = None
            issue["ownership"]["claimed_at"] = None
            if issue["status"] == "in_progress":
                issue["status"] = "new"

            # Save issue
            with open(issue_file, 'w') as f:
                json.dump(issue, f, indent=2)

            # Update coordination.json
            coord = self._load_coordination()
            if self.agent_name in coord["agents"]:
                tasks = coord["agents"][self.agent_name].get("current_tasks", [])
                if issue_id in tasks:
                    tasks.remove(issue_id)
                coord["agents"][self.agent_name]["current_tasks"] = tasks
            self._save_coordination(coord)

            # Update indexes
            self._update_issue_index()

            # Log
            self._log_audit("release_issue", True, f"Released {issue_id}", issue_id=issue_id)

            print(f"✅ Successfully released {issue_id}")
            return True

        finally:
            self.release_lock(issue_id)

    def list_available_issues(self, severity: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List issues available to claim.

        Args:
            severity: Filter by severity (critical, high, medium, low)

        Returns:
            List of available issues
        """
        index_file = ISSUES_DIR / "index.json"
        with open(index_file, 'r') as f:
            index = json.load(f)

        available = []
        for issue in index.get("issues", []):
            # Filter by severity
            if severity and issue.get("severity") != severity:
                continue

            # Only unassigned or assigned to us
            assigned = issue.get("assigned_to")
            if assigned is None or assigned == self.agent_name:
                # Skip resolved
                if issue.get("status") != "resolved":
                    available.append(issue)

        return available

    def get_my_tasks(self) -> List[str]:
        """Get list of issues currently assigned to this agent"""
        coord = self._load_coordination()
        return coord.get("agents", {}).get(self.agent_name, {}).get("current_tasks", [])

    def _find_issue_file(self, issue_id: str) -> Optional[Path]:
        """Find issue file by ID"""
        for severity in ["critical", "high", "medium", "low"]:
            for file in (ISSUES_DIR / severity).glob(f"{issue_id}_*.json"):
                return file
        return None

    def _find_fix_file(self, fix_id: str, status: str = "proposed") -> Optional[Path]:
        """Find fix file by ID"""
        fix_dir = FIXES_DIR / status
        for file in fix_dir.glob(f"{fix_id}_*.json"):
            return file
        return None

    def _update_issue_index(self):
        """Rebuild issue index from JSON files"""
        issues = []
        for severity in ["critical", "high", "medium", "low"]:
            severity_dir = ISSUES_DIR / severity
            for file in severity_dir.glob("issue_*.json"):
                with open(file, 'r') as f:
                    issue = json.load(f)
                issues.append({
                    "issue_id": issue["issue_id"],
                    "title": issue["title"],
                    "severity": issue["severity"],
                    "status": issue["status"],
                    "file_path": str(file.relative_to(PROJECT_ROOT)),
                    "assigned_to": issue.get("ownership", {}).get("assigned_to"),
                    "resolved_by": issue.get("resolved_by")
                })

        # Count by severity and status
        by_severity = {}
        by_status = {}
        for issue in issues:
            sev = issue["severity"]
            stat = issue["status"]
            by_severity[sev] = by_severity.get(sev, 0) + 1
            by_status[stat] = by_status.get(stat, 0) + 1

        index = {
            "version": "1.0.0",
            "last_updated": datetime.utcnow().isoformat(),
            "total_issues": len(issues),
            "by_severity": by_severity,
            "by_status": by_status,
            "issues": issues
        }

        with open(ISSUES_DIR / "index.json", 'w') as f:
            json.dump(index, f, indent=4)

    def _update_fix_index(self):
        """Rebuild fix index from JSON files"""
        fixes = []
        for status in ["applied", "proposed"]:
            fix_dir = FIXES_DIR / status
            for file in fix_dir.glob("fix_*.json"):
                with open(file, 'r') as f:
                    fix = json.load(f)
                fixes.append({
                    "fix_id": fix["fix_id"],
                    "title": fix["title"],
                    "status": fix["status"],
                    "resolves_issue": fix.get("resolves_issue"),
                    "file_path": str(file.relative_to(PROJECT_ROOT)),
                    "implemented_by": fix.get("metadata", {}).get("implemented_by"),
                    "verified_by": fix.get("metadata", {}).get("verified_by", [])
                })

        # Count by status
        by_status = {}
        for fix in fixes:
            stat = fix["status"]
            by_status[stat] = by_status.get(stat, 0) + 1

        index = {
            "version": "1.0.0",
            "last_updated": datetime.utcnow().isoformat(),
            "total_fixes": len(fixes),
            "by_status": by_status,
            "fixes": fixes
        }

        with open(FIXES_DIR / "index.json", 'w') as f:
            json.dump(index, f, indent=4)

    @staticmethod
    def _slugify(text: str) -> str:
        """Convert text to safe filename"""
        text = text.lower()
        text = text.replace(' ', '_')
        text = ''.join(c for c in text if c.isalnum() or c in '_-')
        return text[:80]  # Limit length
