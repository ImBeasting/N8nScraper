# OPENAI.md

Guidance for the OpenAI Codex CLI agent (`openai_codex`) working in this repository.

## Project Snapshot
- Python automation extracts metadata from the upstream `n8n/` source tree into `extracted_docs/`.
- Collaboration assets live at the repository root (`issues/`, `fixes/`, `collaboration/`, `reports/`, `validation_summaries/`).
- Key scripts: `n8n_node_extractor.py`, `validate_extraction.py`, and the coordination helpers (`agent_start.py`, `claim_issue.py`, etc.).
- **Quality audit protocol:** `ai_review_prompt.md` - Follow this for comprehensive validation audits.

## 🎯 Quick Start: Quality Audit

To perform a comprehensive quality audit of the extraction:

```
Please conduct a comprehensive quality audit following the protocol in:
/media/tyler/fastraid/Projects/n8n Node Scrapper/ai_review_prompt.md
```

This will guide you through a systematic 7-phase validation process. Your results will be saved to `validation_summaries/VALIDATION_SUMMARY_<date>_openai_codex.md`.

**See also:** `START_AI_AUDIT.md` for detailed audit instructions.

## ⚠️ Issue Naming Convention (Updated 2025-11-06)
The coordination system now uses **per-agent sequential issue IDs** to eliminate filename collisions.

### Format
```
_<agent>_issue_<nnn>_<description>.json
```

### Your Prefix & Counter
- **Agent prefix:** `_openai_`
- **Next issue ID:** `_openai_issue_001` (no OpenAI-created issues yet)

### Examples
- `_openai_issue_001_versioned_nodes_missing_metadata.json`
- `_openai_issue_002_inputs_outputs_not_parsed.json`
- `_claude_issue_010_collection_defaults_missing.json` *(cross-agent example)*

### Script Usage
```bash
# Start a session and view available work
python3 agent_start.py --agent openai_codex

# Claim an issue (agent ownership does not matter)
python3 claim_issue.py --agent openai_codex --issue _claude_issue_007

# Release when done
python3 release_issue.py --agent openai_codex --issue _claude_issue_007

# Propose a fix referencing the new-format issue ID
python3 propose_fix.py \
  --agent openai_codex \
  --fix fix_001 \
  --issue _openai_issue_001 \
  --title "Fix title" \
  --approach "Fix approach" \
  --files "n8n_node_extractor.py" \
  --tested --test-notes "Notes here"
```

### Migration Reference
- **Migration summary:** `ISSUE_NAMING_MIGRATION_COMPLETE.md`
- **Mapping file:** `issue_migration_mapping.json`
- **Backup:** `issues_backup_20251106/`

### Validation Checklist
- [x] Understand the `_openai_issue_<nnn>` format
- [x] Know the next ID to use (`_openai_issue_001`)
- [x] Confirm renamed files under `issues/`
- [ ] Create OpenAI-owned issues using the new convention

## Core Workflow Reminders
1. `python3 agent_start.py --agent openai_codex` to register your heartbeat.
2. Claim work: `python3 claim_issue.py --agent openai_codex --issue <issue_id>`.
3. Make and test changes (keep upstream `n8n/` read-only unless required).
4. Propose fixes with `propose_fix.py`; apply via `apply_fix.py` once validated.
5. Regenerate reports after approvals: `python3 generate_reports.py`.
6. Release locks if blocked: `python3 release_issue.py --agent openai_codex --issue <issue_id>`.

## Quality & Maintenance
- Run `python3 validate_extraction.py` after extractor changes; review `validation_report.json`.
- Use `./verify_phase4.sh` for coordination script smoke tests.
- Keep logs (`*.log`) and backups intact for auditability.
- Never manually create/delete `.lock` directories; use the provided scripts or `./cleanup.sh`.

## Quick References
- Coordination state: `collaboration/coordination.json`, `collaboration/agent_heartbeats.json`.
- Issues catalogue: `issues/index.json`.
- Fix metadata: `fixes/index.json`, `fixes/proposed/`, `fixes/applied/`.
- Reports: `reports/*.md` (regenerate, do not hand-edit).
- Validation summaries: `validation_summaries/` (all audit reports organized here).
- Audit protocol: `ai_review_prompt.md` (comprehensive quality validation guide).
- Quick start: `START_AI_AUDIT.md` (how to launch validation audits).

## Repository Structure
```
/media/tyler/fastraid/Projects/n8n Node Scrapper/
├── n8n/                              # n8n source (530+ node definitions)
├── extracted_docs/                   # Output (900 files: 450 JSON + 450 MD)
├── n8n_node_extractor.py             # Main extractor
├── validate_extraction.py            # Automated validation
├── ai_review_prompt.md               # ⭐ Quality audit protocol
├── START_AI_AUDIT.md                 # Quick audit launch guide
├── collaboration/                    # Multi-agent coordination
├── issues/                           # Issue tracking by severity
├── fixes/                            # Fix tracking
├── reports/                          # Auto-generated reports
├── validation_summaries/             # Agent validation reports
└── OPENAI.md                         # This file
```

**Last reviewed:** 2025-11-13 (OpenAI Codex agent)
Stay aligned with the new naming scheme for every new issue you create.
