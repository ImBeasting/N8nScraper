---
title: "Node: Elasticsearch"
slug: "node-elasticsearch"
version: "1"
updated: "2026-01-08"
summary: "Consume the Elasticsearch API"
node_type: "regular"
group: "['transform']"
---

# Node: Elasticsearch

**Purpose.** Consume the Elasticsearch API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:elasticsearch.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **elasticsearchApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **paginateNotice** when resource=['document'], operation=['getAll'], returnAll=[True]: By default, you cannot page through more than 10,000 hits. To page through more hits, add "Sort" from options.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `elasticsearchApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** POST

**Headers Used:** Content-Type

---

## Operations

### Index Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an index |
| Delete | `delete` | Delete an index |
| Get | `get` | Get an index |
| Get Many | `getAll` | Get many indices |

### Document Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a document |
| Delete | `delete` | Delete a document |
| Get | `get` | Get a document |
| Get Many | `getAll` | Get many documents |
| Update | `update` | Update a document |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | document | ✗ | Resource to operate on |  |

**Resource options:**

* **Document** (`document`)
* **Index** (`index`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create an index
* **Delete** (`delete`) - Delete an index
* **Get** (`get`) - Get an index
* **Get Many** (`getAll`) - Get many indices

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Index ID | `indexId` | string |  | ✓ | ID of the index to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Index aliases which include the index, as an <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-aliases.html">alias object</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Aliases | `aliases` | json |  | Index aliases which include the index, as an <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-aliases.html">alias object</a> |
| Include Type Name | `include_type_name` | boolean | False | Whether a mapping type is expected in the body of mappings. Defaults to false. |
| Mappings | `mappings` | json |  | Mapping for fields in the index, as <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html">mapping object</a> |
| Master Timeout | `master_timeout` | string | 1m | Period to wait for a connection to the master node. If no response is received before the timeout expires, the request fails and returns an error. Defaults to <code>1m</code>. See the <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#time-units">Elasticsearch time units reference</a> |
| Settings | `settings` | json |  | Configuration options for the index, as an <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules.html#index-modules-settings">index settings object</a> |
| Timeout | `timeout` | string | 30s | Period to wait for a response. If no response is received before the timeout expires, the request fails and returns an error. Defaults to <code>30s</code>. See the <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#time-units">Elasticsearch time units reference</a> |
| Wait for Active Shards | `wait_for_active_shards` | string | 1 | The number of shard copies that must be active before proceeding with the operation. Set to <code>all</code> or any positive integer up to the total number of shards in the index. Default: 1, the primary shard |

</details>

| Index ID | `indexId` | string |  | ✓ | ID of the index to add the document to |  |
| Data to Send | `dataToSend` | options | defineBelow | ✗ | Set the value for each destination column |  |

**Data to Send options:**

* **Define Below for Each Column** (`defineBelow`) - Set the value for each destination column
* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Fields to Send | `fieldsUi` | fixedCollection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `fieldValues` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the document to create and add to the index | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Document ID | `documentId` | string |  | ID of the document to create and add to the index |
| Routing | `routing` | string |  | Target this primary shard |
| Timeout | `timeout` | string | 1m | Period to wait for active shards. Defaults to <code>1m</code> (one minute). See the <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#time-units">Elasticsearch time units reference</a> |

</details>

| Options | `options` | collection | {} | ✗ | Whether to use the bulk operation to create the document/s | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Bulk Create | `bulkOperation` | boolean | False | Whether to use the bulk operation to create the document/s |
| Pipeline ID | `pipeline` | string |  | ID of the pipeline to use to preprocess incoming documents |
| Refresh | `refresh` | options | false | If true, Elasticsearch refreshes the affected shards to make this operation visible to search,if wait_for then wait for a refresh to make this operation visible to search,if false do nothing with refreshes |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Index ID | `indexId` | string |  | ✓ | ID of the index to delete |  |
| Index ID | `indexId` | string |  | ✓ | ID of the index containing the document to delete |  |
| Document ID | `documentId` | string |  | ✓ | ID of the document to delete |  |
| Options | `options` | collection | {} | ✗ | Whether to use the bulk operation to delete the document/s | e.g. Add Option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Bulk Delete | `bulkOperation` | boolean | False | Whether to use the bulk operation to delete the document/s |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Index ID | `indexId` | string |  | ✓ | ID of the index to retrieve |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | If false, return an error if any of the following targets only missing/closed indices: wildcard expression, index alias, or <code>_all</code> value. Defaults to true. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Allow No Indices | `allow_no_indices` | boolean | True | If false, return an error if any of the following targets only missing/closed indices: wildcard expression, index alias, or <code>_all</code> value. Defaults to true. |
| Expand Wildcards | `expand_wildcards` | options | all | Type of index that wildcard expressions can match. Defaults to <code>open</code> |
| Flat Settings | `flat_settings` | boolean | False | Whether to return settings in flat format. Defaults to false. |
| Ignore Unavailable | `ignore_unavailable` | boolean | False | Whether to request that target a missing index return an error. Defaults to false. |
| Include Defaults | `include_defaults` | boolean | False | Whether to return all default settings in the response. Defaults to false. |
| Local | `local` | boolean | False | Whether to retrieve information from the local node only. Defaults to false. |
| Master Timeout | `master_timeout` | string | 1m | Period to wait for a connection to the master node. If no response is received before the timeout expires, the request fails and returns an error. Defaults to <code>1m</code>. See the <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#time-units">Elasticsearch time units reference</a> |

</details>

| Index ID | `indexId` | string |  | ✓ | ID of the index containing the document to retrieve |  |
| Document ID | `documentId` | string |  | ✓ | ID of the document to retrieve |  |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Comma-separated list of source fields to exclude from the response | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Source Excludes | `_source_excludes` | string |  | Comma-separated list of source fields to exclude from the response |
| Source Includes | `_source_includes` | string |  | Comma-separated list of source fields to include in the response |
| Stored Fields | `stored_fields` | boolean | False | Whether to retrieve the document fields stored in the index rather than the document <code>_source</code>. Defaults to false. |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Index ID | `indexId` | string |  | ✓ | ID of the index containing the documents to retrieve |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | If false, return an error if any of the following targets only missing/closed indices: wildcard expression, index alias, or <code>_all</code> value. Defaults to true. | e.g. Add option | min:2, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Allow No Indices | `allow_no_indices` | boolean | True | If false, return an error if any of the following targets only missing/closed indices: wildcard expression, index alias, or <code>_all</code> value. Defaults to true. |
| Allow Partial Search Results | `allow_partial_search_results` | boolean | True | <p>If true, return partial results if there are shard request timeouts or shard failures.</p><p>If false, returns an error with no partial results. Defaults to true.</p>. |
| Batched Reduce Size | `batched_reduce_size` | number | 512 | Number of shard results that should be reduced at once on the coordinating node. Defaults to 512. |
| CCS Minimize Roundtrips | `ccs_minimize_roundtrips` | boolean | True | Whether network round-trips between the coordinating node and the remote clusters are minimized when executing cross-cluster search (CCS) requests. Defaults to true. |
| Doc Value Fields | `docvalue_fields` | string |  | Comma-separated list of fields to return as the docvalue representation of a field for each hit |
| Expand Wildcards | `expand_wildcards` | options | open | Type of index that wildcard expressions can match. Defaults to <code>open</code> |
| Explain | `explain` | boolean | False | Whether to return detailed information about score computation as part of a hit. Defaults to false. |
| Ignore Throttled | `ignore_throttled` | boolean | True | Whether concrete, expanded or aliased indices are ignored when frozen. Defaults to true. |
| Ignore Unavailable | `ignore_unavailable` | boolean | False | Whether missing or closed indices are not included in the response. Defaults to false. |
| Max Concurrent Shard Requests | `max_concurrent_shard_requests` | number | 5 | Define the number of shard requests per node this search executes concurrently. Defaults to 5. |
| Pre-Filter Shard Size | `pre_filter_shard_size` | number | 1 | Define a threshold that enforces a pre-filter roundtrip to prefilter search shards based on query rewriting. Only used if the number of shards the search request expands to exceeds the threshold. |
| Query | `query` | json |  | Query in the <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html">Elasticsearch Query DSL</a> |
| Request Cache | `request_cache` | boolean | False | Whether the caching of search results is enabled for requests where size is 0. See <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/shard-request-cache.html">Elasticsearch shard request cache settings</a>. |
| Routing | `routing` | string |  | Target this primary shard |
| Search Type | `search_type` | options | query_then_fetch | How distributed term frequencies are calculated for relevance scoring. Defaults to Query then Fetch. |
| Sequence Number and Primary Term | `seq_no_primary_term` | boolean | False | Whether to return the sequence number and primary term of the last modification of each hit. See <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/optimistic-concurrency-control.html">Optimistic concurrency control</a>. |
| Sort | `sort` | string |  | Comma-separated list of <code>field:direction</code> pairs |
| Source Excludes | `_source_excludes` | string |  | Comma-separated list of source fields to exclude from the response |
| Source Includes | `_source_includes` | string |  | Comma-separated list of source fields to include in the response |
| Stats | `stats` | string |  | Tag of the request for logging and statistical purposes |
| Stored Fields | `stored_fields` | boolean | False | Whether to retrieve the document fields stored in the index rather than the document <code>_source</code>. Defaults to false. |
| Terminate After | `terminate_after` | number | 0 | Max number of documents to collect for each shard |
| Timeout | `timeout` | string | 1m | Period to wait for active shards. Defaults to <code>1m</code> (one minute). See the <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#time-units">Elasticsearch time units reference</a> |
| Track Scores | `track_scores` | boolean | False | Whether to calculate and return document scores, even if the scores are not used for sorting. Defaults to false. |
| Track Total Hits | `track_total_hits` | number | 10000 | Number of hits matching the query to count accurately. Defaults to 10000. |
| Version | `version` | boolean | False | Whether to return document version as part of a hit. Defaults to false. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Index ID | `indexId` | string |  | ✓ | ID of the document to update |  |
| Document ID | `documentId` | string |  | ✓ | ID of the document to update |  |
| Data to Send | `dataToSend` | options | defineBelow | ✗ | Set the value for each destination column |  |

**Data to Send options:**

* **Define Below for Each Column** (`defineBelow`) - Set the value for each destination column
* **Auto-Map Input Data to Columns** (`autoMapInputData`) - Use when node input properties match destination column names

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. | e.g. Enter properties... |  |
| Fields to Send | `fieldsUi` | fixedCollection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `fieldValues` |  |  |  |

</details>

| Options | `options` | collection | {} | ✗ | Whether to use the bulk operation to update the document/s | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Bulk Update | `bulkOperation` | boolean | False | Whether to use the bulk operation to update the document/s |
| Refresh | `refresh` | options | false | If true, Elasticsearch refreshes the affected shards to make this operation visible to search,if wait_for then wait for a refresh to make this operation visible to search,if false do nothing with refreshes |

</details>


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
* Categories: Development, Data & Storage

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: elasticsearch
displayName: Elasticsearch
description: Consume the Elasticsearch API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: elasticsearchApi
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: indexId
    name: Index ID
    type: string
    default: ''
    required: true
    description: ID of the index to create
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - document
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: Index ID
      name: indexId
  - id: indexId
    name: Index ID
    type: string
    default: ''
    required: true
    description: ID of the index to add the document to
    validation: *id001
    typeInfo: *id002
  - id: dataToSend
    name: Data to Send
    type: options
    default: defineBelow
    required: false
    description: Set the value for each destination column
    validation: &id011
      displayOptions:
        show:
          resource:
          - document
          operation:
          - update
    typeInfo: &id012
      type: options
      displayName: Data to Send
      name: dataToSend
      possibleValues:
      - value: defineBelow
        name: Define Below for Each Column
        description: Set the value for each destination column
      - value: autoMapInputData
        name: Auto-Map Input Data to Columns
        description: Use when node input properties match destination column names
  - id: inputsToIgnore
    name: Inputs to Ignore
    type: string
    default: ''
    required: false
    description: List of input properties to avoid sending, separated by commas. Leave
      empty to send all properties.
    placeholder: Enter properties...
    validation: &id013
      displayOptions:
        show:
          resource:
          - document
          operation:
          - update
          dataToSend:
          - autoMapInputData
    typeInfo: &id014
      type: string
      displayName: Inputs to Ignore
      name: inputsToIgnore
  - id: fieldsUi
    name: Fields to Send
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Field
    validation: &id015
      displayOptions:
        show:
          resource:
          - document
          operation:
          - update
          dataToSend:
          - defineBelow
    typeInfo: &id016
      type: fixedCollection
      displayName: Fields to Send
      name: fieldsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: fieldValues
        displayName: Field
        values:
        - displayName: Field Name
          name: fieldId
          type: string
          default: ''
        - displayName: Field Value
          name: fieldValue
          type: string
          default: ''
- id: delete
  name: Delete
  description: ''
  params:
  - id: indexId
    name: Index ID
    type: string
    default: ''
    required: true
    description: ID of the index to delete
    validation: *id001
    typeInfo: *id002
  - id: indexId
    name: Index ID
    type: string
    default: ''
    required: true
    description: ID of the index containing the document to delete
    validation: *id001
    typeInfo: *id002
  - id: documentId
    name: Document ID
    type: string
    default: ''
    required: true
    description: ID of the document to delete
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - document
          operation:
          - update
    typeInfo: &id004
      type: string
      displayName: Document ID
      name: documentId
- id: get
  name: Get
  description: ''
  params:
  - id: indexId
    name: Index ID
    type: string
    default: ''
    required: true
    description: ID of the index to retrieve
    validation: *id001
    typeInfo: *id002
  - id: indexId
    name: Index ID
    type: string
    default: ''
    required: true
    description: ID of the index containing the document to retrieve
    validation: *id001
    typeInfo: *id002
  - id: documentId
    name: Document ID
    type: string
    default: ''
    required: true
    description: ID of the document to retrieve
    validation: *id003
    typeInfo: *id004
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id009
      displayOptions:
        show:
          resource:
          - document
          operation:
          - getAll
    typeInfo: &id010
      type: boolean
      displayName: Simplify
      name: simple
- id: getAll
  name: Get Many
  description: ''
  params:
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
          - document
          operation:
          - getAll
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          resource:
          - document
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
  - id: indexId
    name: Index ID
    type: string
    default: ''
    required: true
    description: ID of the index containing the documents to retrieve
    validation: *id001
    typeInfo: *id002
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id009
    typeInfo: *id010
- id: update
  name: Update
  description: Update a document
  params:
  - id: indexId
    name: Index ID
    type: string
    default: ''
    required: true
    description: ID of the document to update
    validation: *id001
    typeInfo: *id002
  - id: documentId
    name: Document ID
    type: string
    default: ''
    required: true
    description: ID of the document to update
    validation: *id003
    typeInfo: *id004
  - id: dataToSend
    name: Data to Send
    type: options
    default: defineBelow
    required: false
    description: Set the value for each destination column
    validation: *id011
    typeInfo: *id012
  - id: inputsToIgnore
    name: Inputs to Ignore
    type: string
    default: ''
    required: false
    description: List of input properties to avoid sending, separated by commas. Leave
      empty to send all properties.
    placeholder: Enter properties...
    validation: *id013
    typeInfo: *id014
  - id: fieldsUi
    name: Fields to Send
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Field
    validation: *id015
    typeInfo: *id016
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - POST
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices:
  - name: paginateNotice
    text: By default, you cannot page through more than 10,000 hits. To page through
      more hits, add "Sort" from options.
    conditions:
      show:
        resource:
        - document
        operation:
        - getAll
        returnAll:
        - true
  tooltips: []
  placeholders:
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add Option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: inputsToIgnore
    text: Enter properties...
  - field: fieldsUi
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add Field
  - field: inputsToIgnore
    text: Enter properties...
  - field: fieldsUi
    text: Add Field
  - field: options
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/elasticsearch.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Elasticsearch Node",
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
            "document",
            "index"
          ],
          "default": "document"
        },
        "operation": {
          "description": "Create a document",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "get"
        },
        "indexId": {
          "description": "ID of the document to update",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "ID of the document to create and add to the index",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
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
        "documentId": {
          "description": "ID of the document to update",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Whether to use the bulk operation to update the document/s",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "dataToSend": {
          "description": "Set the value for each destination column",
          "type": "string",
          "enum": [
            "defineBelow",
            "autoMapInputData"
          ],
          "default": "defineBelow"
        },
        "inputsToIgnore": {
          "description": "List of input properties to avoid sending, separated by commas. Leave empty to send all properties.",
          "type": "string",
          "default": "",
          "examples": [
            "Enter properties..."
          ]
        },
        "fieldsUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
      "name": "elasticsearchApi",
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
