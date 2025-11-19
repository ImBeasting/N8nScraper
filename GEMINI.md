# n8n Node Scrapper for AI Training - Gemini CLI Guide

This project contains a Python script (`n8n_node_extractor.py`) designed to extract comprehensive documentation from n8n nodes. The extracted information is formatted into both Markdown (`_documentation.md`) and JSON (`_data.json`) files, making it suitable for AI training and analysis.

## 🎯 Quick Start: Quality Audit

To perform a comprehensive quality audit of the extraction (recommended for Gemini CLI):

```
Please conduct a comprehensive quality audit following the protocol in:
/media/tyler/fastraid/Projects/n8n Node Scrapper/ai_review_prompt.md
```

This will guide you through a systematic 7-phase validation process (~80 minutes). Your results will be saved to `validation_summaries/VALIDATION_SUMMARY_<date>_gemini_cli.md`.

**See also:** `START_AI_AUDIT.md` for detailed audit instructions and troubleshooting.

## ⚠️ IMPORTANT: Issue Naming Convention (Updated 2025-11-06)

**All issues now use per-agent sequential numbering to prevent collisions between AI agents:**

### New Naming Format
```
_<agent>_issue_<nnn>_<description>.json
```

**Examples:**
- `_gemini_issue_001_missing_value_in_options.json`
- `_claude_issue_001_outputs_field_extracted_as_string.json`
- `_openai_issue_001_future_discovery.json`

### Current Issue Counts
- **gemini_cli:** issues 001-012
- **claude_code:** issues 001-014
- **openai_codex:** issues 001-??? (ready for future discoveries)

### Usage in Scripts
```bash
# Claim an issue
python3 claim_issue.py --agent gemini_cli --issue _gemini_issue_001

# Propose a fix
python3 propose_fix.py --agent gemini_cli --fix fix_013 --issue _gemini_issue_001 --title "Fix title"

# Release an issue
python3 release_issue.py --agent gemini_cli --issue _gemini_issue_001
```

**Migration completed:** 2025-11-06
**Backup location:** `issues_backup_20251106/`
**Migration mapping:** `issue_migration_mapping.json`

## Project Structure

```
/media/tyler/fastraid/Projects/n8n Node Scrapper/
├── n8n/                              # n8n source (530+ node definitions)
├── extracted_docs/                   # Output (900 files: 450 JSON + 450 MD)
├── n8n_node_extractor.py             # Main extractor (2700+ lines)
├── validate_extraction.py            # Automated quality validation
├── ai_review_prompt.md               # ⭐ Quality audit protocol (USE THIS!)
├── START_AI_AUDIT.md                 # Quick audit launch guide
├── collaboration/                    # Multi-agent coordination
│   ├── coordination.json             # Agent registry
│   ├── agent_heartbeats.json         # Status tracking
│   └── audit_log.jsonl               # Action history
├── issues/                           # Issue tracking by severity
│   ├── critical/, high/, medium/, low/
│   └── index.json
├── fixes/                            # Fix tracking
│   ├── applied/, proposed/
│   └── index.json
├── reports/                          # Auto-generated reports
│   ├── EXTRACTION_ERRORS_REPORT.md
│   ├── FIXES_APPLIED_REPORT.md
│   └── AGENT_ACTIVITY_REPORT.md
├── validation_summaries/             # Agent validation reports
│   ├── VALIDATION_SUMMARY_<date>_<agent>.md
│   └── README.md
├── coordination_lib.py               # Multi-agent library
├── agent_start.py                    # Start agent session
├── claim_issue.py                    # Claim an issue
├── propose_fix.py                    # Propose a fix
├── apply_fix.py                      # Apply approved fix
├── release_issue.py                  # Release issue lock
├── generate_reports.py               # Regenerate all reports
├── health_check.sh                   # System health check
└── GEMINI.md                         # This file
```

## Key Features and Improvements

The `n8n_node_extractor.py` script has been significantly improved to address several issues and extract more comprehensive information:

