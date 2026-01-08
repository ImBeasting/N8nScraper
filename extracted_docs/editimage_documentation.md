---
title: "Node: Edit Image"
slug: "node-editimage"
version: "1"
updated: "2026-01-08"
summary: "Edits an image like blur, resize or adding border and text"
node_type: "regular"
group: "['transform']"
---

# Node: Edit Image

**Purpose.** Edits an image like blur, resize or adding border and text


---

## Node Details

- **Icon:** `fa:image`
- **Group:** `['transform']`
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
| Background Color | `backgroundColor` | color | #ffffff00 | ✗ | The background color of the image to create |  |
| Image Width | `width` | number | 50 | ✗ | The width of the image to create | min:1, max:∞ |
| Image Height | `height` | number | 50 | ✗ | The height of the image to create | min:1, max:∞ |
| Primitive | `primitive` | options | rectangle | ✗ | The primitive to draw |  |

**Primitive options:**

* **Circle** (`circle`)
* **Line** (`line`)
* **Rectangle** (`rectangle`)

| Color | `color` | color | #ff000000 | ✗ | The color of the primitive to draw |  |
| Start Position X | `startPositionX` | number | 50 | ✗ | X (horizontal) start position of the primitive |  |
| Start Position Y | `startPositionY` | number | 50 | ✗ | Y (horizontal) start position of the primitive |  |
| End Position X | `endPositionX` | number | 250 | ✗ | X (horizontal) end position of the primitive |  |
| End Position Y | `endPositionY` | number | 250 | ✗ | Y (horizontal) end position of the primitive |  |
| Corner Radius | `cornerRadius` | number | 0 | ✗ | The radius of the corner to create round corners |  |
| Text | `text` | string |  | ✗ | Text to write on the image | e.g. Text to render |  |
| Font Size | `fontSize` | number | 18 | ✗ | Size of the text |  |
| Font Color | `fontColor` | color | #000000 | ✗ | Color of the text |  |
| Position X | `positionX` | number | 50 | ✗ | X (horizontal) position of the text |  |
| Position Y | `positionY` | number | 50 | ✗ | Y (vertical) position of the text |  |
| Max Line Length | `lineLength` | number | 80 | ✗ | Max amount of characters in a line before a line-break should get added | min:1, max:∞ |
| Blur | `blur` | number | 5 | ✗ | How strong the blur should be | min:0, max:1000 |
| Sigma | `sigma` | number | 2 | ✗ | The sigma of the blur | min:0, max:1000 |
| Border Width | `borderWidth` | number | 10 | ✗ | The width of the border |  |
| Border Height | `borderHeight` | number | 10 | ✗ | The height of the border |  |
| Border Color | `borderColor` | color | #000000 | ✗ | Color of the border |  |
| Composite Image Property | `dataPropertyNameComposite` | string |  | ✗ | The name of the binary property which contains the data of the image to composite on top of image which is found in Property Name | e.g. data2 |  |
| Operator | `operator` | options | Over | ✗ | The operator to use to combine the images |  |

**Operator options:**

* **Add** (`Add`)
* **Atop** (`Atop`)
* **Bumpmap** (`Bumpmap`)
* **Copy** (`Copy`)
* **Copy Black** (`CopyBlack`)
* **Copy Blue** (`CopyBlue`)
* **Copy Cyan** (`CopyCyan`)
* **Copy Green** (`CopyGreen`)
* **Copy Magenta** (`CopyMagenta`)
* **Copy Opacity** (`CopyOpacity`)
* **Copy Red** (`CopyRed`)
* **Copy Yellow** (`CopyYellow`)
* **Difference** (`Difference`)
* **Divide** (`Divide`)
* **In** (`In`)
* **Minus** (`Minus`)
* **Multiply** (`Multiply`)
* **Out** (`Out`)
* **Over** (`Over`)
* **Plus** (`Plus`)
* **Subtract** (`Subtract`)
* **Xor** (`Xor`)

| Position X | `positionX` | number | 0 | ✗ | X (horizontal) position of composite image |  |
| Position Y | `positionY` | number | 0 | ✗ | Y (vertical) position of composite image |  |
| Width | `width` | number | 500 | ✗ | Crop width |  |
| Height | `height` | number | 500 | ✗ | Crop height |  |
| Position X | `positionX` | number | 0 | ✗ | X (horizontal) position to crop from |  |
| Position Y | `positionY` | number | 0 | ✗ | Y (vertical) position to crop from |  |
| Width | `width` | number | 500 | ✗ | New width of the image |  |
| Height | `height` | number | 500 | ✗ | New height of the image |  |
| Option | `resizeOption` | options | maximumArea | ✗ | Ignore aspect ratio and resize exactly to specified values |  |

