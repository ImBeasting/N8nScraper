---
title: "Node: n8n Form Trigger"
slug: "node-useworkflowtimezone"
version: "['2', '2.1', '2.2', '2.3', '2.4', '2.5']"
updated: "2026-01-08"
summary: "Generate webforms in n8n and pass their responses to the workflow"
node_type: "trigger"
group: "['trigger']"
---

# Node: n8n Form Trigger

**Purpose.** Generate webforms in n8n and pass their responses to the workflow


---

## Node Details

- **Icon:** `file:form.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **httpBasicAuth**: N/A


---

## Trigger Properties

- **Event Trigger Description:** Waiting for you to submit the form
- **Activation Message:** You can now make calls to your production Form URL.
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **formNotice** when responseMode=['responseNode']: In the 'Respond to Webhook' node, select 'Respond With JSON' and set the <strong>formSubmittedText</strong> key to display a custom response in the form, or the <strong>redirectURL</strong> key to redirect users to a URL

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `httpBasicAuth` | ✓ | {'show': {}} |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `Basic Auth` | options | none | ✗ |  |  |

**Authentication options:**

* **Basic Auth** (`basicAuth`)
* **None** (`none`)

| Options | `options` | collection | {} | ✗ | The label of the submit button in the form | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Button Label | `buttonLabel` | string | Submit | The label of the submit button in the form |
| Ignore Bots | `ignoreBots` | boolean | False | Whether to ignore requests from bots like link previewers and web crawlers |
| Custom Form Styling | `customCss` | string |  | Override default styling of the public form interface with CSS |

</details>

| Form Path | `path` | string |  | ✓ | The final segment of the form's URL, both for test and production | e.g. webhook |  |
| Form Title | `formTitle` | string |  | ✓ | Shown at the top of the form | e.g. e.g. Contact us |  |
| Form Description | `formDescription` | string |  | ✗ | Shown underneath the Form Title. Can be used to prompt the user on how to complete the form. Accepts HTML. | e.g. e.g. We'll get back to you soon |  |
| Form Elements | `formFields` | fixedCollection | {} | ✗ | e.g. Add Form Element |  |
| Respond When | `responseMode` | options | onReceived | ✗ | As soon as this node receives the form submission |  |

**Respond When options:**

* **Form Is Submitted** (`onReceived`) - As soon as this node receives the form submission
* **Workflow Finishes** (`lastNode`) - When the last node of the workflow is executed
* **Using 'Respond to Webhook' Node** (`responseNode`) - When the 'Respond to Webhook' node is executed

| Form Response | `respondWithOptions` | fixedCollection | text | ✗ | Show a response text to the user | e.g. Add option |  |

<details>
<summary><strong>Form Response sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Values | `values` |  |  |  |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $parameter["path"] || $parameter["options"]?.path || $webhookId }}`
- `={{$parameter["responseMode"] === "lastNode" ? "noData" : undefined}}`
- `={{$parameter["responseMode"]}}`

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: useWorkflowTimezone
displayName: n8n Form Trigger
description: Generate webforms in n8n and pass their responses to the workflow
version:
- '2'
- '2.1'
- '2.2'
- '2.3'
- '2.4'
- '2.5'
nodeType: trigger
group:
- trigger
credentials:
- name: httpBasicAuth
  required: true
params:
- id: Basic Auth
  name: Authentication
  type: options
  default: none
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: Basic Auth
    possibleValues:
    - value: basicAuth
      name: Basic Auth
      description: ''
    - value: none
      name: None
      description: ''
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: The label of the submit button in the form
  placeholder: Add option
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Options
    name: options
    typeOptions:
      rows: 10
    subProperties:
    - displayName: Button Label
      name: buttonLabel
      type: string
      description: The label of the submit button in the form
      default: Submit
    - displayName: Ignore Bots
      name: ignoreBots
      type: boolean
      description: Whether to ignore requests from bots like link previewers and web
        crawlers
      default: false
    - displayName: Custom Form Styling
      name: customCss
      type: string
      description: Override default styling of the public form interface with CSS
      typeOptions:
        rows: 10
      displayOptions:
        show: {}
- id: path
  name: Form Path
  type: string
  default: ''
  required: true
  description: The final segment of the form's URL, both for test and production
  placeholder: webhook
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Form Path
    name: path
- id: formTitle
  name: Form Title
  type: string
  default: ''
  required: true
  description: Shown at the top of the form
  placeholder: e.g. Contact us
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Form Title
    name: formTitle
