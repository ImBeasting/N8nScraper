---
title: "Node: Google Docs"
slug: "node-googledocs"
version: "['1', '2']"
updated: "2026-01-08"
summary: "Consume Google Docs API."
node_type: "regular"
group: "['input']"
---

# Node: Google Docs

**Purpose.** Consume Google Docs API.
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:googleDocs.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleApi**: N/A
- **googleDocsOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleApi` | ✓ | {'show': {'authentication': ['serviceAccount']}} |
| `googleDocsOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Document Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a document |
| Get | `get` | Get a document |
| Update | `update` | Update a document |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | document | ✗ | Resource to operate on |  |

**Resource options:**

* **Document** (`document`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Operation to perform |  |

**Operation options:**

* **Create** (`create`) - Create a document
* **Get** (`get`) - Get a document
* **Update** (`update`) - Update a document

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Drive Name or ID | `driveId` | options | myDrive | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Folder Name or ID | `folderId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Title | `title` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc ID or URL | `documentURL` | string |  | ✓ | The ID in the document URL (or just paste the whole URL) | url |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Doc ID or URL | `documentURL` | string |  | ✓ | The ID in the document URL (or just paste the whole URL) | url |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Actions | `actionsUi` | fixedCollection | text | ✗ | Actions applied to update the document | e.g. Add Action |  |

<details>
<summary><strong>Actions sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Action Fields | `actionFields` |  |  |  |

</details>

| Update Fields | `updateFields` | fixedCollection | {} | ✗ | Apply changes to the latest revision. Otherwise changes will not be processed. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Write Control Object | `writeControlObject` |  |  |  |

</details>


---

## Load Options Methods

- `getDrives`
- `name`
- `value`

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
* Categories: Miscellaneous

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleDocs
displayName: Google Docs
description: Consume Google Docs API.
version:
- '1'
- '2'
nodeType: regular
group:
- input
credentials:
- name: googleApi
  required: true
- name: googleDocsOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: ''
  params:
  - id: driveId
    name: Drive Name or ID
    type: options
    default: myDrive
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - document
    typeInfo:
      type: options
      displayName: Drive Name or ID
      name: driveId
      typeOptions:
        loadOptionsMethod: getDrives
      possibleValues: []
  - id: folderId
    name: Folder Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - document
    typeInfo:
      type: options
      displayName: Folder Name or ID
      name: folderId
      typeOptions:
        loadOptionsMethod: getFolders
      possibleValues: []
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - document
    typeInfo:
      type: string
      displayName: Title
      name: title
- id: get
  name: Get
  description: ''
  params:
  - id: documentURL
    name: Doc ID or URL
    type: string
    default: ''
    required: true
    description: The ID in the document URL (or just paste the whole URL)
    validation: &id001
      required: true
      format: url
      displayOptions:
        show:
          operation:
          - update
          resource:
          - document
    typeInfo: &id002
      type: string
      displayName: Doc ID or URL
      name: documentURL
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id003
      displayOptions:
        show:
          operation:
          - update
          resource:
          - document
    typeInfo: &id004
      type: boolean
      displayName: Simplify
      name: simple
- id: update
  name: Update
  description: ''
  params:
  - id: documentURL
    name: Doc ID or URL
    type: string
    default: ''
    required: true
    description: The ID in the document URL (or just paste the whole URL)
    validation: *id001
    typeInfo: *id002
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id003
    typeInfo: *id004
  - id: actionsUi
    name: Actions
    type: fixedCollection
    default: text
    required: false
    description: Actions applied to update the document
    placeholder: Add Action
    validation:
      displayOptions:
        show:
          operation:
          - update
          resource:
          - document
    typeInfo:
      type: fixedCollection
      displayName: Actions
      name: actionsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: actionFields
        displayName: Action Fields
        values:
        - displayName: Object
          name: object
          type: options
          description: The update object
          value: footer
          default: text
          options:
          - name: Footer
            value: footer
            displayName: Footer
          - name: Header
            value: header
            displayName: Header
          - name: Named Range
            value: namedRange
            displayName: Named Range
          - name: Page Break
            value: pageBreak
            displayName: Page Break
          - name: Paragraph Bullets
            value: paragraphBullets
            displayName: Paragraph Bullets
          - name: Positioned Object
            value: positionedObject
            displayName: Positioned Object
          - name: Table
            value: table
            displayName: Table
          - name: Table Column
            value: tableColumn
            displayName: Table Column
          - name: Table Row
            value: tableRow
            displayName: Table Row
          - name: Text
            value: text
            displayName: Text
        - displayName: Action
          name: action
          type: options
          description: The update action
          value: replaceAll
          default: ''
          options:
          - name: Find and Replace Text
            value: replaceAll
            displayName: Find And Replace Text
          - name: Insert
            value: insert
            displayName: Insert
          displayOptions:
            show:
              object:
              - text
        - displayName: Action
          name: action
          type: options
          description: The update action
          value: create
          default: ''
          options:
          - name: Create
            value: create
            displayName: Create
          - name: Delete
            value: delete
            displayName: Delete
          displayOptions:
            show:
              object:
              - footer
              - header
              - namedRange
              - paragraphBullets
        - displayName: Action
          name: action
          type: options
          description: The update action
          value: delete
          default: ''
          options:
          - name: Delete
            value: delete
            displayName: Delete
          - name: Insert
            value: insert
            displayName: Insert
          displayOptions:
            show:
              object:
              - tableColumn
              - tableRow
        - displayName: Action
          name: action
          type: options
          description: The update action
          value: insert
          default: ''
          options:
          - name: Insert
            value: insert
            displayName: Insert
          displayOptions:
            show:
              object:
              - pageBreak
              - table
        - displayName: Action
          name: action
          type: options
          description: The update action
          value: delete
          default: ''
          options:
          - name: Delete
            value: delete
            displayName: Delete
          displayOptions:
            show:
              object:
              - positionedObject
        - displayName: Insert Segment
          name: insertSegment
          type: options
          description: The location where to create the object
          value: header
          default: body
          options:
          - name: Header
            value: header
            displayName: Header
          - name: Body
            value: body
            displayName: Body
          - name: Footer
            value: footer
            displayName: Footer
          displayOptions:
            show:
              object:
              - footer
              - header
              - paragraphBullets
              - namedRange
              action:
              - create
        - displayName: Segment ID
          name: segmentId
          type: string
          description: The ID of the header, footer or footnote. The <code>Document
            → Get</code> operation lists all segment IDs (make sure you disable the
            <code>simple</code> toggle).
          default: ''
          displayOptions:
            show:
              object:
              - footer
              - header
              - paragraphBullets
              - namedRange
              action:
              - create
            hide:
              insertSegment:
              - body
        - displayName: Index
          name: index
          type: number
          description: The zero-based index, relative to the beginning of the specified
            segment
          default: 0
          displayOptions:
            show:
              object:
              - footer
              - header
              action:
              - create
        - displayName: Name
          name: name
          type: string
          description: The name of the Named Range. Names do not need to be unique.
          default: ''
          displayOptions:
            show:
              object:
              - namedRange
              action:
              - create
        - displayName: Start Index
          name: startIndex
          type: number
          description: The zero-based start index of this range
          default: 0
          displayOptions:
            show:
              object:
              - namedRange
              action:
              - create
        - displayName: End Index
          name: endIndex
          type: number
          description: The zero-based end index of this range
          default: 0
          displayOptions:
            show:
              object:
              - namedRange
              action:
              - create
        - displayName: Style
          name: bulletPreset
          type: options
          description: A bulleted list with a <code>DISC</code>, <code>CIRCLE</code>
            and <code>SQUARE</code> bullet glyph for the first 3 list nesting levels
          value: BULLET_DISC_CIRCLE_SQUARE
          default: BULLET_DISC_CIRCLE_SQUARE
          options:
          - name: Bullet List
            description: A bulleted list with a <code>DISC</code>, <code>CIRCLE</code>
              and <code>SQUARE</code> bullet glyph for the first 3 list nesting levels
            value: BULLET_DISC_CIRCLE_SQUARE
            displayName: Bullet List
          - name: Checkbox List
            description: A bulleted list with CHECKBOX bullet glyphs for all list
              nesting levels
            value: BULLET_CHECKBOX
            displayName: Checkbox List
          - name: Numbered List
            description: 'A numbered list with <code>DECIMAL</code> numeric glyphs
              separated by periods, where each nesting level uses the previous nesting
              level''s glyph as a prefix. For example: 1., 1.1., 2., 2.2 .'
            value: NUMBERED_DECIMAL_NESTED
            displayName: Numbered List
          displayOptions:
            show:
              object:
              - paragraphBullets
              action:
              - create
        - displayName: Footer ID
          name: footerId
          type: string
          description: The ID of the footer to delete. To retrieve it, use the <code>get
            document</code> where you can find under <code>footers</code> attribute.
          default: ''
          displayOptions:
            show:
              object:
              - footer
              action:
              - delete
        - displayName: Header ID
          name: headerId
          type: string
          description: The ID of the header to delete. To retrieve it, use the <code>get
            document</code> where you can find under <code>headers</code> attribute.
          default: ''
          displayOptions:
            show:
              object:
              - header
              action:
              - delete
        - displayName: Specify Range By
          name: namedRangeReference
          type: options
          description: The value determines which range or ranges to delete
          value: namedRangeId
          default: namedRangeId
          options:
          - name: ID
            value: namedRangeId
            displayName: Id
          - name: Name
            value: name
            displayName: Name
          displayOptions:
            show:
              object:
              - namedRange
              action:
              - delete
        - displayName: ID
          name: value
          type: string
          description: The ID of the range
          default: ''
          displayOptions:
            show:
              object:
              - namedRange
              action:
              - delete
              namedRangeReference:
              - namedRangeId
        - displayName: Name
          name: value
          type: string
          description: The name of the range
          default: ''
          displayOptions:
            show:
              object:
              - namedRange
              action:
              - delete
              namedRangeReference:
              - name
        - displayName: Object ID
          name: objectId
          type: string
          description: The ID of the positioned object to delete (An object that is
            tied to a paragraph and positioned relative to its beginning), See the
            Google <a href="https://developers.google.com/docs/api/reference/rest/v1/documents#positionedobject"
            target="_blank">documentation</a>
          default: ''
          displayOptions:
            show:
              object:
              - positionedObject
              action:
              - delete
        - displayName: Insert Segment
          name: insertSegment
          type: options
          description: The location where to create the object
          value: header
          default: body
          options:
          - name: Header
            value: header
            displayName: Header
          - name: Body
            value: body
            displayName: Body
          - name: Footer
            value: footer
            displayName: Footer
          displayOptions:
            show:
              object:
              - pageBreak
              - table
              - tableColumn
              - tableRow
              - text
              action:
              - insert
        - displayName: Segment ID
          name: segmentId
          type: string
          description: The ID of the header, footer or footnote. The <code>Document
            → Get</code> operation lists all segment IDs (make sure you disable the
            <code>simple</code> toggle).
          default: ''
          displayOptions:
            show:
              object:
              - pageBreak
              - table
              - tableColumn
              - tableRow
              - text
              action:
              - insert
            hide:
              insertSegment:
              - body
        - displayName: Insert Location
          name: locationChoice
          type: options
          description: Inserts the text at the end of a header, footer, footnote,
            or document body
          value: endOfSegmentLocation
          default: endOfSegmentLocation
          options:
          - name: At End of Specific Position
            description: Inserts the text at the end of a header, footer, footnote,
              or document body
            value: endOfSegmentLocation
            displayName: At End Of Specific Position
          - name: At Index
            value: location
            displayName: At Index
          displayOptions:
            show:
              object:
              - pageBreak
              action:
              - insert
        - displayName: Index
          name: index
          type: number
          description: The zero-based index, relative to the beginning of the specified
            segment
          default: 1
          typeOptions:
            minValue: 1
          displayOptions:
            show:
              locationChoice:
              - location
              object:
              - pageBreak
              action:
              - insert
        - displayName: Insert Location
          name: locationChoice
          type: options
          description: Inserts the text at the end of a header, footer, footnote,
            or document body
          value: endOfSegmentLocation
          default: endOfSegmentLocation
          options:
          - name: At End of Specific Position
            description: Inserts the text at the end of a header, footer, footnote,
              or document body
            value: endOfSegmentLocation
            displayName: At End Of Specific Position
          - name: At Index
            value: location
            displayName: At Index
          displayOptions:
            show:
              object:
              - table
              action:
              - insert
        - displayName: Index
          name: index
          type: number
          description: The zero-based index, relative to the beginning of the specified
            segment (use index + 1 to refer to a table)
          default: 1
          typeOptions:
            minValue: 1
          displayOptions:
            show:
              locationChoice:
              - location
              object:
              - table
              action:
              - insert
        - displayName: Rows
          name: rows
          type: number
          description: The number of rows in the table
          default: 0
          displayOptions:
            show:
              object:
              - table
              action:
              - insert
        - displayName: Columns
          name: columns
          type: number
          description: The number of columns in the table
          default: 0
          displayOptions:
            show:
              object:
              - table
              action:
              - insert
        - displayName: Insert Location
          name: locationChoice
          type: options
          description: Inserts the text at the end of a header, footer, footnote,
            or document body
          value: endOfSegmentLocation
          default: endOfSegmentLocation
          options:
          - name: At End of Specific Position
            description: Inserts the text at the end of a header, footer, footnote,
              or document body
            value: endOfSegmentLocation
            displayName: At End Of Specific Position
          - name: At Index
            value: location
            displayName: At Index
          displayOptions:
            show:
              object:
              - text
              action:
              - insert
        - displayName: Index
          name: index
          type: number
          description: The zero-based index, relative to the beginning of the specified
            segment
          default: 1
          typeOptions:
            minValue: 1
          displayOptions:
            show:
              locationChoice:
              - location
              object:
              - text
              action:
              - insert
        - displayName: Text
          name: text
          type: string
          description: The text to insert in the document
          default: ''
          displayOptions:
            show:
              object:
              - text
              action:
              - insert
        - displayName: Old Text
          name: text
          type: string
          description: The text to search for in the document
          default: ''
          displayOptions:
            show:
              object:
              - text
              action:
              - replaceAll
        - displayName: New Text
          name: replaceText
          type: string
          description: The text that will replace the matched text
          default: ''
          displayOptions:
            show:
              object:
              - text
              action:
              - replaceAll
        - displayName: Match Case
          name: matchCase
          type: boolean
          description: Whether the search should respect case sensitivity
          default: false
          displayOptions:
            show:
              object:
              - text
              action:
              - replaceAll
        - displayName: Insert Segment
          name: insertSegment
          type: options
          description: The location where to create the object
          value: header
          default: body
          options:
          - name: Header
            value: header
            displayName: Header
          - name: Body
            value: body
            displayName: Body
          - name: Footer
            value: footer
            displayName: Footer
          displayOptions:
            show:
              object:
              - paragraphBullets
              - tableColumn
              - tableRow
              action:
              - delete
        - displayName: Segment ID
          name: segmentId
          type: string
          description: The ID of the header, footer or footnote. The <code>Document
            → Get</code> operation lists all segment IDs (make sure you disable the
            <code>simple</code> toggle).
          default: ''
          displayOptions:
            show:
              object:
              - paragraphBullets
              - tableColumn
              - tableRow
              action:
              - delete
            hide:
              insertSegment:
              - body
        - displayName: Start Index
          name: startIndex
          type: number
          description: The zero-based start index of this range
          default: 0
          displayOptions:
            show:
              object:
              - paragraphBullets
        - displayName: End Index
          name: endIndex
          type: number
          description: The zero-based end index of this range
          default: 0
          displayOptions:
            show:
              object:
              - paragraphBullets
        - displayName: Insert Position
          name: insertPosition
          type: options
          default: true
          options:
          - name: Before Content at Index
            displayName: Before Content At Index
          - name: After Content at Index
            displayName: After Content At Index
          displayOptions:
            show:
              object:
              - tableColumn
              - tableRow
              action:
              - insert
        - displayName: Index
          name: index
          type: number
          description: The zero-based index, relative to the beginning of the specified
            segment (use index + 1 to refer to a table)
          default: 1
          typeOptions:
            minValue: 1
          displayOptions:
            show:
              object:
              - tableColumn
              - tableRow
        - displayName: Row Index
          name: rowIndex
          type: number
          description: The zero-based row index
          default: 0
          displayOptions:
            show:
              object:
              - tableColumn
              - tableRow
        - displayName: Column Index
          name: columnIndex
          type: number
          description: The zero-based column index
          default: 0
          displayOptions:
            show:
              object:
              - tableColumn
              - tableRow
  - id: updateFields
    name: Update Fields
    type: fixedCollection
    default: {}
    required: false
    description: Apply changes to the latest revision. Otherwise changes will not
      be processed.
    placeholder: Add Field
    validation:
      displayOptions:
        show:
          operation:
          - update
          resource:
          - document
    typeInfo:
      type: fixedCollection
      displayName: Update Fields
      name: updateFields
      subProperties:
      - name: writeControlObject
        displayName: Write Control Object
        values:
        - displayName: Revision Mode
          name: control
          type: options
          description: Apply changes to the latest revision. Otherwise changes will
            not be processed.
          value: targetRevisionId
          default: requiredRevisionId
          options:
          - name: Target
            description: Apply changes to the latest revision. Otherwise changes will
              not be processed.
            value: targetRevisionId
            displayName: Target
          - name: Required
            description: Apply changes to the provided revision while incorporating
              other collaborators' changes. This mode is used for the recent revision,
              Otherwise changes will not be processed.
            value: requiredRevisionId
            displayName: Required
        - displayName: Revision ID
          name: value
          type: string
          default: ''
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: actionsUi
    text: Add Action
  - field: updateFields
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
  "$id": "https://n8n.io/schemas/nodes/googleDocs.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Docs Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get",
        "update"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "serviceAccount",
            "oAuth2"
          ],
          "default": "serviceAccount"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "document"
          ],
          "default": "document"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "create",
            "get",
            "update"
          ],
          "default": "create"
        },
        "driveId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": "myDrive"
        },
        "folderId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "documentURL": {
          "description": "The ID in the document URL (or just paste the whole URL)",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "actionsUi": {
          "description": "Actions applied to update the document",
          "type": "string",
          "default": "text",
          "examples": [
            "Add Action"
          ]
        },
        "updateFields": {
          "description": "Apply changes to the latest revision. Otherwise changes will not be processed.",
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
    "version": [
      "1",
      "2"
    ]
  },
  "credentials": [
    {
      "name": "googleApi",
      "required": true
    },
    {
      "name": "googleDocsOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
