---
title: "Node: AWS ELB"
slug: "node-awselb"
version: "1"
updated: "2025-11-13"
summary: "Sends data to AWS ELB API"
node_type: "regular"
group: "['output']"
---

# Node: AWS ELB

**Purpose.** Sends data to AWS ELB API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:elb.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **aws**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `aws` | ✓ | - |

---

## Operations

### Loadbalancer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a load balancer |
| Delete | `delete` | Delete a load balancer |
| Get | `get` | Get a load balancer |
| Get Many | `getMany` | Get many load balancers |

### Listenercertificate Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add the specified SSL server certificate to the certificate list for the specified HTTPS or TLS listener |
| Get Many | `getMany` | Get many listener certificates |
| Remove | `remove` | Remove the specified certificate from the certificate list for the specified HTTPS or TLS listener |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | loadBalancer | ✗ | Resource to operate on |  |

**Resource options:**

* **Listener Certificate** (`listenerCertificate`)
* **Load Balancer** (`loadBalancer`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a load balancer |  |

**Operation options:**

* **Create** (`create`) - Create a load balancer
* **Delete** (`delete`) - Delete a load balancer
* **Get** (`get`) - Get a load balancer
* **Get Many** (`getMany`) - Get many load balancers

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| IP Address Type | `ipAddressType` | options | ipv4 | ✓ | The type of IP addresses used by the subnets for your load balancer |  |

**IP Address Type options:**

* **Ipv4** (`ipv4`)
* **Dualstack** (`dualstack`)

| Name | `name` | string |  | ✓ | This name must be unique per region per account, can have a maximum of 32 characters |  |
| Schema | `schema` | options | internet-facing | ✓ |  |  |

**Schema options:**

* **Internal** (`internal`)
* **Internet Facing** (`internet-facing`)

| Type | `type` | options | application | ✓ |  |  |

**Type options:**

* **Application** (`application`)
* **Network** (`network`)

| Subnet ID Names or IDs | `subnets` | multiOptions | [] | ✓ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Security Group IDs | `securityGroups` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Tags | `tagsUi` | fixedCollection | {} | The key of the tag |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Load Balancer ARN | `loadBalancerId` | string |  | ✓ | ID of loadBalancer to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Load Balancer ARN | `loadBalancerId` | string |  | ✓ | Unique identifier for a particular loadBalancer |  |

### Get Many parameters (`getMany`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:400 |
| Filters | `filters` | collection | {} | ✗ | The names of the load balancers. Multiples can be defined separated by comma. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Names | `names` | string |  | The names of the load balancers. Multiples can be defined separated by comma. |

</details>

| Load Balancer ARN Name or ID | `loadBalancerId` | options |  | ✓ | Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Listener ARN Name or ID | `listenerId` | options |  | ✓ | Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:400 |

### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Load Balancer ARN Name or ID | `loadBalancerId` | options |  | ✓ | Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Listener ARN Name or ID | `listenerId` | options |  | ✓ | Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Certificate ARN | `certificateId` | string |  | ✓ | Unique identifier for a particular loadBalancer |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Load Balancer ARN Name or ID | `loadBalancerId` | options |  | ✓ | Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Listener ARN Name or ID | `listenerId` | options |  | ✓ | Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Certificate ARN | `certificateId` | string |  | ✓ | Unique identifier for a particular loadBalancer |  |

---

## Load Options Methods

- `getLoadBalancers`
- `if`

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: awsElb
displayName: AWS ELB
description: Sends data to AWS ELB API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: aws
  required: true
operations:
- id: create
  name: Create
  description: Create a load balancer
  params:
  - id: ipAddressType
    name: IP Address Type
    type: options
    default: ipv4
    required: true
    description: The type of IP addresses used by the subnets for your load balancer
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - loadBalancer
          operation:
          - create
    typeInfo:
      type: options
      displayName: IP Address Type
      name: ipAddressType
      possibleValues:
      - value: ipv4
        name: Ipv4
        description: ''
      - value: dualstack
        name: Dualstack
        description: ''
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: This name must be unique per region per account, can have a maximum
      of 32 characters
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - loadBalancer
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: schema
    name: Schema
    type: options
    default: internet-facing
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - loadBalancer
          operation:
          - create
    typeInfo:
      type: options
      displayName: Schema
      name: schema
      possibleValues:
      - value: internal
        name: Internal
        description: ''
      - value: internet-facing
        name: Internet Facing
        description: ''
  - id: type
    name: Type
    type: options
    default: application
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - loadBalancer
          operation:
          - create
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: application
        name: Application
        description: ''
      - value: network
        name: Network
        description: ''
  - id: subnets
    name: Subnet ID Names or IDs
    type: multiOptions
    default: []
    required: true
    description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - loadBalancer
          operation:
          - create
    typeInfo:
      type: multiOptions
      displayName: Subnet ID Names or IDs
      name: subnets
      typeOptions:
        loadOptionsMethod: getSubnets
      possibleValues: []
- id: delete
  name: Delete
  description: Delete a load balancer
  params:
  - id: loadBalancerId
    name: Load Balancer ARN
    type: string
    default: ''
    required: true
    description: ID of loadBalancer to delete
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - listenerCertificate
          operation:
          - remove
    typeInfo: &id002
      type: options
      displayName: Load Balancer ARN Name or ID
      name: loadBalancerId
      typeOptions:
        loadOptionsMethod: getLoadBalancers
      possibleValues: []
- id: get
  name: Get
  description: Get a load balancer
  params:
  - id: loadBalancerId
    name: Load Balancer ARN
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular loadBalancer
    validation: *id001
    typeInfo: *id002
- id: getMany
  name: Get Many
  description: Get many load balancers
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          resource:
          - listenerCertificate
          operation:
          - getMany
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - listenerCertificate
          operation:
          - getMany
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 400
  - id: loadBalancerId
    name: Load Balancer ARN Name or ID
    type: options
    default: ''
    required: true
    description: Unique identifier for a particular loadBalancer. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: listenerId
    name: Listener ARN Name or ID
    type: options
    default: ''
    required: true
    description: Unique identifier for a particular loadBalancer. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - listenerCertificate
          operation:
          - remove
    typeInfo: &id008
      type: options
      displayName: Listener ARN Name or ID
      name: listenerId
      typeOptions:
        loadOptionsMethod: getLoadBalancerListeners
      possibleValues: []
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
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
- id: add
  name: Add
  description: Add the specified SSL server certificate to the certificate list for
    the specified HTTPS or TLS listener
  params:
  - id: loadBalancerId
    name: Load Balancer ARN Name or ID
    type: options
    default: ''
    required: true
    description: Unique identifier for a particular loadBalancer. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: listenerId
    name: Listener ARN Name or ID
    type: options
    default: ''
    required: true
    description: Unique identifier for a particular loadBalancer. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: certificateId
    name: Certificate ARN
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular loadBalancer
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - listenerCertificate
          operation:
          - remove
    typeInfo: &id010
      type: string
      displayName: Certificate ARN
      name: certificateId
- id: remove
  name: Remove
  description: Remove the specified certificate from the certificate list for the
    specified HTTPS or TLS listener
  params:
  - id: loadBalancerId
    name: Load Balancer ARN Name or ID
    type: options
    default: ''
    required: true
    description: Unique identifier for a particular loadBalancer. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: listenerId
    name: Listener ARN Name or ID
    type: options
    default: ''
    required: true
    description: Unique identifier for a particular loadBalancer. Choose from the
      list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: certificateId
    name: Certificate ARN
    type: string
    default: ''
    required: true
    description: Unique identifier for a particular loadBalancer
    validation: *id009
    typeInfo: *id010
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/awsElb.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AWS ELB Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "get",
        "getMany",
        "add",
        "remove"
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
            "listenerCertificate",
            "loadBalancer"
          ],
          "default": "loadBalancer"
        },
        "operation": {
          "description": "Add the specified SSL server certificate to the certificate list for the specified HTTPS or TLS listener",
          "type": "string",
          "enum": [
            "add",
            "getMany",
            "remove"
          ],
          "default": "add"
        },
        "ipAddressType": {
          "description": "The type of IP addresses used by the subnets for your load balancer",
          "type": "string",
          "enum": [
            "ipv4",
            "dualstack"
          ],
          "default": "ipv4"
        },
        "name": {
          "description": "This name must be unique per region per account, can have a maximum of 32 characters",
          "type": "string",
          "default": ""
        },
        "schema": {
          "description": "",
          "type": "string",
          "enum": [
            "internal",
            "internet-facing"
          ],
          "default": "internet-facing"
        },
        "type": {
          "description": "",
          "type": "string",
          "enum": [
            "application",
            "network"
          ],
          "default": "application"
        },
        "subnets": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "additionalFields": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "loadBalancerId": {
          "description": "Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
        "filters": {
          "description": "The names of the load balancers. Multiples can be defined separated by comma.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "listenerId": {
          "description": "Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "certificateId": {
          "description": "Unique identifier for a particular loadBalancer",
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
      "name": "aws",
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
