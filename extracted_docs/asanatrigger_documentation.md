---
title: "Node: Asana Trigger"
slug: "node-asanatrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Asana events occur."
node_type: "trigger"
group: "['trigger']"
---

# Node: Asana Trigger

**Purpose.** Starts the workflow when Asana events occur.


---

## Node Details

- **Icon:** `file:asana.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **asanaApi**: N/A
- **asanaOAuth2Api**: N/A


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
| `asanaApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `asanaOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | string |  | ✓ | The resource ID to subscribe to. The resource can be a task or project. |  |
---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | accessToken | ✗ |  |  |

**Authentication options:**

* **Access Token** (`accessToken`)
* **OAuth2** (`oAuth2`)

| Resource | `resource` | string |  | ✓ | The resource ID to subscribe to. The resource can be a task or project. |  |
| Workspace Name or ID | `workspace` | options |  | ✗ | The workspace ID the resource is registered under. This is only required if you want to allow overriding existing webhooks. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

---

## Load Options Methods

- `getWorkspaces`
- `name`
- `value`

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: asanaTrigger
displayName: Asana Trigger
description: Starts the workflow when Asana events occur.
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: asanaApi
  required: true
- name: asanaOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: accessToken
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: accessToken
      name: Access Token
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
- id: resource
  name: Resource
  type: string
  default: ''
  required: true
  description: The resource ID to subscribe to. The resource can be a task or project.
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Resource
    name: resource
- id: workspace
  name: Workspace Name or ID
  type: options
  default: ''
  required: false
  description: The workspace ID the resource is registered under. This is only required
    if you want to allow overriding existing webhooks. Choose from the list, or specify
    an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  typeInfo:
    type: options
    displayName: Workspace Name or ID
    name: workspace
    typeOptions:
      loadOptionsMethod: getWorkspaces
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
  "$id": "https://n8n.io/schemas/nodes/asanaTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Asana Trigger Node",
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
            "accessToken",
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "resource": {
          "description": "The resource ID to subscribe to. The resource can be a task or project.",
          "type": "string",
          "default": ""
        },
        "workspace": {
          "description": "The workspace ID the resource is registered under. This is only required if you want to allow overriding existing webhooks. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
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
      "name": "asanaApi",
      "required": true
    },
    {
      "name": "asanaOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