**Option options:**

* **Ignore Aspect Ratio** (`ignoreAspectRatio`) - Ignore aspect ratio and resize exactly to specified values
* **Maximum Area** (`maximumArea`) - Specified values are maximum area
* **Minimum Area** (`minimumArea`) - Specified values are minimum area
* **Only if Larger** (`onlyIfLarger`) - Resize only if image is larger than width or height
* **Only if Smaller** (`onlyIfSmaller`) - Resize only if image is smaller than width or height
* **Percent** (`percent`) - Width and height are specified in percents

| Rotate | `rotate` | number | 0 | ✗ | How much the image should be rotated | min:∞, max:360 |
| Background Color | `backgroundColor` | color | #ffffffff | ✗ | The color to use for the background when image gets rotated by anything which is not a multiple of 90 |  |
| Degrees X | `degreesX` | number | 0 | ✗ | X (horizontal) shear degrees |  |
| Degrees Y | `degreesY` | number | 0 | ✗ | Y (vertical) shear degrees |  |
| Color | `color` | color | #ff0000 | ✗ | The color to make transparent |  |

---

## Load Options Methods

- `getFonts`
- `if`

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
* Categories: Marketing, Core Nodes

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: editImage
displayName: Edit Image
description: Edits an image like blur, resize or adding border and text
version: '1'
nodeType: regular
group:
- transform
params:
- id: backgroundColor
  name: Background Color
  type: color
  default: '#ffffff00'
  required: false
  description: The background color of the image to create
  validation: &id009
    displayOptions:
      show:
        operation:
        - rotate
  typeInfo: &id010
    type: color
    displayName: Background Color
    name: backgroundColor
- id: width
  name: Image Width
  type: number
  default: 50
  required: false
  description: The width of the image to create
  validation: &id005
    displayOptions:
      show:
        operation:
        - resize
  typeInfo: &id006
    type: number
    displayName: Width
    name: width
- id: height
  name: Image Height
  type: number
  default: 50
  required: false
  description: The height of the image to create
  validation: &id007
    displayOptions:
      show:
        operation:
        - resize
  typeInfo: &id008
    type: number
    displayName: Height
    name: height
- id: primitive
  name: Primitive
  type: options
  default: rectangle
  required: false
  description: The primitive to draw
  validation:
    displayOptions:
      show:
        operation:
        - draw
  typeInfo:
    type: options
    displayName: Primitive
    name: primitive
    possibleValues:
    - value: circle
      name: Circle
      description: ''
    - value: line
      name: Line
      description: ''
    - value: rectangle
      name: Rectangle
      description: ''
- id: color
  name: Color
  type: color
  default: '#ff000000'
  required: false
  description: The color of the primitive to draw
  validation: &id011
    displayOptions:
      show:
        operation:
        - transparent
  typeInfo: &id012
    type: color
    displayName: Color
    name: color
- id: startPositionX
  name: Start Position X
  type: number
  default: 50
  required: false
  description: X (horizontal) start position of the primitive
  validation:
    displayOptions:
      show:
        operation:
        - draw
        primitive:
        - circle
        - line
        - rectangle
  typeInfo:
    type: number
    displayName: Start Position X
    name: startPositionX
- id: startPositionY
  name: Start Position Y
  type: number
  default: 50
  required: false
  description: Y (horizontal) start position of the primitive
  validation:
    displayOptions:
      show:
        operation:
        - draw
        primitive:
        - circle
        - line
        - rectangle
  typeInfo:
    type: number
    displayName: Start Position Y
    name: startPositionY
- id: endPositionX
  name: End Position X
  type: number
  default: 250
  required: false
  description: X (horizontal) end position of the primitive
  validation:
    displayOptions:
      show:
        operation:
        - draw
        primitive:
        - circle
        - line
        - rectangle
  typeInfo:
    type: number
    displayName: End Position X
    name: endPositionX
