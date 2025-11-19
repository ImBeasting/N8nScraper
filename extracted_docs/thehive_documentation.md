---
title: "Node: TheHive"
slug: "node-thehive"
version: "1"
updated: "2025-11-13"
summary: "Consume TheHive API"
node_type: "regular"
group: "['transform']"
---

# Node: TheHive

**Purpose.** Consume TheHive API
**Subtitle.** ={{$parameter["operation"]}} : {{$parameter["resource"]}}


---

## Node Details

- **Icon:** `file:thehive.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **theHiveApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `theHiveApi` | ✓ | - |

---

## Operations

### Alert Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Observable Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Case Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Log Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create task log |
| Execute Responder | `executeResponder` | Execute a responder on a selected log |
| Get Many | `getAll` | Get many task logs |
| Get | `get` | Get a single log |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | alert | ✓ | Resource to operate on |  |

**Resource options:**

* **Alert** (`alert`)
* **Case** (`case`)
* **Log** (`log`)
* **Observable** (`observable`)
* **Task** (`task`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation Name or ID | `operation` | options | create | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | Title of the alert |  |
| Description | `description` | string |  | ✓ | Description of the alert |  |
| Severity | `severity` | options | 2 | ✓ | Severity of the alert. Default=Medium. |  |

**Severity options:**

* **Low** (``)
* **Medium** (``)
* **High** (``)

| Date | `date` | dateTime |  | ✓ | Date and time when the alert was raised default=now |  |
| Tags | `tags` | string |  | ✓ | Case Tags | e.g. tag,tag2,tag3... |  |
| TLP | `tlp` | options | 2 | ✓ | Traffict Light Protocol (TLP). Default=Amber. |  |

**TLP options:**

* **White** (``)
* **Green** (``)
* **Amber** (``)
* **Red** (``)

| Status | `status` | options | New | ✓ | Status of the alert |  |

**Status options:**

* **New** (`New`)
* **Updated** (`Updated`)
* **Ignored** (`Ignored`)
* **Imported** (`Imported`)

| Type | `type` | string |  | ✓ | Type of the alert |  |
| Source | `source` | string |  | ✓ | Source of the alert |  |
| SourceRef | `sourceRef` | string |  | ✓ | Source reference of the alert |  |
| Follow | `follow` | boolean | True | ✓ | Whether the alert becomes active when updated default=true |  |
| Artifacts | `artifactUi` | fixedCollection | {} | ✗ | Type of the observable. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Artifact |  |

<details>
<summary><strong>Artifacts sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Artifact | `artifactValues` |  |  |  |

</details>

| JSON Parameters | `jsonParameters` | boolean | True | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Case template to use when a case is created from this alert | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Case Template | `caseTemplate` | string |  | Case template to use when a case is created from this alert |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Custom Fields (JSON) | `customFieldsJson` | string |  | Custom fields in JSON format. Overrides Custom Fields UI if set. |

</details>

| Case ID | `caseId` | string |  | ✓ | ID of the case |  |
| Data Type Name or ID | `dataType` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Data | `data` | string |  | ✓ |  |  |
| Input Binary Field | `binaryProperty` | string | data | ✓ | The name of the input binary field that represent the attachment file |  |
| Message | `message` | string |  | ✓ | Description of the observable in the context of the case |  |
| Start Date | `startDate` | dateTime |  | ✓ | Date and time of the begin of the case default=now |  |
| TLP | `tlp` | options | 2 | ✓ | Traffict Light Protocol (TLP). Default=Amber. |  |

**TLP options:**

* **White** (``)
* **Green** (``)
* **Amber** (``)
* **Red** (``)

| IOC | `ioc` | boolean | False | ✓ | Whether the observable is an IOC (Indicator of compromise) |  |
| Sighted | `sighted` | boolean | False | ✓ | Whether sighted previously |  |
| Status | `status` | options |  | ✓ | Status of the observable. Default=Ok. |  |

**Status options:**

* **Ok** (`Ok`)
* **Deleted** (`Deleted`)

| Options | `options` | collection | {} | ✗ | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Observable Tags | `tags` | string |  |  |

</details>

| Title | `title` | string |  | ✓ | Title of the case |  |
| Description | `description` | string |  | ✓ | Description of the case |  |
| Severity | `severity` | options | 2 | ✓ | Severity of the alert. Default=Medium. |  |

**Severity options:**

* **Low** (``)
* **Medium** (``)
* **High** (``)

| Start Date | `startDate` | dateTime |  | ✓ | Date and time of the begin of the case default=now |  |
| Owner | `owner` | string |  | ✓ |  |  |
| Flag | `flag` | boolean | False | ✓ | Flag of the case default=false |  |
| TLP | `tlp` | options | 2 | ✓ | Traffict Light Protocol (TLP). Default=Amber. |  |

**TLP options:**

* **White** (``)
* **Green** (``)
* **Amber** (``)
* **Red** (``)

| Tags | `tags` | string |  | ✓ |  |  |
| JSON Parameters | `jsonParameters` | boolean | True | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Custom Fields (JSON) | `customFieldsJson` | string |  | Custom fields in JSON format. Overrides Custom Fields UI if set. |
| End Date | `endDate` | dateTime |  | Resolution date |
| Summary | `summary` | string |  | Summary of the case, to be provided when closing a case |
| Metrics (JSON) | `metrics` | json | [] | List of metrics |

</details>

| Case ID | `caseId` | string |  | ✓ |  |  |
| Title | `title` | string |  | ✓ | Task details |  |
| Status | `status` | options | Waiting | ✓ | Status of the task. Default=Waiting. |  |

**Status options:**

* **Cancel** (`Cancel`)
* **Completed** (`Completed`)
* **InProgress** (`InProgress`)
* **Waiting** (`Waiting`)

| Flag | `flag` | boolean | False | ✓ | Whether to flag the task. Default=false. |  |
| Options | `options` | collection | {} | ✗ | Task details | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Task details |
| End Date | `endDate` | dateTime |  | Date of the end of the task. This is automatically set when status is set to Completed. |
| Owner | `owner` | string |  | User who owns the task. This is automatically set to current user when status is set to InProgress. |
| Start Date | `startDate` | dateTime |  | Date of the beginning of the task. This is automatically set when status is set to Open. |

</details>

| Task ID | `taskId` | string |  | ✓ | ID of the task |  |
| Message | `message` | string |  | ✓ | Content of the Log |  |
| Start Date | `startDate` | dateTime |  | ✓ | Date of the log submission default=now |  |
| Status | `status` | options |  | ✓ | Status of the log (Ok or Deleted) default=Ok |  |

**Status options:**

* **Ok** (`Ok`)
* **Deleted** (`Deleted`)

| Options | `options` | collection | {} | ✗ | The name of the input binary field which holds binary data | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachment | `attachmentValues` | fixedCollection | {} | The name of the input binary field which holds binary data |

</details>


### Execute Responder parameters (`executeResponder`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Alert ID | `id` | string |  | ✓ | Title of the alert |  |
| Responder Name or ID | `responder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Observable ID | `id` | string |  | ✓ | ID of the observable |  |
| Responder Name or ID | `responder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Case ID | `id` | string |  | ✓ | ID of the case |  |
| Responder Name or ID | `responder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Task ID | `id` | string |  | ✓ | ID of the taks |  |
| Responder Name or ID | `responder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Log ID | `id` | string |  | ✓ |  |  |
| Responder Name or ID | `responder` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort | `sort` | string |  |  |

</details>

| Filters | `filters` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Description | `description` | string |  | Description of the alert |
| Follow | `follow` | boolean | False | Whether the alert becomes active when updated default=true |
| Severity | `severity` | options | 2 | Severity of the alert. Default=Medium. |
| Tags | `tags` | string |  |  |
| Title | `title` | string |  |  |
| TLP | `tlp` | options | 2 | Traffict Light Protocol (TLP). Default=Amber. |

</details>

| Case ID | `caseId` | string |  | ✓ | ID of the case |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Specify the sorting attribut, + for asc, - for desc | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort | `sort` | string |  | Specify the sorting attribut, + for asc, - for desc |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Specify the sorting attribut, + for asc, - for desc | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort | `sort` | string |  | Specify the sorting attribut, + for asc, - for desc |

</details>

| Filters | `filters` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add a Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Description | `description` | string |  | Description of the case |
| End Date | `endDate` | dateTime |  | Resolution date |
| Flag | `flag` | boolean | False | Flag of the case default=false |
| Impact Status | `impactStatus` | options |  |  |
| Owner | `owner` | string |  |  |
| Resolution Status | `resolutionStatus` | options |  |  |
| Severity | `severity` | options | 2 | Severity of the alert. Default=Medium. |
| Start Date | `startDate` | dateTime |  | Date and time of the begin of the case default=now |
| Status | `status` | options | Open |  |
| Summary | `summary` | string |  | Summary of the case, to be provided when closing a case |
| Tags | `tags` | string |  |  |
| Title | `title` | string |  | Title of the case |
| TLP | `tlp` | options | 2 | Traffict Light Protocol (TLP). Default=Amber. |

</details>

| Case ID | `caseId` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Specify the sorting attribut, + for asc, - for desc | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort | `sort` | string |  | Specify the sorting attribut, + for asc, - for desc |

</details>

| Task ID | `taskId` | string |  | ✓ | ID of the task |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Alert ID | `id` | string |  | ✓ | Title of the alert |  |
| Options | `options` | collection | {} | ✗ | Whether to include similar cases | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Similar Cases | `includeSimilar` | boolean | False | Whether to include similar cases |

</details>

| Observable ID | `id` | string |  | ✓ | ID of the observable |  |
| Case ID | `id` | string |  | ✓ | ID of the case |  |
| Task ID | `id` | string |  | ✓ | ID of the taks |  |
| Log ID | `id` | string |  | ✓ |  |  |

---

## Load Options Methods

- `loadResponders`

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"]}}`

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: theHive
displayName: TheHive
description: Consume TheHive API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: theHiveApi
  required: true
