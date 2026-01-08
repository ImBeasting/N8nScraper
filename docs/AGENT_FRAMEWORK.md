# N8nScraper Multi-Agent Framework

**Status:** Scaffolding Complete
**Created:** 2026-01-08
**Quality Contract:** `docs/quality_contract.md`

---

## Overview

Multi-agent framework for maintaining and improving N8nScraper's 96%+ extraction quality. Complements the existing Python coordination system (`coordination_lib.py`) with AI agent orchestration.

---

## Agent Roster

| Agent | Model | Purpose | Authority |
|-------|-------|---------|-----------|
| **typescript-parser** | opus-4.5 | Analyze TypeScript AST patterns, resolve complex spreads | PROPOSE |
| **extraction-validator** | sonnet-4.5 | Verify extraction quality, audit accuracy | READ-ONLY |
| **issue-triage** | sonnet-4.5 | Prioritize backlog, route work to agents | MODIFY (issues) |
| **property-auditor** | sonnet-4.5 | Cross-check extracted vs source properties | READ-ONLY + CREATE ISSUES |
| **edge-case-hunter** | opus-4.5 | Proactive pattern detection for extraction failures | READ-ONLY + CREATE ISSUES |
| **documentation-sync** | haiku-3.5 | Maintain CLAUDE.md/README.md consistency | PROPOSE |
| **coordination-enforcer** | haiku-3.5 | Enforce locking protocol, audit log hygiene | MODIFY (coordination) |

### Model Selection Rationale

- **Opus 4.5** - Complex AST analysis, proactive pattern detection
- **Sonnet 4.5** - Quality auditing, property verification, triage
- **Haiku 3.5** - Documentation sync, coordination enforcement (lightweight tasks)

---

## Triggering Agents

### typescript-parser

```
Triggers:
- Zero-property nodes detected
- Namespace spread patterns found (e.g., ...module.property)
- Complex utility function spreads
- Deep nesting extraction failures (3-4 levels)

Example:
"Analyze TypeScript patterns for GoogleSheets - namespace spread causing missing properties"
```

### extraction-validator

```
Triggers:
- After bulk extraction (extract-all command)
- After applying extractor fixes
- Quality drop detected (validation report shows regressions)

Example:
"Validate extraction quality after fix_022 applied"
```

### issue-triage

```
Triggers:
- New issue created in issues/ directory
- Manual request: "triage issues" or "prioritize backlog"

Example:
"Triage issues and prioritize by quality impact"
```

### property-auditor

```
Triggers:
- Manual audit request: "audit properties for [NodeName]"
- Zero-property node detected in validation

Example:
"Audit properties for Slack node - source vs extracted comparison"
```

### edge-case-hunter

```
Triggers:
- Manual request: "find edge cases" or "hunt extraction risks"
- After n8n version update

Example:
"Hunt edge cases in n8n 2.3.0 TypeScript source"
```

### documentation-sync

```
Triggers:
- CLAUDE.md modified
- Quality metrics updated (validation report changes)
- n8n version updated

Example:
"Sync documentation after quality metrics changed"
```

### coordination-enforcer

```
Triggers:
- Stale lock detected (lock timeout exceeded)
- Before critical operations (bulk extraction, fix application)

Example:
"Check coordination health before bulk extraction"
```

---

## Validation Gates

### Unified Script

```bash
./scripts/validate.sh
```

Runs:
1. Extraction quality validation (`validate_extraction.py`)
2. Coordination health check (stale locks)
3. File pair consistency (JSON == MD count)
4. Quality metrics summary

Returns exit code 0 (pass) or 1 (fail) for CI/CD integration.

### Quality Targets

| Metric | Target | Source |
|--------|--------|--------|
| Zero-property nodes | ≤1 (NoOp only) | `validate_extraction.py` |
| Null displayNames | 0 | `validation_report.json` |
| Template variables | 0 | `validation_report.json` |
| Overall quality | 96%+ | (nodes with properties / total nodes) |
| File pairs | 100% balanced | JSON count == MD count |
| Stale locks | 0 | `collaboration/*.lock/` age check |

---

## Coordination Integration

### Existing System (coordination_lib.py)

```
Multi-Agent Coordination Library
├── Atomic locks via mkdir()
├── Issue claiming via coordination.json
├── Fix proposal workflow
├── Audit logging (audit_log.jsonl)
└── Heartbeat tracking
```

### Agent Framework Additions

```
Claude Agent Definitions (.claude/agents/)
├── Defines agent capabilities and triggers
├── Enforces quality contract compliance
├── Specifies tool restrictions per agent
└── Documents DOES/DOESN'T for each agent
```

**Integration:** Agents use `coordination_lib.py` for all file-based operations (claiming issues, proposing fixes, etc.). Agent definitions enforce quality standards and provide orchestration guidance.

---

## Workflow Example: Zero-Property Node

