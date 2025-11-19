---
title: "Node: Splunk"
slug: "node-splunk"
version: "1"
updated: "2025-11-13"
summary: "Consume the Splunk Enterprise API"
node_type: "regular"
group: "['transform']"
---

# Node: Splunk

**Purpose.** Consume the Splunk Enterprise API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:splunk.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **splunkApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **oldVersionNotice**: <strong>New node version available:</strong> get the latest version with added features from the nodes panel.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `splunkApi` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an user |
| Delete | `delete` | Delete an user |
| Get | `get` | Retrieve an user |
| Get Many | `getAll` | Retrieve many users |
| Update | `update` | Update an user |

### Firedalert Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Report | `getReport` | Retrieve a fired alerts report |

### Searchconfiguration Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a search configuration |
| Get | `get` | Retrieve a search configuration |
| Get Many | `getAll` | Retrieve many search configurations |

### Searchjob Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a search job |
| Delete | `delete` | Delete a search job |
| Get | `get` | Retrieve a search job |
| Get Many | `getAll` | Retrieve many search jobs |

### Searchresult Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Retrieve many search results for a search job |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | searchJob | ✗ | Resource to operate on |  |

**Resource options:**

* **Fired Alert** (`firedAlert`)
* **Search Configuration** (`searchConfiguration`)
* **Search Job** (`searchJob`)
* **Search Result** (`searchResult`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create an user |  |

**Operation options:**

* **Create** (`create`) - Create an user
* **Delete** (`delete`) - Delete an user
* **Get** (`get`) - Retrieve an user
* **Get Many** (`getAll`) - Retrieve many users
* **Update** (`update`) - Update an user

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Login name of the user |  |
| Role Names or IDs | `roles` | multiOptions | [] | ✓ | Comma-separated list of roles to assign to the user. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Password | `password` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Full name of the user | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  |  |
| Full Name | `realname` | string |  | Full name of the user |

</details>

| Query | `search` | string |  | ✓ | Search language string to execute, in Splunk's <a href="https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual">Search Processing Language</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Seconds after which the search job automatically cancels | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Ad Hoc Search Level | `adhoc_search_level` | options | verbose |  |
| Auto-Cancel After (Seconds) | `auto_cancel` | number | 0 | Seconds after which the search job automatically cancels |
| Auto-Finalize After (Num Events) | `auto_finalize_ec` | number | 0 | Auto-finalize the search after at least this many events are processed |
| Auto Pause After (Seconds) | `auto_pause` | number | 0 | Seconds of inactivity after which the search job automatically pauses |
| Earliest Index | `index_earliest` | dateTime |  | The earliest index time for the search (inclusive) |
| Earliest Time | `earliest_time` | dateTime |  | The earliest cut-off for the search (inclusive) |
| Exec Mode | `exec_mode` | options | blocking |  |
| Indexed Real Time Offset | `indexedRealtimeOffset` | number | 0 | Seconds of disk sync delay for indexed real-time search |
| Latest Index | `index_latest` | dateTime |  | The latest index time for the search (inclusive) |
| Latest Time | `latest_time` | dateTime |  | The latest cut-off for the search (inclusive) |
| Max Time | `max_time` | number | 0 | Number of seconds to run this search before finalizing. Enter <code>0</code> to never finalize. |
| Namespace | `namespace` | string |  | Application namespace in which to restrict searches |
| Reduce Frequency | `reduce_freq` | number | 0 | How frequently to run the MapReduce reduce phase on accumulated map values |
| Remote Server List | `remote_server_list` | string |  | Comma-separated list of (possibly wildcarded) servers from which raw events should be pulled. This same server list is to be used in subsearches. |
| Reuse Limit (Seconds) | `reuse_max_seconds_ago` | number | 0 | Number of seconds ago to check when an identical search is started and return the job’s search ID instead of starting a new job |
| Required Field | `rf` | string |  | Name of a required field to add to the search. Even if not referenced or used directly by the search, a required field is still included in events and summary endpoints. |
| Search Mode | `search_mode` | options | normal |  |
| Status Buckets | `status_buckets` | number | 0 | The most status buckets to generate. Set <code>0</code> generate no timeline information. |
| Timeout | `timeout` | number | 86400 | Number of seconds to keep this search after processing has stopped |
| Workload Pool | `workload_pool` | string |  | New workload pool where the existing running search should be placed |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✓ | ID of the user to delete |  |
| Search Configuration ID | `searchConfigurationId` | string |  | ✓ | ID of the search configuration to delete |  |
| Search ID | `searchJobId` | string |  | ✓ | ID of the search job to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✓ | ID of the user to retrieve |  |
| Search Configuration ID | `searchConfigurationId` | string |  | ✓ | ID of the search configuration to retrieve |  |
| Search ID | `searchJobId` | string |  | ✓ | ID of the search job to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Options | `options` | collection | {} | ✗ | Whether to include a boolean value for each saved search to show whether the search is orphaned, meaning that it has no valid owner | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Add Orphan Field | `add_orphan_field` | boolean | False | Whether to include a boolean value for each saved search to show whether the search is orphaned, meaning that it has no valid owner |
| List Default Actions | `listDefaultActionArgs` | boolean | False |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Options | `options` | collection | {} | ✗ | Key name to use for sorting | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort Direction | `sort_dir` | options | asc |  |
| Sort Key | `sort_key` | string |  | Key name to use for sorting |
| Sort Mode | `sort_mode` | options | auto | If all field values are numeric, collate numerically. Otherwise, collate alphabetically. |

</details>

| Search ID | `searchJobId` | string |  | ✓ | ID of the search whose results to retrieve |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Key-value pair to match against. Example: if "Key" is set to <code>user</code> and "Field" is set to <code>john</code>, only the results where <code>user</code> is <code>john</code> will be returned. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Key-Value Match | `keyValueMatch` | fixedCollection | {} | Key-value pair to match against. Example: if "Key" is set to <code>user</code> and "Field" is set to <code>john</code>, only the results where <code>user</code> is <code>john</code> will be returned. |

</details>

| Options | `options` | collection | {} | ✗ | Whether to include field summary statistics in the response | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Add Summary to Metadata | `add_summary_to_metadata` | boolean | False | Whether to include field summary statistics in the response |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User ID | `userId` | string |  | ✓ | ID of the user to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Full name of the user | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  |  |
| Full Name | `realname` | string |  | Full name of the user |
| Password | `password` | string |  |  |
| Role Names or IDs | `roles` | multiOptions | [] | Comma-separated list of roles to assign to the user. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


---

## Load Options Methods

- `getRoles`

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: splunk
displayName: Splunk
description: Consume the Splunk Enterprise API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: splunkApi
  required: true
operations:
- id: create
  name: Create
  description: Create an user
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Login name of the user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: roles
    name: Role Names or IDs
    type: multiOptions
    default: []
    required: true
    description: Comma-separated list of roles to assign to the user. Choose from
      the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: multiOptions
      displayName: Role Names or IDs
      name: roles
      typeOptions:
        loadOptionsMethod: getRoles
      possibleValues: []
  - id: password
    name: Password
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo:
      type: string
      displayName: Password
      name: password
      typeOptions:
        password: true
  - id: search
    name: Query
    type: string
    default: ''
    required: true
    description: Search language string to execute, in Splunk's <a href="https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual">Search
      Processing Language</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - searchJob
          operation:
          - create
    typeInfo:
      type: string
      displayName: Query
      name: search
- id: delete
  name: Delete
  description: Delete an user
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: ID of the user to delete
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: User ID
      name: userId
  - id: searchConfigurationId
    name: Search Configuration ID
    type: string
    default: ''
    required: true
    description: ID of the search configuration to delete
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - searchConfiguration
          operation:
          - get
    typeInfo: &id004
      type: string
      displayName: Search Configuration ID
      name: searchConfigurationId
  - id: searchJobId
    name: Search ID
    type: string
    default: ''
    required: true
    description: ID of the search job to delete
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - searchResult
          operation:
          - getAll
    typeInfo: &id006
      type: string
      displayName: Search ID
      name: searchJobId
- id: get
  name: Get
  description: Retrieve an user
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: ID of the user to retrieve
    validation: *id001
    typeInfo: *id002
  - id: searchConfigurationId
    name: Search Configuration ID
    type: string
    default: ''
    required: true
    description: ID of the search configuration to retrieve
    validation: *id003
    typeInfo: *id004
  - id: searchJobId
    name: Search ID
    type: string
    default: ''
    required: true
    description: ID of the search job to retrieve
    validation: *id005
    typeInfo: *id006
- id: getAll
  name: Get Many
  description: Retrieve many users
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id007
      displayOptions:
        show:
          resource:
          - searchResult
          operation:
          - getAll
    typeInfo: &id008
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id009
      displayOptions:
        show:
          resource:
          - searchResult
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id010
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id007
    typeInfo: *id008
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id007
    typeInfo: *id008
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
  - id: searchJobId
    name: Search ID
    type: string
    default: ''
    required: true
    description: ID of the search whose results to retrieve
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id007
    typeInfo: *id008
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id009
    typeInfo: *id010
- id: update
  name: Update
  description: Update an user
  params:
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: ID of the user to update
    validation: *id001
    typeInfo: *id002
- id: getReport
  name: Get Report
  description: Retrieve a fired alerts report
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices:
  - name: oldVersionNotice
    text: <strong>New node version available:</strong> get the latest version with
      added features from the nodes panel.
    conditions: null
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/splunk.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Splunk Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "get",
        "getAll",
        "update",
        "getReport"
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
            "firedAlert",
            "searchConfiguration",
            "searchJob",
            "searchResult",
            "user"
          ],
          "default": "searchJob"
        },
        "operation": {
          "description": "Retrieve many search results for a search job",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "getAll"
        },
        "name": {
          "description": "Login name of the user",
          "type": "string",
          "default": ""
        },
        "roles": {
          "description": "Comma-separated list of roles to assign to the user. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "password": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Seconds after which the search job automatically cancels",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "userId": {
          "description": "ID of the user to update",
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
          "default": 50
        },
        "updateFields": {
          "description": "Full name of the user",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "searchConfigurationId": {
          "description": "ID of the search configuration to retrieve",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Whether to include field summary statistics in the response",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "search": {
          "description": "Search language string to execute, in Splunk's <a href=\"https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual\">Search Processing Language</a>",
          "type": "string",
          "default": ""
        },
        "searchJobId": {
          "description": "ID of the search whose results to retrieve",
          "type": "string",
          "default": ""
        },
        "filters": {
          "description": "Key-value pair to match against. Example: if \"Key\" is set to <code>user</code> and \"Field\" is set to <code>john</code>, only the results where <code>user</code> is <code>john</code> will be returned.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
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
      "name": "splunkApi",
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