operations:
- id: create
  name: Create
  description: Create task log
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the alert
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
    typeInfo: &id006
      type: string
      displayName: Title
      name: title
  - id: description
    name: Description
    type: string
    default: ''
    required: true
    description: Description of the alert
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
    typeInfo: &id008
      type: string
      displayName: Description
      name: description
  - id: severity
    name: Severity
    type: options
    default: 2
    required: true
    description: Severity of the alert. Default=Medium.
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
    typeInfo: &id010
      type: options
      displayName: Severity
      name: severity
      possibleValues:
      - value: Low
        name: Low
        description: ''
      - value: Medium
        name: Medium
        description: ''
      - value: High
        name: High
        description: ''
  - id: date
    name: Date
    type: dateTime
    default: ''
    required: true
    description: Date and time when the alert was raised default=now
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - alert
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Date
      name: date
  - id: tags
    name: Tags
    type: string
    default: ''
    required: true
    description: Case Tags
    placeholder: tag,tag2,tag3...
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
    typeInfo: &id014
      type: string
      displayName: Tags
      name: tags
  - id: tlp
    name: TLP
    type: options
    default: 2
    required: true
    description: Traffict Light Protocol (TLP). Default=Amber.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
    typeInfo: &id002
      type: options
      displayName: TLP
      name: tlp
      possibleValues:
      - value: White
        name: White
        description: ''
      - value: Green
        name: Green
        description: ''
      - value: Amber
        name: Amber
        description: ''
      - value: Red
        name: Red
        description: ''
  - id: status
    name: Status
    type: options
    default: New
    required: true
    description: Status of the alert
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - log
          operation:
          - create
    typeInfo: &id004
      type: options
      displayName: Status
      name: status
      possibleValues:
      - value: Ok
        name: Ok
        description: ''
      - value: Deleted
        name: Deleted
        description: ''
  - id: type
    name: Type
    type: string
    default: ''
    required: true
    description: Type of the alert
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - alert
          operation:
          - create
    typeInfo:
      type: string
      displayName: Type
      name: type
  - id: source
    name: Source
    type: string
    default: ''
    required: true
    description: Source of the alert
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - alert
          operation:
          - create
    typeInfo:
      type: string
      displayName: Source
      name: source
  - id: sourceRef
    name: SourceRef
    type: string
    default: ''
    required: true
    description: Source reference of the alert
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - alert
          operation:
          - create
    typeInfo:
      type: string
      displayName: SourceRef
      name: sourceRef
  - id: follow
    name: Follow
    type: boolean
    default: true
    required: true
    description: Whether the alert becomes active when updated default=true
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - alert
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: Follow
      name: follow
  - id: artifactUi
    name: Artifacts
    type: fixedCollection
    default: {}
    required: false
    description: Type of the observable. Choose from the list, or specify an ID using
      an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    hint: The name of the input binary field containing the file to be written
    placeholder: Add Artifact
    validation:
      displayOptions:
        show:
          resource:
          - alert
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Artifacts
      name: artifactUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: artifactValues
        displayName: Artifact
        values:
        - displayName: Data Type Name or ID
          name: dataType
          type: options
          description: Type of the observable. Choose from the list, or specify an
            ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: ''
          typeOptions:
            loadOptionsMethod: loadObservableTypes
        - displayName: Data
          name: data
          type: string
          default: ''
          displayOptions:
            hide:
              dataType:
              - file
        - displayName: Input Binary Field
          name: binaryProperty
          type: string
          hint: The name of the input binary field containing the file to be written
          default: data
          displayOptions:
            show:
              dataType:
              - file
        - displayName: Message
          name: message
          type: string
          default: ''
        - displayName: Case Tags
          name: tags
          type: string
          default: ''
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: true
    required: false
    description: ''
    validation: &id015
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
          - update
    typeInfo: &id016
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of the case
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
          - getAll
    typeInfo: &id018
      type: string
      displayName: Case ID
      name: caseId
  - id: dataType
    name: Data Type Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - observable
          operation:
          - create
          - executeAnalyzer
    typeInfo:
      type: options
      displayName: Data Type Name or ID
      name: dataType
      typeOptions:
        loadOptionsMethod: loadObservableTypes
      possibleValues: []
  - id: data
    name: Data
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - observable
          operation:
          - create
        hide:
          dataType:
          - file
    typeInfo:
      type: string
      displayName: Data
      name: data
  - id: binaryProperty
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: The name of the input binary field that represent the attachment
      file
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - observable
          operation:
          - create
          dataType:
          - file
    typeInfo:
      type: string
      displayName: Input Binary Field
      name: binaryProperty
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: Description of the observable in the context of the case
    validation: &id021
      required: true
      displayOptions:
        show:
          resource:
          - log
          operation:
          - create
    typeInfo: &id022
      type: string
      displayName: Message
      name: message
  - id: startDate
    name: Start Date
    type: dateTime
    default: ''
    required: true
    description: Date and time of the begin of the case default=now
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - log
          operation:
          - create
    typeInfo: &id012
      type: dateTime
      displayName: Start Date
      name: startDate
  - id: tlp
    name: TLP
    type: options
    default: 2
    required: true
    description: Traffict Light Protocol (TLP). Default=Amber.
    validation: *id001
    typeInfo: *id002
  - id: ioc
    name: IOC
    type: boolean
    default: false
    required: true
    description: Whether the observable is an IOC (Indicator of compromise)
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - observable
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: IOC
      name: ioc
  - id: sighted
    name: Sighted
    type: boolean
    default: false
    required: true
    description: Whether sighted previously
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - observable
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: Sighted
      name: sighted
  - id: status
    name: Status
    type: options
    default: ''
    required: true
    description: Status of the observable. Default=Ok.
    validation: *id003
    typeInfo: *id004
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the case
    validation: *id005
    typeInfo: *id006
  - id: description
    name: Description
    type: string
    default: ''
    required: true
    description: Description of the case
    validation: *id007
    typeInfo: *id008
  - id: severity
    name: Severity
    type: options
    default: 2
    required: true
    description: Severity of the alert. Default=Medium.
    validation: *id009
    typeInfo: *id010
  - id: startDate
    name: Start Date
    type: dateTime
    default: ''
    required: true
    description: Date and time of the begin of the case default=now
    validation: *id011
    typeInfo: *id012
  - id: owner
    name: Owner
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
    typeInfo:
      type: string
      displayName: Owner
      name: owner
  - id: flag
    name: Flag
    type: boolean
    default: false
    required: true
    description: Flag of the case default=false
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
    typeInfo: &id020
      type: boolean
      displayName: Flag
      name: flag
  - id: tlp
    name: TLP
    type: options
    default: 2
    required: true
    description: Traffict Light Protocol (TLP). Default=Amber.
    validation: *id001
    typeInfo: *id002
  - id: tags
    name: Tags
    type: string
    default: ''
    required: true
    description: ''
    validation: *id013
    typeInfo: *id014
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: true
    required: false
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Task details
    validation: *id005
    typeInfo: *id006
  - id: status
    name: Status
    type: options
    default: Waiting
    required: true
    description: Status of the task. Default=Waiting.
    validation: *id003
    typeInfo: *id004
  - id: flag
    name: Flag
    type: boolean
    default: false
    required: true
    description: Whether to flag the task. Default=false.
    validation: *id019
    typeInfo: *id020
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task
    validation: &id031
      required: true
      displayOptions:
        show:
          resource:
          - log
          operation:
          - create
          - getAll
    typeInfo: &id032
      type: string
      displayName: Task ID
      name: taskId
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: Content of the Log
    validation: *id021
    typeInfo: *id022
  - id: startDate
    name: Start Date
    type: dateTime
    default: ''
    required: true
    description: Date of the log submission default=now
    validation: *id011
    typeInfo: *id012
  - id: status
    name: Status
    type: options
    default: ''
    required: true
    description: Status of the log (Ok or Deleted) default=Ok
    validation: *id003
    typeInfo: *id004
