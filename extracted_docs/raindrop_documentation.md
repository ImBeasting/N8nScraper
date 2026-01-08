---
title: "Node: Raindrop"
slug: "node-raindrop"
version: "1"
updated: "2026-01-08"
summary: "Consume the Raindrop API"
node_type: "regular"
group: "['transform']"
---

# Node: Raindrop

**Purpose.** Consume the Raindrop API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:raindrop.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **raindropOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `raindropOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** user-agent, Content-Type

---

## Operations

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a user |

### Bookmark Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a bookmark |
| Delete | `delete` | Delete a bookmark |
| Get | `get` | Get a bookmark |
| Get Many | `getAll` | Get many bookmarks |
| Update | `update` | Update a bookmark |

### Collection Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a collection |
| Delete | `delete` | Delete a collection |
| Get | `get` | Get a collection |
| Get Many | `getAll` | Get many collections |
| Update | `update` | Update a collection |

### Tag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a tag |
| Get Many | `getAll` | Get many tags |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | collection | ✗ | Resource to operate on |  |

**Resource options:**

* **Bookmark** (`bookmark`)
* **Collection** (`collection`)
* **Tag** (`tag`)
* **User** (`user`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Operation to perform |  |

**Operation options:**

* **Get** (`get`) - Get a user

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Self | `self` | boolean | True | ✓ | Whether to return details on the logged-in user |  |
| User ID | `userId` | string |  | ✓ | The ID of the user to retrieve |  |
| Bookmark ID | `bookmarkId` | string |  | ✓ | The ID of the bookmark to retrieve |  |
| Collection ID | `collectionId` | string |  | ✓ | The ID of the collection to retrieve |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Collection Name or ID | `collectionId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Link | `link` | string |  | ✓ | Link of the bookmark to be created |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether this bookmark is marked as favorite | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Important | `important` | boolean | False | Whether this bookmark is marked as favorite |
| Order | `order` | number | 0 | Sort order for the bookmark. For example, to move it to first place, enter 0. |
| Parse Metadata | `pleaseParse` | boolean | False | Whether Raindrop should load cover, description and HTML for the URL |
| Tags | `tags` | string |  | Bookmark tags. Multiple tags can be set separated by comma. |
| Title | `title` | string |  | Title of the bookmark to create |

</details>

| Title | `title` | string |  | ✓ | Title of the collection to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | URL of an image to use as cover for the collection | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Cover | `cover` | string |  | URL of an image to use as cover for the collection |
| Public | `public` | boolean | False | Whether the collection will be accessible without authentication |
| Parent ID | `parentId` | string |  | ID of this collection's parent collection, if it is a child collection |
| Sort Order | `sort` | number | 1 | Descending sort order of this collection. The number is the position of the collection among all the collections with the same parent ID. |
| View | `view` | options | list | View style of this collection |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bookmark ID | `bookmarkId` | string |  | ✓ | The ID of the bookmark to delete |  |
| Collection ID | `collectionId` | string |  | ✓ | The ID of the collection to delete |  |
| Tags | `tags` | string |  | ✓ | One or more tags to delete. Enter comma-separated values to delete multiple tags. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | It's possible to restrict remove action to just one collection. It's optional. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Collection Name or ID | `collectionId` | options |  | It's possible to restrict remove action to just one collection. It's optional. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Collection Name or ID | `collectionId` | options | [] | ✓ | The ID of the collection from which to retrieve all bookmarks. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Type | `type` | options | parent | ✓ | Root-level collections |  |

**Type options:**

* **Parent** (`parent`) - Root-level collections
* **Children** (`children`) - Nested collections

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 5 | ✗ | Max number of results to return | min:1, max:10 |
| Filters | `filters` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Collection Name or ID | `collectionId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bookmark ID | `bookmarkId` | string |  | ✓ | The ID of the bookmark to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Collection Name or ID | `collectionId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Important | `important` | boolean | False | Whether this bookmark is marked as favorite |
| Order | `order` | number | 0 | For example if you want to move bookmark to the first place set this field to 0 |
| Parse Metadata | `pleaseParse` | boolean | False | Whether Raindrop should reload cover, description and HTML for the URL |
| Tags | `tags` | string |  | Bookmark tags. Multiple tags can be set separated by comma. |
| Title | `title` | string |  | Title of the bookmark to be created |

</details>

