---
title: "Node: Item Lists"
slug: "node-item-lists"
version: "['2', '2.1', '2.2']"
updated: "2026-01-08"
summary: "Helper for working with lists of items and transforming arrays"
node_type: "regular"
group: "['input']"
---

# Node: Item Lists

**Purpose.** Helper for working with lists of items and transforming arrays
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:itemLists.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Concatenate Items | `aggregateItems` | Combine fields into a list in a single new item |
| Limit | `limit` | Remove items if there are too many |
| Remove Duplicates | `removeDuplicates` | Remove extra items that are similar |
| Sort | `sort` | Change the item order |
| Split Out Items | `splitOutItems` | Turn a list or values of object's properties inside item(s) into separate items |
| Summarize | `summarize` | Aggregate items together (pivot table) |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | hidden | itemList | ✗ | Resource to operate on |  |
---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | splitOutItems | ✗ | Combine fields into a list in a single new item |  |

**Operation options:**

* **Concatenate Items** (`aggregateItems`) - Combine fields into a list in a single new item
* **Limit** (`limit`) - Remove items if there are too many
* **Remove Duplicates** (`removeDuplicates`) - Remove extra items that are similar
* **Sort** (`sort`) - Change the item order
* **Split Out Items** (`splitOutItems`) - Turn a list or values of object's properties inside item(s) into separate items
* **Summarize** (`summarize`) - Aggregate items together (pivot table)

---

### Concatenate Items parameters (`aggregateItems`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Aggregate | `aggregate` | options | aggregateIndividualFields | ✗ |  |  |

**Aggregate options:**

* **Individual Fields** (`aggregateIndividualFields`)
* **All Item Data (Into a Single List)** (`aggregateAllItemData`)

| Fields To Aggregate | `fieldsToAggregate` | fixedCollection |  | ✗ | The name of a field in the input items to aggregate together | e.g. Add Field To Aggregate |  |

<details>
<summary><strong>Fields To Aggregate sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| fieldToAggregate | `fieldToAggregate` |  |  |  |

</details>

| Put Output in Field | `destinationFieldName` | string | data | ✗ | The name of the output field to put the data in |  |
| Include | `include` | options | allFields | ✗ |  |  |

**Include options:**

* **All Fields** (`allFields`)
* **Specified Fields** (`specifiedFields`)
* **All Fields Except** (`allFieldsExcept`)

| Fields To Exclude | `fieldsToExclude` | fixedCollection | {} | ✗ | A field in the input to exclude from the object in output array | e.g. Add Field To Exclude |  |

<details>
<summary><strong>Fields To Exclude sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| fields | `fields` |  |  |  |

</details>

| Fields To Include | `fieldsToInclude` | fixedCollection | {} | ✗ | Specify fields that will be included in output array | e.g. Add Field To Include |  |

<details>
<summary><strong>Fields To Include sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| fields | `fields` |  |  |  |

</details>

| Options | `options` | collection | {} | ✗ | Whether to disallow referencing child fields using `parent.child` in the field name | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |
| Destination Field Name | `destinationFieldName` | string |  | The field in the output under which to put the split field contents |
| Merge Lists | `mergeLists` | boolean | False | Whether to merge the output into a single flat list (rather than a list of lists), if the field to aggregate is a list |
| Keep Missing And Null Values | `keepMissing` | boolean | False | Whether to add a null entry to the aggregated list when there is a missing or null value |

</details>


### Limit parameters (`limit`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Max Items | `maxItems` | number | 1 | ✗ | If there are more items than this number, some are removed | min:1, max:∞ |
| Keep | `keep` | options | firstItems | ✗ | When removing items, whether to keep the ones at the start or the ending |  |

**Keep options:**

* **First Items** (`firstItems`)
* **Last Items** (`lastItems`)


### Remove Duplicates parameters (`removeDuplicates`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Compare | `compare` | options | allFields | ✗ | The fields of the input items to compare to see if they are the same |  |

**Compare options:**

* **All Fields** (`allFields`)
* **All Fields Except** (`allFieldsExcept`)
* **Selected Fields** (`selectedFields`)

| Fields To Exclude | `fieldsToExclude` | fixedCollection | {} | ✗ | A field in the input to exclude from the comparison | e.g. Add Field To Exclude |  |

<details>
<summary><strong>Fields To Exclude sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| fields | `fields` |  |  |  |

