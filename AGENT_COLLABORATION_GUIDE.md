# Multi-Agent Collaboration Guide

**Version:** 1.0.0
**Last Updated:** 2025-11-06

Welcome to the n8n Node Extractor Multi-Agent Collaboration System! This guide explains how Claude Code, Google Gemini CLI, and OpenAI Codex CLI work together on fixing extraction issues.

---

## 🎯 Quick Start

### For Claude Code
```bash
cd "/media/tyler/fastraid/Projects/n8n Node Scrapper"

# Check for available work
python3 coordination_cli.py --agent claude_code --action list_tasks

# Claim an issue
python3 coordination_cli.py --agent claude_code --action claim --issue issue_007

# Work on issue... make changes... test...

# Mark complete
python3 coordination_cli.py --agent claude_code --action complete --issue issue_007 --fix fix_011

# Reports auto-regenerate
```

### For Google Gemini CLI
```bash
cd "/media/tyler/fastraid/Projects/n8n Node Scrapper"

# Send heartbeat
python3 coordination_cli.py --agent gemini_cli --action heartbeat

# Find work matching capabilities
python3 coordination_cli.py --agent gemini_cli --action find_work --capability testing

# Claim and work...
```

### For OpenAI Codex CLI
```bash
cd "/media/tyler/fastraid/Projects/n8n Node Scrapper"

# Check system status
python3 coordination_cli.py --action status

# Find unassigned high-priority issues
python3 coordination_cli.py --agent openai_codex --action list_tasks --priority high --status new

# Work on issues...
```

---

## 📁 System Structure

```
collaboration/          # Coordination files
  ├── coordination.json       # Agent registry & state
  ├── audit_log.jsonl        # All actions logged here
  └── agent_heartbeats.json  # Agent status

issues/                # Issue tracking (JSON)
  ├── index.json            # Issue registry
  ├── critical/*.json       # Critical issues
  ├── high/*.json          # High priority
  └── medium/*.json        # Medium priority

fixes/                 # Fix tracking (JSON)
  ├── index.json            # Fix registry
  ├── applied/*.json        # Implemented fixes
  └── proposed/*.json       # Pending fixes

reports/               # Auto-generated reports
  ├── EXTRACTION_ERRORS_REPORT.md
  ├── FIXES_APPLIED_REPORT.md
  └── AGENT_ACTIVITY_REPORT.md
```

---

## 🔄 Workflow Overview

### 1. Agent Starts
- Register/update agent info in `coordination.json`
- Send heartbeat to `agent_heartbeats.json`
- Check for available work in `work_queue`

### 2. Claim Issue
- Attempt atomic lock on issue (creates `collaboration/issue_XXX.lock`)
- If successful:
  - Update `ownership_registry` in `coordination.json`
  - Add to `current_tasks` for agent
  - Log action to `audit_log.jsonl`
- If lock fails:
  - Another agent owns it
  - Pick different issue

### 3. Work on Issue
- Read issue JSON from `issues/critical/issue_XXX.json`
- Analyze problem
- Implement fix in `n8n_node_extractor.py`
- Test on sample nodes
- Create fix JSON in `fixes/proposed/fix_XXX.json`

### 4. Complete Work
- Update issue status to "resolved"
- Move fix from `proposed/` to `applied/`
- Release lock (delete `.lock` file)
- Update coordination state
- Trigger report regeneration

### 5. Reports Auto-Update
- `generate_reports.py` reads all JSON files
- Regenerates markdown reports
- No manual editing of reports needed!

---

## 🔒 Lock Mechanism (Prevents Conflicts)

### Atomic Lock Creation
```python
# Atomic lock acquisition
lock_file = f"collaboration/issue_{issue_id}.lock"
try:
    # O_EXCL ensures atomic creation
    fd = os.open(lock_file, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.write(fd, agent_id.encode())
    os.close(fd)
    print("✅ Lock acquired!")
except FileExistsError:
    print("❌ Issue already locked by another agent")
```

### Lock Expiration
- Locks auto-expire after 60 minutes
- Any agent can remove stale locks
- Work can be resumed by another agent

### Release Lock
```python
# Always release when done
lock_file = f"collaboration/issue_{issue_id}.lock"
if os.path.exists(lock_file):
    os.remove(lock_file)
```

---

## 📝 Working with Issues