| Collection ID | `collectionId` | string |  | ✓ | The ID of the collection to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Name of the binary property containing the data for the image to upload as a cover | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Cover | `cover` | string | data | Name of the binary property containing the data for the image to upload as a cover |
| Public | `public` | boolean | False | Whether the collection will be accessible without authentication |
| Parent ID | `parentId` | string |  | ID of this collection's parent collection, if it is a child collection |
| Sort Order | `sort` | number | 1 | Descending sort order of this collection. The number is the position of the collection among all the collections with the same parent ID. |
| Title | `title` | string |  | Title of the collection to update |
| View | `view` | options | list | View style of this collection |

</details>


---

## Load Options Methods

- `getCollections`

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
* Categories: Productivity

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: raindrop
displayName: Raindrop
description: Consume the Raindrop API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: raindropOAuth2Api
  required: true
operations:
- id: get
  name: Get
  description: ''
  params:
  - id: self
    name: Self
    type: boolean
    default: true
    required: true
    description: Whether to return details on the logged-in user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
    typeInfo:
      type: boolean
      displayName: Self
      name: self
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: The ID of the user to retrieve
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
          self:
          - false
    typeInfo:
      type: string
      displayName: User ID
      name: userId
  - id: bookmarkId
    name: Bookmark ID
    type: string
    default: ''
    required: true
    description: The ID of the bookmark to retrieve
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - bookmark
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Bookmark ID
      name: bookmarkId
  - id: collectionId
    name: Collection ID
    type: string
    default: ''
    required: true
    description: The ID of the collection to retrieve
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - collection
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: Collection ID
      name: collectionId
- id: create
  name: Create
  description: ''
  params:
  - id: collectionId
    name: Collection Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: link
    name: Link
    type: string
    default: ''
    required: true
    description: Link of the bookmark to be created
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - bookmark
          operation:
          - create
    typeInfo:
      type: string
      displayName: Link
      name: link
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the collection to create
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - collection
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
- id: delete
  name: Delete
  description: ''
  params:
  - id: bookmarkId
    name: Bookmark ID
    type: string
    default: ''
    required: true
    description: The ID of the bookmark to delete
    validation: *id003
    typeInfo: *id004
  - id: collectionId
    name: Collection ID
    type: string
    default: ''
    required: true
    description: The ID of the collection to delete
    validation: *id001
    typeInfo: *id002
  - id: tags
    name: Tags
    type: string
    default: ''
    required: true
    description: One or more tags to delete. Enter comma-separated values to delete
      multiple tags.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - delete
    typeInfo:
      type: string
      displayName: Tags
      name: tags
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: collectionId
    name: Collection Name or ID
    type: options
    default: []
    required: true
    description: The ID of the collection from which to retrieve all bookmarks. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id005
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - getAll
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          resource:
          - tag
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id008
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 10
  - id: type
    name: Type
    type: options
    default: parent
    required: true
    description: Root-level collections
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - collection
          operation:
          - getAll
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: parent
        name: Parent
        description: Root-level collections
      - value: children
        name: Children
        description: Nested collections
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 5
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: update
  name: Update
  description: ''
  params:
  - id: bookmarkId
    name: Bookmark ID
    type: string
    default: ''
    required: true
    description: The ID of the bookmark to update
    validation: *id003
    typeInfo: *id004
  - id: collectionId
    name: Collection ID
    type: string
    default: ''
    required: true
    description: The ID of the collection to update
    validation: *id001
    typeInfo: *id002
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - user-agent
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Filter
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/raindrop.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Raindrop Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "create",
        "delete",
        "getAll",
        "update"
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
            "bookmark",
            "collection",
            "tag",
            "user"
          ],
          "default": "collection"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "delete",
            "getAll"
          ],
          "default": "get"
        },
        "self": {
          "description": "Whether to return details on the logged-in user",
          "type": "boolean",
          "default": true
        },
        "userId": {
          "description": "The ID of the user to retrieve",
          "type": "string",
          "default": ""
        },
        "collectionId": {
          "description": "The ID of the collection to update",
          "type": "string",
          "default": ""
        },
        "link": {
          "description": "Link of the bookmark to be created",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "It's possible to restrict remove action to just one collection. It's optional. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "bookmarkId": {
          "description": "The ID of the bookmark to update",
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
          "default": 5
        },
        "updateFields": {
          "description": "Name of the binary property containing the data for the image to upload as a cover",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "title": {
          "description": "Title of the collection to create",
          "type": "string",
          "default": ""
        },
        "type": {
          "description": "Root-level collections",
          "type": "string",
          "enum": [
            "parent",
            "children"
          ],
          "default": "parent"
        },
        "tags": {
          "description": "One or more tags to delete. Enter comma-separated values to delete multiple tags.",
          "type": "string",
          "default": ""
        },
        "filters": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
      "name": "raindropOAuth2Api",
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
