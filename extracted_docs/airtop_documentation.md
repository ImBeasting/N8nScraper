---
title: "Node: Airtop"
slug: "node-airtop"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Scrape and control any site with Airtop"
node_type: "regular"
group: "['transform']"
---

# Node: Airtop

**Purpose.** Scrape and control any site with Airtop
**Subtitle.** ={{ $parameter["operation"] + ": " + $parameter["resource"] }}


---

## Node Details

- **Icon:** `file:airtop.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **airtopApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice** when resource=['session'], operation=['save']: Note: This operation is not needed if you enabled 'Save Profile' in the 'Create Session' operation

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `airtopApi` | ✓ | - |

---

## API Patterns

**HTTP Methods:** GET

---

## Operations

### Agent Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Run | `run` | Run an Airtop agent |

### Session Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create Session | `create` | Create an Airtop browser session |
| Save Profile on Termination | `save` | Save in a profile changes made in your browsing session such as cookies and local storage |
| Terminate Session | `terminate` | Terminate a session |
| Wait for Download | `waitForDownload` | Wait for a file download to become available |

### Window Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Close Window | `close` | Close a window inside a session |
| Create a New Browser Window | `create` | Create a new browser window inside a session. Can load a URL when created. |
| Get Live View | `getLiveView` | Get information about a browser window, including the live view URL |
| List Windows | `list` | List all browser windows in a session |
| Load URL | `load` | Load a URL in an existing window |
| Take Screenshot | `takeScreenshot` | Take a screenshot of the current window |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `deleteFile` | Delete an uploaded file |
| Get | `get` | Get a details of an uploaded file |
| Get Many | `getMany` | Get details of multiple uploaded files |
| Load | `load` | Load a file into a session |
| Upload | `upload` | Upload a file into a session |

### Extraction Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Query Page | `query` | Query a page to extract data or ask a question given the data on the page |
| Query Page with Pagination | `getPaginated` | Extract content from paginated or dynamically loaded pages |
| Smart Scrape | `scrape` | Scrape a page and return the data as markdown |

### Interaction Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Click an Element | `click` | Execute a click on an element given a description |
| Fill Form | `fill` | Fill a form with the provided information |
| Hover on an Element | `hover` | Execute a hover action on an element given a description |
| Scroll | `scroll` | Execute a scroll action on the page |
| Type | `type` | Execute a Type action on an element given a description |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | session | ✗ | Resource to operate on |  |

**Resource options:**

* **Agent** (`agent`)
* **Extraction** (`extraction`)
* **File** (`file`)
* **Interaction** (`interaction`)
* **Session** (`session`)
* **Window** (`window`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | run | ✗ | Run an Airtop agent |  |

**Operation options:**

* **Run** (`run`) - Run an Airtop agent

---

### Run parameters (`run`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Timeout | `timeout` | number | 600 | ✗ | Timeout in seconds to wait for the agent to finish |  |

### Create Session parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Get Live View | `getLiveView` | boolean | False | ✗ | Whether to get the URL of the window's <a href="https://docs.airtop.ai/guides/how-to/creating-a-live-view" target="_blank">Live View</a> |  |
| Include Navigation Bar | `includeNavigationBar` | boolean | False | ✗ | Whether to include the navigation bar in the Live View. When enabled, the navigation bar will be visible allowing you to navigate between pages. |  |
| Screen Resolution | `screenResolution` | string |  | ✗ | The screen resolution of the Live View. Setting a resolution will force the window to open at that specific size. | e.g. e.g. 1280x720 |  |
| Disable Resize | `disableResize` | boolean | False | ✗ | Whether to disable the window from being resized in the Live View |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Wait until the specified loading event occurs | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Wait Until | `waitUntil` | options | load | Wait until the specified loading event occurs |

</details>


### Save Profile on Termination parameters (`save`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |

### Get Live View parameters (`getLiveView`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the navigation bar in the Live View. When enabled, the navigation bar will be visible allowing you to navigate between pages. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Navigation Bar | `includeNavigationBar` | boolean | False | Whether to include the navigation bar in the Live View. When enabled, the navigation bar will be visible allowing you to navigate between pages. |
| Screen Resolution | `screenResolution` | string |  | The screen resolution of the Live View. Setting a resolution will force the window to open at that specific size. |
| Disable Resize | `disableResize` | boolean | False | Whether to disable the window from being resized in the Live View |

</details>


### Load URL parameters (`load`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Wait until the specified loading event occurs. Defaults to 'Fully Loaded'. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Wait Until | `waitUntil` | options | load | Wait until the specified loading event occurs. Defaults to 'Fully Loaded'. |

</details>


### Take Screenshot parameters (`takeScreenshot`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Output Binary Image | `outputImageAsBinary` | boolean | False | ✗ | Whether to output the image as a binary file instead of a base64 encoded string |  |

### Delete parameters (`deleteFile`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| File ID | `fileId` | string |  | ✓ | ID of the file to delete |  |

### Get Many parameters (`getMany`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Limit | `limit` | number | 10 | ✗ | Max number of results to return | min:1, max:100 |

### Query Page parameters (`query`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Prompt | `prompt` | string |  | ✓ | The prompt to query the page content | e.g. e.g. Is there a login form in this page? |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to analyze the web page visually when fulfilling the request | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Visual Analysis | `includeVisualAnalysis` | boolean | False | Whether to analyze the web page visually when fulfilling the request |

</details>


### Query Page with Pagination parameters (`getPaginated`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Prompt | `prompt` | string |  | ✓ | The prompt to extract data from the pages | e.g. e.g. Extract all the product names and prices |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The strategy for interacting with the page | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Interaction Mode | `interactionMode` | options | auto | The strategy for interacting with the page |
| Pagination Mode | `paginationMode` | options | auto | The pagination approach to use |

</details>


### Click an Element parameters (`click`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Defines the strategy for visual analysis of the current window | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Visual Scope | `visualScope` | options | auto | Defines the strategy for visual analysis of the current window |
| Wait Until Event After Navigation | `waitForNavigation` | options | load | The condition to wait for the navigation to complete after an interaction (click, type or hover). Defaults to 'Fully Loaded'. |

</details>

| Click Type | `clickType` | options | click | ✗ | The type of click to perform. Defaults to left click. |  |

**Click Type options:**

* **Left Click** (`click`)
* **Double Click** (`doubleClick`)
* **Right Click** (`rightClick`)


### Fill Form parameters (`fill`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Form Data | `formData` | string |  | ✓ | The information to fill into the form written in natural language | e.g. e.g. "Name: John Doe, Email: john.doe@example.com" |  |

### Hover on an Element parameters (`hover`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Defines the strategy for visual analysis of the current window | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Visual Scope | `visualScope` | options | auto | Defines the strategy for visual analysis of the current window |
| Wait Until Event After Navigation | `waitForNavigation` | options | load | The condition to wait for the navigation to complete after an interaction (click, type or hover). Defaults to 'Fully Loaded'. |

</details>


### Scroll parameters (`scroll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Defines the strategy for visual analysis of the current window | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Visual Scope | `visualScope` | options | auto | Defines the strategy for visual analysis of the current window |
| Wait Until Event After Navigation | `waitForNavigation` | options | load | The condition to wait for the navigation to complete after an interaction (click, type or hover). Defaults to 'Fully Loaded'. |

