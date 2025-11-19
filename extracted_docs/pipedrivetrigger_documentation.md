---
title: "Node: Pipedrive Trigger"
slug: "node-pipedrivetrigger"
version: "['1', '1.1']"
updated: "2025-11-13"
summary: "Starts the workflow when Pipedrive events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Pipedrive Trigger

**Purpose.** Starts the workflow when Pipedrive events occur


---

## Node Details

- **Icon:** `file:pipedrive.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **pipedriveApi**: N/A
- **pipedriveOAuth2Api**: N/A
- **httpBasicAuth**: N/A


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
| `pipedriveApi` | ✓ | {'show': {'authentication': ['apiToken']}} |
| `pipedriveOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |
| `httpBasicAuth` | ✓ | {'show': {'incomingAuthentication': ['basicAuth']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | apiToken | ✗ |  |  |

**Authentication options:**

* **API Token** (`apiToken`)
* **OAuth2** (`oAuth2`)

| Incoming Authentication | `incomingAuthentication` | options | none | ✗ | If authentication should be activated for the webhook (makes it more secure) |  |

**Incoming Authentication options:**

* **Basic Auth** (`basicAuth`)
* **None** (`none`)

| Action | `action` | options | * | ✗ | Data got added |  |

**Action options:**

* **Added** (`added`) - Data got added
* **All** (`*`) - Any change
* **Deleted** (`deleted`) - Data got deleted
* **Merged** (`merged`) - Data got merged
* **Updated** (`updated`) - Data got updated

| Entity | `entity` | options | * | ✗ | Type of object to receive notifications about |  |
| Object | `object` | options | * | ✗ | Type of object to receive notifications about |  |

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
* Categories: Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: pipedriveTrigger
displayName: Pipedrive Trigger
description: Starts the workflow when Pipedrive events occur
version:
- '1'
- '1.1'
nodeType: trigger
group:
- trigger
credentials:
- name: pipedriveApi
  required: true
- name: pipedriveOAuth2Api
  required: true
- name: httpBasicAuth
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: apiToken
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: apiToken
      name: API Token
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
- id: incomingAuthentication
  name: Incoming Authentication
  type: options
  default: none
  required: false
  description: If authentication should be activated for the webhook (makes it more
    secure)
  typeInfo:
    type: options
    displayName: Incoming Authentication
    name: incomingAuthentication
    possibleValues:
    - value: basicAuth
      name: Basic Auth
      description: ''
    - value: none
      name: None
      description: ''
- id: action
  name: Action
  type: options
  default: '*'
  required: false
  description: Data got added
  validation:
    displayOptions:
      hide: {}
  typeInfo:
    type: options
    displayName: Action
    name: action
    possibleValues:
    - value: added
      name: Added
      description: Data got added
    - value: '*'
      name: All
      description: Any change
    - value: deleted
      name: Deleted
      description: Data got deleted
    - value: merged
      name: Merged
      description: Data got merged
    - value: updated
      name: Updated
      description: Data got updated
- id: entity
  name: Entity
  type: options
  default: '*'
  required: false
  description: Type of object to receive notifications about
  validation:
    displayOptions:
      hide: {}
  typeInfo:
    type: options
    displayName: Entity
    name: entity
    possibleValues: []
- id: object
  name: Object
  type: options
  default: '*'
  required: false
  description: Type of object to receive notifications about
  validation:
    displayOptions:
      hide: {}
  typeInfo:
    type: options
    displayName: Object
    name: object
    possibleValues: []
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders: []
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
  "$id": "https://n8n.io/schemas/nodes/pipedriveTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Pipedrive Trigger Node",
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
            "apiToken",
            "oAuth2"
          ],
          "default": "apiToken"
        },
        "incomingAuthentication": {
          "description": "If authentication should be activated for the webhook (makes it more secure)",
          "type": "string",
          "enum": [
            "basicAuth",
            "none"
          ],
          "default": "none"
        },
        "action": {
          "description": "Data got added",
          "type": "string",
          "enum": [
            "added",
            "*",
            "deleted",
            "merged",
            "updated"
          ],
          "default": "*"
        },
        "entity": {
          "description": "Type of object to receive notifications about",
          "type": "string",
          "default": "*"
        },
        "object": {
          "description": "Type of object to receive notifications about",
          "type": "string",
          "default": "*"
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
    "version": [
      "1",
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "pipedriveApi",
      "required": true
    },
    {
      "name": "pipedriveOAuth2Api",
      "required": true
    },
    {
      "name": "httpBasicAuth",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