</details>

| Fields To Compare | `fieldsToCompare` | fixedCollection | {} | ✗ | A field in the input to add to the comparison | e.g. Add Field To Compare |  |

<details>
<summary><strong>Fields To Compare sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| fields | `fields` |  |  |  |

</details>

| Options | `options` | collection | {} | ✗ | Whether to remove any fields that are not being compared. If disabled, will keep the values from the first of the duplicates. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Remove Other Fields | `removeOtherFields` | boolean | False | Whether to remove any fields that are not being compared. If disabled, will keep the values from the first of the duplicates. |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |

</details>


### Sort parameters (`sort`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Type | `type` | options | simple | ✗ | The fields of the input items to compare to see if they are the same |  |

**Type options:**

* **Simple** (`simple`)
* **Random** (`random`)
* **Code** (`code`)

| Fields To Sort By | `sortFieldsUi` | fixedCollection |  | ✓ | The field to sort by | e.g. Add Field To Sort By |  |

<details>
<summary><strong>Fields To Sort By sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| sortField | `sortField` |  |  |  |

</details>

| Code | `code` | string | // The two items to compare are in the variables a and b
// Access the fields in a.json and b.json
// Return -1 if a should go before b
// Return 1 if b should go before a
// Return 0 if there's no difference

fieldName = 'myField';

if (a.json[fieldName] < b.json[fieldName]) {
		return -1;
}
if (a.json[fieldName] > b.json[fieldName]) {
		return 1;
}
return 0; | ✗ | Javascript code to determine the order of any two items |  |
| Options | `options` | collection | {} | ✗ | Whether to disallow referencing child fields using `parent.child` in the field name | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |

</details>


### Split Out Items parameters (`splitOutItems`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Fields To Split Out | `fieldToSplitOut` | string |  | ✓ | The name of the input fields to break out into separate items |  |
| Include | `include` | options | noOtherFields | ✗ | Whether to copy any other fields into the new items |  |

**Include options:**

* **No Other Fields** (`noOtherFields`)
* **All Other Fields** (`allOtherFields`)
* **Selected Other Fields** (`selectedOtherFields`)

| Fields To Include | `fieldsToInclude` | fixedCollection | {} | ✗ | A field in the input items to aggregate together | e.g. Add Field To Include |  |

<details>
<summary><strong>Fields To Include sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| fields | `fields` |  |  |  |

</details>

| Options | `options` | collection | {} | ✗ | Whether to disallow referencing child fields using `parent.child` in the field name | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |
| Destination Field Name | `destinationFieldName` | string |  | The field in the output under which to put the split field contents |
| Merge Lists | `mergeLists` | boolean | False | Whether to merge the output into a single flat list (rather than a list of lists), if the field to aggregate is a list |
| Keep Missing And Null Values | `keepMissing` | boolean | False | Whether to add a null entry to the aggregated list when there is a missing or null value |

</details>


### Summarize parameters (`summarize`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Fields to Summarize | `fieldsToSummarize` | fixedCollection | count | ✗ | How to combine the values of the field you want to summarize | e.g. Add Field |  |

<details>
<summary><strong>Fields to Summarize sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| values | `values` |  |  |  |

</details>

| Fields to Split By | `fieldsToSplitBy` | string |  | ✗ | The name of the input fields that you want to split the summary by | e.g. e.g. country, city |  |
| Fields to Group By | `fieldsToSplitBy` | string |  | ✗ | The name of the input fields that you want to split the summary by | e.g. e.g. country, city |  |
| Options | `options` | collection | {} | ✗ | Whether to disallow referencing child fields using `parent.child` in the field name | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Dot Notation | `disableDotNotation` | boolean | False | Whether to disallow referencing child fields using `parent.child` in the field name |
| Output Format | `outputFormat` | options | separateItems |  |
| Ignore items without valid fields to group by | `skipEmptySplitFields` | boolean | False |  |

