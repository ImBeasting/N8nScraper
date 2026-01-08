# CLAUDE.md - N8nScraper

---

## AI Layer (Multi-Agent Framework)

This repository uses a multi-agent framework with quality-controlled operations.

### Quality Contract

All agent outputs must comply with the quality contract at `docs/quality_contract.md`.

**Non-Negotiables:**
| Rule | Requirement |
|------|-------------|
| N1 | Every claim cites source or marked `UNKNOWN - TODO: verify [target]` |
| N2 | Performance claims state mechanism + conditions |
| N3 | No config values without `__MEASURED__` / `__TUNED__` / derivation |
| N4 | Primary sources preferred |
| N5 | Cache sharing requires token-identical prefix contract |
| N6 | Math uses declared formula + consistent units |
| N7 | Memory/cache topics require DOES/DOESN'T table |
| N8 | All model references verified against registry |
| N9 | All version/count claims include verification date |
| N10 | Papers >6 months cite model used + current equivalent |
| N11 | High-volatility claims flagged for 30-day refresh |
| N12 | Direct source verification required (no web search for versions) |

### Subagent Roster

| Agent | Model | Purpose | Trigger |
|-------|-------|---------|---------|
| typescript-parser | opus | TypeScript AST analysis, spread resolution | Zero-property extraction failures, critical patterns |
| extraction-validator | sonnet | Quality verification, accuracy audits | Post-extraction validation, weekly audits |
| issue-triage | sonnet | Backlog analysis, priority assignment | 5+ new issues, backlog review requests |
| property-auditor | sonnet | Cross-check extracted vs source properties | Node re-extraction, random sampling |
| edge-case-hunter | opus | Proactive pattern detection | After major fix, n8n version updates |
| documentation-sync | haiku | CLAUDE.md/README.md consistency | After extract-all, after n8n update |
| coordination-enforcer | haiku | Locking protocol, audit log hygiene | Hourly health check, lock conflicts |

Agent definitions: `.claude/agents/`

### Agent Invocation Protocol

**CRITICAL:** Custom agents in `.claude/agents/` are NOT auto-discovered by Claude Code's Task tool. When a task matches an agent's trigger conditions, you MUST:

1. **Identify the matching agent** from the Subagent Roster above
2. **Read the agent file:** `Read .claude/agents/{agent-name}.md`
3. **Follow the agent's instructions:**
   - Purpose: What the agent does
   - Tool Restrictions: What tools/files it can access
   - Must Never: Hard constraints to obey
   - Definition of Done: Checklist for completion
4. **Report completion** using the agent's output format

**Trigger Examples:**
| User Request | Agent to Invoke |
|--------------|-----------------|
| "Why does X have zero properties?" | `typescript-parser` |
| "Audit extraction quality" | `extraction-validator` |
| "Prioritize the issue backlog" | `issue-triage` |
| "Spot check properties for Slack" | `property-auditor` |
| "Check for new patterns after n8n update" | `edge-case-hunter` |
| "Update documentation after extraction" | `documentation-sync` |
| "Check for stale locks" | `coordination-enforcer` |

**Example invocation flow:**
```
User: "Audit extraction quality"
→ Match: extraction-validator agent
→ Read: .claude/agents/extraction-validator.md
→ Execute: Follow agent's purpose, inputs, outputs
→ Report: Use agent's Definition of Done format
```

### Validation Gates

Run before committing:
```bash
./scripts/validate.sh
```

### UNKNOWN/TODO Policy

If you cannot verify a claim:
```
UNKNOWN - TODO: verify [specific claim] at [verification target]
```

Never assert unverified facts.

---

## PRESERVED DOMAIN CONTENT

**The following content is the authoritative domain documentation. It MUST NOT be modified, summarized, or deleted.**

---

# CLAUDE.md

**Project:** n8n Node Documentation Extractor for AI Training
**Repository:** https://github.com/ImBeasting/N8nScraper
**Status:** ✅ Production Ready (96%+ quality)
**Last Updated:** 2026-01-08
**n8n Version:** 2.3.0 (January 8, 2026)

