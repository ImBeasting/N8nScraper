---
title: "Node: n8n Form"
slug: "node-form"
version: "['1', '2.3']"
updated: "2025-11-13"
summary: "Generate webforms in n8n and pass their responses to the workflow"
node_type: "regular"
group: "['input']"
---

# Node: n8n Form

**Purpose.** Generate webforms in n8n and pass their responses to the workflow


---

## Node Details

- **Icon:** `file:form.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Define Form | `defineForm` | options | fields | ✗ |  |  |

**Define Form options:**

* **Using Fields Below** (`fields`)
* **Using JSON** (`json`)

| Form Fields | `jsonOutput` | json | [\n  {\n     | ✗ | e.g. <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.form/" target="_blank">See docs</a> for field syntax |  |
| Form Elements | `formFields` | fixedCollection | {} | ✓ | Label that appears above the input field | e.g. Add Form Element |  |

<details>
<summary><strong>Form Elements sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Values | `values` |  |  |  |

</details>

| Limit Type | `limitType` | options | afterTimeInterval | ✗ | Sets the condition for the execution to resume. Can be a specified date or after some time. |  |

**Limit Type options:**

* **After Time Interval** (`afterTimeInterval`) - Waits for a certain amount of time
* **At Specified Time** (`atSpecifiedTime`) - Waits until the set date and time to continue

| Amount | `resumeAmount` | number | 1 | ✗ | The time to wait | min:0, max:∞ |
| Unit | `resumeUnit` | options | hours | ✗ | Unit of the interval value |  |

**Unit options:**

* **Minutes** (`minutes`)
* **Hours** (`hours`)
* **Days** (`days`)

| Max Date and Time | `maxDateAndTime` | dateTime |  | ✗ | Continue execution after the specified date and time |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `{{ $input.all() }}`
- `{{ $execution.resumeFormUrl }}`

---

## Execution Settings

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |
| Always Output Data | `alwaysOutputData` | boolean | False | If active, will output a single, empty item when the output would have been empty. Use to prevent the workflow finishing on this node |
| Execute Once | `executeOnce` | boolean | False | If active, the node executes only once, with data from the first item it receives |
| Retry On Fail | `retryOnFail` | boolean | False | If active, the node tries to execute again when it fails |
| Max. Tries | `maxTries` | number | 3 | Number of times to attempt to execute the node before failing the execution *(Only visible when 'Retry On Fail' is enabled)* (min: 2, max: 5) |
| Wait Between Tries (ms) | `waitBetweenTries` | number | 1000 | How long to wait between each attempt (in milliseconds) *(Only visible when 'Retry On Fail' is enabled)* (min: 0, max: 5000) |
| On Error | `onError` | options | stopWorkflow | Action to take when the node execution fails |

**On Error Options:**

* **Stop Workflow** (`stopWorkflow`) — Halt execution and fail workflow
* **Continue** (`continueRegularOutput`) — Pass error message as item in regular output
* **Continue (using error output)** (`continueErrorOutput`) — Pass item to an extra `error` output

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Core Nodes
* Aliases: _Form, form, table, submit, post, page, step, stage, multi

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: form
displayName: n8n Form
description: Generate webforms in n8n and pass their responses to the workflow
version:
- '1'
- '2.3'
nodeType: regular
group:
- input
params:
- id: defineForm
  name: Define Form
  type: options
  default: fields
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Define Form
    name: defineForm
    possibleValues:
    - value: fields
      name: Using Fields Below
      description: ''
    - value: json
      name: Using JSON
      description: ''
- id: jsonOutput
  name: Form Fields
  type: json
  default: '[\n  {\n    '
  required: false
  description: ''
  hint: <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.form/"
    target="_blank">See docs</a> for field syntax
  validation:
    displayOptions:
      show:
        defineForm:
        - json
  typeInfo:
    type: json
    displayName: Form Fields
    name: jsonOutput
    typeOptions:
      rows: 5
- id: formFields
  name: Form Elements
  type: fixedCollection
  default: {}
  required: true
  description: Label that appears above the input field
  hint: Does not accept <code>&lt;script&gt;</code>, <code>&lt;style&gt;</code> or
    <code>&lt;input&gt;</code> tags
  placeholder: Add Form Element
  validation:
    required: true
    displayOptions:
      hide:
        fieldType:
        - hiddenField
        - html
  typeInfo:
    type: fixedCollection
    displayName: Form Elements
    name: formFields
    typeOptions:
      multipleValues: true
    subProperties:
    - name: values
      displayName: Values
      values:
      - displayName: Field Name
        name: fieldLabel
        type: string
        description: Label that appears above the input field
        placeholder: e.g. What is your name?
        default: ''
        required: true
        displayOptions:
          hide:
            fieldType:
            - hiddenField
            - html
      - displayName: Field Name
        name: fieldName
        type: string
        description: The name of the field, used in input attributes and referenced
          by the workflow
        default: ''
        displayOptions:
          show:
            fieldType:
            - hiddenField
      - displayName: Element Type
        name: fieldType
        type: options
        description: The type of field to add to the form
        value: checkbox
        default: text
        required: true
        options:
        - name: Checkboxes
          value: checkbox
          displayName: Checkboxes
        - name: Custom HTML
          value: html
          displayName: Custom Html
        - name: Date
          value: date
          displayName: Date
        - name: Dropdown
          value: dropdown
          displayName: Dropdown
        - name: Email
          value: email
          displayName: Email
        - name: File
          value: file
          displayName: File
        - name: Hidden Field
          value: hiddenField
          displayName: Hidden Field
        - name: Number
          value: number
          displayName: Number
        - name: Password
          value: password
          displayName: Password
        - name: Radio Buttons
          value: radio
          displayName: Radio Buttons
        - name: Text
          value: text
          displayName: Text
        - name: Textarea
          value: textarea
          displayName: Textarea
      - displayName: Element Name
        name: elementName
        type: string
        description: Optional field. It can be used to include the html in the output.
        placeholder: e.g. content-section
        default: ''
        displayOptions:
          show:
            fieldType:
            - html
      - displayName: Placeholder
        name: placeholder
        type: string
        description: Sample text to display inside the field
        default: ''
        displayOptions:
          hide:
            fieldType:
            - dropdown
            - date
            - file
            - html
            - hiddenField
            - radio
            - checkbox
      - displayName: Field Value
        name: fieldValue
        type: string
        description: Input value can be set here or will be passed as a query parameter
          via Field Name if no value is set
        default: ''
        displayOptions:
          show:
            fieldType:
            - hiddenField
      - displayName: Field Options
        name: fieldOptions
        type: fixedCollection
        description: List of options that can be selected from the dropdown
        placeholder: Add Field Option
        default: ''
        required: true
        options:
        - name: values
          displayName: Values
          values:
          - displayName: Option
            name: option
            type: string
            default: ''
        typeOptions:
          multipleValues: true
        displayOptions:
          show:
            fieldType:
            - dropdown
      - displayName: Checkboxes
        name: fieldOptions
        type: fixedCollection
        placeholder: Add Checkbox
        default: ''
        required: true
        options:
        - name: values
          displayName: Values
          values:
          - displayName: Checkbox Label
            name: option
            type: string
            default: ''
        typeOptions:
          multipleValues: true
        displayOptions:
          show:
            fieldType:
            - checkbox
      - displayName: Radio Buttons
        name: fieldOptions
        type: fixedCollection
        placeholder: Add Radio Button
        default: ''
        required: true
        options:
        - name: values
          displayName: Values
          values:
          - displayName: Radio Button Label
            name: option
            type: string
            default: ''
        typeOptions:
          multipleValues: true
        displayOptions:
          show:
            fieldType:
            - radio
      - displayName: Multiple Choice is a legacy option, please use Checkboxes or
          Radio Buttons field type instead
        name: multiselectLegacyNotice
        type: notice
        default: ''
        displayOptions:
          show:
            multiselect:
            - true
            fieldType:
            - dropdown
      - displayName: Multiple Choice
        name: multiselect
        type: boolean
        description: Whether to allow the user to select multiple options from the
          dropdown list
        default: false
        displayOptions:
          show:
            fieldType:
            - dropdown
      - displayName: Limit Selection
        name: limitSelection
        type: options
        value: exact
        default: unlimited
        options:
        - name: Exact Number
          value: exact
          displayName: Exact Number
        - name: Range
          value: range
          displayName: Range
        - name: Unlimited
          value: unlimited
          displayName: Unlimited
        displayOptions:
          show:
            fieldType:
            - checkbox
      - displayName: Number of Selections
        name: numberOfSelections
        type: number
        default: 1
        typeOptions:
          minValue: 1
          numberPrecision: 0
        displayOptions:
          show:
            fieldType:
            - checkbox
            limitSelection:
            - exact
      - displayName: Minimum Selections
        name: minSelections
        type: number
        default: 0
        typeOptions:
          minValue: 0
          numberPrecision: 0
        displayOptions:
          show:
            fieldType:
            - checkbox
            limitSelection:
            - range
      - displayName: Maximum Selections
        name: maxSelections
        type: number
        default: 1
        typeOptions:
          minValue: 1
          numberPrecision: 0
        displayOptions:
          show:
            fieldType:
            - checkbox
            limitSelection:
            - range
      - displayName: HTML
        name: html
        type: string
        description: HTML elements to display on the form page
        hint: Does not accept <code>&lt;script&gt;</code>, <code>&lt;style&gt;</code>
          or <code>&lt;input&gt;</code> tags
        noDataExpression: true
        typeOptions: {}
        displayOptions:
          show:
            fieldType:
            - html
      - displayName: Multiple Files
        name: multipleFiles
        type: boolean
        description: Whether to allow the user to select multiple files from the file
          input or just one
        default: true
        displayOptions:
          show:
            fieldType:
            - file
      - displayName: Accepted File Types
        name: acceptFileTypes
        type: string
        description: Comma-separated list of allowed file extensions
        placeholder: e.g. .jpg, .png
        hint: Leave empty to allow all file types
        default: ''
        displayOptions:
          show:
            fieldType:
            - file
      - displayName: The displayed date is formatted based on the locale of the user's
          browser
        name: formatDate
        type: notice
        default: ''
        displayOptions:
          show:
            fieldType:
            - date
      - displayName: Required Field
        name: requiredField
        type: boolean
        description: Whether to require the user to enter a value for this field before
          submitting the form
        default: false
        displayOptions:
          hide:
            fieldType:
            - html
            - hiddenField
- id: limitType
  name: Limit Type
  type: options
  default: afterTimeInterval
  required: false
  description: Sets the condition for the execution to resume. Can be a specified
    date or after some time.
  typeInfo:
    type: options
    displayName: Limit Type
    name: limitType
    possibleValues:
    - value: afterTimeInterval
      name: After Time Interval
      description: Waits for a certain amount of time
    - value: atSpecifiedTime
      name: At Specified Time
      description: Waits until the set date and time to continue
- id: resumeAmount
  name: Amount
  type: number
  default: 1
  required: false
  description: The time to wait
  validation:
    displayOptions:
      show:
        limitType:
        - afterTimeInterval
  typeInfo:
    type: number
    displayName: Amount
    name: resumeAmount
    typeOptions:
      minValue: 0
      numberPrecision: 2
- id: resumeUnit
  name: Unit
  type: options
  default: hours
  required: false
  description: Unit of the interval value
  validation:
    displayOptions:
      show:
        limitType:
        - afterTimeInterval
  typeInfo:
    type: options
    displayName: Unit
    name: resumeUnit
    possibleValues:
    - value: minutes
      name: Minutes
      description: ''
    - value: hours
      name: Hours
      description: ''
    - value: days
      name: Days
      description: ''
- id: maxDateAndTime
  name: Max Date and Time
  type: dateTime
  default: ''
  required: false
  description: Continue execution after the specified date and time
  validation:
    displayOptions:
      show:
        limitType:
        - atSpecifiedTime
  typeInfo:
    type: dateTime
    displayName: Max Date and Time
    name: maxDateAndTime
common_expressions:
- '{{ $input.all() }}'
- '{{ $execution.resumeFormUrl }}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: formFields
    text: Add Form Element
  hints:
  - field: jsonOutput
    text: <a href="https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.form/"
      target="_blank">See docs</a> for field syntax
  - field: formFields
    text: Does not accept <code>&lt;script&gt;</code>, <code>&lt;style&gt;</code>
      or <code>&lt;input&gt;</code> tags
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
  executable:
    alwaysOutputData:
      name: Always Output Data
      field_id: alwaysOutputData
      type: boolean
      default: false
      description: If active, will output a single, empty item when the output would
        have been empty. Use to prevent the workflow finishing on this node
    executeOnce:
      name: Execute Once
      field_id: executeOnce
      type: boolean
      default: false
      description: If active, the node executes only once, with data from the first
        item it receives
    retryOnFail:
      name: Retry On Fail
      field_id: retryOnFail
      type: boolean
      default: false
      description: If active, the node tries to execute again when it fails
    maxTries:
      name: Max. Tries
      field_id: maxTries
      type: number
      default: 3
      min: 2
      max: 5
      description: Number of times to attempt to execute the node before failing the
        execution
      displayOptions:
        show:
          retryOnFail:
          - true
    waitBetweenTries:
      name: Wait Between Tries (ms)
      field_id: waitBetweenTries
      type: number
      default: 1000
      min: 0
      max: 5000
      description: How long to wait between each attempt (in milliseconds)
      displayOptions:
        show:
          retryOnFail:
          - true
    onError:
      name: On Error
      field_id: onError
      type: options
      default: stopWorkflow
      description: Action to take when the node execution fails
      options:
      - name: Stop Workflow
        value: stopWorkflow
        description: Halt execution and fail workflow
      - name: Continue
        value: continueRegularOutput
        description: Pass error message as item in regular output
      - name: Continue (using error output)
        value: continueErrorOutput
        description: Pass item to an extra `error` output
  note: Executable nodes have both common and executable settings

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/form.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "n8n Form Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "defineForm": {
          "description": "",
          "type": "string",
          "enum": [
            "fields",
            "json"
          ],
          "default": "fields"
        },
        "jsonOutput": {
          "description": "",
          "type": "string",
          "default": "[\\n  {\\n    "
        },
        "formFields": {
          "description": "Label that appears above the input field",
          "type": "string",
          "default": {},
          "examples": [
            "Add Form Element"
          ]
        },
        "limitType": {
          "description": "Sets the condition for the execution to resume. Can be a specified date or after some time.",
          "type": "string",
          "enum": [
            "afterTimeInterval",
            "atSpecifiedTime"
          ],
          "default": "afterTimeInterval"
        },
        "resumeAmount": {
          "description": "The time to wait",
          "type": "number",
          "default": 1
        },
        "resumeUnit": {
          "description": "Unit of the interval value",
          "type": "string",
          "enum": [
            "minutes",
            "hours",
            "days"
          ],
          "default": "hours"
        },
        "maxDateAndTime": {
          "description": "Continue execution after the specified date and time",
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
        },
        "alwaysOutputData": {
          "type": "boolean",
          "default": false,
          "description": "If active, will output a single, empty item when the output would have been empty. Use to prevent the workflow finishing on this node"
        },
        "executeOnce": {
          "type": "boolean",
          "default": false,
          "description": "If active, the node executes only once, with data from the first item it receives"
        },
        "retryOnFail": {
          "type": "boolean",
          "default": false,
          "description": "If active, the node tries to execute again when it fails"
        },
        "maxTries": {
          "type": "number",
          "default": 3,
          "description": "Number of times to attempt to execute the node before failing the execution",
          "minimum": 2,
          "maximum": 5
        },
        "waitBetweenTries": {
          "type": "number",
          "default": 1000,
          "description": "How long to wait between each attempt (in milliseconds)",
          "minimum": 0,
          "maximum": 5000
        },
        "onError": {
          "type": "options",
          "default": "stopWorkflow",
          "description": "Action to take when the node execution fails",
          "enum": [
            "stopWorkflow",
            "continueRegularOutput",
            "continueErrorOutput"
          ]
        }
      }
    }
  },
  "metadata": {
    "nodeType": "regular",
    "version": [
      "1",
      "2.3"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2.3'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
