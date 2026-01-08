---
title: "Node: KoBoToolbox"
slug: "node-kobotoolbox"
version: "1"
updated: "2026-01-08"
summary: "Work with KoBoToolbox forms and submissions"
node_type: "regular"
group: "['transform']"
---

# Node: KoBoToolbox

**Purpose.** Work with KoBoToolbox forms and submissions
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:koBoToolbox.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **koBoToolboxApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **jsonNotice** when resource=['submission'], operation=['getAll'], filterType=['json']: See <a href="https://github.com/SEL-Columbia/formhub/wiki/Formhub-Access-Points-(API)#api-parameters" target="_blank">Formhub API docs</a> to creating filters, using the MongoDB JSON format - e.g. {"_submission_time":{"$lt":"2021-10-01T01:02:03"}}

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `koBoToolboxApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** GET

**Common Endpoints:**
- `/api/v2/assets/`

---

## Operations

### Form Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a form |
| Get Many | `getAll` | Get many forms |
| Redeploy | `redeploy` | Redeploy Current Form Version |

### Hook Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a single hook definition |
| Get Many | `getAll` | List many hooks on a form |
| Logs | `getLogs` | Get hook logs |
| Retry All | `retryAll` | Retry all failed attempts for a given hook |
| Retry One | `retryOne` | Retry a specific hook |

### Submission Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a single submission |
| Get | `get` | Get a single submission |
| Get Many | `getAll` | Get many submissions |
| Get Validation Status | `getValidation` | Get the validation status for the submission |
| Update Validation Status | `setValidation` | Set the validation status of the submission |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a file |
| Delete | `delete` | Delete file |
| Get | `get` | Get a file content |
| Get Many | `getAll` | Get many files |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | submission | ✓ | Resource to operate on |  |

**Resource options:**

* **File** (`file`)
* **Form** (`form`)
* **Hook** (`hook`)
* **Submission** (`submission`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Get a form |  |

**Operation options:**

* **Get** (`get`) - Get a form
* **Get Many** (`getAll`) - Get many forms
* **Redeploy** (`redeploy`) - Redeploy Current Form Version

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Hook ID | `hookId` | string |  | ✓ | Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4) |  |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Submission ID | `submissionId` | string |  | ✓ | Submission ID (number, e.g. 245128) |  |
| Options | `options` | collection | {} | ✗ | Whether to download submitted attachments | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Download Attachments | `download` | boolean | False | Whether to download submitted attachments |
| Attachments Naming Scheme | `binaryNamingScheme` | options | sequence |  |
| Attachments Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" |
| Fields to Retrieve | `fields` | string |  | Comma-separated list of fields to retrieve (e.g. _submission_time,_submitted_by). If left blank, all fields are retrieved. |
| File Size | `version` | options | download_url | Attachment size to retrieve, if multiple versions are available |
| Multiselect Mask | `selectMask` | string | select_* | Comma-separated list of wildcard-style selectors for fields that should be treated as multiselect fields, i.e. parsed as arrays. |
| Number Mask | `numberMask` | string | n_*, f_* | Comma-separated list of wildcard-style selectors for fields that should be treated as numbers |
| Reformat | `reformat` | boolean | False | Whether to apply some reformatting to the submission data, such as parsing GeoJSON coordinates |
| Sort | `sort` | json |  | Sort predicates, in MongoDB JSON format (e.g. {"_submission_time":1}) |

</details>

| File ID | `fileId` | string |  | ✓ | Uid of the file (should start with "af" e.g. "afQoJxA4kmKEXVpkH6SYbhb" |  |
| Property Name | `binaryPropertyName` | string | data | ✓ | Name of the binary property to write the file into |  |
| Download File Content | `download` | boolean | False | ✓ | Whether to download the file content into a binary property |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 1000 | ✗ | Max number of results to return | min:∞, max:3000 |
| Options | `options` | collection | {} | ✗ | Whether to sort by descending order | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort | `sort` | fixedCollection | {} | Whether to sort by descending order |

</details>

| Filters | `filters` | collection | {} | ✗ | A text search query based on form data - e.g. "owner__username:meg AND name__icontains:quixotic" - see <a href="https://github.com/kobotoolbox/kpi#searching" target="_blank">docs</a> for more details | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filter | `filter` | string | asset_type:survey | A text search query based on form data - e.g. "owner__username:meg AND name__icontains:quixotic" - see <a href="https://github.com/kobotoolbox/kpi#searching" target="_blank">docs</a> for more details |

</details>

| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 1000 | ✗ | Max number of results to return | min:∞, max:3000 |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:∞, max:3000 |
| Filter | `filterType` | options | none | ✗ |  |  |

**Filter options:**

* **None** (`none`)
* **JSON** (`json`)

| Filters (JSON) | `filterJson` | string |  | ✗ |  |  |
| Options | `options` | collection | {} | ✗ | Whether to download submitted attachments | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Download Attachments | `download` | boolean | False | Whether to download submitted attachments |
| Attachments Naming Scheme | `binaryNamingScheme` | options | sequence |  |
| Attachments Prefix | `dataPropertyAttachmentsPrefixName` | string | attachment_ | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment_" the first attachment is saved to "attachment_0" |
| Fields to Retrieve | `fields` | string |  | Comma-separated list of fields to retrieve (e.g. _submission_time,_submitted_by). If left blank, all fields are retrieved. |
| File Size | `version` | options | download_url | Attachment size to retrieve, if multiple versions are available |
| Multiselect Mask | `selectMask` | string | select_* | Comma-separated list of wildcard-style selectors for fields that should be treated as multiselect fields, i.e. parsed as arrays. |
| Number Mask | `numberMask` | string | n_*, f_* | Comma-separated list of wildcard-style selectors for fields that should be treated as numbers |
| Reformat | `reformat` | boolean | False | Whether to apply some reformatting to the submission data, such as parsing GeoJSON coordinates |
| Sort | `sort` | json |  | Sort predicates, in MongoDB JSON format (e.g. {"_submission_time":1}) |

</details>


### Redeploy parameters (`redeploy`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Logs parameters (`getLogs`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Hook ID | `hookId` | string |  | ✓ | Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4) |  |
| Log Status | `status` | options |  | ✗ | Only retrieve logs with a specific status |  |

**Log Status options:**

* **All** (``)
* **Failed** (`0`)
* **Pending** (`1`)
* **Success** (`2`)

| Start Date | `startDate` | dateTime |  | ✗ | Minimum date for the hook log to retrieve |  |
| End Date | `endDate` | dateTime |  | ✗ | Maximum date for the hook log to retrieve |  |

### Retry All parameters (`retryAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Hook ID | `hookId` | string |  | ✓ | Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4) |  |

