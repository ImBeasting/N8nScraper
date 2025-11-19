---
title: "Node: Local File Trigger"
slug: "node-localfiletrigger"
version: "1"
updated: "2025-11-13"
summary: "Triggers a workflow on file system changes"
node_type: "trigger"
group: "['trigger']"
---

# Node: Local File Trigger

**Purpose.** Triggers a workflow on file system changes
**Subtitle.** =Path: {{$parameter["path"]}}


---

## Node Details

- **Icon:** `fa:folder-open`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False
- **Trigger Panel:**
```json
{
  "executionsHelp": "{\n\t\t\t\tinactive:\n\t\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then make a change to your watched file or folder. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Once you're happy with your workflow</b>, <a data-key='activate'>activate</a> it. Then every time a change is detected, the workflow will execute. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t\t\tactive:\n\t\t\t\t\t\"<b>While building your workflow</b>, click the 'execute step' button, then make a change to your watched file or folder. This will trigger an execution, which will show up in this editor.<br /> <br /><b>Your workflow will also execute automatically</b>, since it's activated. Every time a change is detected, this node will trigger an execution. These executions will show up in the <a data-key='executions'>executions list</a>, but not in the editor.\",\n\t\t\t}",
  "activationHint": "Once you\u2019ve finished building your workflow, <a data-key="
}
```

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger On | `triggerOn` | options |  | ✓ |  |  |

**Trigger On options:**

* **Changes to a Specific File** (`file`)
* **Changes Involving a Specific Folder** (`folder`)

| File to Watch | `path` | string |  | ✗ | e.g. /data/invoices/1.pdf |  |
| Folder to Watch | `path` | string |  | ✗ | e.g. /data/invoices |  |
| Watch for | `events` | multiOptions | [] | ✓ | Triggers whenever a new file was added |  |

**Watch for options:**

* **File Added** (`add`) - Triggers whenever a new file was added
* **File Changed** (`change`) - Triggers whenever a file was changed
* **File Deleted** (`unlink`) - Triggers whenever a file was deleted
* **Folder Added** (`addDir`) - Triggers whenever a new folder was added
* **Folder Deleted** (`unlinkDir`) - Triggers whenever a folder was deleted

