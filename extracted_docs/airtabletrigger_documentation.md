---
title: "Node: Airtable Trigger"
slug: "node-airtabletrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when Airtable events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Airtable Trigger

**Purpose.** Starts the workflow when Airtable events occur
**Subtitle.** ={{$parameter["event"]}}


---

## Node Details

- **Icon:** `file:airtable.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **airtableApi**: N/A
- **airtableTokenApi**: N/A
- **airtableOAuth2Api**: N/A


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
| `airtableApi` | ✓ | {'show': {'authentication': ['airtableApi']}} |
| `airtableTokenApi` | ✓ | {'show': {'authentication': ['airtableTokenApi']}} |
| `airtableOAuth2Api` | ✓ | {'show': {'authentication': ['airtableOAuth2Api']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | airtableApi | ✗ |  |  |

**Authentication options:**

* **API Key** (`airtableApi`)
* **Access Token** (`airtableTokenApi`)
* **OAuth2** (`airtableOAuth2Api`)

| Base | `baseId` | resourceLocator |  | ✓ | The Airtable Base in which to operate on | e.g. https://airtable.com/app12DiScdfes/tblAAAAAAAAAAAAA/viwHdfasdfeieg5p |  |
| Table | `tableId` | resourceLocator |  | ✓ | e.g. https://airtable.com/app12DiScdfes/tblAAAAAAAAAAAAA/viwHdfasdfeieg5p |  |
| Trigger Field | `triggerField` | string |  | ✓ | A Created Time or Last Modified Time field that will be used to sort records. If you do not have a Created Time or Last Modified Time field in your schema, please create one, because without this field trigger will not work correctly. |  |
| Download Attachments | `downloadAttachments` | boolean | False | ✗ | Whether the attachment fields define in 'Download Fields' will be downloaded |  |
| Download Fields | `downloadFieldNames` | string |  | ✓ | Name of the fields of type 'attachment' that should be downloaded. Multiple ones can be defined separated by comma. Case sensitive. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Fields to be included in the response. Multiple ones can be set separated by comma. Example: <code>name, id</code>. By default just the trigger field will be included. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Fields to be included in the response. Multiple ones can be set separated by comma. Example: <code>name, id</code>. By default just the trigger field will be included. |
| Formula | `formula` | string |  | Formulas may involve functions, numeric operations, logical operations, and text operations that operate on fields. More info <a href="https://support.airtable.com/hc/en-us/articles/203255215-Formula-Field-Reference">here</a>. |
| View ID | `viewId` | string |  | The name or ID of a view in the table. If set, only the records in that view will be returned. |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["event"]}}`

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
* Categories: Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: airtableTrigger
displayName: Airtable Trigger
description: Starts the workflow when Airtable events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: airtableApi
  required: true
- name: airtableTokenApi
  required: true
- name: airtableOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: airtableApi
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: airtableApi
      name: API Key
      description: ''
    - value: airtableTokenApi
      name: Access Token
      description: ''
    - value: airtableOAuth2Api
      name: OAuth2
      description: ''
- id: baseId
  name: Base
  type: resourceLocator
  default: ''
  required: true
  description: The Airtable Base in which to operate on
  placeholder: https://airtable.com/app12DiScdfes/tblAAAAAAAAAAAAA/viwHdfasdfeieg5p
  validation:
    required: true
  typeInfo:
    type: resourceLocator
    displayName: Base
    name: baseId
- id: tableId
  name: Table
  type: resourceLocator
  default: ''
  required: true
  description: ''
  placeholder: https://airtable.com/app12DiScdfes/tblAAAAAAAAAAAAA/viwHdfasdfeieg5p
  validation:
    required: true
  typeInfo:
    type: resourceLocator
    displayName: Table
    name: tableId
- id: triggerField
  name: Trigger Field
  type: string
  default: ''
  required: true
  description: A Created Time or Last Modified Time field that will be used to sort
    records. If you do not have a Created Time or Last Modified Time field in your
    schema, please create one, because without this field trigger will not work correctly.
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Trigger Field
    name: triggerField
- id: downloadAttachments
  name: Download Attachments
  type: boolean
  default: false
  required: false
  description: Whether the attachment fields define in 'Download Fields' will be downloaded
  typeInfo:
    type: boolean
    displayName: Download Attachments
    name: downloadAttachments
- id: downloadFieldNames
  name: Download Fields
  type: string
  default: ''
  required: true
  description: Name of the fields of type 'attachment' that should be downloaded.
    Multiple ones can be defined separated by comma. Case sensitive.
  validation:
    required: true
    displayOptions:
      show:
        downloadAttachments:
        - true
  typeInfo:
    type: string
    displayName: Download Fields
    name: downloadFieldNames
- id: additionalFields
  name: Additional Fields
  type: collection
  default: {}
  required: false
  description: 'Fields to be included in the response. Multiple ones can be set separated
    by comma. Example: <code>name, id</code>. By default just the trigger field will
    be included.'
  placeholder: Add Field
  typeInfo:
    type: collection
    displayName: Additional Fields
    name: additionalFields
    subProperties:
    - displayName: Fields
      name: fields
      type: string
      description: 'Fields to be included in the response. Multiple ones can be set
        separated by comma. Example: <code>name, id</code>. By default just the trigger
        field will be included.'
      default: ''
    - displayName: Formula
      name: formula
      type: string
      description: Formulas may involve functions, numeric operations, logical operations,
        and text operations that operate on fields. More info <a href="https://support.airtable.com/hc/en-us/articles/203255215-Formula-Field-Reference">here</a>.
      default: ''
    - displayName: View ID
      name: viewId
      type: string
      description: The name or ID of a view in the table. If set, only the records
        in that view will be returned.
      default: ''
common_expressions:
- ={{$parameter["event"]}}
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: baseId
    text: https://airtable.com/app12DiScdfes/tblAAAAAAAAAAAAA/viwHdfasdfeieg5p
  - field: tableId
    text: https://airtable.com/app12DiScdfes/tblAAAAAAAAAAAAA/viwHdfasdfeieg5p
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/airtableTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Airtable Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "airtableApi",
            "airtableTokenApi",
            "airtableOAuth2Api"
          ],
          "default": "airtableApi"
        },
        "baseId": {
          "description": "The Airtable Base in which to operate on",
          "type": "string",
          "examples": [
            "https://airtable.com/app12DiScdfes/tblAAAAAAAAAAAAA/viwHdfasdfeieg5p"
          ]
        },
        "tableId": {
          "description": "",
          "type": "string",
          "examples": [
            "https://airtable.com/app12DiScdfes/tblAAAAAAAAAAAAA/viwHdfasdfeieg5p"
          ]
        },
        "triggerField": {
          "description": "A Created Time or Last Modified Time field that will be used to sort records. If you do not have a Created Time or Last Modified Time field in your schema, please create one, because without this field trigger will not work correctly.",
          "type": "string",
          "default": ""
        },
        "downloadAttachments": {
          "description": "Whether the attachment fields define in 'Download Fields' will be downloaded",
          "type": "boolean",
          "default": false
        },
        "downloadFieldNames": {
          "description": "Name of the fields of type 'attachment' that should be downloaded. Multiple ones can be defined separated by comma. Case sensitive.",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Fields to be included in the response. Multiple ones can be set separated by comma. Example: <code>name, id</code>. By default just the trigger field will be included.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
      "name": "airtableApi",
      "required": true
    },
    {
      "name": "airtableTokenApi",
      "required": true
    },
    {
      "name": "airtableOAuth2Api",
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