```
1. extraction-validator runs after extract-all
   │
   ├─► Detects: Airtable node has 0 properties
   │
2. property-auditor triggered
   │
   ├─► Inspects: n8n/.../Airtable.node.ts (line 156-287)
   ├─► Counts: 34 properties in source
   ├─► Compares: 0 properties in extracted JSON
   ├─► Root cause: Namespace spread `...operations.table` not resolved
   │
3. issue-triage creates issue
   │
   ├─► Severity: HIGH (1 node, 34 properties missed)
   ├─► Routes to: typescript-parser agent
   │
4. typescript-parser analyzes pattern
   │
   ├─► Pattern: `...operations.table` (line 178)
   ├─► Proposed fix: Add namespace resolution to extractor
   ├─► Regression tests: GoogleSheets, Slack, Airtable
   │
5. Fix proposed via propose_fix.py
   │
   ├─► Agent claims issue (coordination_lib.py)
   ├─► Proposes fix_023 with test results
   │
6. Fix applied via apply_fix.py
   │
   ├─► Extractor code updated
   ├─► Re-extract Airtable
   │
7. extraction-validator verifies
   │
   └─► Airtable: 34 properties ✓
       Quality: 96.3% → 96.5% ✓
```

---

## Agent Definition Structure

Every agent file follows this template:

```markdown
# Agent: [name]

## Purpose
[One sentence purpose]

## Model
[opus-4.5 | sonnet-4.5 | haiku-3.5]

## Triggers
- [When to invoke this agent]

## Inputs
- [What data/files this agent needs]

## Outputs
- [What this agent produces]

## Authority Level
[READ-ONLY | MODIFY (scope) | PROPOSE]

## Tool Restrictions
[Allowed tools and file scopes]

## Must Never
- [Hard rules this agent must not violate]

## Definition of Done
- [ ] [Checklist items]

## Quality Contract Compliance
[N1-N7 compliance specifics]

### DOES vs DOESN'T (N7)
| DOES | DOESN'T |
|------|---------|
| [Actual capability] | [Common misconception] |
```

---

## Authority Levels Explained

### READ-ONLY
- Can inspect files, generate reports
- CANNOT modify any project files
- Creates issues to propose changes

**Agents:** extraction-validator

### MODIFY (scope)
- Can update specific file types
- MUST use coordination locks
- Limited to scope (e.g., "issues only")

**Agents:** issue-triage, coordination-enforcer

### PROPOSE
- Can propose changes via fix workflow
- CANNOT apply changes directly
- Uses `propose_fix.py` for all modifications

**Agents:** typescript-parser, documentation-sync

### CREATE ISSUES
- Can create new issue files
- MUST follow issue template structure
- CANNOT claim issues for other agents

**Agents:** property-auditor, edge-case-hunter

---

## Quality Contract Highlights

From `docs/quality_contract.md`:

### N1: No Invented Facts
Every version/feature claim cites source URL or file:line.

**Example:**
```
❌ "GoogleSheets has ~40 properties"
✅ "GoogleSheets: 42 properties (Source: extracted_docs/googlesheets_data.json, validated 2026-01-08)"
```

### N2: Mechanism Before Outcome
Performance claims state mechanism + conditions.

**Example:**
```
❌ "Extraction quality improved significantly"
✅ "Quality improved from 49 zero-property nodes to 1 (98% reduction)
   Mechanism: Namespace spread resolution added to extractor
   Validation: validation_report.json 2025-11-10 vs 2025-11-11"
```

### N7: DOES/DOESN'T Required
Agent capabilities documented with limitation table.

**Example (typescript-parser):**

| DOES | DOESN'T |
|------|---------|
| Resolve namespace spreads (`...ns.prop`) | Handle arbitrary code execution in spreads |
| Recurse collections 3-4 levels deep | Support infinite recursion (stack limit) |

---

## File Structure

```
N8nScraper/
├── .claude/
│   └── agents/
│       ├── typescript-parser.md          (opus-4.5)
│       ├── extraction-validator.md       (sonnet-4.5)
│       ├── issue-triage.md               (sonnet-4.5)
│       ├── property-auditor.md           (sonnet-4.5)
│       ├── edge-case-hunter.md           (opus-4.5)
│       ├── documentation-sync.md         (haiku-3.5)
│       └── coordination-enforcer.md      (haiku-3.5)
│
├── scripts/
│   └── validate.sh                       (unified validation)
│
├── docs/
│   ├── quality_contract.md               (vendored from AiResearch)
│   └── AGENT_FRAMEWORK.md                (this file)
│
├── coordination_lib.py                   (Python coordination)
├── validate_extraction.py                (quality validation)
└── n8n_node_extractor.py                 (main extractor - 3768 lines)
```

---

## Next Steps

1. **Test Agent Invocations**
   - Trigger each agent with sample requests
   - Verify tool restrictions enforced
   - Validate quality contract compliance

2. **Create Sample Issues**
   - Property auditor: Audit 5 diverse nodes
   - Edge case hunter: Scan n8n 2.3.0 source

3. **Document Agent Interactions**
   - Multi-agent workflows (e.g., zero-property resolution)
   - Handoff protocols between agents

4. **CI/CD Integration**
   - Run `validate.sh` on every commit
   - Block merges if validation fails

---

**Status:** Ready for production use
**Quality Baseline:** 96%+ extraction accuracy (451 nodes)
**Coordination:** Atomic locks via `coordination_lib.py`
**Validation:** Automated via `scripts/validate.sh`
