# Repository Guidelines - Multi-Agent System

## Project Overview
This workspace hosts the **n8n Node Scrapper multi-agent coordination system**. Python automation wraps the upstream `n8n` source (mirrored under `n8n/`) to extract node metadata, track quality issues, and manage fixes through collaborating AI agents (Claude Code, Google Gemini CLI, and OpenAI Codex CLI). The coordination layer lives at the repository root and orchestrates locking, issue management, and report generation around the primary extractor script `n8n_node_extractor.py`.

## 🎯 Quality Validation Protocol

All agents should perform regular quality audits using the standardized protocol:

```
Please conduct a comprehensive quality audit following the protocol in:
/media/tyler/fastraid/Projects/n8n Node Scrapper/ai_review_prompt.md
```

**What this does:**
- 7-phase systematic validation (~80 minutes)
- Cross-references extracted data with TypeScript source
- Documents issues with quantified evidence
- Identifies patterns affecting multiple nodes
- Generates summary report in `validation_summaries/`

**See:** `START_AI_AUDIT.md` for detailed instructions.

## Environment & Tooling
- Prefer Python 3.10+; every helper script uses `#!/usr/bin/env python3`.
- `jq` is used in documentation examples for inspecting JSON indexes.
- No Node.js or pnpm workflows are required for the coordination layer (the upstream `n8n/` tree is treated as read-only input).
- Ensure scripts in the root (`*.py`, `*.sh`) are executable when run directly.

## Key Directories
- `collaboration/` — Runtime state for the agent network (`coordination.json`, `agent_heartbeats.json`, `audit_log.jsonl`, and per-issue `.lock` directories).
- `issues/` — JSON issues grouped by severity (`critical/`, `high/`, `medium/`, `low/`) with a consolidated `index.json`. Issue statuses flow `new → in_progress → review → resolved`.
- `fixes/` — Fix metadata (`proposed/`, `applied/`, `templates/`) plus `index.json`. Fix entries reference resolved issue IDs and record testing notes.
- `reports/` — Auto-generated markdown summaries (`EXTRACTION_ERRORS_REPORT.md`, `FIXES_APPLIED_REPORT.md`, `AGENT_ACTIVITY_REPORT.md`) and `generation_metadata.json`. Never edit these files directly; regenerate them.
- `validation_summaries/` — Agent quality audit reports (`VALIDATION_SUMMARY_<date>_<agent>.md`). All validation summaries are organized here.
- `extracted_docs/` — Output data from `n8n_node_extractor.py` used by validation tooling.
- `logs` & archives — `*.log` files at the root capture extraction runs and migrations; keep them for traceability.
- `n8n_node_extractor.py` and `validate_extraction.py` are the main operational scripts for extraction and quality checks.
- `ai_review_prompt.md` — Comprehensive quality audit protocol for systematic validation (⭐ use this for audits).

## Coordination Workflow
1. **Start a session** with `python3 agent_start.py --agent <claude_code|gemini_cli|openai_codex>` to record a heartbeat, list active tasks, and view open issues by severity.
2. **Claim work** via `python3 claim_issue.py --agent <name> --issue issue_XXX`. This acquires an atomic lock (`collaboration/issue_XXX.lock`), updates ownership, and moves the issue to `in_progress`.
3. **Implement and test** changes, typically in `n8n_node_extractor.py` or related helpers. Capture results and affected files.
4. **Propose a fix** using `python3 propose_fix.py --agent <name> --fix fix_YYY --issue issue_XXX --title "..." --approach "..." --files "file1.py,file2.py" [--tested --test-notes "..."]`. This writes a JSON entry under `fixes/proposed/` and refreshes `fixes/index.json`.
5. **Apply/approve fixes** with `python3 apply_fix.py --agent <name> --fix fix_YYY` once validated. The command moves metadata into `fixes/applied/`, updates indexes, and marks the linked issue as `resolved`.
6. **Release work** if blocked by calling `python3 release_issue.py --agent <name> --issue issue_XXX` to drop locks and restore the previous status.
7. **Regenerate reports** after any approved change: `python3 generate_reports.py`. This rebuilds every markdown report and writes backups in `reports/backups/`.

