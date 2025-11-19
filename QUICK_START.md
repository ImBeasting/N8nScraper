# Multi-Agent System - Quick Start Guide

**System Status:** ✅ Fully Operational
**Last Updated:** 2025-11-06

---

## 🚀 Quick Start for Tyler (Project Owner)

### View System Status
```bash
cd "/media/tyler/fastraid/Projects/n8n Node Scrapper"

# Quick health check
./health_check.sh

# View current statistics
cat issues/index.json | jq '.total_issues, .by_severity, .by_status'
cat fixes/index.json | jq '.total_fixes, .by_status'

# View agent activity
cat collaboration/agent_heartbeats.json | jq .
```

### Let an Agent Start Working
Just tell the agent:
```
"Use the multi-agent collaboration system. Start by running:
python3 agent_start.py --agent <your_agent_name>"
```

### Monitor Work in Real-Time
```bash
# Watch audit log live
tail -f collaboration/audit_log.jsonl

# Check who's working on what
cat collaboration/coordination.json | jq '.agents'

# See current locks
ls -l collaboration/*.lock/ 2>/dev/null || echo "No locks active"
```

### Regenerate Reports After Changes
```bash
python3 generate_reports.py

# View the reports
cat reports/EXTRACTION_ERRORS_REPORT.md
cat reports/FIXES_APPLIED_REPORT.md
cat reports/AGENT_ACTIVITY_REPORT.md
```

---

## 🤖 Quick Start for Claude Code

### Start Your Session
```bash
python3 agent_start.py --agent claude_code
```

### Claim and Fix an Issue
```bash
# See what's available
python3 agent_start.py --agent claude_code

# Claim an issue
python3 claim_issue.py --agent claude_code --issue issue_XXX

# After fixing, propose the fix
python3 propose_fix.py --agent claude_code --fix fix_XXX --issue issue_XXX \
  --title "Your fix title" \
  --approach "Description of what you did" \
  --files "file1.py,file2.py" \
  --tested --test-notes "Test results"

# Apply the fix
python3 apply_fix.py --agent claude_code --fix fix_XXX

# Regenerate reports
python3 generate_reports.py
```

### Release an Issue (If You Can't Fix It)
```bash
python3 release_issue.py --agent claude_code --issue issue_XXX
```

---

## 🧠 Quick Start for Google Gemini CLI

### Start Your Session
```bash
python3 agent_start.py --agent gemini_cli
```

### Find High-Priority Work
```bash
# View available issues
python3 agent_start.py --agent gemini_cli

# Focus on critical/high priority
cat issues/index.json | jq '.issues[] | select(.severity == "critical" or .severity == "high")'
```

### Complete Workflow
```bash
# Claim issue
python3 claim_issue.py --agent gemini_cli --issue issue_XXX

# Develop fix...

# Propose fix
python3 propose_fix.py --agent gemini_cli --fix fix_XXX --issue issue_XXX \
  --title "Fix title" --approach "Your approach" \
  --files "changed_files.py" --tested --test-notes "Results"

# Apply fix
python3 apply_fix.py --agent gemini_cli --fix fix_XXX

# Update reports
python3 generate_reports.py
```

---

## 🔮 Quick Start for OpenAI Codex CLI

### Start Your Session
```bash
python3 agent_start.py --agent openai_codex
```

### Review Proposed Fixes (Peer Review Role)
```bash
# See proposed fixes waiting for verification
ls -la fixes/proposed/

# Review a proposed fix
cat fixes/proposed/fix_XXX_*.json | jq .

# If verified, apply it
python3 apply_fix.py --agent openai_codex --fix fix_XXX
```

### Or Claim Your Own Issue
```bash
# See available work
python3 agent_start.py --agent openai_codex

# Claim and work
python3 claim_issue.py --agent openai_codex --issue issue_XXX
# ... (same workflow as other agents)
```

---

## 📋 Common Tasks

### See All Available Issues
```bash
cat issues/index.json | jq '.issues[] | select(.status != "resolved")'
```

### See Your Current Tasks
```bash
cat collaboration/coordination.json | jq '.agents.claude_code.current_tasks'
# Replace claude_code with your agent name
```

### See Recent Activity
```bash
tail -20 collaboration/audit_log.jsonl | python3 -m json.tool
```

### Check Report Freshness
```bash
ls -lh reports/*.md
```

### Clean Stale Locks (If Needed)
```bash
./cleanup.sh
```

---

## 🆘 Troubleshooting

### "Could not acquire lock" Error
**Cause:** Another agent is working on the same issue.
**Solution:**
```bash
# Check who has the lock
cat collaboration/issue_XXX.lock/lock_info.json

# If lock is stale (>60 min), run cleanup
./cleanup.sh

# Or try a different issue
python3 agent_start.py --agent <your_agent>
```

### "Issue not found" Error
**Cause:** Issue ID doesn't exist.
**Solution:**
```bash
# List all available issues
cat issues/index.json | jq '.issues[].issue_id'

# Use exact issue_id from the list
```

### Reports Not Updating
**Cause:** Need to regenerate after changes.
**Solution:**
```bash
python3 generate_reports.py
```

### Script Not Executable
**Cause:** File permissions.
**Solution:**
```bash
chmod +x agent_start.py claim_issue.py propose_fix.py apply_fix.py release_issue.py
```

---

## 📚 Full Documentation

For complete details, see:
- **PHASE_4_AUTOMATION_COMPLETE.md** - Complete Phase 4 implementation details
- **AGENT_COLLABORATION_GUIDE.md** - Comprehensive workflow guide
- **MULTI_AGENT_SYSTEM_README.md** - System overview

---

## 🎯 Quick Reference Card

| Task | Command |
|------|---------|
| Start session | `python3 agent_start.py --agent <name>` |
| Claim issue | `python3 claim_issue.py --agent <name> --issue <id>` |
| Propose fix | `python3 propose_fix.py --agent <name> --fix <id> --issue <id> --title "..." --approach "..." --files "..." --tested` |
| Apply fix | `python3 apply_fix.py --agent <name> --fix <id>` |
| Release issue | `python3 release_issue.py --agent <name> --issue <id>` |
| Update reports | `python3 generate_reports.py` |
| Check health | `./health_check.sh` |
| Cleanup | `./cleanup.sh` |
| View issues | `cat issues/index.json \| jq .` |
| View fixes | `cat fixes/index.json \| jq .` |
| View activity | `tail collaboration/audit_log.jsonl` |

---

## 🌟 Best Practices

1. **Always start with** `agent_start.py` to see available work
2. **Claim before working** to prevent conflicts
3. **Test before proposing** to ensure quality
4. **Regenerate reports** after applying fixes
5. **Release if blocked** so others can help
6. **Check health regularly** to catch issues early
7. **Use descriptive titles** for fixes to help others understand
8. **Add test notes** to show verification was done

---

## ✅ System Verification

Run this anytime to verify everything is working:
```bash
./verify_phase4.sh
```

**Expected output:**
```
✅ coordination_lib.py
✅ agent_start.py
✅ claim_issue.py
✅ propose_fix.py
✅ apply_fix.py
✅ release_issue.py
✅ Phase 4 verification complete!
```

---

**System Ready:** ✅ All agents can begin work immediately!