| Options | `options` | collection | {} | ✗ | Whether to wait until files finished writing to avoid partially read | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Await Write Finish | `awaitWriteFinish` | boolean | False | Whether to wait until files finished writing to avoid partially read |
| Include Linked Files/Folders | `followSymlinks` | boolean | True | Whether linked files/folders will also be watched (this includes symlinks, aliases on MacOS and shortcuts on Windows). Otherwise only the links themselves will be monitored). |
| Ignore | `ignored` | string |  | Files or paths to ignore. The whole path is tested, not just the filename. Supports <a href="https://github.com/micromatch/anymatch">Anymatch</a>- syntax. Regex patterns may not work on macOS. To ignore files based on substring matching, use the 'Ignore Mode' option with 'Contain'. |
| Ignore Existing Files/Folders | `ignoreInitial` | boolean | True | Whether to ignore existing files/folders to not trigger an event |
| Max Folder Depth | `depth` | options |  | How deep into the folder structure to watch for changes |
| Use Polling | `usePolling` | boolean | False | Whether to use polling for watching. Typically necessary to successfully watch files over a network. |
| Ignore Mode | `ignoreMode` | options | match | Ignore files using regex patterns (e.g., **/*.txt), Not supported on macOS |

</details>


---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Core Nodes
* Aliases: Watch, Monitor

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: localFileTrigger
displayName: Local File Trigger
description: Triggers a workflow on file system changes
version: '1'
nodeType: trigger
group:
- trigger
params:
- id: triggerOn
  name: Trigger On
  type: options
  default: ''
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Trigger On
    name: triggerOn
    possibleValues:
    - value: file
      name: Changes to a Specific File
      description: ''
    - value: folder
      name: Changes Involving a Specific Folder
      description: ''
- id: path
  name: File to Watch
  type: string
  default: ''
  required: false
  description: ''
  placeholder: /data/invoices/1.pdf
  validation: &id001
    displayOptions:
      show:
        triggerOn:
        - folder
  typeInfo: &id002
    type: string
    displayName: Folder to Watch
    name: path
- id: path
  name: Folder to Watch
  type: string
  default: ''
  required: false
  description: ''
  placeholder: /data/invoices
  validation: *id001
  typeInfo: *id002
- id: events
  name: Watch for
  type: multiOptions
  default: []
  required: true
  description: Triggers whenever a new file was added
  validation:
    required: true
    displayOptions:
      show:
        triggerOn:
        - folder
  typeInfo:
    type: multiOptions
    displayName: Watch for
    name: events
    possibleValues:
    - value: add
      name: File Added
      description: Triggers whenever a new file was added
    - value: change
      name: File Changed
      description: Triggers whenever a file was changed
    - value: unlink
      name: File Deleted
      description: Triggers whenever a file was deleted
    - value: addDir
      name: Folder Added
      description: Triggers whenever a new folder was added
    - value: unlinkDir
      name: Folder Deleted
      description: Triggers whenever a folder was deleted
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to wait until files finished writing to avoid partially read
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Await Write Finish
      name: awaitWriteFinish
      type: boolean
      description: Whether to wait until files finished writing to avoid partially
        read
      default: false
    - displayName: Include Linked Files/Folders
      name: followSymlinks
      type: boolean
      description: Whether linked files/folders will also be watched (this includes
        symlinks, aliases on MacOS and shortcuts on Windows). Otherwise only the links
        themselves will be monitored).
      default: true
    - displayName: Ignore
      name: ignored
      type: string
      description: Files or paths to ignore. The whole path is tested, not just the
        filename. Supports <a href="https://github.com/micromatch/anymatch">Anymatch</a>-
        syntax. Regex patterns may not work on macOS. To ignore files based on substring
        matching, use the 'Ignore Mode' option with 'Contain'.
      placeholder: '**/*.txt or ignore-me/subfolder'
      default: ''
    - displayName: Ignore Existing Files/Folders
      name: ignoreInitial
      type: boolean
      description: Whether to ignore existing files/folders to not trigger an event
      default: true
    - displayName: Max Folder Depth
      name: depth
      type: options
      description: How deep into the folder structure to watch for changes
      options:
      - name: 1 Levels Down
        displayName: 1 Levels Down
      - name: 2 Levels Down
        displayName: 2 Levels Down
      - name: 3 Levels Down
        displayName: 3 Levels Down
      - name: 4 Levels Down
        displayName: 4 Levels Down
      - name: 5 Levels Down
        displayName: 5 Levels Down
      - name: Top Folder Only
        displayName: Top Folder Only
      - name: Unlimited
        displayName: Unlimited
    - displayName: Use Polling
      name: usePolling
      type: boolean
      description: Whether to use polling for watching. Typically necessary to successfully
        watch files over a network.
      default: false
    - displayName: Ignore Mode
      name: ignoreMode
      type: options
      description: Ignore files using regex patterns (e.g., **/*.txt), Not supported
        on macOS
      value: match
      default: match
      options:
      - name: Match
        description: Ignore files using regex patterns (e.g., **/*.txt), Not supported
          on macOS
        value: match
        displayName: Match
      - name: Contain
        description: Ignore files if their path contains the specified value
        value: contain
        displayName: Contain
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: path
    text: /data/invoices/1.pdf
  - field: path
    text: /data/invoices
  - field: options
    text: Add option
  hints: []
settings:
  common:
    notes:
      name: Notes
      field_id: notes
      type: string
      default: ''
      description: Optional note to save with the node
    notesInFlow:
      name: Display Note in Flow?
      field_id: notesInFlow
      type: boolean
      default: false
      description: If active, the note above will display in the flow as a subtitle
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/localFileTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Local File Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "triggerOn": {
          "description": "",
          "type": "string",
          "enum": [
            "file",
            "folder"
          ],
          "default": ""
        },
        "path": {
          "description": "",
          "type": "string",
          "default": "",
          "examples": [
            "/data/invoices"
          ]
        },
        "events": {
          "description": "Triggers whenever a new file was added",
          "type": "string",
          "default": []
        },
        "options": {
          "description": "Whether to wait until files finished writing to avoid partially read",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        }
      }
    },
    "settings": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "notes": {
          "type": "string",
          "default": "",
          "description": "Optional note to save with the node"
        },
        "notesInFlow": {
          "type": "boolean",
          "default": false,
          "description": "If active, the note above will display in the flow as a subtitle"
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
    "version": "1"
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