---

## Project Overview

Python-based tool that extracts comprehensive documentation from n8n TypeScript node definitions, generating markdown docs and machine-readable schemas (YAML/JSON) optimized for AI training.

**Current Quality:** 96%+ extraction accuracy across 451 nodes

---

## Quick Start

### First-Time Setup

The `n8n/` directory is **gitignored** (external dependency). Clone it after checking out the repo:

```bash
git clone https://github.com/ImBeasting/N8nScraper.git
cd N8nScraper
git clone --depth 1 https://github.com/n8n-io/n8n.git n8n
```

### Update n8n Source

```bash
rm -rf n8n && git clone --depth 1 https://github.com/n8n-io/n8n.git n8n
```

### Essential Commands

```bash
# Extract single node
python3 n8n_node_extractor.py extract <NodeName>

# Extract all nodes
python3 n8n_node_extractor.py extract-all

# List available nodes
python3 n8n_node_extractor.py list

# Validate extraction quality
python3 validate_extraction.py

# Multi-agent collaboration
python3 agent_start.py --agent claude_code
python3 claim_issue.py --agent claude_code --issue <issue_id>
python3 propose_fix.py --agent claude_code --fix <fix_id> --issue <issue_id> --title "..." --tested
python3 apply_fix.py --agent claude_code --fix <fix_id>
python3 generate_reports.py
```

---

## Repository Structure

```
N8nScraper/
├── n8n/                              # n8n source (GITIGNORED - clone separately)
├── extracted_docs/                   # Output (902 files: 451 JSON + 451 MD)
├── n8n_node_extractor.py             # Main extractor (2700+ lines)
├── validate_extraction.py            # Quality validation
├── coordination_lib.py               # Multi-agent library
├── agent_start.py                    # Start agent session
├── claim_issue.py                    # Claim an issue
├── propose_fix.py                    # Propose a fix
├── apply_fix.py                      # Apply approved fix
│
├── docs/                             # Documentation
│   ├── ai_review_prompt.md           # AI audit protocol (START HERE)
│   └── MULTI_AGENT_SYSTEM_README.md  # Multi-agent workflow guide
│
├── collaboration/                    # Multi-agent coordination
│   ├── coordination.json             # Agent registry
│   ├── agent_heartbeats.json         # Status tracking
│   └── audit_log.jsonl               # Action history
│
├── issues/                           # Issue tracking
│   ├── resolved/                     # Completed issues
│   ├── corrupted_json/               # Issues with bad JSON (need cleanup)
│   └── index.json
│
├── fixes/                            # Fix tracking
│   ├── applied/
│   ├── proposed/
│   └── index.json
│
└── _archive/                         # Historical files (reference only)
    ├── reports/                      # Old auto-generated reports
    ├── scripts/                      # Deprecated scripts
    └── validation_summaries/         # Old validation reports
```

**Note:** The `n8n/` directory is gitignored. After cloning, run:
```bash
git clone --depth 1 https://github.com/n8n-io/n8n.git n8n
```

---

## Issue Naming Convention

**Format:** `_<agent>_issue_<nnn>_<description>.json`

**Current Agents:**
- `claude_code` - Analysis, documentation, code review, bug fixing
- `gemini_cli` - Testing, validation, performance optimization
- `openai_codex` - Code generation, pattern recognition, error detection

**Examples:**
```bash
python3 claim_issue.py --agent claude_code --issue _claude_issue_032
python3 propose_fix.py --agent claude_code --fix fix_022 --issue _claude_issue_032 --title "..." --tested
python3 apply_fix.py --agent claude_code --fix fix_022
```

---

## Main Extractor Features

### What It Extracts

