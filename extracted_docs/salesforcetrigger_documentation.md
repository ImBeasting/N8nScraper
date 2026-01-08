---
title: "Node: Salesforce Trigger"
slug: "node-salesforcetrigger"
version: "1"
updated: "2026-01-08"
summary: "Fetches data from Salesforce and starts the workflow on specified polling intervals."
node_type: "trigger"
group: "['trigger']"
---

# Node: Salesforce Trigger

**Purpose.** Fetches data from Salesforce and starts the workflow on specified polling intervals.
**Subtitle.** ={{($parameter["triggerOn"])}}


---

## Node Details

- **Icon:** `file:salesforce.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **salesforceOAuth2Api**: N/A


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
| `salesforceOAuth2Api` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Trigger On | `triggerOn` | options |  | ✗ | Which Salesforce event should trigger the node |  |

**Trigger On options:**

* **Account Created** (`accountCreated`) - When a new account is created
* **Account Updated** (`accountUpdated`) - When an existing account is modified
* **Attachment Created** (`attachmentCreated`) - When a file is uploaded and attached to an object
* **Attachment Updated** (`attachmentUpdated`) - When an existing file is modified
* **Case Created** (`caseCreated`) - When a new case is created
* **Case Updated** (`caseUpdated`) - When an existing case is modified
* **Contact Created** (`contactCreated`) - When a new contact is created
* **Contact Updated** (`contactUpdated`) - When an existing contact is modified
* **Custom Object Created** (`customObjectCreated`) - When a new object of a given type is created
* **Custom Object Updated** (`customObjectUpdated`) - When an object of a given type is modified
* **Lead Created** (`leadCreated`) - When a new lead is created
* **Lead Updated** (`leadUpdated`) - When an existing lead is modified
* **Opportunity Created** (`opportunityCreated`) - When a new opportunity is created
* **Opportunity Updated** (`opportunityUpdated`) - When an existing opportunity is modified
* **Task Created** (`taskCreated`) - When a new task is created
* **Task Updated** (`taskUpdated`) - When an existing task is modified
* **User Created** (`userCreated`) - When a new user is created
* **User Updated** (`userUpdated`) - When an existing user is modified

| Custom Object Name or ID | `customObject` | options |  | ✓ | Name of the custom object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

---

## Load Options Methods

- `getCustomObjects`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{($parameter["triggerOn"])}}`

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
* Categories: Sales, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: salesforceTrigger
displayName: Salesforce Trigger
description: Fetches data from Salesforce and starts the workflow on specified polling
  intervals.
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: salesforceOAuth2Api
  required: true
params:
- id: triggerOn
  name: Trigger On
  type: options
  default: ''
  required: false
  description: Which Salesforce event should trigger the node
  typeInfo:
    type: options
    displayName: Trigger On
    name: triggerOn
    possibleValues:
    - value: accountCreated
      name: Account Created
      description: When a new account is created
    - value: accountUpdated
      name: Account Updated
      description: When an existing account is modified
    - value: attachmentCreated
      name: Attachment Created
      description: When a file is uploaded and attached to an object
    - value: attachmentUpdated
      name: Attachment Updated
      description: When an existing file is modified
    - value: caseCreated
      name: Case Created
      description: When a new case is created
    - value: caseUpdated
      name: Case Updated
      description: When an existing case is modified
    - value: contactCreated
      name: Contact Created
      description: When a new contact is created
    - value: contactUpdated
      name: Contact Updated
      description: When an existing contact is modified
    - value: customObjectCreated
      name: Custom Object Created
      description: When a new object of a given type is created
    - value: customObjectUpdated
      name: Custom Object Updated
      description: When an object of a given type is modified
    - value: leadCreated
      name: Lead Created
      description: When a new lead is created
    - value: leadUpdated
      name: Lead Updated
      description: When an existing lead is modified
    - value: opportunityCreated
      name: Opportunity Created
      description: When a new opportunity is created
    - value: opportunityUpdated
      name: Opportunity Updated
      description: When an existing opportunity is modified
    - value: taskCreated
      name: Task Created
      description: When a new task is created
    - value: taskUpdated
      name: Task Updated
      description: When an existing task is modified
    - value: userCreated
      name: User Created
      description: When a new user is created
    - value: userUpdated
      name: User Updated
      description: When an existing user is modified
- id: customObject
  name: Custom Object Name or ID
  type: options
  default: ''
  required: true
  description: Name of the custom object. Choose from the list, or specify an ID using
    an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
  validation:
    required: true
    displayOptions:
      show:
        triggerOn:
        - customObjectUpdated
        - customObjectCreated
  typeInfo:
    type: options
    displayName: Custom Object Name or ID
    name: customObject
    typeOptions:
      loadOptionsMethod: getCustomObjects
    possibleValues: []
common_expressions:
- ={{($parameter["triggerOn"])}}
api_patterns:
  http_methods:
  - POST
  endpoints: []
  headers:
  - Content-Type
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
  "$id": "https://n8n.io/schemas/nodes/salesforceTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Salesforce Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "triggerOn": {
          "description": "Which Salesforce event should trigger the node",
          "type": "string",
          "enum": [
            "accountCreated",
            "accountUpdated",
            "attachmentCreated",
            "attachmentUpdated",
            "caseCreated",
            "caseUpdated",
            "contactCreated",
            "contactUpdated",
            "customObjectCreated",
            "customObjectUpdated",
            "leadCreated",
            "leadUpdated",
            "opportunityCreated",
            "opportunityUpdated",
            "taskCreated",
            "taskUpdated",
            "userCreated",
            "userUpdated"
          ],
          "default": ""
        },
        "customObject": {
          "description": "Name of the custom object. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
      "name": "salesforceOAuth2Api",
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
