# How to Start an AI Quality Audit

## Quick Start (Copy/Paste This)

Use this exact message with **any AI agent** (Claude Code, Gemini, ChatGPT, etc.):

```
Please conduct a comprehensive quality audit following the protocol in:
/media/tyler/fastraid/Projects/n8n Node Scrapper/ai_review_prompt.md

This is your validation assignment for the n8n node extraction project.
```

**That's it!** The AI will read the protocol and begin the systematic audit.

---

## What Happens Next

The AI will automatically:

1. ✅ Run baseline validation (`python3 validate_extraction.py`)
2. ✅ Sample 35-50 nodes strategically
3. ✅ Cross-reference extracted data with TypeScript source files
4. ✅ Document all issues found with quantified evidence
5. ✅ Identify patterns affecting multiple nodes
6. ✅ Generate reports (`python3 generate_reports.py`)
7. ✅ Create validation summary in `validation_summaries/`

**Time:** ~80 minutes for thorough audit

---

## Multi-Agent Workflow

### Starting Multiple Agents

Run audits in parallel for faster coverage:

**Claude Code:**
```bash
# Terminal 1
Please conduct a comprehensive quality audit following the protocol in:
/media/tyler/fastraid/Projects/n8n Node Scrapper/ai_review_prompt.md
```

**Gemini CLI:**
```bash
# Terminal 2
Please conduct a comprehensive quality audit following the protocol in:
/media/tyler/fastraid/Projects/n8n Node Scrapper/ai_review_prompt.md
```

**OpenAI Codex:**
```bash
# Terminal 3
Please conduct a comprehensive quality audit following the protocol in:
/media/tyler/fastraid/Projects/n8n Node Scrapper/ai_review_prompt.md
```

---

## Expected Deliverables

Each AI agent will produce:

1. **Issues** - JSON files in `issues/<severity>/`
   - Format: `_<agent>_issue_<nnn>_description.json`
   - 5-20+ issues depending on findings

2. **Validation Summary** - Markdown report in `validation_summaries/`
   - Format: `VALIDATION_SUMMARY_<date>_<agent>.md`
   - Includes: stats, findings, recommendations

3. **Updated Reports** - Auto-generated in `reports/`
   - `EXTRACTION_ERRORS_REPORT.md`
   - `FIXES_APPLIED_REPORT.md`
   - `AGENT_ACTIVITY_REPORT.md`

---

## Troubleshooting

### AI Can't Read the File?

If the AI says it can't access the file:

**Option 1: Verify path**
```bash
ls -la "/media/tyler/fastraid/Projects/n8n Node Scrapper/ai_review_prompt.md"
```

**Option 2: Paste content instead**
```bash
cat "/media/tyler/fastraid/Projects/n8n Node Scrapper/ai_review_prompt.md"
# Copy output and paste to AI with: "Follow this protocol:"
```

### AI Starts But Gets Stuck?

Remind it of the phases:
```
You're currently on Phase X. Please continue with the next steps:
[Reference specific phase from protocol]
```

### Want a Quick Status Check?

```
What phase are you on? How many nodes analyzed so far? Any issues found?
```

---

## After Audit Completion

### Review Results

```bash
# Check issues created by agent
ls -1 issues/*/_<agent>_issue_*.json

# View validation summary
cat validation_summaries/VALIDATION_SUMMARY_<date>_<agent>.md

# Check updated reports
cat reports/EXTRACTION_ERRORS_REPORT.md
```

### Act on Findings

1. Review the agent's validation summary
2. Prioritize issues by severity (critical → high → medium → low)
3. Claim high-priority issues: `python3 claim_issue.py --agent <agent> --issue <id>`
4. Fix and test: Work through issues systematically
5. Apply fixes: `python3 apply_fix.py --agent <agent> --fix <id>`

---

## Pro Tips

### For Best Results

✅ **Let the AI work autonomously** - The protocol is comprehensive, trust the process

✅ **Run multiple agents** - Parallel audits cover more ground and find different issues

✅ **Review summaries first** - Prioritize based on "Top 5 Critical Findings" section

✅ **Cross-reference agents** - If 2+ agents find the same issue, it's definitely real

### Avoid These Mistakes

❌ **Don't interrupt mid-phase** - Let each phase complete before asking questions

❌ **Don't skip the summary** - It's the most valuable deliverable

❌ **Don't ignore patterns** - Pattern issues affect many nodes, fix these first

---

## Example Session

```
User: Please conduct a comprehensive quality audit following the protocol in:
      /media/tyler/fastraid/Projects/n8n Node Scrapper/ai_review_prompt.md

AI:   I'll begin the quality audit following the protocol...

      Phase 1: Baseline Assessment
      Running: python3 validate_extraction.py
      Stats: 450 files, 1 zero-property node, 0 null displayNames...

      Phase 2: Strategic Sampling
      Selected 38 nodes across categories:
      - 5 zero-property nodes
      - 5 high-value nodes (Slack, HTTP Request...)
      ...

      [80 minutes later]

      Phase 7: Validation Summary
      Created: validation_summaries/VALIDATION_SUMMARY_2025-11-13_claude_code.md

      Summary:
      - Nodes sampled: 38 (8.4% of total)
      - Issues found: 12 total (4 critical, 5 high, 2 medium, 1 low)
      - Top 3 problems:
        1. [Issue #028] Pattern: All versioned nodes...
        2. [Issue #029] Slack operations missing properties...
        3. [Issue #030] Collection nesting depth limit...

      Audit complete. Recommend prioritizing Issues #028-030 for immediate fixing.
```

---

**Quick Reference:** `ai_review_prompt.md` contains the full protocol
**Questions?** Check `validation_summaries/README.md` for more details
