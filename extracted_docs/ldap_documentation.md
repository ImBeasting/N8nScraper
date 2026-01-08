---
title: "Node: Ldap"
slug: "node-ldap"
version: "1"
updated: "2026-01-08"
summary: "Interact with LDAP servers"
node_type: "regular"
group: "['transform']"
---

# Node: Ldap

**Purpose.** Interact with LDAP servers
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:ldap.svg', 'dark': 'file:ldap.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **ldap**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `ldap` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Compare | `compare` | Compare an attribute |
| Create | `create` | Create a new entry |
| Delete | `delete` | Delete an entry |
| Rename | `rename` | Rename the DN of an existing entry |
| Search | `search` | Search LDAP |
| Update | `update` | Update attributes |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | search | ✗ | Compare an attribute |  |

**Operation options:**

* **Compare** (`compare`) - Compare an attribute
* **Create** (`create`) - Create a new entry
* **Delete** (`delete`) - Delete an entry
* **Rename** (`rename`) - Rename the DN of an existing entry
* **Search** (`search`) - Search LDAP
* **Update** (`update`) - Update attributes

---

### Compare parameters (`compare`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| DN | `dn` | string |  | ✓ | The distinguished name of the entry to compare | e.g. e.g. ou=users,dc=n8n,dc=io |  |
| Attribute ID | `id` | options | [] | ✓ | The ID of the attribute to compare |  |
| Value | `value` | string |  | ✗ | The value to compare |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| DN | `dn` | string |  | ✓ | The distinguished name of the entry to create | e.g. e.g. ou=users,dc=n8n,dc=io |  |
| Attributes | `attributes` | fixedCollection | {} | ✓ | Attributes to add to the entry | e.g. Add Attributes |  |

<details>
<summary><strong>Attributes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attribute | `attribute` |  |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| DN | `dn` | string |  | ✓ | The distinguished name of the entry to delete | e.g. e.g. ou=users,dc=n8n,dc=io |  |

### Rename parameters (`rename`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| DN | `dn` | string |  | ✓ | The distinguished name of the entry to rename | e.g. e.g. cn=john,ou=users,dc=n8n,dc=io |  |
| New DN | `targetDn` | string |  | ✓ | The new distinguished name for the entry | e.g. e.g. cn=nathan,ou=users,dc=n8n,dc=io |  |

### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Base DN | `baseDN` | string |  | ✓ | The distinguished name of the subtree to search in | e.g. e.g. ou=users, dc=n8n, dc=io |  |
| Search For | `searchFor` | options | [] | ✗ | Directory object class to search for |  |
| Custom Filter | `customFilter` | string | (objectclass=*) | ✗ | Custom LDAP filter. Escape these chars * ( ) \ with a backslash "\". |  |
| Attribute | `attribute` | options | [] | ✓ | Attribute to search for |  |
| Search Text | `searchText` | string |  | ✓ | Text to search for, Use * for a wildcard |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Options | `options` | collection | {} | ✗ | Comma-separated list of attributes to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attribute Names or IDs | `attributes` | multiOptions | [] | Comma-separated list of attributes to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Page Size | `pageSize` | number | 1000 | Maximum number of results to request at one time. Set to 0 to disable paging. |
| Scope | `scope` | options | sub | The set of entries at or below the BaseDN that may be considered potential matches |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| DN | `dn` | string |  | ✓ | The distinguished name of the entry to update | e.g. e.g. ou=users,dc=n8n,dc=io |  |
| Update Attributes | `attributes` | fixedCollection | {} | ✓ | Update entry attributes | e.g. Update Attributes |  |

<details>
<summary><strong>Update Attributes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Add | `add` |  |  |  |
| Replace | `replace` |  |  |  |
| Remove | `delete` |  |  |  |

</details>


---

## Load Options Methods

- `getAttributes`

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
* Categories: Development, Developer Tools
* Aliases: ad, active directory

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: ldap
displayName: Ldap
description: Interact with LDAP servers
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: ldap
  required: true