</details>

| Scroll Mode | `scrollingMode` | options | automatic | ✓ | Choose the mode of scrolling |  |

**Scroll Mode options:**

* **Automatic** (`automatic`) - Describe with natural language the element to scroll to
* **Manual** (`manual`) - Define the direction and amount to scroll by

| Element Description | `scrollToElement` | string |  | ✓ | A natural language description of the element to scroll to | e.g. e.g. the page section titled "Contact Us" |  |
| Scroll To Edge | `scrollToEdge` | fixedCollection | {} | ✗ | The direction to scroll to. When 'Scroll By' is defined, 'Scroll To Edge' action will be executed first, then 'Scroll By' action. | e.g. Add Edge Direction |  |

<details>
<summary><strong>Scroll To Edge sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Page Edges | `edgeValues` |  |  |  |

</details>

| Scroll By | `scrollBy` | fixedCollection | {} | ✗ | The amount to scroll by. When 'Scroll To Edge' is defined, 'Scroll By' action will be executed after 'Scroll To Edge'. | e.g. Add Scroll Amount |  |

<details>
<summary><strong>Scroll By sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Scroll Values | `scrollValues` |  |  |  |

</details>

| Scrollable Area | `scrollWithin` | string |  | ✗ | Scroll within an element on the page | e.g. e.g. the left sidebar |  |

