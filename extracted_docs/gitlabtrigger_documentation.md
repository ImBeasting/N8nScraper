---
title: "Node: GitLab Trigger"
slug: "node-gitlabtrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when GitLab events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: GitLab Trigger

**Purpose.** Starts the workflow when GitLab events occur
**Subtitle.** ={{$parameter["owner"] + "/" + $parameter["repository"] + ": " + $parameter["events"].join(", ")}}


---

## Node Details

- **Icon:** `file:gitlab.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **gitlabApi**: N/A
- **gitlabOAuth2Api**: N/A


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
| `gitlabApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `gitlabOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | accessToken | ✗ |  |  |

**Authentication options:**

* **Access Token** (`accessToken`)
* **OAuth2** (`oAuth2`)

| Repository Owner | `owner` | string |  | ✓ | Owner of the repository | e.g. n8n-io |  |
| Repository Name | `repository` | string |  | ✓ | The name of the repository | e.g. n8n |  |
| Events | `events` | multiOptions | [] | ✓ | Any time any event is triggered (Wildcard Event) |  |

**Events options:**

* ***** (`*`) - Any time any event is triggered (Wildcard Event)


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["owner"] + "/" + $parameter["repository"] + ": " + $parameter["events"].join(", ")}}`

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: gitlabTrigger
displayName: GitLab Trigger
description: Starts the workflow when GitLab events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: gitlabApi
  required: true
- name: gitlabOAuth2Api
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
- id: owner
  name: Repository Owner
  type: string
  default: ''
  required: true
  description: Owner of the repository
  placeholder: n8n-io
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Repository Owner
    name: owner
- id: repository
  name: Repository Name
  type: string
  default: ''
  required: true
  description: The name of the repository
  placeholder: n8n
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Repository Name
    name: repository
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: Any time any event is triggered (Wildcard Event)
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: '*'
      name: '*'
      description: Any time any event is triggered (Wildcard Event)
common_expressions:
- '={{$parameter["owner"] + "/" + $parameter["repository"] + ": " + $parameter["events"].join(",
  ")}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: owner
    text: n8n-io
  - field: repository
    text: n8n
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
  "$id": "https://n8n.io/schemas/nodes/gitlabTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GitLab Trigger Node",
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
        "owner": {
          "description": "Owner of the repository",
          "type": "string",
          "default": "",
          "examples": [
            "n8n-io"
          ]
        },
        "repository": {
          "description": "The name of the repository",
          "type": "string",
          "default": "",
          "examples": [
            "n8n"
          ]
        },
        "events": {
          "description": "Any time any event is triggered (Wildcard Event)",
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
      "name": "gitlabApi",
      "required": true
    },
    {
      "name": "gitlabOAuth2Api",
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