operations:
- id: compare
  name: Compare
  description: Compare an attribute
  params:
  - id: dn
    name: DN
    type: string
    default: ''
    required: true
    description: The distinguished name of the entry to compare
    placeholder: e.g. ou=users,dc=n8n,dc=io
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: DN
      name: dn
      typeOptions:
        alwaysOpenEditWindow: false
  - id: id
    name: Attribute ID
    type: options
    default: []
    required: true
    description: The ID of the attribute to compare
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - compare
    typeInfo:
      type: options
      displayName: Attribute ID
      name: id
      typeOptions:
        loadOptionsMethod: getAttributesForDn
      possibleValues: []
  - id: value
    name: Value
    type: string
    default: ''
    required: false
    description: The value to compare
    validation:
      displayOptions:
        show:
          operation:
          - compare
    typeInfo:
      type: string
      displayName: Value
      name: value
- id: create
  name: Create
  description: Create a new entry
  params:
  - id: dn
    name: DN
    type: string
    default: ''
    required: true
    description: The distinguished name of the entry to create
    placeholder: e.g. ou=users,dc=n8n,dc=io
    validation: *id001
    typeInfo: *id002
  - id: attributes
    name: Attributes
    type: fixedCollection
    default: {}
    required: true
    description: Attributes to add to the entry
    placeholder: Add Attributes
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - update
    typeInfo: &id004
      type: fixedCollection
      displayName: Update Attributes
      name: attributes
      typeOptions:
        multipleValues: true
      subProperties:
      - name: add
        displayName: Add
        values:
        - displayName: Attribute ID
          name: id
          type: string
          description: The ID of the attribute to add
          default: ''
          required: true
        - displayName: Value
          name: value
          type: string
          description: Value of the attribute to set
          default: ''
      - name: replace
        displayName: Replace
        values:
        - displayName: Attribute ID
          name: id
          type: string
          description: The ID of the attribute to replace
          default: ''
          required: true
        - displayName: Value
          name: value
          type: string
          description: Value of the attribute to replace
          default: ''
      - name: delete
        displayName: Remove
        values:
        - displayName: Attribute ID
          name: id
          type: string
          description: The ID of the attribute to remove
          default: ''
          required: true
        - displayName: Value
          name: value
          type: string
          description: Value of the attribute to remove
          default: ''
- id: delete
  name: Delete
  description: Delete an entry
  params:
  - id: dn
    name: DN
    type: string
    default: ''
    required: true
    description: The distinguished name of the entry to delete
    placeholder: e.g. ou=users,dc=n8n,dc=io
    validation: *id001
    typeInfo: *id002
- id: rename
  name: Rename
  description: Rename the DN of an existing entry
  params:
  - id: dn
    name: DN
    type: string
    default: ''
    required: true
    description: The distinguished name of the entry to rename
    placeholder: e.g. cn=john,ou=users,dc=n8n,dc=io
    validation: *id001
    typeInfo: *id002
  - id: targetDn
    name: New DN
    type: string
    default: ''
    required: true
    description: The new distinguished name for the entry
    placeholder: e.g. cn=nathan,ou=users,dc=n8n,dc=io
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - rename
    typeInfo:
      type: string
      displayName: New DN
      name: targetDn
