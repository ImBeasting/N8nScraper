---
title: "Node: NASA"
slug: "node-nasa"
version: "1"
updated: "2025-11-13"
summary: "Retrieve data from the NASA API"
node_type: "regular"
group: "['transform']"
---

# Node: NASA

**Purpose.** Retrieve data from the NASA API
**Subtitle.** ={{$parameter["operation"] + ":" + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:nasa.png`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **nasaApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `nasaApi` | ✓ | - |

---

## Operations

### Astronomypictureoftheday Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get the Astronomy Picture of the Day |

### Asteroidneofeed Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve a list of asteroids based on their closest approach date to Earth |

### Asteroidneolookup Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Look up an asteroid based on its NASA SPK-ID |

### Asteroidneobrowse Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Browse the overall asteroid dataset |

### Donkicoronalmassejection Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve DONKI coronal mass ejection data |

### Donkigeomagneticstorm Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve DONKI geomagnetic storm data |

### Donkiinterplanetaryshock Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve DONKI interplanetary shock data |

### Donkisolarflare Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve DONKI solar flare data |

### Donkisolarenergeticparticle Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve DONKI solar energetic particle data |

### Donkimagnetopausecrossing Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve data on DONKI magnetopause crossings |

### Donkiradiationbeltenhancement Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve DONKI radiation belt enhancement data |

### Donkihighspeedstream Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve DONKI high speed stream data |

### Donkiwsaenlilsimulation Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve DONKI WSA+EnlilSimulation data |

### Donkinotifications Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve DONKI notifications data |

### Earthimagery Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve Earth imagery |

### Earthassets Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve Earth assets |

### Insightmarsweatherservice Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve Insight Mars Weather Service data |

### Imageandvideolibrary Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve Image and Video Library data |

### Techtransfer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve TechTransfer data |

### Twolineelementset Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve Two-Line Element Set data |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | astronomyPictureOfTheDay | ✗ | Resource to operate on |  |

**Resource options:**

* **Asteroid Neo-Browse** (`asteroidNeoBrowse`)
* **Asteroid Neo-Feed** (`asteroidNeoFeed`)
* **Asteroid Neo-Lookup** (`asteroidNeoLookup`)
* **Astronomy Picture of the Day** (`astronomyPictureOfTheDay`)
* **DONKI Coronal Mass Ejection** (`donkiCoronalMassEjection`)
* **DONKI High Speed Stream** (`donkiHighSpeedStream`)
* **DONKI Geomagnetic Storm** (`donkiGeomagneticStorm`)
* **DONKI Interplanetary Shock** (`donkiInterplanetaryShock`)
* **DONKI Magnetopause Crossing** (`donkiMagnetopauseCrossing`)
* **DONKI Notification** (`donkiNotifications`)
* **DONKI Radiation Belt Enhancement** (`donkiRadiationBeltEnhancement`)
* **DONKI Solar Energetic Particle** (`donkiSolarEnergeticParticle`)
* **DONKI Solar Flare** (`donkiSolarFlare`)
* **DONKI WSA+EnlilSimulation** (`donkiWsaEnlilSimulation`)
* **Earth Asset** (`earthAssets`)
* **Earth Imagery** (`earthImagery`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | get | ✗ | Get the Astronomy Picture of the Day |  |

**Operation options:**

* **Get** (`get`) - Get the Astronomy Picture of the Day

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Asteroid ID | `asteroidId` | string |  | ✓ | The ID of the asteroid to be returned | e.g. 3542519 |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include all the close approach data in the asteroid lookup | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Close Approach Data | `includeCloseApproachData` | boolean | False | Whether to include all the close approach data in the asteroid lookup |

</details>

| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date | `date` | dateTime |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Start Date | `startDate` | dateTime |  |  |
| End Date | `endDate` | dateTime |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | The location of the geomagnetic storm | e.g. Add field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Start Date | `startDate` | dateTime |  |  |
| End Date | `endDate` | dateTime |  |  |
| Location | `location` | options | ALL | The location of the geomagnetic storm |
| Catalog | `catalog` | options | ALL | The catalog of the geomagnetic storm |

</details>

| Latitude | `lat` | number |  | ✗ | Latitude for the location of the image | e.g. 47.751076 |  |
| Longitude | `lon` | number |  | ✗ | Longitude for the location of the image | e.g. -120.740135 |  |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Date of the image | e.g. Add field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date | `date` | dateTime |  | Date of the image |
| Degrees | `dim` | number |  | Width and height of the image in degrees |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ":" + $parameter["resource"]}}`

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
node: nasa
displayName: NASA
description: Retrieve data from the NASA API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: nasaApi
  required: true
operations:
- id: get
  name: Get
  description: Get the Astronomy Picture of the Day
  params:
  - id: asteroidId
    name: Asteroid ID
    type: string
    default: ''
    required: true
    description: The ID of the asteroid to be returned
    placeholder: '3542519'
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - asteroidNeoLookup
          operation:
          - get
    typeInfo:
      type: string
      displayName: Asteroid ID
      name: asteroidId
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - earthImagery
    typeInfo: &id002
      type: string
      displayName: Put Output File in Field
      name: binaryPropertyName
  - id: lat
    name: Latitude
    type: number
    default: ''
    required: false
    description: Latitude for the location of the image
    placeholder: '47.751076'
    validation:
      displayOptions:
        show:
          resource:
          - earthImagery
          - earthAssets
          operation:
          - get
    typeInfo:
      type: number
      displayName: Latitude
      name: lat
  - id: lon
    name: Longitude
    type: number
    default: ''
    required: false
    description: Longitude for the location of the image
    placeholder: '-120.740135'
    validation:
      displayOptions:
        show:
          resource:
          - earthImagery
          - earthAssets
          operation:
          - get
    typeInfo:
      type: number
      displayName: Longitude
      name: lon
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Browse the overall asteroid dataset
  params:
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
          - getAll
    typeInfo:
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 20
    required: false
    description: Max number of results to return
    validation:
      displayOptions:
        show:
          operation:
          - getAll
          returnAll:
          - false
    typeInfo:
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
common_expressions:
- ={{$parameter["operation"] + ":" + $parameter["resource"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: asteroidId
    text: '3542519'
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add field
  - field: additionalFields
    text: Add field
  - field: additionalFields
    text: Add field
  - field: lat
    text: '47.751076'
  - field: lon
    text: '-120.740135'
  - field: additionalFields
    text: Add field
  hints:
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
  - field: binaryPropertyName
    text: The name of the output binary field to put the file in
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
  "$id": "https://n8n.io/schemas/nodes/nasa.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "NASA Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll"
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
            "asteroidNeoBrowse",
            "asteroidNeoFeed",
            "asteroidNeoLookup",
            "astronomyPictureOfTheDay",
            "donkiCoronalMassEjection",
            "donkiHighSpeedStream",
            "donkiGeomagneticStorm",
            "donkiInterplanetaryShock",
            "donkiMagnetopauseCrossing",
            "donkiNotifications",
            "donkiRadiationBeltEnhancement",
            "donkiSolarEnergeticParticle",
            "donkiSolarFlare",
            "donkiWsaEnlilSimulation",
            "earthAssets",
            "earthImagery"
          ],
          "default": "astronomyPictureOfTheDay"
        },
        "operation": {
          "description": "Retrieve Two-Line Element Set data",
          "type": "string",
          "enum": [
            "get"
          ],
          "default": "get"
        },
        "asteroidId": {
          "description": "The ID of the asteroid to be returned",
          "type": "string",
          "default": "",
          "examples": [
            "3542519"
          ]
        },
        "additionalFields": {
          "description": "Date of the image",
          "type": "string",
          "default": {},
          "examples": [
            "Add field"
          ]
        },
        "download": {
          "description": "By default just the URL of the image is returned. When set to true the image will be downloaded.",
          "type": "boolean",
          "default": true
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "lat": {
          "description": "Latitude for the location of the image",
          "type": "number",
          "default": "",
          "examples": [
            "47.751076"
          ]
        },
        "lon": {
          "description": "Longitude for the location of the image",
          "type": "number",
          "default": "",
          "examples": [
            "-120.740135"
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
          "default": 20
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
      "name": "nasaApi",
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