- id: executeResponder
  name: Execute Responder
  description: Execute a responder on a selected log
  params:
  - id: id
    name: Alert ID
    type: string
    default: ''
    required: true
    description: Title of the alert
    validation: &id023
      required: true
      displayOptions:
        show:
          resource:
          - log
          operation:
          - executeResponder
          - get
    typeInfo: &id024
      type: string
      displayName: Log ID
      name: id
  - id: responder
    name: Responder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id025
      required: true
      displayOptions:
        show:
          resource:
          - log
          operation:
          - executeResponder
        hide:
          id:
          - ''
    typeInfo: &id026
      type: options
      displayName: Responder Name or ID
      name: responder
      typeOptions:
        loadOptionsMethod: loadResponders
      possibleValues: []
  - id: id
    name: Observable ID
    type: string
    default: ''
    required: true
    description: ID of the observable
    validation: *id023
    typeInfo: *id024
  - id: responder
    name: Responder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id025
    typeInfo: *id026
  - id: id
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of the case
    validation: *id023
    typeInfo: *id024
  - id: responder
    name: Responder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id025
    typeInfo: *id026
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the taks
    validation: *id023
    typeInfo: *id024
  - id: responder
    name: Responder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id025
    typeInfo: *id026
  - id: id
    name: Log ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id023
    typeInfo: *id024
  - id: responder
    name: Responder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id025
    typeInfo: *id026