- **Complete node properties** with types, defaults, validation rules
- **Multi-resource node support** (Slack, Salesforce, etc.)
- **Versioned node handling** (v1, v2, v3, etc.)
- **Namespace spread resolution** (`import * as`, `...module.property`)
- **Collection/FixedCollection recursion** (nested options)
- **Operation tagging** (`_operation` field for filtering)
- **Dynamic outputs detection** (branching nodes)
- **Constant resolution** (n8n-workflow imports)
- **Credentials, operations, UI elements, validation rules**
- **Real-world workflow examples**

### Recent Major Fixes (2025-11-11)

✅ **Namespace Spreads** - GoogleSheets: 5→42 properties (740% increase)
✅ **Collection Recursion** - HTTP Request nested options extracted
✅ **Spread with .map()** - Transformation detection added
✅ **Dynamic Outputs** - Switch node documented correctly
✅ **Constants** - SEND_AND_WAIT_OPERATION resolved
✅ **Operation Tagging** - 5000+ properties tagged

**Result:** Zero-property nodes reduced from 49 to 1 (98% improvement)

---

## Multi-Agent Collaboration

### Quick Workflow

1. **Start session:** `python3 agent_start.py --agent <agent_name>`
2. **Claim issue:** `python3 claim_issue.py --agent <agent_name> --issue <issue_id>`
3. **Work on fix:** Make code changes, test thoroughly
4. **Propose fix:** `python3 propose_fix.py --agent <agent_name> --fix <fix_id> --issue <issue_id> --title "..." --approach "..." --files "..." --tested`
5. **Apply fix:** `python3 apply_fix.py --agent <agent_name> --fix <fix_id>`
6. **Regenerate reports:** `python3 generate_reports.py`

### Key Features

- **Atomic file-based locks** - No race conditions
- **Issue-based ownership** - Clear assignments
- **Auto-generated reports** - Never manually edit
- **Complete audit trail** - JSONL logging
- **Peer review workflow** - Propose → Review → Apply

---

## Output Format

### Markdown Documentation
- Frontmatter (YAML metadata)
- Node type badges
- Credentials & operations
- Parameters (grouped by operation)
- Real-world examples
- Expression patterns
- Machine-readable schemas (YAML + JSON)

### JSON Data
- `node_info` - displayName, version, type, group
- `properties` - All parameters with full details
- `operations` / `operations_by_resource`
- `credentials` - Auth requirements
- `workflow_examples` - Real usage
- `validation_rules`, `type_info`, `ui_elements`
- `_source`, `_operation` tags for filtering

---

## Configuration

**Hardcoded paths** (update for your system):
```python
CURRENT_DIR = Path("/home/tyler/Projects/N8nScraper")
N8N_REPO = CURRENT_DIR / "n8n"
OUTPUT_DIR = CURRENT_DIR / "extracted_docs"
```

---

## Quality Metrics

### Current State (2026-01-08)
- **n8n version:** 2.3.0 (January 8, 2026)
- **Total nodes:** 451 extracted (85.0% of 531 available)
- **Files generated:** 902 (451 JSON + 451 MD)
- **Duplicate groups:** 0 ✅
- **Zero properties:** 1 (NoOp - correct by design) ✅
- **Null displayNames:** 0 ✅
- **Template variables:** 0 ✅
- **Overall quality:** 96%+

### Quality by Node Type
- **Simple nodes (60%):** 95-100% ✅
- **Moderate nodes (20%):** 90-95% ✅
- **Complex nodes (20%):** 85-95% ✅

---

## Known Limitations

### Minor Issues Remaining (2 high-priority)
1. **Collection deep nesting** - 3-4 level recursion needs enhancement
2. **Utility function spreads** - `...getSendAndWaitProperties([...])` detection added, resolution pending

### Medium Priority (5 issues)
3. Template literal API patterns (cosmetic)
4. Historical version extraction (V1/V2)
5. Remaining missing outputs (5 edge case nodes)

**Status:** Production-ready for 96%+ of nodes. Remaining issues affect <5% of nodes.

---

## Troubleshooting