</details>


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
node: Item Lists
displayName: Item Lists
description: Helper for working with lists of items and transforming arrays
version:
- '2'
- '2.1'
- '2.2'
nodeType: regular
group:
- input
operations:
- id: aggregateItems
  name: Concatenate Items
  description: Combine fields into a list in a single new item
  params:
  - id: aggregate
    name: Aggregate
    type: options
    default: aggregateIndividualFields
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - aggregateItems
    typeInfo:
      type: options
      displayName: Aggregate
      name: aggregate
      possibleValues:
      - value: aggregateIndividualFields
        name: Individual Fields
        description: ''
      - value: aggregateAllItemData
        name: All Item Data (Into a Single List)
        description: ''
  - id: fieldsToAggregate
    name: Fields To Aggregate
    type: fixedCollection
    default: ''
    required: false
    description: The name of a field in the input items to aggregate together
    hint: Enter the field name as text
    placeholder: Add Field To Aggregate
    validation:
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - aggregateItems
          aggregate:
          - aggregateIndividualFields
    typeInfo:
      type: fixedCollection
      displayName: Fields To Aggregate
      name: fieldsToAggregate
      typeOptions:
        multipleValues: true
      subProperties:
      - name: fieldToAggregate
        values:
        - displayName: Input Field Name
          name: fieldToAggregate
          type: string
          description: The name of a field in the input items to aggregate together
          placeholder: e.g. id
          hint: Enter the field name as text
          default: ''
        - displayName: Rename Field
          name: renameField
          type: boolean
          description: Whether to give the field a different name in the output
          default: false
        - displayName: Output Field Name
          name: outputFieldName
          type: string
          description: The name of the field to put the aggregated data in. Leave
            blank to use the input field name.
          default: ''
          displayOptions:
            show:
              renameField:
              - true
  - id: destinationFieldName
    name: Put Output in Field
    type: string
    default: data
    required: false
    description: The name of the output field to put the data in
    validation:
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - aggregateItems
          aggregate:
          - aggregateAllItemData
    typeInfo:
      type: string
      displayName: Put Output in Field
      name: destinationFieldName
  - id: include
    name: Include
    type: options
    default: allFields
    required: false
    description: ''
    validation: &id003
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - aggregateItems
          aggregate:
          - aggregateAllItemData
    typeInfo: &id004
      type: options
      displayName: Include
      name: include
      possibleValues:
      - value: allFields
        name: All Fields
        description: ''
      - value: specifiedFields
        name: Specified Fields
        description: ''
      - value: allFieldsExcept
        name: All Fields Except
        description: ''
  - id: fieldsToExclude
    name: Fields To Exclude
    type: fixedCollection
    default: {}
    required: false
    description: A field in the input to exclude from the object in output array
    hint: Enter the field name as text
    placeholder: Add Field To Exclude
    validation: &id001
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - removeDuplicates
          compare:
          - allFieldsExcept
    typeInfo: &id002
      type: fixedCollection
      displayName: Fields To Exclude
      name: fieldsToExclude
      typeOptions:
        multipleValues: true
      subProperties:
      - name: fields
        values:
        - displayName: Field Name
          name: fieldName
          type: string
          description: A field in the input to exclude from the comparison
          placeholder: e.g. id
          hint: Enter the field name as text
          default: ''
  - id: fieldsToInclude
    name: Fields To Include
    type: fixedCollection
    default: {}
    required: false
    description: Specify fields that will be included in output array
    hint: Enter the field name as text
    placeholder: Add Field To Include
    validation: &id005
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - aggregateItems
          aggregate:
          - aggregateAllItemData
          include:
          - specifiedFields
    typeInfo: &id006
      type: fixedCollection
      displayName: Fields To Include
      name: fieldsToInclude
      typeOptions:
        multipleValues: true
      subProperties:
      - name: fields
        values:
        - displayName: Field Name
          name: fieldName
          type: string
          description: Specify fields that will be included in output array
          placeholder: e.g. id
          hint: Enter the field name as text
          default: ''
- id: limit
  name: Limit
  description: Remove items if there are too many
  params:
  - id: maxItems
    name: Max Items
    type: number
    default: 1
    required: false
    description: If there are more items than this number, some are removed
    validation:
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - limit
    typeInfo:
      type: number
      displayName: Max Items
      name: maxItems
      typeOptions:
        minValue: 1
  - id: keep
    name: Keep
    type: options
    default: firstItems
    required: false
    description: When removing items, whether to keep the ones at the start or the
      ending
    validation:
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - limit
    typeInfo:
      type: options
      displayName: Keep
      name: keep
      possibleValues:
      - value: firstItems
        name: First Items
        description: ''
      - value: lastItems
        name: Last Items
        description: ''
