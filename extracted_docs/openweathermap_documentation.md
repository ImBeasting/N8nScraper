---
title: "Node: OpenWeatherMap"
slug: "node-openweathermap"
version: "1"
updated: "2026-01-08"
summary: "Gets current and future weather information"
node_type: "regular"
group: "['input']"
---

# Node: OpenWeatherMap

**Purpose.** Gets current and future weather information


---

## Node Details

- **Icon:** `file:openWeatherMap.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **openWeatherMapApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `openWeatherMapApi` | ✓ | - |

---

## Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Current Weather | `currentWeather` | Returns the current weather data |
| 5 Day Forecast | `5DayForecast` | Returns the weather data for the next 5 days |

---

## Parameters

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | currentWeather | ✗ | Returns the current weather data |  |

**Operation options:**

* **Current Weather** (`currentWeather`) - Returns the current weather data
* **5 Day Forecast** (`5DayForecast`) - Returns the weather data for the next 5 days

---

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
* Categories: Miscellaneous, Utility

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: openWeatherMap
displayName: OpenWeatherMap
description: Gets current and future weather information
version: '1'
nodeType: regular
group:
- input
credentials:
- name: openWeatherMapApi
  required: true
operations:
- id: currentWeather
  name: Current Weather
  description: Returns the current weather data
- id: 5DayForecast
  name: 5 Day Forecast
  description: Returns the weather data for the next 5 days
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: cityName
    text: berlin,de
  - field: latitude
    text: '13.39'
  - field: longitude
    text: '52.52'
  - field: zipCode
    text: 10115,de
  - field: language
    text: en
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
  "$id": "https://n8n.io/schemas/nodes/openWeatherMap.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "OpenWeatherMap Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "currentWeather",
        "5DayForecast"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operation": {
          "description": "Returns the current weather data",
          "type": "string",
          "enum": [
            "currentWeather",
            "5DayForecast"
          ],
          "default": "currentWeather"
        },
        "format": {
          "description": "Fahrenheit | miles/hour",
          "type": "string",
          "enum": [
            "imperial",
            "metric",
            "standard"
          ],
          "default": "metric"
        },
        "locationSelection": {
          "description": "How to define the location for which to return the weather",
          "type": "string",
          "enum": [
            "cityName",
            "cityId",
            "coordinates",
            "zipCode"
          ],
          "default": "cityName"
        },
        "cityName": {
          "description": "The name of the city to return the weather of",
          "type": "string",
          "default": "",
          "examples": [
            "berlin,de"
          ]
        },
        "cityId": {
          "description": "The ID of city to return the weather of. List can be downloaded here: http://bulk.openweathermap.org/sample/.",
          "type": "number",
          "default": 160001123
        },
        "latitude": {
          "description": "The latitude of the location to return the weather of",
          "type": "string",
          "default": "",
          "examples": [
            "13.39"
          ]
        },
        "longitude": {
          "description": "The longitude of the location to return the weather of",
          "type": "string",
          "default": "",
          "examples": [
            "52.52"
          ]
        },
        "zipCode": {
          "description": "The ID of city to return the weather of. List can be downloaded here: http://bulk.openweathermap.org/sample/.",
          "type": "string",
          "default": "",
          "examples": [
            "10115,de"
          ]
        },
        "language": {
          "description": "The two letter language code to get your output in (eg. en, de, ...).",
          "type": "string",
          "default": "",
          "examples": [
            "en"
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
      "name": "openWeatherMapApi",
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