### Issue JSON Structure
```json
{
  "issue_id": "issue_007",
  "title": "Incomplete Operations Extraction",
  "severity": "high",
  "status": "new",  // new → in_progress → review → resolved
  "priority": 7,

  "metadata": {
    "created_at": "2025-11-06T10:49:00Z",
    "created_by": "claude_code",
    "affected_nodes": "Chargebee, multi-resource nodes"
  },

  "description": {
    "problem": "Only 1 of 5 operations extracted...",
    "impact": "High - Multi-resource nodes incomplete",
    "examples": [...]
  },

  "ownership": {
    "assigned_to": null,  // Your agent_id when claimed
    "locked_by": null,
    "lock_acquired_at": null,
    "lock_expires_at": null
  }
}
```

### Claiming an Issue
1. Check `ownership.locked_by` is null
2. Create lock file: `collaboration/issue_007.lock`
3. Update JSON: `ownership.assigned_to = "gemini_cli"`
4. Update coordination.json
5. Begin work!

### Updating Issue Status
```python
# Read issue
with open('issues/high/issue_007_incomplete_operations.json') as f:
    issue = json.load(f)

# Update status
issue['status'] = 'in_progress'
issue['ownership']['assigned_to'] = 'gemini_cli'
issue['ownership']['locked_at'] = datetime.now().isoformat()

# Save
with open('issues/high/issue_007_incomplete_operations.json', 'w') as f:
    json.dump(issue, f, indent=2)
```

---

## 🔧 Working with Fixes

### Creating a Fix
```python
fix = {
    "fix_id": "fix_011",
    "title": "Complete Operations Extraction for Multi-Resource Nodes",
    "status": "proposed",
    "resolves_issue": "issue_007",

    "metadata": {
        "implemented_by": "gemini_cli",
        "implemented_at": datetime.now().isoformat()
    },

    "implementation": {
        "approach": "Modified operations extraction to check all resource blocks...",
        "files_modified": ["n8n_node_extractor.py"],
        "lines_changed": "1580-1610"
    },

    "test_results": {
        "success_rate": "100%",
        "nodes_tested": [
            {"node": "Chargebee", "result": "✅", "output": "5 operations found"},
            {"node": "Salesforce", "result": "✅", "output": "12 operations found"}
        ]
    }
}

# Save to proposed fixes
import json
with open('fixes/proposed/fix_011_complete_operations.json', 'w') as f:
    json.dump(fix, f, indent=2)
```

### Peer Review (Optional)
```python
# After testing, request review
fix['peer_reviews'].append({
    "reviewer": "claude_code",
    "reviewed_at": datetime.now().isoformat(),
    "verdict": "approved",
    "comments": "Implementation looks good, all tests pass"
})
```

### Applying a Fix
```python
# Move from proposed to applied
import shutil
shutil.move(
    'fixes/proposed/fix_011_complete_operations.json',
    'fixes/applied/fix_011_complete_operations.json'
)

# Update status
fix['status'] = 'applied'

# Update issue
issue['status'] = 'resolved'

# Regenerate reports
os.system('python3 generate_reports.py')
```

---

## 🤝 Coordination Rules

### Rule 1: Never Edit Reports Manually
✅ **DO:** Modify JSON files in `issues/` and `fixes/`
❌ **DON'T:** Edit `EXTRACTION_ERRORS_REPORT.md` directly

Reports are auto-generated. Changes will be overwritten!

### Rule 2: Always Acquire Locks
✅ **DO:** Create `.lock` file before working
❌ **DON'T:** Work on issues without locking

Prevents conflicts between agents.

### Rule 3: Send Heartbeats
✅ **DO:** Update heartbeat every 30 seconds when active
❌ **DON'T:** Let heartbeat go stale

Other agents need to know you're alive!

### Rule 4: Release Locks When Done
✅ **DO:** Delete `.lock` file after completing work
❌ **DON'T:** Leave locks hanging

Prevents blocking other agents.

### Rule 5: Log All Actions
✅ **DO:** Append to `audit_log.jsonl` for all actions
❌ **DON'T:** Make changes without logging

Audit trail is essential for debugging.

---

## 🛠 Command Reference

### List Available Tasks
```bash
python3 coordination_cli.py --agent claude_code --action list_tasks
```

### Claim an Issue
```bash
python3 coordination_cli.py --agent gemini_cli --action claim --issue issue_008
```

### Update Status
```bash
python3 coordination_cli.py --agent openai_codex --action status_update \
    --issue issue_009 --status in_progress
```

### Complete Issue
```bash
python3 coordination_cli.py --agent claude_code --action complete \
    --issue issue_010 --fix fix_015
```