### Empty Properties Extracted
**Rare** - Only 1 node affected (NoOp, correct by design)
- Run: `python3 validate_extraction.py`

### Node Not Found
```bash
python3 n8n_node_extractor.py list  # See available nodes (case-sensitive)
```

### n8n Directory Missing
```bash
git clone --depth 1 https://github.com/n8n-io/n8n.git n8n
```

---

## Essential Documentation

### Current System Docs
- **docs/ai_review_prompt.md** - ⭐ AI quality audit protocol (START HERE for validation)
- **docs/MULTI_AGENT_SYSTEM_README.md** - Complete multi-agent workflow
- **QUICK_START.md** - Quick reference for all agents

### Archived Documentation (in `_archive/`)
- `_archive/FIXES_APPLIED_2025-11-11_COMPREHENSIVE.md` - Historical fixes
- `_archive/validation_summaries/` - Old validation reports
- `_archive/reports/` - Old auto-generated reports

---

## Testing

### Quick Test
```bash
python3 n8n_node_extractor.py extract GoogleSheets
jq '.properties | length' extracted_docs/googlesheets_data.json  # Should be ~23
python3 validate_extraction.py
```

### Regression Test Nodes
```bash
python3 n8n_node_extractor.py extract Slack         # Multi-resource
python3 n8n_node_extractor.py extract HttpRequest   # Complex collections
python3 n8n_node_extractor.py extract Switch        # Dynamic outputs
python3 n8n_node_extractor.py extract Elasticsearch # Spread operators
```

---

## Dependencies

```bash
pip install pyyaml  # Required
python3 --version   # Needs 3.6+
```

---

## System Health

```bash
./health_check.sh        # Check for stale locks, validate heartbeats
./cleanup.sh             # Remove stale locks, archive old logs
```

---

## Performance Notes

- **Single node extraction:** <1 second
- **Bulk extraction (531 nodes):** ~7-10 seconds
- **Memory usage:** <500MB typical
- **Output size:** ~27MB total (JSON + MD)

---

## Statistics

### Extractor Code
- **Lines:** 2700+ (single file)
- **Classes:** 8 specialized extractors
- **Expression patterns:** 11
- **Field types:** 20+
- **Documentation sections:** 11 per node

### Multi-Agent System
- **Agents registered:** 3
- **Issues tracked:** 40
- **Fixes applied:** 21
- **Audit entries:** Complete history
- **System health:** ✅ All checks passing

---

## Success Metrics - ACHIEVED ✅

- ✅ Zero-property nodes: 1 (NoOp only - by design)
- ✅ GoogleSheets: 23 properties
- ✅ Slack: 111 properties
- ✅ HttpRequest: 42 properties
- ✅ Dynamic outputs: Working
- ✅ Operation tagging: 90%+
- ✅ Overall quality: 96%+ (target: 92-95%)

---

## Quick Reference

### View Status
```bash
ls -1 issues/resolved/*.json | wc -l   # Resolved issues
ls -1 fixes/applied/*.json | wc -l     # Applied fixes
python3 validate_extraction.py          # Run validation
```

### Common Patterns
```bash
# Test single node
python3 n8n_node_extractor.py extract <NodeName>

# Check property count
jq '.properties | length' extracted_docs/<nodename>_data.json

# Validate quality
python3 validate_extraction.py

# Multi-agent workflow
python3 agent_start.py --agent claude_code
# Follow prompts for issue claiming and fixing
```

---

**Version:** 3.2 (Production Ready)
**Repository:** https://github.com/ImBeasting/N8nScraper
**n8n Version:** 2.3.0 (January 8, 2026)
**Quality:** 96%+ across 451 nodes
**Status:** ✅ Active development
**Last Extraction:** 2026-01-08

For detailed technical documentation, see:
- QUICK_START.md (quick reference)
- docs/MULTI_AGENT_SYSTEM_README.md (multi-agent workflow)
- docs/ai_review_prompt.md (AI audit protocol)