- id: formDescription
  name: Form Description
  type: string
  default: ''
  required: false
  description: Shown underneath the Form Title. Can be used to prompt the user on
    how to complete the form. Accepts HTML.
  placeholder: e.g. We'll get back to you soon
  typeInfo:
    type: string
    displayName: Form Description
    name: formDescription
    typeOptions:
      rows: 2
- id: formFields
  name: Form Elements
  type: fixedCollection
  default: {}
  required: false
  description: ''
  placeholder: Add Form Element
  typeInfo:
    type: fixedCollection
    displayName: Form Elements
    name: formFields
    typeOptions:
      multipleValues: true
    subProperties: []
- id: responseMode
  name: Respond When
  type: options
  default: onReceived
  required: false
  description: As soon as this node receives the form submission
  typeInfo:
    type: options
    displayName: Respond When
    name: responseMode
    possibleValues:
    - value: onReceived
      name: Form Is Submitted
      description: As soon as this node receives the form submission
    - value: lastNode
      name: Workflow Finishes
      description: When the last node of the workflow is executed
    - value: responseNode
      name: Using 'Respond to Webhook' Node
      description: When the 'Respond to Webhook' node is executed
- id: respondWithOptions
  name: Form Response
  type: fixedCollection
  default: text
  required: false
  description: Show a response text to the user
  placeholder: Add option
  validation:
    displayOptions:
      show:
        respondWith:
        - text
  typeInfo:
    type: fixedCollection
    displayName: Form Response
    name: respondWithOptions
    subProperties:
    - name: values
      displayName: Values
      values:
      - displayName: Respond With
        name: respondWith
        type: options
        description: Show a response text to the user
        value: text
        default: text
        options:
        - name: Form Submitted Text
          description: Show a response text to the user
          value: text
          displayName: Form Submitted Text
        - name: Redirect URL
          description: Redirect the user to a URL
          value: redirect
          displayName: Redirect Url
      - displayName: Text to Show
        name: formSubmittedText
        type: string
        description: The text displayed to users after they fill the form. Leave it
          empty if don't want to show any additional text.
        default: Your response has been recorded
        displayOptions:
          show:
            respondWith:
            - text
      - displayName: URL to Redirect to
        name: redirectUrl
        type: string
        description: The URL to redirect users to after they fill the form. Must be
          a valid URL.
        placeholder: e.g. http://www.n8n.io
        validateType: url
        default: ''
        displayOptions:
          show:
            respondWith:
            - redirect
common_expressions:
- ={{ $parameter["path"] || $parameter["options"]?.path || $webhookId }}
- '={{$parameter["responseMode"] === "lastNode" ? "noData" : undefined}}'
- ={{$parameter["responseMode"]}}
ui_elements:
  notices:
  - name: formNotice
    text: In the 'Respond to Webhook' node, select 'Respond With JSON' and set the
      <strong>formSubmittedText</strong> key to display a custom response in the form,
      or the <strong>redirectURL</strong> key to redirect users to a URL
    conditions:
      show:
        responseMode:
        - responseNode
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: path
    text: webhook
  - field: formTitle
    text: e.g. Contact us
  - field: formDescription
    text: e.g. We'll get back to you soon
  - field: formFields
    text: Add Form Element
  - field: respondWithOptions
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
  "$id": "https://n8n.io/schemas/nodes/useWorkflowTimezone.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "n8n Form Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "Basic Auth": {
          "description": "",
          "type": "string",
          "enum": [
            "basicAuth",
            "none"
          ],
          "default": "none"
        },
        "options": {
          "description": "The label of the submit button in the form",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "path": {
          "description": "The final segment of the form's URL, both for test and production",
          "type": "string",
          "default": "",
          "examples": [
            "webhook"
          ]
        },
        "formTitle": {
          "description": "Shown at the top of the form",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Contact us"
          ]
        },
        "formDescription": {
          "description": "Shown underneath the Form Title. Can be used to prompt the user on how to complete the form. Accepts HTML.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. We'll get back to you soon"
          ]
        },
        "formFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Form Element"
          ]
        },
        "responseMode": {
          "description": "As soon as this node receives the form submission",
          "type": "string",
          "enum": [
            "onReceived",
            "lastNode",
            "responseNode"
          ],
          "default": "onReceived"
        },
        "respondWithOptions": {
          "description": "Show a response text to the user",
          "type": "string",
          "default": "text",
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
    "version": [
      "2",
      "2.1",
      "2.2",
      "2.3",
      "2.4",
      "2.5"
    ]
  },
  "credentials": [
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
| ['2', '2.1', '2.2', '2.3', '2.4', '2.5'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