### Send Heartbeat
```bash
python3 coordination_cli.py --agent gemini_cli --action heartbeat
```

### Check System Status
```bash
python3 coordination_cli.py --action status
```

### Regenerate Reports
```bash
python3 generate_reports.py
```

---

## 🔍 Monitoring & Debugging

### Check Agent Status
```bash
cat collaboration/agent_heartbeats.json | jq '.'
```

### View Recent Activity
```bash
tail -20 collaboration/audit_log.jsonl | jq '.'
```

### Find Stale Locks
```bash
find collaboration/ -name "*.lock" -mmin +60
```

### Remove Stale Lock
```bash
rm collaboration/issue_007.lock
```

### View Issue Status
```bash
cat issues/index.json | jq '.by_status'
```

### View Fix Statistics
```bash
cat fixes/index.json | jq '.by_status'
```

---

## 🚨 Troubleshooting

### Issue: Can't Acquire Lock
**Problem:** Another agent owns the issue
**Solution:** Pick a different issue or wait for lock to expire (60 min)

### Issue: Stale Lock Blocking Work
**Problem:** Lock older than 60 minutes exists
**Solution:** Remove lock file manually: `rm collaboration/issue_XXX.lock`

### Issue: Reports Not Updating
**Problem:** Reports not reflecting JSON changes
**Solution:** Run `python3 generate_reports.py` manually

### Issue: Coordination State Mismatch
**Problem:** `coordination.json` out of sync
**Solution:** Run health check: `python3 health_check.py`

### Issue: Audit Log Too Large
**Problem:** `audit_log.jsonl` > 10MB
**Solution:** Run cleanup: `python3 cleanup.py`

---

## 📊 Best Practices

### Before Starting Work
1. ✅ Send heartbeat
2. ✅ Check for stale locks
3. ✅ Review work queue
4. ✅ Claim issue atomically

### While Working
1. ✅ Update heartbeat regularly (every 30 sec)
2. ✅ Log significant actions
3. ✅ Test thoroughly before proposing fix
4. ✅ Update issue progress in JSON

### After Completing Work
1. ✅ Create fix JSON with test results
2. ✅ Update issue status to "resolved"
3. ✅ Release lock immediately
4. ✅ Regenerate reports
5. ✅ Log completion event

---

## 🎓 Examples

### Example 1: Claude Code Fixes Issue
```bash
# 1. Start work
python3 coordination_cli.py --agent claude_code --action claim --issue issue_007

# 2. Make changes to n8n_node_extractor.py
# ... code changes ...

# 3. Test
python3 n8n_node_extractor.py extract Chargebee
# Verify: Found 5 operations ✅

# 4. Create fix
python3 coordination_cli.py --agent claude_code --action propose_fix \
    --issue issue_007 --fix fix_011 --description "Fixed operations extraction"

# 5. Complete
python3 coordination_cli.py --agent claude_code --action complete \
    --issue issue_007 --fix fix_011

# Done! Reports auto-update.
```

### Example 2: Gemini Reviews Fix
```bash
# 1. Check proposed fixes
python3 coordination_cli.py --agent gemini_cli --action list_fixes --status proposed

# 2. Review fix_012
python3 coordination_cli.py --agent gemini_cli --action review_fix \
    --fix fix_012 --verdict approved --comment "Tests pass, looks good"

# 3. Apply fix
python3 coordination_cli.py --agent gemini_cli --action apply_fix --fix fix_012
```

### Example 3: OpenAI Discovers New Issue
```bash
# 1. Create new issue
python3 coordination_cli.py --agent openai_codex --action create_issue \
    --title "Missing Icon URLs for themed nodes" \
    --severity medium \
    --description "Nodes with light/dark icon themes losing icon data"

# Issue auto-assigned ID: issue_015
# Appears in next report generation
```

---

## 📚 Additional Resources

- **Full API**: See `coordination_lib.py` for all functions
- **Examples**: See `examples/` directory
- **Health Checks**: Run `python3 health_check.py` regularly
- **Cleanup**: Run `python3 cleanup.py` weekly

---

## ✨ Summary

**Key Points:**
1. All agents work from same JSON source files
2. Atomic locks prevent conflicts
3. Reports are always auto-generated
4. Full audit trail for all actions
5. Equal access for all agents

**Golden Rule:**
*Never manually edit generated reports - always modify JSON and regenerate!*

---

**Guide Version:** 1.0.0
**Last Updated:** 2025-11-06
**Maintained by:** Multi-Agent Coordination System
