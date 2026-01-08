---
title: "Node: QuickChart"
slug: "node-quickchart"
version: "1"
updated: "2026-01-08"
summary: "Create a chart via QuickChart"
node_type: "regular"
group: "['output']"
---

# Node: QuickChart

**Purpose.** Create a chart via QuickChart


---

## Node Details

- **Icon:** `file:quickChart.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chart Type | `chartType` | options | bar | ✗ | The type of chart to create |  |
| Add Labels | `labelsMode` | options | manually | ✗ |  |  |

**Add Labels options:**

* **Manually** (`manually`)
* **From Array** (`array`)

| Labels | `labelsUi` | fixedCollection | {} | ✓ | Labels to use in the chart | e.g. Add Label |  |

<details>
<summary><strong>Labels sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Labels | `labelsValues` |  |  |  |

</details>

| Labels Array | `labelsArray` | string |  | ✓ | The array of labels to be used in the chart | e.g. e.g. ["Berlin", "Paris", "Rome", "New York"] |  |
| Data | `data` | json |  | ✓ | Data to use for the dataset, documentation and examples <a href="https://quickchart.io/documentation/chart-types/" target="_blank">here</a> | e.g. e.g. [60, 10, 12, 20] |  |
| Put Output In Field | `output` | string | data | ✓ | The binary data will be displayed in the Output panel on the right, under the Binary tab | e.g. The name of the output field to put the binary file data in |  |
| Chart Options | `chartOptions` | collection | {} | ✗ | Background color of the chart | e.g. Add option |  |

<details>
<summary><strong>Chart Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Background Color | `backgroundColor` | color |  | Background color of the chart |
| Device Pixel Ratio | `devicePixelRatio` | number | 2 | Pixel ratio of the chart |
| Format | `format` | options | png | File format of the resulting chart |
| Height | `height` | number | 300 | Height of the chart |
| Horizontal | `horizontal` | boolean | False | Whether the chart should use its Y axis horizontal |
| Width | `width` | number | 500 | Width of the chart |

</details>

| Dataset Options | `datasetOptions` | collection | {} | ✗ | Color used for the background the dataset (area of a line graph, fill of a bar chart, etc.) | e.g. Add option |  |

<details>
<summary><strong>Dataset Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Background Color | `backgroundColor` | color |  | Color used for the background the dataset (area of a line graph, fill of a bar chart, etc.) |
| Border Color | `borderColor` | color |  | Color used for lines of the dataset |
| Fill | `fill` | boolean | True | Whether to fill area of the dataset |
| Label | `label` | string |  | The label of the dataset |
| Point Style | `pointStyle` | options | circle | Style to use for points of the dataset |

</details>

| Bar Chart | `Bar Chart` |  |  | ✗ |  |  |
| Doughnut Chart | `Doughnut Chart` |  |  | ✗ |  |  |
| Line Chart | `Line Chart` |  |  | ✗ |  |  |
| Pie Chart | `Pie Chart` |  |  | ✗ |  |  |
| Polar Chart | `Polar Chart` |  |  | ✗ |  |  |

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: BarChart

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "labelsUi": {
    "labelsValues": [
      {
        "label": "Q1"
      },
      {
        "label": "Q2"
      },
      {
        "label": "Q3"
      },
      {
        "label": "Q4"
      }
    ]
  },
  "data": "={{ $json.data }}",
  "chartOptions": {
    "backgroundColor": "#f93636ff",
    "devicePixelRatio": 2,
    "format": "png",
    "height": 300,
    "horizontal": true,
    "width": 500
  },
  "datasetOptions": {
    "backgroundColor": "={{ $json[\"backgroundColor\"] }}",
    "borderColor": "#e81010",
    "label": "={{ $json[\"label\"] }}"
  }
}
```

