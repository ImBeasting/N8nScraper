---
title: "Node: KoBoToolbox Trigger"
slug: "node-kobotoolboxtrigger"
version: "1"
updated: "2026-01-08"
summary: "Process KoBoToolbox submissions"
node_type: "trigger"
group: "['trigger']"
---

# Node: KoBoToolbox Trigger

**Purpose.** Process KoBoToolbox submissions


---

## Node Details

- **Icon:** `file:koBoToolbox.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **koBoToolboxApi**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `koBoToolboxApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** GET

**Common Endpoints:**
- `/api/v2/assets/`

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Trigger On | `triggerOn` | options | formSubmission | ✓ |  |  |

**Trigger On options:**

* **On Form Submission** (`formSubmission`)

| Options | `formatOptions` | collection | {} | ✗ | Whether to download submitted attachments | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Download Attachments | `download` | boolean | False | Whether to download submitted attachments |
| Attachments Naming Scheme | `binaryNamingScheme` | options | sequence |  |
| Attachments Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" |
| File Size | `version` | options | download_url | Attachment size to retrieve, if multiple versions are available |
| Multiselect Mask | `selectMask` | string | select_* | Comma-separated list of wildcard-style selectors for fields that should be treated as multiselect fields, i.e. parsed as arrays. |
| Number Mask | `numberMask` | string | n_*, f_* | Comma-separated list of wildcard-style selectors for fields that should be treated as numbers |
| Reformat | `reformat` | boolean | False | Whether to apply some reformatting to the submission data, such as parsing GeoJSON coordinates |

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
* Categories: Communication, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: koBoToolboxTrigger
displayName: KoBoToolbox Trigger
description: Process KoBoToolbox submissions
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: koBoToolboxApi
  required: true
params:
- id: formId
  name: Form Name or ID
  type: options
  default: ''
  required: true
  description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
    an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Form Name or ID
    name: formId
    typeOptions:
      loadOptionsMethod: loadForms
    possibleValues: []
- id: triggerOn
  name: Trigger On
  type: options
  default: formSubmission
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Trigger On
    name: triggerOn
    possibleValues:
    - value: formSubmission
      name: On Form Submission
      description: ''
- id: formatOptions
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to download submitted attachments
  placeholder: Add option
  validation:
    displayOptions:
      show:
        download:
        - true
  typeInfo:
    type: collection
    displayName: Options
    name: formatOptions
    subProperties:
    - displayName: Download Attachments
      name: download
      type: boolean
      description: Whether to download submitted attachments
      default: false
    - displayName: Attachments Naming Scheme
      name: binaryNamingScheme
      type: options
      value: sequence
      default: sequence
      options:
      - name: Sequence (e.g. attachment_N)
        value: sequence
        displayName: Sequence (e.g. attachment N)
      - name: Use Original Form Question ID
        value: question
        displayName: Use Original Form Question Id
      displayOptions:
        show:
          download:
          - true
    - displayName: Attachments Prefix
      name: dataPropertyAttachmentsPrefixName
      type: string
      description: Prefix for name of the binary property to which to write the attachments.
        An index starting with 0 will be added. So if name is "attachment_" the first
        attachment is saved to "attachment_0"
      default: attachment_
      displayOptions:
        show:
          download:
          - true
          binaryNamingScheme:
          - sequence
    - displayName: File Size
      name: version
      type: options
      description: Attachment size to retrieve, if multiple versions are available
      value: download_url
      default: download_url
      options:
      - name: Original
        value: download_url
        displayName: Original
      - name: Small
        value: download_small_url
        displayName: Small
      - name: Medium
        value: download_medium_url
        displayName: Medium
      - name: Large
        value: download_large_url
        displayName: Large
      displayOptions:
        show:
          download:
          - true
    - displayName: Multiselect Mask
      name: selectMask
      type: string
      description: Comma-separated list of wildcard-style selectors for fields that
        should be treated as multiselect fields, i.e. parsed as arrays.
      default: select_*
    - displayName: Number Mask
      name: numberMask
      type: string
      description: Comma-separated list of wildcard-style selectors for fields that
        should be treated as numbers
      default: n_*, f_*
    - displayName: Reformat
      name: reformat
      type: boolean
      description: Whether to apply some reformatting to the submission data, such
        as parsing GeoJSON coordinates
      default: false
api_patterns:
  http_methods:
  - GET
  endpoints:
  - /api/v2/assets/
  headers: []
  query_params:
  - name
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: formatOptions
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
  "$id": "https://n8n.io/schemas/nodes/koBoToolboxTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "KoBoToolbox Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "formId": {
          "description": "Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "triggerOn": {
          "description": "",
          "type": "string",
          "enum": [
            "formSubmission"
          ],
          "default": "formSubmission"
        },
        "formatOptions": {
          "description": "Whether to download submitted attachments",
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
  },
  "credentials": [
    {
      "name": "koBoToolboxApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
