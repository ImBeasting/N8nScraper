# AGENTS.md - N8nScraper Multi-Agent Coordination System

## Project Overview
**N8nScraper** is a Python-based extraction engine designed to convert the n8n source code (TypeScript node definitions) into comprehensive, structured documentation (JSON/Markdown) for AI training purposes.

**Key Goal:** Extract 100% of node properties, credentials, outputs, and metadata from the upstream `n8n/` directory.

## System Architecture
The project operates as a **multi-agent collaboration system** where different AI agents (Claude, Gemini, OpenAI) perform specialized roles.

### Directory Structure
*   **`n8n_node_extractor.py`**: The core extraction logic.
*   **`n8n/`**: The target n8n source code (ReadOnly).
*   **`extracted_docs/`**: The output directory for scraped JSON/MD files.
*   **`issues/`**: Active issue tracking (JSON format).
    *   `critical/`, `high/`, `medium/`, `low/`: Severity buckets.
    *   `resolved/`: Completed tasks.
*   **`fixes/`**: Applied patches and improvements.
*   **`docs/`**: System documentation and guides.

## Operational Workflow

1.  **Discovery:** Agents run `validate_extraction.py` or `n8n_node_extractor.py` to find bugs or missing data.
2.  **Reporting:** Create a JSON issue file in `issues/<severity>/` (e.g., `_agent_issue_001_missing_icon.json`).
3.  **Coordination:** Use `agent_start.py` and `claim_issue.py` to lock tasks (prevents collisions).
4.  **Implementation:** Modify `n8n_node_extractor.py` to fix the bug.
5.  **Verification:** Run extraction on the affected node and verify the output.
6.  **Resolution:** Move the issue file to `issues/resolved/` and document the fix.

## Agent Roles & Responsibilities

### 🧠 Claude (Architect & Logic)
*   **Focus:** Complex refactoring, TypeScript parsing logic, architectural decisions.
*   **Tasks:** Handling versioned nodes, recursive collection parsing, dynamic output resolution.
*   **Guide:** See `CLAUDE.md`.

### ⚡ Gemini (Execution & DevOps)
*   **Focus:** Shell operations, file management, high-speed testing, system integrity.
*   **Tasks:** Running bulk extractions, verifying fixes across hundreds of nodes, managing the file system, cleaning up logs.
*   **Guide:** See `GEMINI.md`.

### 🤖 OpenAI (Code Generation & Patterns)
*   **Focus:** Regex optimization, generating boilerplate, spotting syntax patterns.
*   **Tasks:** Writing specific parser functions, generating unit tests, fixing small logic errors.
*   **Guide:** See `OPENAI.md`.

## Best Practices
1.  **PascalCase Directories:** All project directories use PascalCase (e.g., `~/Projects/N8nScraper`).
2.  **Relative Paths:** Always use `Path(__file__).parent` or relative paths. **NEVER** hardcode `/home/tyler` or `/media/...`.
3.  **Git Identity:** Commits should be made as `Tyler <fringethresholdstudios@gmail.com>`.
4.  **Atomic Writes:** When updating JSON/scripts, ensure the file is written completely to avoid corruption.

## Current Status (Nov 2025)
*   **Project:** Restored and Cleaned.
*   **Git:** Initialized.
*   **Open Issues:** Critical issue `_gemini_issue_011` (Webhook extraction) and `_claude_issue_017` (GoogleSheets metadata) are confirmed open.