- id: search
  name: Search
  description: Search LDAP
  params:
  - id: baseDN
    name: Base DN
    type: string
    default: ''
    required: true
    description: The distinguished name of the subtree to search in
    placeholder: e.g. ou=users, dc=n8n, dc=io
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - search
    typeInfo:
      type: string
      displayName: Base DN
      name: baseDN
  - id: searchFor
    name: Search For
    type: options
    default: []
    required: false
    description: Directory object class to search for
    validation:
      displayOptions:
        show:
          operation:
          - search
    typeInfo:
      type: options
      displayName: Search For
      name: searchFor
      typeOptions:
        loadOptionsMethod: getObjectClasses
      possibleValues: []
  - id: customFilter
    name: Custom Filter
    type: string
    default: (objectclass=*)
    required: false
    description: Custom LDAP filter. Escape these chars * ( ) \ with a backslash "\".
    validation:
      displayOptions:
        show:
          operation:
          - search
          searchFor:
          - custom
    typeInfo:
      type: string
      displayName: Custom Filter
      name: customFilter
  - id: attribute
    name: Attribute
    type: options
    default: []
    required: true
    description: Attribute to search for
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - search
        hide:
          searchFor:
          - custom
    typeInfo:
      type: options
      displayName: Attribute
      name: attribute
      typeOptions:
        loadOptionsMethod: getAttributes
      possibleValues: []
  - id: searchText
    name: Search Text
    type: string
    default: ''
    required: true
    description: Text to search for, Use * for a wildcard
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - search
        hide:
          searchFor:
          - custom
    typeInfo:
      type: string
      displayName: Search Text
      name: searchText
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation:
      displayOptions:
        show:
          operation:
          - search
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - search
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
- id: update
  name: Update
  description: Update attributes
  params:
  - id: dn
    name: DN
    type: string
    default: ''
    required: true
    description: The distinguished name of the entry to update
    placeholder: e.g. ou=users,dc=n8n,dc=io
    validation: *id001
    typeInfo: *id002
  - id: attributes
    name: Update Attributes
    type: fixedCollection
    default: {}
    required: true
    description: Update entry attributes
    placeholder: Update Attributes
    validation: *id003
    typeInfo: *id004
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: dn
    text: e.g. ou=users,dc=n8n,dc=io
  - field: dn
    text: e.g. ou=users,dc=n8n,dc=io
  - field: dn
    text: e.g. ou=users,dc=n8n,dc=io
  - field: dn
    text: e.g. cn=john,ou=users,dc=n8n,dc=io
  - field: dn
    text: e.g. ou=users,dc=n8n,dc=io
  - field: dn
    text: e.g. ou=users,dc=n8n,dc=io
  - field: targetDn
    text: e.g. cn=nathan,ou=users,dc=n8n,dc=io
  - field: attributes
    text: Add Attributes
  - field: attributes
    text: Update Attributes
  - field: baseDN
    text: e.g. ou=users, dc=n8n, dc=io
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
  "$id": "https://n8n.io/schemas/nodes/ldap.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Ldap Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "compare",
        "create",
        "delete",
        "rename",
        "search",
        "update"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Compare an attribute",
          "type": "string",
          "enum": [
            "compare",
            "create",
            "delete",
            "rename",
            "search",
            "update"
          ],
          "default": "search"
        },
        "nodeDebug": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "dn": {
          "description": "The distinguished name of the entry to update",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. ou=users,dc=n8n,dc=io"
          ]
        },
        "id": {
          "description": "The ID of the attribute to compare",
          "type": "string",
          "default": []
        },
        "value": {
          "description": "The value to compare",
          "type": "string",
          "default": ""
        },
        "targetDn": {
          "description": "The new distinguished name for the entry",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. cn=nathan,ou=users,dc=n8n,dc=io"
          ]
        },
        "attributes": {
          "description": "Update entry attributes",
          "type": "string",
          "default": {},
          "examples": [
            "Update Attributes"
          ]
        },
        "baseDN": {
          "description": "The distinguished name of the subtree to search in",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. ou=users, dc=n8n, dc=io"
          ]
        },
        "searchFor": {
          "description": "Directory object class to search for",
          "type": "string",
          "default": []
        },
        "customFilter": {
          "description": "Custom LDAP filter. Escape these chars * ( ) \\ with a backslash \"\\\".",
          "type": "string",
          "default": "(objectclass=*)"
        },
        "attribute": {
          "description": "Attribute to search for",
          "type": "string",
          "default": []
        },
        "searchText": {
          "description": "Text to search for, Use * for a wildcard",
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
        "options": {
          "description": "Comma-separated list of attributes to return. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
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
      "name": "ldap",
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