- id: removeDuplicates
  name: Remove Duplicates
  description: Remove extra items that are similar
  params:
  - id: compare
    name: Compare
    type: options
    default: allFields
    required: false
    description: The fields of the input items to compare to see if they are the same
    validation:
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - removeDuplicates
    typeInfo:
      type: options
      displayName: Compare
      name: compare
      possibleValues:
      - value: allFields
        name: All Fields
        description: ''
      - value: allFieldsExcept
        name: All Fields Except
        description: ''
      - value: selectedFields
        name: Selected Fields
        description: ''
  - id: fieldsToExclude
    name: Fields To Exclude
    type: fixedCollection
    default: {}
    required: false
    description: A field in the input to exclude from the comparison
    hint: Enter the field name as text
    placeholder: Add Field To Exclude
    validation: *id001
    typeInfo: *id002
  - id: fieldsToCompare
    name: Fields To Compare
    type: fixedCollection
    default: {}
    required: false
    description: A field in the input to add to the comparison
    hint: Enter the field name as text
    placeholder: Add Field To Compare
    validation:
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - removeDuplicates
          compare:
          - selectedFields
    typeInfo:
      type: fixedCollection
      displayName: Fields To Compare
      name: fieldsToCompare
      typeOptions:
        multipleValues: true
      subProperties:
      - name: fields
        values:
        - displayName: Field Name
          name: fieldName
          type: string
          description: A field in the input to add to the comparison
          placeholder: e.g. id
          hint: Enter the field name as text
          default: ''
- id: sort
  name: Sort
  description: Change the item order
  params:
  - id: type
    name: Type
    type: options
    default: simple
    required: false
    description: The fields of the input items to compare to see if they are the same
    validation:
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - sort
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: simple
        name: Simple
        description: ''
      - value: random
        name: Random
        description: ''
      - value: code
        name: Code
        description: ''
  - id: sortFieldsUi
    name: Fields To Sort By
    type: fixedCollection
    default: ''
    required: true
    description: The field to sort by
    hint: Enter the field name as text
    placeholder: Add Field To Sort By
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - sort
          type:
          - simple
    typeInfo:
      type: fixedCollection
      displayName: Fields To Sort By
      name: sortFieldsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: sortField
        values:
        - displayName: Field Name
          name: fieldName
          type: string
          description: The field to sort by
          placeholder: e.g. id
          hint: Enter the field name as text
          default: ''
          required: true
        - displayName: Order
          name: order
          type: options
          description: The order to sort by
          value: ascending
          default: ascending
          options:
          - name: Ascending
            value: ascending
            displayName: Ascending
          - name: Descending
            value: descending
            displayName: Descending
  - id: code
    name: Code
    type: string
    default: "// The two items to compare are in the variables a and b\n// Access\
      \ the fields in a.json and b.json\n// Return -1 if a should go before b\n//\
      \ Return 1 if b should go before a\n// Return 0 if there's no difference\n\n\
      fieldName = 'myField';\n\nif (a.json[fieldName] < b.json[fieldName]) {\n\t\t\
      return -1;\n}\nif (a.json[fieldName] > b.json[fieldName]) {\n\t\treturn 1;\n\
      }\nreturn 0;"
    required: false
    description: Javascript code to determine the order of any two items
    validation:
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - sort
          type:
          - code
    typeInfo:
      type: string
      displayName: Code
      name: code
      typeOptions:
        rows: 10
        alwaysOpenEditWindow: true
- id: splitOutItems
  name: Split Out Items
  description: Turn a list or values of object's properties inside item(s) into separate
    items
  params:
  - id: fieldToSplitOut
    name: Fields To Split Out
    type: string
    default: ''
    required: true
    description: The name of the input fields to break out into separate items
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - splitOutItems
    typeInfo:
      type: string
      displayName: Fields To Split Out
      name: fieldToSplitOut
  - id: include
    name: Include
    type: options
    default: noOtherFields
    required: false
    description: Whether to copy any other fields into the new items
    validation: *id003
    typeInfo: *id004
  - id: fieldsToInclude
    name: Fields To Include
    type: fixedCollection
    default: {}
    required: false
    description: A field in the input items to aggregate together
    hint: Enter the field name as text
    placeholder: Add Field To Include
    validation: *id005
    typeInfo: *id006