- id: endPositionY
  name: End Position Y
  type: number
  default: 250
  required: false
  description: Y (horizontal) end position of the primitive
  validation:
    displayOptions:
      show:
        operation:
        - draw
        primitive:
        - circle
        - line
        - rectangle
  typeInfo:
    type: number
    displayName: End Position Y
    name: endPositionY
- id: cornerRadius
  name: Corner Radius
  type: number
  default: 0
  required: false
  description: The radius of the corner to create round corners
  validation:
    displayOptions:
      show:
        operation:
        - draw
        primitive:
        - rectangle
  typeInfo:
    type: number
    displayName: Corner Radius
    name: cornerRadius
- id: text
  name: Text
  type: string
  default: ''
  required: false
  description: Text to write on the image
  placeholder: Text to render
  validation:
    displayOptions:
      show:
        operation:
        - text
  typeInfo:
    type: string
    displayName: Text
    name: text
    typeOptions:
      rows: 5
- id: fontSize
  name: Font Size
  type: number
  default: 18
  required: false
  description: Size of the text
  validation:
    displayOptions:
      show:
        operation:
        - text
  typeInfo:
    type: number
    displayName: Font Size
    name: fontSize
- id: fontColor
  name: Font Color
  type: color
  default: '#000000'
  required: false
  description: Color of the text
  validation:
    displayOptions:
      show:
        operation:
        - text
  typeInfo:
    type: color
    displayName: Font Color
    name: fontColor
- id: positionX
  name: Position X
  type: number
  default: 50
  required: false
  description: X (horizontal) position of the text
  validation: &id001
    displayOptions:
      show:
        operation:
        - crop
  typeInfo: &id002
    type: number
    displayName: Position X
    name: positionX
- id: positionY
  name: Position Y
  type: number
  default: 50
  required: false
  description: Y (vertical) position of the text
  validation: &id003
    displayOptions:
      show:
        operation:
        - crop
  typeInfo: &id004
    type: number
    displayName: Position Y
    name: positionY
- id: lineLength
  name: Max Line Length
  type: number
  default: 80
  required: false
  description: Max amount of characters in a line before a line-break should get added
  validation:
    displayOptions:
      show:
        operation:
        - text
  typeInfo:
    type: number
    displayName: Max Line Length
    name: lineLength
    typeOptions:
      minValue: 1
- id: blur
  name: Blur
  type: number
  default: 5
  required: false
  description: How strong the blur should be
  validation:
    displayOptions:
      show:
        operation:
        - blur
  typeInfo:
    type: number
    displayName: Blur
    name: blur
    typeOptions:
      minValue: 0
      maxValue: 1000
- id: sigma
  name: Sigma
  type: number
  default: 2
  required: false
  description: The sigma of the blur
  validation:
    displayOptions:
      show:
        operation:
        - blur
  typeInfo:
    type: number
    displayName: Sigma
    name: sigma
    typeOptions:
      minValue: 0
      maxValue: 1000
- id: borderWidth
  name: Border Width
  type: number
  default: 10
  required: false
  description: The width of the border
  validation:
    displayOptions:
      show:
        operation:
        - border
  typeInfo:
    type: number
    displayName: Border Width
    name: borderWidth
- id: borderHeight
  name: Border Height
  type: number
  default: 10
  required: false
  description: The height of the border
  validation:
    displayOptions:
      show:
        operation:
        - border
  typeInfo:
    type: number
    displayName: Border Height
    name: borderHeight
- id: borderColor
  name: Border Color
  type: color
  default: '#000000'
  required: false
  description: Color of the border
  validation:
    displayOptions:
      show:
        operation:
        - border
  typeInfo:
    type: color
    displayName: Border Color
    name: borderColor
- id: dataPropertyNameComposite
  name: Composite Image Property
  type: string
  default: ''
  required: false
  description: The name of the binary property which contains the data of the image
    to composite on top of image which is found in Property Name
  placeholder: data2
  validation:
    displayOptions:
      show:
        operation:
        - composite
  typeInfo:
    type: string
    displayName: Composite Image Property
    name: dataPropertyNameComposite
