---
title: "Node: Facebook Trigger"
slug: "node-facebooktrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when Facebook events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Facebook Trigger

**Purpose.** Starts the workflow when Facebook events occur
**Subtitle.** ={{$parameter["appId"] +"/"+ $parameter["object"]}}


---

## Node Details

- **Icon:** `file:facebook.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **facebookGraphAppApi**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **whatsappBusinessAccountNotice** when object=['whatsappBusinessAccount']: To watch Whatsapp business account events use the Whatsapp trigger node

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `facebookGraphAppApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| APP ID | `appId` | string |  | ✓ | Facebook APP ID |  |
| Object | `object` | options | user | ✓ | Get updates about Ad Account |  |

**Object options:**

* **Ad Account** (`adAccount`) - Get updates about Ad Account
* **Application** (`application`) - Get updates about the app
* **Certificate Transparency** (`certificateTransparency`) - Get updates about Certificate Transparency
* **Group** (`group`) - Get updates about activity in groups and events in groups for Workplace
* **Instagram** (`instagram`) - Get updates about comments on your media
* **Link** (`link`) - Get updates about links for rich previews by an external provider
* **Page** (`page`) - Page updates
* **Permissions** (`permissions`) - Updates regarding granting or revoking permissions
* **User** (`user`) - User profile updates
* **Whatsapp Business Account** (`whatsappBusinessAccount`) - Get updates about Whatsapp business account
* **Workplace Security** (`workplaceSecurity`) - Get updates about Workplace Security

| Field Names or IDs | `fields` | multiOptions | [] | ✗ | The set of fields in this object that are subscribed to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Options | `options` | collection | {} | ✗ | Whether change notifications should include the new values | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Values | `includeValues` | boolean | True | Whether change notifications should include the new values |

</details>


---

## Load Options Methods

- `getObjectFields`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["appId"] +"/"+ $parameter["object"]}}`

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
* Categories: Marketing
* Aliases: FB

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: facebookTrigger
displayName: Facebook Trigger
description: Starts the workflow when Facebook events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: facebookGraphAppApi
  required: true
params:
- id: appId
  name: APP ID
  type: string
  default: ''
  required: true
  description: Facebook APP ID
  validation:
    required: true
  typeInfo:
    type: string
    displayName: APP ID
    name: appId
- id: object
  name: Object
  type: options
  default: user
  required: true
  description: Get updates about Ad Account
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Object
    name: object
    possibleValues:
    - value: adAccount
      name: Ad Account
      description: Get updates about Ad Account
    - value: application
      name: Application
      description: Get updates about the app
    - value: certificateTransparency
      name: Certificate Transparency
      description: Get updates about Certificate Transparency
    - value: group
      name: Group
      description: Get updates about activity in groups and events in groups for Workplace
    - value: instagram
      name: Instagram
      description: Get updates about comments on your media
    - value: link
      name: Link
      description: Get updates about links for rich previews by an external provider
    - value: page
      name: Page
      description: Page updates
    - value: permissions
      name: Permissions
      description: Updates regarding granting or revoking permissions
    - value: user
      name: User
      description: User profile updates
    - value: whatsappBusinessAccount
      name: Whatsapp Business Account
      description: Get updates about Whatsapp business account
    - value: workplaceSecurity
      name: Workplace Security
      description: Get updates about Workplace Security
- id: fields
  name: Field Names or IDs
  type: multiOptions
  default: []
  required: false
  description: The set of fields in this object that are subscribed to. Choose from
    the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  typeInfo:
    type: multiOptions
    displayName: Field Names or IDs
    name: fields
    typeOptions:
      loadOptionsMethod: getObjectFields
    possibleValues: []
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether change notifications should include the new values
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Include Values
      name: includeValues
      type: boolean
      description: Whether change notifications should include the new values
      default: true
common_expressions:
- ={{$parameter["appId"] +"/"+ $parameter["object"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: whatsappBusinessAccountNotice
    text: To watch Whatsapp business account events use the Whatsapp trigger node
    conditions:
      show:
        object:
        - whatsappBusinessAccount
  tooltips: []
  placeholders:
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
  "$id": "https://n8n.io/schemas/nodes/facebookTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Facebook Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "appId": {
          "description": "Facebook APP ID",
          "type": "string",
          "default": ""
        },
        "object": {
          "description": "Get updates about Ad Account",
          "type": "string",
          "enum": [
            "adAccount",
            "application",
            "certificateTransparency",
            "group",
            "instagram",
            "link",
            "page",
            "permissions",
            "user",
            "whatsappBusinessAccount",
            "workplaceSecurity"
          ],
          "default": "user"
        },
        "fields": {
          "description": "The set of fields in this object that are subscribed to. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "options": {
          "description": "Whether change notifications should include the new values",
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
      "name": "facebookGraphAppApi",
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