- id: getAll
  name: Get Many
  description: Get many task logs
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id027
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - log
    typeInfo: &id028
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id029
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - log
          returnAll:
          - false
    typeInfo: &id030
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of the case
    validation: *id017
    typeInfo: *id018
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task
    validation: *id031
    typeInfo: *id032
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id027
    typeInfo: *id028
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id029
    typeInfo: *id030
- id: get
  name: Get
  description: Get a single log
  params:
  - id: id
    name: Alert ID
    type: string
    default: ''
    required: true
    description: Title of the alert
    validation: *id023
    typeInfo: *id024
  - id: id
    name: Observable ID
    type: string
    default: ''
    required: true
    description: ID of the observable
    validation: *id023
    typeInfo: *id024
  - id: id
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of the case
    validation: *id023
    typeInfo: *id024
  - id: id
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the taks
    validation: *id023
    typeInfo: *id024
  - id: id
    name: Log ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id023
    typeInfo: *id024
common_expressions:
- ={{$parameter["operation"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: tags
    text: tag,tag2,tag3...
  - field: artifactUi
    text: Add Artifact
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: filters
    text: Add Filter
  - field: options
    text: Add option
  - field: updateFields
    text: tag1,tag2
  - field: options
    text: Add option
  - field: filters
    text: Add Filter
  - field: options
    text: Add option
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: filters
    text: Add a Filter
  - field: options
    text: Add option
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: filters
    text: Add Filter
  - field: options
    text: Add option
  hints:
  - field: artifactUi
    text: The name of the input binary field containing the file to be written
  - field: updateFields
    text: The name of the input binary field containing the file to be written
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
  "$id": "https://n8n.io/schemas/nodes/theHive.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TheHive Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "executeResponder",
        "getAll",
        "get"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "alert",
            "case",
            "log",
            "observable",
            "task"
          ],
          "default": "alert"
        },
        "operation": {
          "description": "Create task log",
          "type": "string",
          "enum": [
            "create",
            "executeResponder",
            "getAll",
            "get"
          ],
          "default": "getAll"
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "id": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "caseId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "Task details",
          "type": "string",
          "default": ""
        },
        "description": {
          "description": "Description of the case",
          "type": "string",
          "default": ""
        },
        "severity": {
          "description": "Severity of the alert. Default=Medium.",
          "type": "string",
          "enum": [
            "Low",
            "Medium",
            "High"
          ],
          "default": 2
        },
        "date": {
          "description": "Date and time when the alert was raised default=now",
          "type": "string",
          "default": ""
        },
        "tags": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "tlp": {
          "description": "Traffict Light Protocol (TLP). Default=Amber.",
          "type": "string",
          "enum": [
            "White",
            "Green",
            "Amber",
            "Red"
          ],
          "default": 2
        },
        "status": {
          "description": "Status of the log (Ok or Deleted) default=Ok",
          "type": "string",
          "enum": [
            "Ok",
            "Deleted"
          ],
          "default": ""
        },
        "type": {
          "description": "Type of the alert",
          "type": "string",
          "default": ""
        },
        "source": {
          "description": "Source of the alert",
          "type": "string",
          "default": ""
        },
        "sourceRef": {
          "description": "Source reference of the alert",
          "type": "string",
          "default": ""
        },
        "follow": {
          "description": "Whether the alert becomes active when updated default=true",
          "type": "boolean",
          "default": true
        },
        "artifactUi": {
          "description": "Type of the observable. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Artifact"
          ]
        },
        "responder": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "",
          "type": "boolean",
          "default": true
        },
        "additionalFields": {
          "description": "Case template to use when a case is created from this alert",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "Task details",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "options": {
          "description": "The name of the input binary field which holds binary data",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "filters": {
          "description": "Task details",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "dataType": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "data": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "binaryProperty": {
          "description": "The name of the input binary field that represent the attachment file",
          "type": "string",
          "default": "data"
        },
        "message": {
          "description": "Content of the Log",
          "type": "string",
          "default": ""
        },
        "startDate": {
          "description": "Date of the log submission default=now",
          "type": "string",
          "default": ""
        },
        "ioc": {
          "description": "Whether the observable is an IOC (Indicator of compromise)",
          "type": "boolean",
          "default": false
        },
        "sighted": {
          "description": "Whether sighted previously",
          "type": "boolean",
          "default": false
        },
        "analyzers": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "owner": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "flag": {
          "description": "Whether to flag the task. Default=false.",
          "type": "boolean",
          "default": false
        },
        "taskId": {
          "description": "ID of the task",
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
    "version": "1"
  },
  "credentials": [
    {
      "name": "theHiveApi",
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