- id: summarize
  name: Summarize
  description: Aggregate items together (pivot table)
  params:
  - id: fieldsToSummarize
    name: Fields to Summarize
    type: fixedCollection
    default: count
    required: false
    description: How to combine the values of the field you want to summarize
    hint: Enter the field name as text
    placeholder: Add Field
    validation:
      displayOptions:
        hide:
          aggregation:
          - countUnique
          - count
    typeInfo:
      type: fixedCollection
      displayName: Fields to Summarize
      name: fieldsToSummarize
      typeOptions:
        multipleValues: true
      subProperties:
      - name: values
        values:
        - displayName: Aggregation
          name: aggregation
          type: options
          description: How to combine the values of the field you want to summarize
          value: append
          default: count
          options:
          - name: Append
            value: append
            displayName: Append
          - name: Average
            value: average
            displayName: Average
          - name: Concatenate
            value: concatenate
            displayName: Concatenate
          - name: Count
            value: count
            displayName: Count
          - name: Count Unique
            value: countUnique
            displayName: Count Unique
          - name: Max
            value: max
            displayName: Max
          - name: Min
            value: min
            displayName: Min
          - name: Sum
            value: sum
            displayName: Sum
        - displayName: Field
          name: field
          type: string
          description: The name of an input field that you want to summarize
          placeholder: e.g. cost
          hint: Enter the field name as text
          default: ''
          displayOptions:
            hide:
              aggregation:
              - countUnique
              - count
        - displayName: Field
          name: field
          type: string
          description: The name of an input field that you want to summarize. The
            field should contain numerical values; null, undefined, empty strings
            would be ignored.
          placeholder: e.g. cost
          hint: Enter the field name as text
          default: ''
          displayOptions:
            show: {}
        - displayName: Field
          name: field
          type: string
          description: The name of an input field that you want to summarize; null,
            undefined, empty strings would be ignored
          placeholder: e.g. cost
          hint: Enter the field name as text
          default: ''
          displayOptions:
            show:
              aggregation:
              - countUnique
              - count
        - displayName: Include Empty Values
          name: includeEmpty
          type: boolean
          default: false
          displayOptions:
            show:
              aggregation:
              - append
              - concatenate
        - displayName: Separator
          name: separateBy
          type: options
          hint: What to insert between values
          value: ','
          default: ','
          options:
          - name: Comma
            value: ','
            displayName: Comma
          - name: Comma and Space
            value: ','
            displayName: Comma And Space
          - name: New Line
            value: n
            displayName: New Line
          - name: None
            displayName: None
          - name: Space
            displayName: Space
          - name: Other
            value: other
            displayName: Other
          displayOptions:
            show:
              aggregation:
              - concatenate
        - displayName: Custom Separator
          name: customSeparator
          type: string
          default: ''
          displayOptions:
            show:
              aggregation:
              - concatenate
              separateBy:
              - other
  - id: fieldsToSplitBy
    name: Fields to Split By
    type: string
    default: ''
    required: false
    description: The name of the input fields that you want to split the summary by
    hint: Enter the name of the fields as text (separated by commas)
    placeholder: e.g. country, city
    validation: &id007
      displayOptions:
        show:
          resource:
          - itemList
          operation:
          - summarize
    typeInfo: &id008
      type: string
      displayName: Fields to Group By
      name: fieldsToSplitBy
  - id: fieldsToSplitBy
    name: Fields to Group By
    type: string
    default: ''
    required: false
    description: The name of the input fields that you want to split the summary by
    hint: Enter the name of the fields as text (separated by commas)
    placeholder: e.g. country, city
    validation: *id007
    typeInfo: *id008
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: fieldsToInclude
    text: Add Field To Include
  - field: fieldsToAggregate
    text: Add Field To Aggregate
  - field: fieldsToExclude
    text: Add Field To Exclude
  - field: fieldsToInclude
    text: Add Field To Include
  - field: fieldsToExclude
    text: Add Field To Exclude
  - field: fieldsToCompare
    text: Add Field To Compare
  - field: sortFieldsUi
    text: Add Field To Sort By
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: fieldsToSummarize
    text: Add Field
  - field: fieldsToSplitBy
    text: e.g. country, city
  - field: fieldsToSplitBy
    text: e.g. country, city
  - field: options
    text: Add option
  hints:
  - field: fieldsToInclude
    text: Enter the field name as text
  - field: fieldsToAggregate
    text: Enter the field name as text
  - field: fieldsToExclude
    text: Enter the field name as text
  - field: fieldsToInclude
    text: Enter the field name as text
  - field: fieldsToExclude
    text: Enter the field name as text
  - field: fieldsToCompare
    text: Enter the field name as text
  - field: sortFieldsUi
    text: Enter the field name as text
  - field: fieldsToSummarize
    text: Enter the field name as text
  - field: fieldsToSplitBy
    text: Enter the name of the fields as text (separated by commas)
  - field: fieldsToSplitBy
    text: Enter the name of the fields as text (separated by commas)
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
  "$id": "https://n8n.io/schemas/nodes/Item Lists.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Item Lists Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "aggregateItems",
        "limit",
        "removeDuplicates",
        "sort",
        "splitOutItems",
        "summarize"
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
          "default": "itemList"
        },
        "operation": {
          "description": "Combine fields into a list in a single new item",
          "type": "string",
          "enum": [
            "aggregateItems",
            "limit",
            "removeDuplicates",
            "sort",
            "splitOutItems",
            "summarize"
          ],
          "default": "splitOutItems"
        },
        "fieldToSplitOut": {
          "description": "The name of the input fields to break out into separate items",
          "type": "string",
          "default": ""
        },
        "include": {
          "description": "",
          "type": "string",
          "enum": [
            "allFields",
            "specifiedFields",
            "allFieldsExcept"
          ],
          "default": "allFields"
        },
        "fieldsToInclude": {
          "description": "Specify fields that will be included in output array",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field To Include"
          ]
        },
        "aggregate": {
          "description": "",
          "type": "string",
          "enum": [
            "aggregateIndividualFields",
            "aggregateAllItemData"
          ],
          "default": "aggregateIndividualFields"
        },
        "fieldsToAggregate": {
          "description": "The name of a field in the input items to aggregate together",
          "type": "string",
          "default": "",
          "examples": [
            "Add Field To Aggregate"
          ]
        },
        "destinationFieldName": {
          "description": "The name of the output field to put the data in",
          "type": "string",
          "default": "data"
        },
        "fieldsToExclude": {
          "description": "A field in the input to exclude from the comparison",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field To Exclude"
          ]
        },
        "compare": {
          "description": "The fields of the input items to compare to see if they are the same",
          "type": "string",
          "enum": [
            "allFields",
            "allFieldsExcept",
            "selectedFields"
          ],
          "default": "allFields"
        },
        "fieldsToCompare": {
          "description": "A field in the input to add to the comparison",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field To Compare"
          ]
        },
        "type": {
          "description": "The fields of the input items to compare to see if they are the same",
          "type": "string",
          "enum": [
            "simple",
            "random",
            "code"
          ],
          "default": "simple"
        },
        "sortFieldsUi": {
          "description": "The field to sort by",
          "type": "string",
          "default": "",
          "examples": [
            "Add Field To Sort By"
          ]
        },
        "code": {
          "description": "Javascript code to determine the order of any two items",
          "type": "string",
          "default": "// The two items to compare are in the variables a and b\n// Access the fields in a.json and b.json\n// Return -1 if a should go before b\n// Return 1 if b should go before a\n// Return 0 if there's no difference\n\nfieldName = 'myField';\n\nif (a.json[fieldName] < b.json[fieldName]) {\n\t\treturn -1;\n}\nif (a.json[fieldName] > b.json[fieldName]) {\n\t\treturn 1;\n}\nreturn 0;"
        },
        "maxItems": {
          "description": "If there are more items than this number, some are removed",
          "type": "number",
          "default": 1
        },
        "keep": {
          "description": "When removing items, whether to keep the ones at the start or the ending",
          "type": "string",
          "enum": [
            "firstItems",
            "lastItems"
          ],
          "default": "firstItems"
        },
        "options": {
          "description": "Whether to disallow referencing child fields using `parent.child` in the field name",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "fieldsToSummarize": {
          "description": "How to combine the values of the field you want to summarize",
          "type": "string",
          "default": "count",
          "examples": [
            "Add Field"
          ]
        },
        "fieldsToSplitBy": {
          "description": "The name of the input fields that you want to split the summary by",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. country, city"
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
    "version": [
      "2",
      "2.1",
      "2.2"
    ]
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2', '2.1', '2.2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
