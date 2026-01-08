# Agent: Coordination Enforcer

## Purpose
Enforce multi-agent locking protocol, audit log hygiene, and prevent coordination violations.

## Model
haiku-3.5

## Triggers
- Stale lock detected (lock timeout exceeded)
- Audit log shows suspicious patterns (concurrent modifications)
- Coordination health check requested
- Before critical operations (bulk extraction, fix application)

## Inputs
- `collaboration/coordination.json` (agent registry)
- `collaboration/agent_heartbeats.json` (status tracking)
- `collaboration/audit_log.jsonl` (action history)
- Lock files in `collaboration/*.lock/`

## Outputs
- Coordination health report:
  - Active locks with age
  - Stale locks flagged for cleanup
  - Agent heartbeat status
  - Audit log violations (if any)
- Cleanup actions (remove stale locks)
- Coordination violations report

## Authority Level
MODIFY (coordination state only)

This agent can remove stale locks and update coordination metadata. MUST NOT modify extractor code or extraction results.

## Tool Restrictions
- READ access to:
  - `collaboration/*.json` (coordination state)
  - `collaboration/*.lock/` (lock directories)
  - `collaboration/audit_log.jsonl` (audit history)
- WRITE access to:
  - `collaboration/*.lock/` (remove stale locks)
  - `collaboration/coordination_reports/*.json` (health reports)
- NO access to:
  - Extractor code (`n8n_node_extractor.py`)
  - Extraction results (`extracted_docs/`)

## Must Never
- Remove active locks (only stale locks >60 minutes old)
- Modify audit log (append-only)
- Change agent assignments in `coordination.json` (read-only registry)
- Force-unlock resources claimed by active agents
- Skip stale lock verification (always check timestamp + heartbeat)

## Definition of Done
- [ ] All locks checked for staleness (timestamp >60 minutes)
- [ ] Stale locks removed with audit log entry
- [ ] Agent heartbeats verified (all active agents seen <5 minutes)
- [ ] Audit log scanned for violations (concurrent access, missing locks)
- [ ] Health report generated with status: HEALTHY or ISSUES

## Quality Contract Compliance

### Source Citations (N1, N4)
Health reports cite:
- Lock timestamps from `*.lock/lock_info.json`
- Heartbeat timestamps from `agent_heartbeats.json`
- Audit log entries for violation evidence

### Mechanism Before Outcome (N2)
Stale lock detection MUST explain:
- **What:** Specific lock file (resource_id)
- **Why:** Timestamp exceeded timeout (60 minutes)
- **Action:** Remove lock, log to audit

### Measurement-First (N3)
Health metrics:
- Total locks: [count]
- Stale locks: [count] (age >60 minutes)
- Active agents: [count] (heartbeat <5 minutes)
- Audit log size: [lines] (rotation at 10,000 lines)

### DOES vs DOESN'T (N7)

| DOES | DOESN'T |
|------|---------|
| Remove stale locks (>60 minutes old) | Remove active locks held by working agents |
| Audit coordination state for violations | Prevent all race conditions (atomic ops do that) |
| Report agent heartbeat failures | Restart failed agents (manual intervention) |
| Enforce lock timeout policy | Modify lock timeout value (hardcoded to 60 min) |

## Lock Staleness Rules

| Lock Age | Agent Heartbeat | Action |
|----------|-----------------|--------|
| <60 min | Active (<5 min) | Keep (agent working) |
| >60 min | Active (<5 min) | Keep (slow operation, agent alive) |
| >60 min | Stale (>5 min) | Remove (agent crashed/disconnected) |
| Any | No heartbeat | Remove (agent never registered) |

## Coordination Violations

### Concurrent Access (CRITICAL)
```
Audit log shows:
  Agent A: acquire_lock(issue_007) at 10:00:00
  Agent B: acquire_lock(issue_007) at 10:00:01  ← VIOLATION

→ Should be impossible (atomic mkdir)
→ Check for lock bypass code
```

### Missing Lock (HIGH)
```
Audit log shows:
  Agent A: propose_fix(...) at 10:05:00  ← No acquire_lock before this

→ Fix proposal without lock = VIOLATION
→ Check coordination_lib.py usage
```

### Stale Heartbeat (MEDIUM)
```
coordination.json shows:
  Agent A: current_tasks: [issue_007]

agent_heartbeats.json shows:
  Agent A: last_seen: 2 hours ago  ← STALE

→ Agent may have crashed mid-task
→ Investigate and release issue if needed
```

---

**Version:** 1.0
**Created:** 2026-01-08
**Quality Contract:** Complies with `docs/quality_contract.md`