-   **Improved Node Type Detection**: The script now accurately identifies node types (regular, trigger, webhook).
-   **Enhanced Property Extraction**:
    -   **Authentication Details**: Extracts detailed authentication information, including `name` and `description`.
    -   **`icon`**: Extracts the icon associated with the node.
    -   **`defaults`**: Extracts default values for node parameters.
    -   **`inputs` and `outputs`**: Extracts information about node inputs and outputs, parsing `NodeConnectionTypes` correctly.
    -   **`group`**: Extracts the group the node belongs to.
    -   **`loadOptionsMethods`**: Identifies and extracts `loadOptionsMethod` definitions.
    -   **Trigger-Specific Properties**: Extracts `eventTriggerDescription`, `activationMessage`, `triggerPanel`, and `supportsCORS` for trigger and webhook nodes.
-   **Robust Regex Handling**: All regular expressions used for parsing TypeScript files have been carefully reviewed and corrected for proper escaping, resolving `SyntaxError` issues.
-   **Safer Data Extraction**: Replaced `eval()` with safer regex-based parsing for `inputs` to prevent `NameError` and improve security.
-   **Error Handling**: Improved handling of missing keys in extracted data (e.g., `name` and `description` in authentication details) to prevent `KeyError` exceptions.
-   **YAML Readability**: The script now uses `yaml.Dumper` for improved YAML output readability (though this is not directly visible in the Markdown output, it's an internal improvement for JSON/YAML generation).

## Multi-Agent Collaboration System

This project now includes a multi-agent collaboration system that allows multiple AI agents to work together on improving the `n8n_node_extractor.py` script. The system is designed to manage issues, fixes, and reports in a structured way, preventing conflicts and ensuring a smooth workflow.

For more details on the multi-agent system, please refer to the following documents:

-   `MULTI_AGENT_SYSTEM_README.md`: Provides a complete overview of the system, including its architecture, features, and usage.
-   `AGENT_COLLABORATION_GUIDE.md`: A comprehensive guide for agents on how to use the system.

## Usage

To use the `n8n_node_extractor.py` script, navigate to the project's root directory in your terminal.

### Prerequisites

-   Python 3.x
-   PyYAML library (`pip install PyYAML`)
-   A local clone of the n8n repository, with the `packages/nodes-base` directory located at `./n8n/packages/nodes-base` relative to the script.

### Commands

1.  **List all available nodes:**
    ```bash
    python3 n8n_node_extractor.py list
    ```

2.  **Extract documentation for a specific node:**
    ```bash
    python3 n8n_node_extractor.py extract <NodeName>
    ```
    Replace `<NodeName>` with the actual name of the n8n node (e.g., `ReadWriteFile`, `Salesforce`, `Webhook`).

3.  **Extract documentation for all nodes:**
    ```bash
    python3 n8n_node_extractor.py extract-all
    ```

### Multi-Agent Collaboration Commands

- **Start agent session:**
  ```bash
  python3 agent_start.py --agent gemini_cli
  ```

- **Claim an issue:**
  ```bash
  python3 claim_issue.py --agent gemini_cli --issue _gemini_issue_001
  ```

- **Propose a fix:**
  ```bash
  python3 propose_fix.py --agent gemini_cli --fix fix_013 --issue _gemini_issue_001 --title "Fix title"
  ```

- **Release an issue:**
  ```bash
  python3 release_issue.py --agent gemini_cli --issue _gemini_issue_001
  ```

## Quality Validation

After making changes to the extractor:

1. **Run automated validation:**
   ```bash
   python3 validate_extraction.py
   ```

2. **Review validation report:**
   ```bash
   cat validation_report.json | jq '.stats'
   ```

3. **Conduct comprehensive audit** (recommended after major changes):
   ```
   Follow protocol in: /media/tyler/fastraid/Projects/n8n Node Scrapper/ai_review_prompt.md
   ```

   Save your summary to: `validation_summaries/VALIDATION_SUMMARY_<date>_gemini_cli.md`

## Key Documentation Files

- **CLAUDE.md** - Comprehensive project documentation
- **AGENT_COLLABORATION_GUIDE.md** - Multi-agent workflow guide
- **QUICK_START.md** - Quick reference for all agents
- **ai_review_prompt.md** - Quality audit protocol (for validation audits)
- **START_AI_AUDIT.md** - How to launch validation audits

**Last Updated:** 2025-11-13 (Gemini CLI agent)
