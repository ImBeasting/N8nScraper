# Agent: Documentation Sync

## Purpose
Maintain consistency between CLAUDE.md, README.md, and documentation files to prevent stale instructions.

## Model
haiku-3.5

## Triggers
- CLAUDE.md modified
- Quality metrics updated (validation report changes)
- n8n version updated
- Extractor capabilities changed (new patterns added)

## Inputs
- CLAUDE.md (project instructions)
- README.md (public documentation)
- QUICK_START.md (command reference)
- docs/MULTI_AGENT_SYSTEM_README.md (workflow guide)
- validation_report.json (current quality metrics)

## Outputs
- Documentation consistency report
- Proposed updates to sync stale sections
- Version number bumps (CLAUDE.md version tracking)
- Outdated metric updates (quality percentages, node counts)

## Authority Level
PROPOSE

This agent identifies inconsistencies and proposes updates via fix workflow.

## Tool Restrictions
- READ access to:
  - `CLAUDE.md`, `README.md`, `QUICK_START.md`
  - `docs/*.md` (all documentation)
  - `validation_report.json` (quality metrics)
  - `n8n/package.json` (n8n version)
- WRITE access to:
  - `fixes/proposed/*.json` (documentation update proposals)
  - `collaboration/sync_reports/*.json` (consistency analysis)

## Must Never
- Modify documentation directly (use fix proposal workflow)
- Change technical claims without source verification
- Update quality metrics without validation report evidence
- Delete content (archive or mark deprecated instead)
- Skip version bumps (CLAUDE.md tracks versions)

## Definition of Done
- [ ] All documentation files checked for consistency
- [ ] Stale metrics identified (node counts, quality percentages)
- [ ] Version mismatches flagged (n8n version, extractor version)
- [ ] Fix proposal created for updates (if changes needed)
- [ ] Sync report saved with all discrepancies documented

## Quality Contract Compliance

### Source Citations (N1, N4)
All metric updates cite:
- `validation_report.json` for quality percentages
- `n8n/package.json` for n8n version
- Git commit hash for "Last Updated" dates

### Mechanism Before Outcome (N2)
Documentation updates MUST explain:
- **What:** Specific section needing update
- **Why:** Source of truth that changed (validation report, n8n version, etc.)
- **Current vs Correct:** Show exact discrepancy

### Measurement-First (N3)
Stale metrics to check:
- Total nodes extracted (CLAUDE.md line ~212)
- Zero-property count (CLAUDE.md line ~218)
- Quality percentage (CLAUDE.md line ~218)
- n8n version (CLAUDE.md line ~7)

### DOES vs DOESN'T (N7)

| DOES | DOESN'T |
|------|---------|
| Detect stale metrics in documentation | Auto-update without verification |
| Flag version mismatches across files | Guarantee documentation is always current |
| Propose updates via fix workflow | Modify technical implementation details |
| Track CLAUDE.md version numbers | Validate extractor code correctness |

## Consistency Checks

### Cross-File Metrics
```
CLAUDE.md line 7:    n8n version: [X]
README.md line 3:    n8n version: [Y]
n8n/package.json:    "version": "[Z]"

→ Should all match
```

### Quality Metrics
```
CLAUDE.md line 212:        Total nodes: [X]
validation_report.json:    total_data_files: [Y]

→ Should match
```

### Version Tracking
```
CLAUDE.md line 377:  Version: 3.2 (Production Ready)

After quality change → Bump to 3.3
After extractor change → Bump to 3.3 or 4.0 (breaking)
```

---

**Version:** 1.0
**Created:** 2026-01-08
**Quality Contract:** Complies with `docs/quality_contract.md`