### Type parameters (`type`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Defines the strategy for visual analysis of the current window | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Visual Scope | `visualScope` | options | auto | Defines the strategy for visual analysis of the current window |
| Wait Until Event After Navigation | `waitForNavigation` | options | load | The condition to wait for the navigation to complete after an interaction (click, type or hover). Defaults to 'Fully Loaded'. |

</details>

| Text | `text` | string |  | ✓ | The text to type into the browser window | e.g. e.g. email@example.com |  |
| Press Enter Key | `pressEnterKey` | boolean | False | ✗ | Whether to press the Enter key after typing the text |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $json["sessionId"] }}`
- `={{ $json["windowId"] }}`
- `={{ $parameter["operation"] + ": " + $parameter["resource"] }}`

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
* Categories: Productivity, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: airtop
displayName: Airtop
description: Scrape and control any site with Airtop
version:
- '1'
- '1.1'
nodeType: regular
group:
- transform
credentials:
- name: airtopApi
  required: true
operations:
- id: run
  name: Run
  description: Run an Airtop agent
  params:
  - id: timeout
    name: Timeout
    type: number
    default: 600
    required: false
    description: Timeout in seconds to wait for the agent to finish
    validation:
      displayOptions:
        show:
          resource:
          - agent
          operation:
          - run
          awaitExecution:
          - true
    typeInfo:
      type: number
      displayName: Timeout
      name: timeout
- id: create
  name: Create Session
  description: Create an Airtop browser session
  params:
  - id: getLiveView
    name: Get Live View
    type: boolean
    default: false
    required: false
    description: Whether to get the URL of the window's <a href="https://docs.airtop.ai/guides/how-to/creating-a-live-view"
      target="_blank">Live View</a>
    validation:
      displayOptions:
        show:
          resource:
          - window
          operation:
          - create
    typeInfo:
      type: boolean
      displayName: Get Live View
      name: getLiveView
  - id: includeNavigationBar
    name: Include Navigation Bar
    type: boolean
    default: false
    required: false
    description: Whether to include the navigation bar in the Live View. When enabled,
      the navigation bar will be visible allowing you to navigate between pages.
    validation:
      displayOptions:
        show:
          resource:
          - window
          operation:
          - create
          getLiveView:
          - true
    typeInfo:
      type: boolean
      displayName: Include Navigation Bar
      name: includeNavigationBar
  - id: screenResolution
    name: Screen Resolution
    type: string
    default: ''
    required: false
    description: The screen resolution of the Live View. Setting a resolution will
      force the window to open at that specific size.
    placeholder: e.g. 1280x720
    validation:
      displayOptions:
        show:
          resource:
          - window
          operation:
          - create
          getLiveView:
          - true
    typeInfo:
      type: string
      displayName: Screen Resolution
      name: screenResolution
  - id: disableResize
    name: Disable Resize
    type: boolean
    default: false
    required: false
    description: Whether to disable the window from being resized in the Live View
    validation:
      displayOptions:
        show:
          resource:
          - window
          operation:
          - create
          getLiveView:
          - true
    typeInfo:
      type: boolean
      displayName: Disable Resize
      name: disableResize
- id: save
  name: Save Profile on Termination
  description: Save in a profile changes made in your browsing session such as cookies
    and local storage
  params: []
- id: terminate
  name: Terminate Session
  description: Terminate a session
- id: waitForDownload
  name: Wait for Download
  description: Wait for a file download to become available
- id: close
  name: Close Window
  description: Close a window inside a session
- id: getLiveView
  name: Get Live View
  description: Get information about a browser window, including the live view URL
  params: []
- id: list
  name: List Windows
  description: List all browser windows in a session
- id: load
  name: Load URL
  description: Load a URL in an existing window
  params: []
- id: takeScreenshot
  name: Take Screenshot
  description: Take a screenshot of the current window
  params:
  - id: outputImageAsBinary
    name: Output Binary Image
    type: boolean
    default: false
    required: false
    description: Whether to output the image as a binary file instead of a base64
      encoded string
    validation:
      displayOptions:
        show:
          resource:
          - window
          operation:
          - takeScreenshot
    typeInfo:
      type: boolean
      displayName: Output Binary Image
      name: outputImageAsBinary
- id: deleteFile
  name: Delete
  description: Delete an uploaded file
  params:
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: true
    description: ID of the file to delete
    validation:
      required: true
    typeInfo:
      type: string
      displayName: File ID
      name: fileId
- id: get
  name: Get
  description: Get a details of an uploaded file
- id: getMany
  name: Get Many
  description: Get details of multiple uploaded files
  params:
  - id: limit
    name: Limit
    type: number
    default: 10
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          resource:
          - file
          operation:
          - getMany
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
- id: upload
  name: Upload
  description: Upload a file into a session
- id: query
  name: Query Page
  description: Query a page to extract data or ask a question given the data on the
    page
  params:
  - id: prompt
    name: Prompt
    type: string
    default: ''
    required: true
    description: The prompt to query the page content
    placeholder: e.g. Is there a login form in this page?
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - extraction
          operation:
          - query
    typeInfo: &id002
      type: string
      displayName: Prompt
      name: prompt
      typeOptions:
        rows: 4
- id: getPaginated
  name: Query Page with Pagination
  description: Extract content from paginated or dynamically loaded pages
  params:
  - id: prompt
    name: Prompt
    type: string
    default: ''
    required: true
    description: The prompt to extract data from the pages
    placeholder: e.g. Extract all the product names and prices
    validation: *id001
    typeInfo: *id002
- id: scrape
  name: Smart Scrape
  description: Scrape a page and return the data as markdown
- id: click
  name: Click an Element
  description: Execute a click on an element given a description
  params:
  - id: clickType
    name: Click Type
    type: options
    default: click
    required: false
    description: The type of click to perform. Defaults to left click.
    validation:
      displayOptions:
        show:
          resource:
          - interaction
          operation:
          - click
    typeInfo:
      type: options
      displayName: Click Type
      name: clickType
      possibleValues:
      - value: click
        name: Left Click
        description: ''
      - value: doubleClick
        name: Double Click
        description: ''
      - value: rightClick
        name: Right Click
        description: ''
- id: fill
  name: Fill Form
  description: Fill a form with the provided information
  params:
  - id: formData
    name: Form Data
    type: string
    default: ''
    required: true
    description: The information to fill into the form written in natural language
    placeholder: 'e.g. "Name: John Doe, Email: john.doe@example.com"'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - interaction
          operation:
          - fill
    typeInfo:
      type: string
      displayName: Form Data
      name: formData
      typeOptions:
        rows: 4
- id: hover
  name: Hover on an Element
  description: Execute a hover action on an element given a description
  params: []
- id: scroll
  name: Scroll
  description: Execute a scroll action on the page
  params:
  - id: scrollingMode
    name: Scroll Mode
    type: options
    default: automatic
    required: true
    description: Choose the mode of scrolling
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - interaction
          operation:
          - scroll
    typeInfo:
      type: options
      displayName: Scroll Mode
      name: scrollingMode
      possibleValues:
      - value: automatic
        name: Automatic
        description: Describe with natural language the element to scroll to
      - value: manual
        name: Manual
        description: Define the direction and amount to scroll by
  - id: scrollToElement
    name: Element Description
    type: string
    default: ''
    required: true
    description: A natural language description of the element to scroll to
    placeholder: e.g. the page section titled "Contact Us"
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - interaction
          operation:
          - scroll
          scrollingMode:
          - automatic
    typeInfo:
      type: string
      displayName: Element Description
      name: scrollToElement
  - id: scrollToEdge
    name: Scroll To Edge
    type: fixedCollection
    default: {}
    required: false
    description: The direction to scroll to. When 'Scroll By' is defined, 'Scroll
      To Edge' action will be executed first, then 'Scroll By' action.
    placeholder: Add Edge Direction
    validation:
      displayOptions:
        show:
          resource:
          - interaction
          operation:
          - scroll
          scrollingMode:
          - manual
    typeInfo:
      type: fixedCollection
      displayName: Scroll To Edge
      name: scrollToEdge
      subProperties:
      - name: edgeValues
        displayName: Page Edges
        values:
        - displayName: Vertically
          name: yAxis
          type: options
          default: ''
          options:
          - name: Empty
            displayName: Empty
          - name: Top
            value: top
            displayName: Top
          - name: Bottom
            value: bottom
            displayName: Bottom
        - displayName: Horizontally
          name: xAxis
          type: options
          default: ''
          options:
          - name: Empty
            displayName: Empty
          - name: Left
            value: left
            displayName: Left
          - name: Right
            value: right
            displayName: Right
  - id: scrollBy
    name: Scroll By
    type: fixedCollection
    default: {}
    required: false
    description: The amount to scroll by. When 'Scroll To Edge' is defined, 'Scroll
      By' action will be executed after 'Scroll To Edge'.
    placeholder: Add Scroll Amount
    validation:
      displayOptions:
        show:
          resource:
          - interaction
          operation:
          - scroll
          scrollingMode:
          - manual
    typeInfo:
      type: fixedCollection
      displayName: Scroll By
      name: scrollBy
      subProperties:
      - name: scrollValues
        displayName: Scroll Values
        values:
        - displayName: Vertically
          name: yAxis
          type: string
          placeholder: e.g. 200px, 50%, -100px
          default: ''
        - displayName: Horizontally
          name: xAxis
          type: string
          placeholder: e.g. 50px, 10%, -200px
          default: ''
  - id: scrollWithin
    name: Scrollable Area
    type: string
    default: ''
    required: false
    description: Scroll within an element on the page
    placeholder: e.g. the left sidebar
    validation:
      displayOptions:
        show:
          resource:
          - interaction
          operation:
          - scroll
    typeInfo:
      type: string
      displayName: Scrollable Area
      name: scrollWithin
- id: type
  name: Type
  description: Execute a Type action on an element given a description
  params:
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: The text to type into the browser window
    placeholder: e.g. email@example.com
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - interaction
          operation:
          - type
    typeInfo:
      type: string
      displayName: Text
      name: text
  - id: pressEnterKey
    name: Press Enter Key
    type: boolean
    default: false
    required: false
    description: Whether to press the Enter key after typing the text
    validation:
      displayOptions:
        show:
          resource:
          - interaction
          operation:
          - type
    typeInfo:
      type: boolean
      displayName: Press Enter Key
      name: pressEnterKey
common_expressions:
- ={{ $json["sessionId"] }}
- ={{ $json["windowId"] }}
- '={{ $parameter["operation"] + ": " + $parameter["resource"] }}'
api_patterns:
  http_methods:
  - GET
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: notice
    text: 'Note: This operation is not needed if you enabled ''Save Profile'' in the
      ''Create Session'' operation'
    conditions:
      show:
        resource:
        - session
        operation:
        - save
  tooltips: []
  placeholders:
  - field: proxyConfig
    text: Add Attribute
  - field: additionalFields
    text: Add Field
  - field: profileName
    text: e.g. my-x-profile
  - field: screenResolution
    text: e.g. 1280x720
  - field: additionalFields
    text: Add Field
  - field: url
    text: e.g. https://google.com
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: sessionIds
    text: e.g. 6aac6f73-bd89-4a76-ab32-5a6c422e8b0b, a13c6f73-bd89-4a76-ab32-5a6c422e8224
  - field: elementDescription
    text: e.g. the search box at the top of the page
  - field: prompt
    text: e.g. Extract all the product names and prices
  - field: additionalFields
    text: Add Field
  - field: prompt
    text: e.g. Is there a login form in this page?
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: formData
    text: 'e.g. "Name: John Doe, Email: john.doe@example.com"'
  - field: scrollToElement
    text: e.g. the page section titled "Contact Us"
  - field: scrollToEdge
    text: Add Edge Direction
  - field: scrollBy
    text: Add Scroll Amount
  - field: scrollWithin
    text: e.g. the left sidebar
  - field: text
    text: e.g. email@example.com
  hints:
  - field: profileName
    text: <a href="https://docs.airtop.ai/guides/how-to/saving-a-profile" target="_blank">Learn
      more</a> about Airtop profiles
  - field: outputSchema
    text: If you want to force your output to be JSON, provide a valid JSON schema
      describing the output. You can generate one automatically in the <a href="https://portal.airtop.ai/"
      target="_blank">Airtop API Playground</a>.
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
  "$id": "https://n8n.io/schemas/nodes/airtop.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Airtop Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "run",
        "create",
        "save",
        "terminate",
        "waitForDownload",
        "close",
        "getLiveView",
        "list",
        "load",
        "takeScreenshot",
        "deleteFile",
        "get",
        "getMany",
        "upload",
        "query",
        "getPaginated",
        "scrape",
        "click",
        "fill",
        "hover",
        "scroll",
        "type"
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
            "agent",
            "extraction",
            "file",
            "interaction",
            "session",
            "window"
          ],
          "default": "session"
        },
        "operation": {
          "description": "Execute a click on an element given a description",
          "type": "string",
          "enum": [
            "click",
            "fill",
            "hover",
            "scroll",
            "type"
          ],
          "default": "click"
        },
        "webhookUrl": {
          "description": "Webhook URL to invoke the Airtop agent. Visit <a href=\"https://portal.airtop.ai/agents\" target=\"_blank\">Airtop Agents</a> for more information.",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "agentParameters": {
          "description": "Agent's input parameters in JSON format. Visit <a href=\"https://portal.airtop.ai/agents\" target=\"_blank\">Airtop Agents</a> for more information.",
          "type": "string",
          "default": "{}"
        },
        "awaitExecution": {
          "description": "Whether to wait for the agent to complete its execution",
          "type": "boolean",
          "default": true
        },
        "timeout": {
          "description": "Timeout in seconds to wait for the agent to finish",
          "type": "number",
          "default": 600
        },
        "saveProfileOnTermination": {
          "description": "Whether to automatically save the <a href=\"https://docs.airtop.ai/guides/how-to/saving-a-profile\" target=\"_blank\">Airtop profile</a> for this session upon termination",
          "type": "boolean",
          "default": false
        },
        "record": {
          "description": "Whether to record the browser session. <a href=\"https://docs.airtop.ai/guides/how-to/recording-a-session\" target=\"_blank\">More details</a>.",
          "type": "boolean",
          "default": false
        },
        "timeoutMinutes": {
          "description": "Minutes to wait before the session is terminated due to inactivity",
          "type": "number",
          "default": 10
        },
        "proxy": {
          "description": "Choose how to configure the proxy for this session",
          "type": "string",
          "enum": [
            "none",
            "integrated",
            "proxyUrl"
          ],
          "default": "none"
        },
        "proxyConfig": {
          "description": "The Airtop-provided configuration to use for the proxy",
          "type": "string",
          "default": "US",
          "examples": [
            "Add Attribute"
          ]
        },
        "proxyUrl": {
          "description": "The URL of the proxy to use",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "additionalFields": {
          "description": "Defines the strategy for visual analysis of the current window",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "profileName": {
          "description": "The name of the Airtop profile to load or create",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. my-x-profile"
          ]
        },
        "sessionId": {
          "description": "The ID of the <a href=\"https://docs.airtop.ai/guides/how-to/creating-a-session\" target=\"_blank\">Session</a> to use",
          "type": "string",
          "default": "={{ $json["
        },
        "windowId": {
          "description": "The ID of the <a href=\"https://docs.airtop.ai/guides/how-to/creating-a-session#windows\" target=\"_blank\">Window</a> to use",
          "type": "string",
          "default": "={{ $json["
        },
        "getLiveView": {
          "description": "Whether to get the URL of the window's <a href=\"https://docs.airtop.ai/guides/how-to/creating-a-live-view\" target=\"_blank\">Live View</a>",
          "type": "boolean",
          "default": false
        },
        "includeNavigationBar": {
          "description": "Whether to include the navigation bar in the Live View. When enabled, the navigation bar will be visible allowing you to navigate between pages.",
          "type": "boolean",
          "default": false
        },
        "screenResolution": {
          "description": "The screen resolution of the Live View. Setting a resolution will force the window to open at that specific size.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. 1280x720"
          ]
        },
        "disableResize": {
          "description": "Whether to disable the window from being resized in the Live View",
          "type": "boolean",
          "default": false
        },
        "url": {
          "description": "URL from where to fetch the file to upload",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "outputImageAsBinary": {
          "description": "Whether to output the image as a binary file instead of a base64 encoded string",
          "type": "boolean",
          "default": false
        },
        "fileId": {
          "description": "ID of the file to load into the session",
          "type": "string",
          "default": ""
        },
        "outputBinaryFile": {
          "description": "Whether to output the file in binary format if the file is ready for download",
          "type": "boolean",
          "default": false
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 10
        },
        "sessionIds": {
          "description": "Comma-separated list of <a href=\"https://docs.airtop.ai/api-reference/airtop-api/sessions/create\" target=\"_blank\">Session IDs</a> to filter files by. When empty, all files from all sessions will be returned.",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. 6aac6f73-bd89-4a76-ab32-5a6c422e8b0b, a13c6f73-bd89-4a76-ab32-5a6c422e8224"
          ]
        },
        "outputSingleItem": {
          "description": "Whether to output one item containing all files or output each file as a separate item",
          "type": "boolean",
          "default": true
        },
        "elementDescription": {
          "description": "A specific description of the element to execute the interaction on",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. the search box at the top of the page"
          ]
        },
        "includeHiddenElements": {
          "description": "Whether to include hidden elements in the interaction",
          "type": "boolean",
          "default": true
        },
        "fileName": {
          "description": "Name for the file to upload. For a session, all files loaded should have <b>unique names</b>.",
          "type": "string",
          "default": ""
        },
        "fileType": {
          "description": "Choose the type of file to upload. Defaults to 'Customer Upload'.",
          "type": "string",
          "enum": [
            "browser_download",
            "screenshot",
            "video",
            "customer_upload"
          ],
          "default": "customer_upload"
        },
        "source": {
          "description": "Source of the file to upload",
          "type": "string",
          "enum": [
            "url",
            "binary"
          ],
          "default": "url"
        },
        "binaryPropertyName": {
          "description": "Name of the binary property containing the file data",
          "type": "string",
          "default": "data"
        },
        "triggerFileInputParameter": {
          "description": "Whether to automatically trigger the file input dialog in the current window. If disabled, the file will only be uploaded to the session without opening the file input dialog.",
          "type": "boolean",
          "default": true
        },
        "prompt": {
          "description": "The prompt to query the page content",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Is there a login form in this page?"
          ]
        },
        "outputSchema": {
          "description": "JSON schema defining the structure of the output",
          "type": "string",
          "default": ""
        },
        "parseJsonOutput": {
          "description": "Whether to parse the model's response to JSON in the output. Requires the 'JSON Output Schema' parameter to be set.",
          "type": "boolean",
          "default": true
        },
        "clickType": {
          "description": "The type of click to perform. Defaults to left click.",
          "type": "string",
          "enum": [
            "click",
            "doubleClick",
            "rightClick"
          ],
          "default": "click"
        },
        "formData": {
          "description": "The information to fill into the form written in natural language",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. \"Name: John Doe, Email: john.doe@example.com\""
          ]
        },
        "scrollingMode": {
          "description": "Choose the mode of scrolling",
          "type": "string",
          "enum": [
            "automatic",
            "manual"
          ],
          "default": "automatic"
        },
        "scrollToElement": {
          "description": "A natural language description of the element to scroll to",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. the page section titled \"Contact Us\""
          ]
        },
        "scrollToEdge": {
          "description": "The direction to scroll to. When 'Scroll By' is defined, 'Scroll To Edge' action will be executed first, then 'Scroll By' action.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Edge Direction"
          ]
        },
        "scrollBy": {
          "description": "The amount to scroll by. When 'Scroll To Edge' is defined, 'Scroll By' action will be executed after 'Scroll To Edge'.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Scroll Amount"
          ]
        },
        "scrollWithin": {
          "description": "Scroll within an element on the page",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. the left sidebar"
          ]
        },
        "text": {
          "description": "The text to type into the browser window",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. email@example.com"
          ]
        },
        "pressEnterKey": {
          "description": "Whether to press the Enter key after typing the text",
          "type": "boolean",
          "default": false
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
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "airtopApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
