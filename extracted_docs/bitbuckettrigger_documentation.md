---
title: "Node: Bitbucket Trigger"
slug: "node-bitbuckettrigger"
version: "['1', '1.1']"
updated: "2025-11-13"
summary: "Handle Bitbucket events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Bitbucket Trigger

**Purpose.** Handle Bitbucket events via webhooks


---

## Node Details

- **Icon:** `file:bitbucket.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **bitbucketApi**: N/A
- **bitbucketAccessTokenApi**: N/A


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
| `bitbucketApi` | ✓ | {'show': {'authentication': ['password']}} |
| `bitbucketAccessTokenApi` | ✓ | {'show': {'authentication': ['accessToken']}} |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | workspace | ✓ | Resource to operate on |  |

**Resource options:**

* **Repository** (`repository`)
* **Workspace** (`workspace`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | password | ✗ |  |  |

**Authentication options:**

* **Password (Deprecated)** (`password`)
* **Access Token** (`accessToken`)

| Resource | `resource` | options | workspace | ✓ |  |  |

**Resource options:**

* **Repository** (`repository`)
* **Workspace** (`workspace`)

| Workspace Name or ID | `workspace` | options |  | ✓ | The repository of which to listen to the events. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Event Names or IDs | `events` | multiOptions | [] | ✓ | The events to listen to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Repository Name or ID | `repository` | options |  | ✓ | The repository of which to listen to the events. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Event Names or IDs | `events` | multiOptions | [] | ✓ | The events to listen to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

---

## Load Options Methods

- `getWorkspaceEvents`
- `for`
- `name`
- `value`
- `description`

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
* Categories: Development, Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: bitbucketTrigger
displayName: Bitbucket Trigger
description: Handle Bitbucket events via webhooks
version:
- '1'
- '1.1'
nodeType: trigger
group:
- trigger
credentials:
- name: bitbucketApi
  required: true
- name: bitbucketAccessTokenApi
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: password
  required: false
  description: ''
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: password
      name: Password (Deprecated)
      description: ''
    - value: accessToken
      name: Access Token
      description: ''
- id: resource
  name: Resource
  type: options
  default: workspace
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: repository
      name: Repository
      description: ''
    - value: workspace
      name: Workspace
      description: ''
- id: workspace
  name: Workspace Name or ID
  type: options
  default: ''
  required: true
  description: The repository of which to listen to the events. Choose from the list,
    or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - workspace
        - repository
  typeInfo:
    type: options
    displayName: Workspace Name or ID
    name: workspace
    typeOptions:
      loadOptionsMethod: getWorkspaces
    possibleValues: []
- id: events
  name: Event Names or IDs
  type: multiOptions
  default: []
  required: true
  description: The events to listen to. Choose from the list, or specify IDs using
    an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation: &id001
    required: true
    displayOptions:
      show:
        resource:
        - repository
  typeInfo: &id002
    type: multiOptions
    displayName: Event Names or IDs
    name: events
    typeOptions:
      loadOptionsMethod: getRepositoriesEvents
    possibleValues: []
- id: repository
  name: Repository Name or ID
  type: options
  default: ''
  required: true
  description: The repository of which to listen to the events. Choose from the list,
    or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - repository
  typeInfo:
    type: options
    displayName: Repository Name or ID
    name: repository
    typeOptions:
      loadOptionsMethod: getRepositories
    possibleValues: []
- id: events
  name: Event Names or IDs
  type: multiOptions
  default: []
  required: true
  description: The events to listen to. Choose from the list, or specify IDs using
    an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation: *id001
  typeInfo: *id002
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
  "$id": "https://n8n.io/schemas/nodes/bitbucketTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Bitbucket Trigger Node",
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
            "password",
            "accessToken"
          ],
          "default": "password"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "repository",
            "workspace"
          ],
          "default": "workspace"
        },
        "workspace": {
          "description": "The repository of which to listen to the events. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "events": {
          "description": "The events to listen to. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "repository": {
          "description": "The repository of which to listen to the events. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
    "version": [
      "1",
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "bitbucketApi",
      "required": true
    },
    {
      "name": "bitbucketAccessTokenApi",
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