- id: operator
  name: Operator
  type: options
  default: Over
  required: false
  description: The operator to use to combine the images
  validation:
    displayOptions:
      show:
        operation:
        - composite
  typeInfo:
    type: options
    displayName: Operator
    name: operator
    possibleValues:
    - value: Add
      name: Add
      description: ''
    - value: Atop
      name: Atop
      description: ''
    - value: Bumpmap
      name: Bumpmap
      description: ''
    - value: Copy
      name: Copy
      description: ''
    - value: CopyBlack
      name: Copy Black
      description: ''
    - value: CopyBlue
      name: Copy Blue
      description: ''
    - value: CopyCyan
      name: Copy Cyan
      description: ''
    - value: CopyGreen
      name: Copy Green
      description: ''
    - value: CopyMagenta
      name: Copy Magenta
      description: ''
    - value: CopyOpacity
      name: Copy Opacity
      description: ''
    - value: CopyRed
      name: Copy Red
      description: ''
    - value: CopyYellow
      name: Copy Yellow
      description: ''
    - value: Difference
      name: Difference
      description: ''
    - value: Divide
      name: Divide
      description: ''
    - value: In
      name: In
      description: ''
    - value: Minus
      name: Minus
      description: ''
    - value: Multiply
      name: Multiply
      description: ''
    - value: Out
      name: Out
      description: ''
    - value: Over
      name: Over
      description: ''
    - value: Plus
      name: Plus
      description: ''
    - value: Subtract
      name: Subtract
      description: ''
    - value: Xor
      name: Xor
      description: ''
- id: positionX
  name: Position X
  type: number
  default: 0
  required: false
  description: X (horizontal) position of composite image
  validation: *id001
  typeInfo: *id002
- id: positionY
  name: Position Y
  type: number
  default: 0
  required: false
  description: Y (vertical) position of composite image
  validation: *id003
  typeInfo: *id004
- id: width
  name: Width
  type: number
  default: 500
  required: false
  description: Crop width
  validation: *id005
  typeInfo: *id006
- id: height
  name: Height
  type: number
  default: 500
  required: false
  description: Crop height
  validation: *id007
  typeInfo: *id008
- id: positionX
  name: Position X
  type: number
  default: 0
  required: false
  description: X (horizontal) position to crop from
  validation: *id001
  typeInfo: *id002
- id: positionY
  name: Position Y
  type: number
  default: 0
  required: false
  description: Y (vertical) position to crop from
  validation: *id003
  typeInfo: *id004
- id: width
  name: Width
  type: number
  default: 500
  required: false
  description: New width of the image
  validation: *id005
  typeInfo: *id006
- id: height
  name: Height
  type: number
  default: 500
  required: false
  description: New height of the image
  validation: *id007
  typeInfo: *id008
- id: resizeOption
  name: Option
  type: options
  default: maximumArea
  required: false
  description: Ignore aspect ratio and resize exactly to specified values
  validation:
    displayOptions:
      show:
        operation:
        - resize
  typeInfo:
    type: options
    displayName: Option
    name: resizeOption
    possibleValues:
    - value: ignoreAspectRatio
      name: Ignore Aspect Ratio
      description: Ignore aspect ratio and resize exactly to specified values
    - value: maximumArea
      name: Maximum Area
      description: Specified values are maximum area
    - value: minimumArea
      name: Minimum Area
      description: Specified values are minimum area
    - value: onlyIfLarger
      name: Only if Larger
      description: Resize only if image is larger than width or height
    - value: onlyIfSmaller
      name: Only if Smaller
      description: Resize only if image is smaller than width or height
    - value: percent
      name: Percent
      description: Width and height are specified in percents
- id: rotate
  name: Rotate
  type: number
  default: 0
  required: false
  description: How much the image should be rotated
  validation:
    displayOptions:
      show:
        operation:
        - rotate
  typeInfo:
    type: number
    displayName: Rotate
    name: rotate
    typeOptions:
      maxValue: 360
- id: backgroundColor
  name: Background Color
  type: color
  default: '#ffffffff'
  required: false
  description: The color to use for the background when image gets rotated by anything
    which is not a multiple of 90
  validation: *id009
  typeInfo: *id010
- id: degreesX
  name: Degrees X
  type: number
  default: 0
  required: false
  description: X (horizontal) shear degrees
  validation:
    displayOptions:
      show:
        operation:
        - shear
  typeInfo:
    type: number
    displayName: Degrees X
    name: degreesX
- id: degreesY
  name: Degrees Y
  type: number
  default: 0
  required: false
  description: Y (vertical) shear degrees
  validation:
    displayOptions:
      show:
        operation:
        - shear
  typeInfo:
    type: number
    displayName: Degrees Y
    name: degreesY