### Example 2: Doughnut

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "chartType": "doughnut",
  "labelsUi": {
    "labelsValues": [
      {
        "label": "Q1"
      },
      {
        "label": "Q2"
      },
      {
        "label": "Q3"
      },
      {
        "label": "Q4"
      }
    ]
  },
  "data": "={{ $json.data }}",
  "chartOptions": {
    "backgroundColor": "#f93636ff",
    "devicePixelRatio": 2,
    "format": "png",
    "height": 300,
    "width": 500
  },
  "datasetOptions": {
    "backgroundColor": "={{ $json[\"backgroundColor\"] }}",
    "borderColor": "#e81010",
    "label": "={{ $json[\"label\"] }}"
  }
}
```


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
* Categories: Marketing
* Aliases: image, graph, report, chart, diagram, data, visualize

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: quickChart
displayName: QuickChart
description: Create a chart via QuickChart
version: '1'
nodeType: regular
group:
- output
params:
- id: chartType
  name: Chart Type
  type: options
  default: bar
  required: false
  description: The type of chart to create
  typeInfo:
    type: options
    displayName: Chart Type
    name: chartType
    possibleValues: []
- id: labelsMode
  name: Add Labels
  type: options
  default: manually
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Add Labels
    name: labelsMode
    possibleValues:
    - value: manually
      name: Manually
      description: ''
    - value: array
      name: From Array
      description: ''
- id: labelsUi
  name: Labels
  type: fixedCollection
  default: {}
  required: true
  description: Labels to use in the chart
  placeholder: Add Label
  validation:
    required: true
    displayOptions:
      show:
        labelsMode:
        - manually
  typeInfo:
    type: fixedCollection
    displayName: Labels
    name: labelsUi
    typeOptions:
      multipleValues: true
    subProperties:
    - name: labelsValues
      displayName: Labels
      values:
      - displayName: Label
        name: label
        type: string
        default: ''
- id: labelsArray
  name: Labels Array
  type: string
  default: ''
  required: true
  description: The array of labels to be used in the chart
  placeholder: e.g. ["Berlin", "Paris", "Rome", "New York"]
  validation:
    required: true
    displayOptions:
      show:
        labelsMode:
        - array
  typeInfo:
    type: string
    displayName: Labels Array
    name: labelsArray
- id: data
  name: Data
  type: json
  default: ''
  required: true
  description: Data to use for the dataset, documentation and examples <a href="https://quickchart.io/documentation/chart-types/"
    target="_blank">here</a>
  placeholder: e.g. [60, 10, 12, 20]
  validation:
    required: true
  typeInfo:
    type: json
    displayName: Data
    name: data
- id: output
  name: Put Output In Field
  type: string
  default: data
  required: true
  description: The binary data will be displayed in the Output panel on the right,
    under the Binary tab
  hint: The name of the output field to put the binary file data in
  validation:
    required: true
  typeInfo:
    type: string
    displayName: Put Output In Field
    name: output
- id: chartOptions
  name: Chart Options
  type: collection
  default: {}
  required: false
  description: Background color of the chart
  placeholder: Add option
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Chart Options
    name: chartOptions
    subProperties:
    - displayName: Background Color
      name: backgroundColor
      type: color
      description: Background color of the chart
      default: ''
      typeOptions: {}
    - displayName: Device Pixel Ratio
      name: devicePixelRatio
      type: number
      description: Pixel ratio of the chart
      default: 2
      typeOptions:
        minValue: 1
        maxValue: 2
    - displayName: Format
      name: format
      type: options
      description: File format of the resulting chart
      value: png
      default: png
      options:
      - name: PNG
        value: png
        displayName: Png
      - name: PDF
        value: pdf
        displayName: Pdf
      - name: SVG
        value: svg
        displayName: Svg
      - name: WebP
        value: webp
        displayName: Web P
    - displayName: Height
      name: height
      type: number
      description: Height of the chart
      default: 300
    - displayName: Horizontal
      name: horizontal
      type: boolean
      description: Whether the chart should use its Y axis horizontal
      default: false
      displayOptions:
        show: {}
    - displayName: Width
      name: width
      type: number
      description: Width of the chart
      default: 500
- id: datasetOptions
  name: Dataset Options
  type: collection
  default: {}
  required: false
  description: Color used for the background the dataset (area of a line graph, fill
    of a bar chart, etc.)
  placeholder: Add option
  validation:
    displayOptions:
      show: {}
  typeInfo:
    type: collection
    displayName: Dataset Options
    name: datasetOptions
    subProperties:
    - displayName: Background Color
      name: backgroundColor
      type: color
      description: Color used for the background the dataset (area of a line graph,
        fill of a bar chart, etc.)
      default: ''
      typeOptions: {}
    - displayName: Border Color
      name: borderColor
      type: color
      description: Color used for lines of the dataset
      default: ''
      typeOptions: {}
    - displayName: Fill
      name: fill
      type: boolean
      description: Whether to fill area of the dataset
      default: true
      displayOptions:
        show: {}
    - displayName: Label
      name: label
      type: string
      description: The label of the dataset
      default: ''
    - displayName: Point Style
      name: pointStyle
      type: options
      description: Style to use for points of the dataset
      value: circle
      default: circle
      options:
      - name: Circle
        value: circle
        displayName: Circle
      - name: Cross
        value: cross
        displayName: Cross
      - name: CrossRot
        value: crossRot
        displayName: Cross Rot
      - name: Dash
        value: dash
        displayName: Dash
      - name: Line
        value: line
        displayName: Line
      - name: Rect
        value: rect
        displayName: Rect
      - name: Rect Rot
        value: rectRot
        displayName: Rect Rot
      - name: Rect Rounded
        value: rectRounded
        displayName: Rect Rounded
      - name: Star
        value: star
        displayName: Star
      - name: Triangle
        value: triangle
        displayName: Triangle
      displayOptions:
        show: {}
- id: Bar Chart
  name: Bar Chart
  type: ''
  default: ''
  required: false
  description: ''
  typeInfo:
    type: unknown
    displayName: Bar Chart
    name: Bar Chart
- id: Doughnut Chart
  name: Doughnut Chart
  type: ''
  default: ''
  required: false
  description: ''
  typeInfo:
    type: unknown
    displayName: Doughnut Chart
    name: Doughnut Chart
- id: Line Chart
  name: Line Chart
  type: ''
  default: ''
  required: false
  description: ''
  typeInfo:
    type: unknown
    displayName: Line Chart
    name: Line Chart
- id: Pie Chart
  name: Pie Chart
  type: ''
  default: ''
  required: false
  description: ''
  typeInfo:
    type: unknown
    displayName: Pie Chart
    name: Pie Chart
- id: Polar Chart
  name: Polar Chart
  type: ''
  default: ''
  required: false
  description: ''
  typeInfo:
    type: unknown
    displayName: Polar Chart
    name: Polar Chart
examples:
- name: BarChart
  parameters:
    labelsUi:
      labelsValues:
      - label: Q1
      - label: Q2
      - label: Q3
      - label: Q4
    data: ={{ $json.data }}
    chartOptions:
      backgroundColor: '#f93636ff'
      devicePixelRatio: 2
      format: png
      height: 300
      horizontal: true
      width: 500
    datasetOptions:
      backgroundColor: ={{ $json["backgroundColor"] }}
      borderColor: '#e81010'
      label: ={{ $json["label"] }}
  workflow: Unnamed workflow
- name: Doughnut
  parameters:
    chartType: doughnut
    labelsUi:
      labelsValues:
      - label: Q1
      - label: Q2
      - label: Q3
      - label: Q4
    data: ={{ $json.data }}
    chartOptions:
      backgroundColor: '#f93636ff'
      devicePixelRatio: 2
      format: png
      height: 300
      width: 500
    datasetOptions:
      backgroundColor: ={{ $json["backgroundColor"] }}
      borderColor: '#e81010'
      label: ={{ $json["label"] }}
  workflow: Unnamed workflow
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: labelsUi
    text: Add Label
  - field: labelsArray
    text: e.g. ["Berlin", "Paris", "Rome", "New York"]
  - field: data
    text: e.g. [60, 10, 12, 20]
  - field: chartOptions
    text: Add option
  - field: datasetOptions
    text: Add option
  hints:
  - field: output
    text: The name of the output field to put the binary file data in
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
  "$id": "https://n8n.io/schemas/nodes/quickChart.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "QuickChart Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "chartType": {
          "description": "The type of chart to create",
          "type": "string",
          "default": "bar"
        },
        "labelsMode": {
          "description": "",
          "type": "string",
          "enum": [
            "manually",
            "array"
          ],
          "default": "manually"
        },
        "labelsUi": {
          "description": "Labels to use in the chart",
          "type": "string",
          "default": {},
          "examples": [
            "Add Label"
          ]
        },
        "labelsArray": {
          "description": "The array of labels to be used in the chart",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. [\"Berlin\", \"Paris\", \"Rome\", \"New York\"]"
          ]
        },
        "data": {
          "description": "Data to use for the dataset, documentation and examples <a href=\"https://quickchart.io/documentation/chart-types/\" target=\"_blank\">here</a>",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. [60, 10, 12, 20]"
          ]
        },
        "output": {
          "description": "The binary data will be displayed in the Output panel on the right, under the Binary tab",
          "type": "string",
          "default": "data"
        },
        "chartOptions": {
          "description": "Background color of the chart",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "datasetOptions": {
          "description": "Color used for the background the dataset (area of a line graph, fill of a bar chart, etc.)",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "Bar Chart": {
          "description": "",
          "type": "string"
        },
        "Doughnut Chart": {
          "description": "",
          "type": "string"
        },
        "Line Chart": {
          "description": "",
          "type": "string"
        },
        "Pie Chart": {
          "description": "",
          "type": "string"
        },
        "Polar Chart": {
          "description": "",
          "type": "string"
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
  "examples": [
    {
      "description": "BarChart",
      "value": {
        "labelsUi": {
          "labelsValues": [
            {
              "label": "Q1"
            },
            {
              "label": "Q2"
            },
            {
              "label": "Q3"
            },
            {
              "label": "Q4"
            }
          ]
        },
        "data": "={{ $json.data }}",
        "chartOptions": {
          "backgroundColor": "#f93636ff",
          "devicePixelRatio": 2,
          "format": "png",
          "height": 300,
          "horizontal": true,
          "width": 500
        },
        "datasetOptions": {
          "backgroundColor": "={{ $json[\"backgroundColor\"] }}",
          "borderColor": "#e81010",
          "label": "={{ $json[\"label\"] }}"
        }
      }
    },
    {
      "description": "Doughnut",
      "value": {
        "chartType": "doughnut",
        "labelsUi": {
          "labelsValues": [
            {
              "label": "Q1"
            },
            {
              "label": "Q2"
            },
            {
              "label": "Q3"
            },
            {
              "label": "Q4"
            }
          ]
        },
        "data": "={{ $json.data }}",
        "chartOptions": {
          "backgroundColor": "#f93636ff",
          "devicePixelRatio": 2,
          "format": "png",
          "height": 300,
          "width": 500
        },
        "datasetOptions": {
          "backgroundColor": "={{ $json[\"backgroundColor\"] }}",
          "borderColor": "#e81010",
          "label": "={{ $json[\"label\"] }}"
        }
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