### Retry One parameters (`retryOne`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Hook ID | `hookId` | string |  | ✓ | Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4) |  |
| Hook Log ID | `logId` | string |  | ✓ | Hook log ID (starts with hl, e.g. hlSbGKaUKzTVNoWEVMYbLHe) |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Submission ID | `submissionId` | string |  | ✓ | Submission ID (number, e.g. 245128) |  |
| File ID | `fileId` | string |  | ✓ | Uid of the file (should start with "af" e.g. "afQoJxA4kmKEXVpkH6SYbhb" |  |

### Get Validation Status parameters (`getValidation`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Submission ID | `submissionId` | string |  | ✓ | Submission ID (number, e.g. 245128) |  |

### Update Validation Status parameters (`setValidation`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Name or ID | `formId` | options |  | ✓ | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Submission ID | `submissionId` | string |  | ✓ | Submission ID (number, e.g. 245128) |  |
| Validation Status | `validationStatus` | options |  | ✓ | Desired Validation Status |  |

**Validation Status options:**

* **Approved** (`validation_status_approved`)
* **Not Approved** (`validation_status_not_approved`)
* **On Hold** (`validation_status_on_hold`)


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File Upload Mode | `fileMode` | options | binary | ✓ |  |  |

**File Upload Mode options:**

* **Binary File** (`binary`)
* **URL** (`url`)

| Property Name | `binaryPropertyName` | string | data | ✓ | Name of the binary property containing the file to upload. Supported types: image, audio, video, csv, xml, zip. |  |
| File URL | `fileUrl` | string |  | ✓ | HTTP(s) link to the file to upload | url |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`

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
* Categories: Communication, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: koBoToolbox
displayName: KoBoToolbox
description: Work with KoBoToolbox forms and submissions
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: koBoToolboxApi
  required: true
operations:
- id: get
  name: Get
  description: Get a form
  params:
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - file
    typeInfo: &id002
      type: options
      displayName: Form Name or ID
      name: formId
      typeOptions:
        loadOptionsMethod: loadForms
      possibleValues: []
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: hookId
    name: Hook ID
    type: string
    default: ''
    required: true
    description: Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4)
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - hook
          operation:
          - get
          - retryOne
          - retryAll
          - getLogs
    typeInfo: &id008
      type: string
      displayName: Hook ID
      name: hookId
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: submissionId
    name: Submission ID
    type: string
    default: ''
    required: true
    description: Submission ID (number, e.g. 245128)
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - submission
          operation:
          - get
          - delete
          - getValidation
          - setValidation
    typeInfo: &id010
      type: string
      displayName: Submission ID
      name: submissionId
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: true
    description: Uid of the file (should start with "af" e.g. "afQoJxA4kmKEXVpkH6SYbhb"
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - delete
          - get
    typeInfo: &id012
      type: string
      displayName: File ID
      name: fileId
  - id: binaryPropertyName
    name: Property Name
    type: string
    default: data
    required: true
    description: Name of the binary property to write the file into
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - create
          fileMode:
          - binary
    typeInfo: &id014
      type: string
      displayName: Property Name
      name: binaryPropertyName
  - id: download
    name: Download File Content
    type: boolean
    default: false
    required: true
    description: Whether to download the file content into a binary property
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - get
    typeInfo:
      type: boolean
      displayName: Download File Content
      name: download
- id: getAll
  name: Get Many
  description: Get many forms
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - submission
          operation:
          - getAll
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 1000
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - submission
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        maxValue: 3000
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 1000
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: filterType
    name: Filter
    type: options
    default: none
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - submission
          operation:
          - getAll
    typeInfo:
      type: options
      displayName: Filter
      name: filterType
      possibleValues:
      - value: none
        name: None
        description: ''
      - value: json
        name: JSON
        description: ''
  - id: filterJson
    name: Filters (JSON)
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - submission
          operation:
          - getAll
          filterType:
          - json
    typeInfo:
      type: string
      displayName: Filters (JSON)
      name: filterJson
- id: redeploy
  name: Redeploy
  description: Redeploy Current Form Version
  params:
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
- id: getLogs
  name: Logs
  description: Get hook logs
  params:
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: hookId
    name: Hook ID
    type: string
    default: ''
    required: true
    description: Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4)
    validation: *id007
    typeInfo: *id008
  - id: status
    name: Log Status
    type: options
    default: ''
    required: false
    description: Only retrieve logs with a specific status
    validation:
      displayOptions:
        show:
          resource:
          - hook
          operation:
          - getLogs
    typeInfo:
      type: options
      displayName: Log Status
      name: status
      possibleValues:
      - value: All
        name: All
        description: ''
      - value: '0'
        name: Failed
        description: ''
      - value: '1'
        name: Pending
        description: ''
      - value: '2'
        name: Success
        description: ''
  - id: startDate
    name: Start Date
    type: dateTime
    default: ''
    required: false
    description: Minimum date for the hook log to retrieve
    validation:
      displayOptions:
        show:
          resource:
          - hook
          operation:
          - getLogs
    typeInfo:
      type: dateTime
      displayName: Start Date
      name: startDate
  - id: endDate
    name: End Date
    type: dateTime
    default: ''
    required: false
    description: Maximum date for the hook log to retrieve
    validation:
      displayOptions:
        show:
          resource:
          - hook
          operation:
          - getLogs
    typeInfo:
      type: dateTime
      displayName: End Date
      name: endDate
- id: retryAll
  name: Retry All
  description: Retry all failed attempts for a given hook
  params:
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: hookId
    name: Hook ID
    type: string
    default: ''
    required: true
    description: Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4)
    validation: *id007
    typeInfo: *id008
- id: retryOne
  name: Retry One
  description: Retry a specific hook
  params:
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: hookId
    name: Hook ID
    type: string
    default: ''
    required: true
    description: Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4)
    validation: *id007
    typeInfo: *id008
  - id: logId
    name: Hook Log ID
    type: string
    default: ''
    required: true
    description: Hook log ID (starts with hl, e.g. hlSbGKaUKzTVNoWEVMYbLHe)
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - hook
          operation:
          - retryOne
    typeInfo:
      type: string
      displayName: Hook Log ID
      name: logId
- id: delete
  name: Delete
  description: Delete a single submission
  params:
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: submissionId
    name: Submission ID
    type: string
    default: ''
    required: true
    description: Submission ID (number, e.g. 245128)
    validation: *id009
    typeInfo: *id010
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: true
    description: Uid of the file (should start with "af" e.g. "afQoJxA4kmKEXVpkH6SYbhb"
    validation: *id011
    typeInfo: *id012
- id: getValidation
  name: Get Validation Status
  description: Get the validation status for the submission
  params:
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: submissionId
    name: Submission ID
    type: string
    default: ''
    required: true
    description: Submission ID (number, e.g. 245128)
    validation: *id009
    typeInfo: *id010
- id: setValidation
  name: Update Validation Status
  description: Set the validation status of the submission
  params:
  - id: formId
    name: Form Name or ID
    type: options
    default: ''
    required: true
    description: Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: submissionId
    name: Submission ID
    type: string
    default: ''
    required: true
    description: Submission ID (number, e.g. 245128)
    validation: *id009
    typeInfo: *id010
  - id: validationStatus
    name: Validation Status
    type: options
    default: ''
    required: true
    description: Desired Validation Status
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - submission
          operation:
          - setValidation
    typeInfo:
      type: options
      displayName: Validation Status
      name: validationStatus
      possibleValues:
      - value: validation_status_approved
        name: Approved
        description: ''
      - value: validation_status_not_approved
        name: Not Approved
        description: ''
      - value: validation_status_on_hold
        name: On Hold
        description: ''
- id: create
  name: Create
  description: Create a file
  params:
  - id: fileMode
    name: File Upload Mode
    type: options
    default: binary
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - file
          operation:
          - create
    typeInfo:
      type: options
      displayName: File Upload Mode
      name: fileMode
      possibleValues:
      - value: binary
        name: Binary File
        description: ''
      - value: url
        name: URL
        description: ''
  - id: binaryPropertyName
    name: Property Name
    type: string
    default: data
    required: true
    description: 'Name of the binary property containing the file to upload. Supported
      types: image, audio, video, csv, xml, zip.'
    validation: *id013
    typeInfo: *id014
  - id: fileUrl
    name: File URL
    type: string
    default: ''
    required: true
    description: HTTP(s) link to the file to upload
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - file
          operation:
          - create
          fileMode:
          - url
    typeInfo:
      type: string
      displayName: File URL
      name: fileUrl
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - GET
  endpoints:
  - /api/v2/assets/
  headers: []
  query_params:
  - name
ui_elements:
  notices:
  - name: jsonNotice
    text: See <a href="https://github.com/SEL-Columbia/formhub/wiki/Formhub-Access-Points-(API)#api-parameters"
      target="_blank">Formhub API docs</a> to creating filters, using the MongoDB
      JSON format - e.g. {"_submission_time":{"$lt":"2021-10-01T01:02:03"}}
    conditions:
      show:
        resource:
        - submission
        operation:
        - getAll
        filterType:
        - json
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/koBoToolbox.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "KoBoToolbox Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
        "redeploy",
        "getLogs",
        "retryAll",
        "retryOne",
        "delete",
        "getValidation",
        "setValidation",
        "create"
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
            "file",
            "form",
            "hook",
            "submission"
          ],
          "default": "submission"
        },
        "operation": {
          "description": "Create a file",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll"
          ],
          "default": "get"
        },
        "formId": {
          "description": "Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
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
        "options": {
          "description": "Whether to download submitted attachments",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "filters": {
          "description": "A text search query based on form data - e.g. \"owner__username:meg AND name__icontains:quixotic\" - see <a href=\"https://github.com/kobotoolbox/kpi#searching\" target=\"_blank\">docs</a> for more details",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "hookId": {
          "description": "Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4)",
          "type": "string",
          "default": ""
        },
        "logId": {
          "description": "Hook log ID (starts with hl, e.g. hlSbGKaUKzTVNoWEVMYbLHe)",
          "type": "string",
          "default": ""
        },
        "status": {
          "description": "Only retrieve logs with a specific status",
          "type": "string",
          "enum": [
            "All",
            "0",
            "1",
            "2"
          ],
          "default": ""
        },
        "startDate": {
          "description": "Minimum date for the hook log to retrieve",
          "type": "string",
          "default": ""
        },
        "endDate": {
          "description": "Maximum date for the hook log to retrieve",
          "type": "string",
          "default": ""
        },
        "submissionId": {
          "description": "Submission ID (number, e.g. 245128)",
          "type": "string",
          "default": ""
        },
        "validationStatus": {
          "description": "Desired Validation Status",
          "type": "string",
          "enum": [
            "validation_status_approved",
            "validation_status_not_approved",
            "validation_status_on_hold"
          ],
          "default": ""
        },
        "filterType": {
          "description": "",
          "type": "string",
          "enum": [
            "none",
            "json"
          ],
          "default": "none"
        },
        "filterJson": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "fileId": {
          "description": "Uid of the file (should start with \"af\" e.g. \"afQoJxA4kmKEXVpkH6SYbhb\"",
          "type": "string",
          "default": ""
        },
        "binaryPropertyName": {
          "description": "Name of the binary property containing the file to upload. Supported types: image, audio, video, csv, xml, zip.",
          "type": "string",
          "default": "data"
        },
        "download": {
          "description": "Whether to download the file content into a binary property",
          "type": "boolean",
          "default": false
        },
        "fileMode": {
          "description": "",
          "type": "string",
          "enum": [
            "binary",
            "url"
          ],
          "default": "binary"
        },
        "fileUrl": {
          "description": "HTTP(s) link to the file to upload",
          "type": "string",
          "default": "",
          "format": "url"
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
      "name": "koBoToolboxApi",
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