- id: color
  name: Color
  type: color
  default: '#ff0000'
  required: false
  description: The color to make transparent
  validation: *id011
  typeInfo: *id012
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: text
    text: Text to render
  - field: dataPropertyNameComposite
    text: data2
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
  "$id": "https://n8n.io/schemas/nodes/editImage.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Edit Image Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "backgroundColor": {
          "description": "The color to use for the background when image gets rotated by anything which is not a multiple of 90",
          "type": "string",
          "default": "#ffffffff"
        },
        "width": {
          "description": "New width of the image",
          "type": "number",
          "default": 500
        },
        "height": {
          "description": "New height of the image",
          "type": "number",
          "default": 500
        },
        "primitive": {
          "description": "The primitive to draw",
          "type": "string",
          "enum": [
            "circle",
            "line",
            "rectangle"
          ],
          "default": "rectangle"
        },
        "color": {
          "description": "The color to make transparent",
          "type": "string",
          "default": "#ff0000"
        },
        "startPositionX": {
          "description": "X (horizontal) start position of the primitive",
          "type": "number",
          "default": 50
        },
        "startPositionY": {
          "description": "Y (horizontal) start position of the primitive",
          "type": "number",
          "default": 50
        },
        "endPositionX": {
          "description": "X (horizontal) end position of the primitive",
          "type": "number",
          "default": 250
        },
        "endPositionY": {
          "description": "Y (horizontal) end position of the primitive",
          "type": "number",
          "default": 250
        },
        "cornerRadius": {
          "description": "The radius of the corner to create round corners",
          "type": "number",
          "default": 0
        },
        "text": {
          "description": "Text to write on the image",
          "type": "string",
          "default": "",
          "examples": [
            "Text to render"
          ]
        },
        "fontSize": {
          "description": "Size of the text",
          "type": "number",
          "default": 18
        },
        "fontColor": {
          "description": "Color of the text",
          "type": "string",
          "default": "#000000"
        },
        "positionX": {
          "description": "X (horizontal) position to crop from",
          "type": "number",
          "default": 0
        },
        "positionY": {
          "description": "Y (vertical) position to crop from",
          "type": "number",
          "default": 0
        },
        "lineLength": {
          "description": "Max amount of characters in a line before a line-break should get added",
          "type": "number",
          "default": 80
        },
        "blur": {
          "description": "How strong the blur should be",
          "type": "number",
          "default": 5
        },
        "sigma": {
          "description": "The sigma of the blur",
          "type": "number",
          "default": 2
        },
        "borderWidth": {
          "description": "The width of the border",
          "type": "number",
          "default": 10
        },
        "borderHeight": {
          "description": "The height of the border",
          "type": "number",
          "default": 10
        },
        "borderColor": {
          "description": "Color of the border",
          "type": "string",
          "default": "#000000"
        },
        "dataPropertyNameComposite": {
          "description": "The name of the binary property which contains the data of the image to composite on top of image which is found in Property Name",
          "type": "string",
          "default": "",
          "examples": [
            "data2"
          ]
        },
        "operator": {
          "description": "The operator to use to combine the images",
          "type": "string",
          "enum": [
            "Add",
            "Atop",
            "Bumpmap",
            "Copy",
            "CopyBlack",
            "CopyBlue",
            "CopyCyan",
            "CopyGreen",
            "CopyMagenta",
            "CopyOpacity",
            "CopyRed",
            "CopyYellow",
            "Difference",
            "Divide",
            "In",
            "Minus",
            "Multiply",
            "Out",
            "Over",
            "Plus",
            "Subtract",
            "Xor"
          ],
          "default": "Over"
        },
        "resizeOption": {
          "description": "Ignore aspect ratio and resize exactly to specified values",
          "type": "string",
          "enum": [
            "ignoreAspectRatio",
            "maximumArea",
            "minimumArea",
            "onlyIfLarger",
            "onlyIfSmaller",
            "percent"
          ],
          "default": "maximumArea"
        },
        "rotate": {
          "description": "How much the image should be rotated",
          "type": "number",
          "default": 0
        },
        "degreesX": {
          "description": "X (horizontal) shear degrees",
          "type": "number",
          "default": 0
        },
        "degreesY": {
          "description": "Y (vertical) shear degrees",
          "type": "number",
          "default": 0
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
