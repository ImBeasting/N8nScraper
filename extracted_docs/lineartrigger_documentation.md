---
title: "Node: Linear Trigger"
slug: "node-lineartrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when Linear events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Linear Trigger

**Purpose.** Starts the workflow when Linear events occur
**Subtitle.** ={{$parameter["triggerOn"]}}


---

## Node Details

- **Icon:** `file:linear.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **linearApi**: N/A
- **linearOAuth2Api**: N/A


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

- **notice**: Make sure your credential has the "Admin" scope to create webhooks.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `linearApi` | ✓ | {'show': {'authentication': ['apiToken']}} |
| `linearOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**HTTP Methods:** POST

**Common Endpoints:**
- `https://api.linear.app/graphql`

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | apiToken | ✗ |  |  |

**Authentication options:**

* **API Token** (`apiToken`)
* **OAuth2** (`oAuth2`)

| Team Name or ID | `teamId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Listen to Resources | `resources` | multiOptions | [] | ✓ |  |  |

**Listen to Resources options:**

* **Comment Reaction** (`reaction`)
* **Cycle** (`cycle`)
* **Issue Attachment** (`attachment`)
* **Issue** (`issue`)
* **Issue Comment** (`comment`)
* **Issue Label** (`issueLabel`)
* **Project** (`project`)


---

## Load Options Methods

- `getTeams`
- `query`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["triggerOn"]}}`

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
node: linearTrigger
displayName: Linear Trigger
description: Starts the workflow when Linear events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: linearApi
  required: true
- name: linearOAuth2Api
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
- id: teamId
  name: Team Name or ID
  type: options
  default: ''
  required: false
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  typeInfo:
    type: options
    displayName: Team Name or ID
    name: teamId
    typeOptions:
      loadOptionsMethod: getTeams
    possibleValues: []
- id: resources
  name: Listen to Resources
  type: multiOptions
  default: []
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Listen to Resources
    name: resources
    possibleValues:
    - value: reaction
      name: Comment Reaction
      description: ''
    - value: cycle
      name: Cycle
      description: ''
    - value: attachment
      name: Issue Attachment
      description: ''
    - value: issue
      name: Issue
      description: ''
    - value: comment
      name: Issue Comment
      description: ''
    - value: issueLabel
      name: Issue Label
      description: ''
    - value: project
      name: Project
      description: ''
common_expressions:
- ={{$parameter["triggerOn"]}}
api_patterns:
  http_methods:
  - POST
  endpoints:
  - https://api.linear.app/graphql
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices:
  - name: notice
    text: Make sure your credential has the "Admin" scope to create webhooks.
    conditions: null
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
  "$id": "https://n8n.io/schemas/nodes/linearTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Linear Trigger Node",
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
        "teamId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "resources": {
          "description": "",
          "type": "string",
          "default": []
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
      "name": "linearApi",
      "required": true
    },
    {
      "name": "linearOAuth2Api",
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