## Locking & Collaboration Rules
- The coordination client (`coordination_lib.CoordinationClient`) enforces atomic directory-based locks and expires them after 60 minutes. Never manually create or delete lock directories; use the provided scripts or `cleanup.sh` for stale locks.
- Agent registration lives in `collaboration/coordination.json`. All scripts validate that the agent name is known before mutating state.
- `collaboration/audit_log.jsonl` is append-only and captures every meaningful action. Do not truncate it without archiving.
- Heartbeats are updated on every command run so the system can detect idle agents.

## Data & Reporting Conventions
- Treat `issues/*.json` and `fixes/*.json` as the single source of truth. Modify these via coordination scripts or by hand only when the scripts do not cover a maintenance use case, then immediately run `python3 generate_reports.py` to refresh markdown outputs.
- `reports/backups/` stores previous report revisions automatically — retain them for auditing.
- Whenever new issues or fixes are created outside the helper scripts, update `index.json` by running the coordination client's index refresh routines (triggered automatically by the scripts) or `python3 generate_reports.py`.
- All extracted node artifacts should remain in `extracted_docs/` with the `_data.json` and `_documentation.md` naming convention expected by the validator.

## Testing & Validation
- Run `python3 validate_extraction.py` to scan `extracted_docs/` for duplicates, empty property sets, unresolved template variables, and other quality issues. The script emits a summary and writes a detailed report alongside validation metrics.
- Use `./verify_phase4.sh` to confirm the coordination scripts and library are consistent; it exercises the main command-line entry points.
- `./health_check.sh` inspects lock freshness, agent registrations, and index consistency. Run it when state files look suspicious or after a system restart.
- `./cleanup.sh` safely removes stale locks and temp files; use it when you see expired lock metadata.

## Maintenance Notes
- Keep the absolute `PROJECT_ROOT` path in `coordination_lib.py`, `validate_extraction.py`, and related scripts up to date if the project directory moves.
- `migrate_to_collaboration_system.py` and the logs under `reports/backups/` document the initial migration from markdown-only reporting; do not delete them.
- Archive or rotate large `*.log` files rather than deleting them so that automation history remains available.
- The upstream `n8n/` mirror is large—avoid modifying it from coordination scripts unless a fix explicitly requires touching the source. Treat it as read-only input for the extractor.

## Quick Reference Commands

### Agent Session Management
- `python3 agent_start.py --agent <agent_name>` — Start a session and list work.
- `python3 claim_issue.py --agent <agent_name> --issue <issue_id>` — Claim an issue (includes locking).
- `python3 release_issue.py --agent <agent_name> --issue <issue_id>` — Release an issue lock.

### Fix Workflow
- `python3 propose_fix.py --agent <agent_name> --fix <fix_id> --issue <issue_id> --title "..." --approach "..." --files "..." --tested --test-notes "..."` — Submit a fix record.
- `python3 apply_fix.py --agent <agent_name> --fix <fix_id>` — Apply approved fix.

### Quality & Reporting
- `python3 validate_extraction.py` — Run automated extraction quality validation.
- `python3 generate_reports.py` — Rebuild all markdown reports from JSON sources.
- `./health_check.sh` / `./cleanup.sh` — Monitor and repair coordination state.

### Quality Audits
- **Comprehensive audit:** Follow protocol in `ai_review_prompt.md`
- **Quick audit guide:** See `START_AI_AUDIT.md`
- **Results location:** `validation_summaries/VALIDATION_SUMMARY_<date>_<agent>.md`

## Agent-Specific Documentation
- **CLAUDE.md** — Comprehensive project documentation and quick reference
- **GEMINI.md** — Gemini CLI agent guide
- **OPENAI.md** — OpenAI Codex agent guide
- **AGENT_COLLABORATION_GUIDE.md** — Complete multi-agent workflow
- **ai_review_prompt.md** — Quality audit protocol (⭐ primary validation guide)
- **START_AI_AUDIT.md** — How to launch validation audits
