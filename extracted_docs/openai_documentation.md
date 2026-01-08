---
title: "Node: OpenAI"
slug: "node-openai"
version: "['1', '1.1']"
updated: "2026-01-08"
summary: "Consume Open AI"
node_type: "regular"
group: "['transform']"
---

# Node: OpenAI

**Purpose.** Consume Open AI
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:openAi.svg', 'dark': 'file:openAi.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **openAiApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **oldVersionNotice**: <strong>New node version available:</strong> get the latest version with added features from the nodes panel.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `openAiApi` | ✓ | - |

---

## Operations

### Chat Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Image Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Text Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | text | ✗ | Resource to operate on |  |

**Resource options:**

* **Chat** (`chat`)
* **Image** (`image`)
* **Text** (`text`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | text | ✗ |  |  |

**Resource options:**

* **Chat** (`chat`)
* **Image** (`image`)
* **Text** (`text`)

| Operation | `operation` | options | complete | ✗ | Create one or more completions for a given text |  |
| Model | `model` | options | gpt-3.5-turbo | ✗ | The model which will generate the completion. <a href="https://beta.openai.com/docs/models/overview">Learn more</a>. |  |
| Model | `chatModel` | options | gpt-3.5-turbo | ✗ | The model which will generate the completion. <a href="https://beta.openai.com/docs/models/overview">Learn more</a>. |  |
| Prompt | `prompt` | fixedCollection | {} | ✗ | e.g. Add Message |  |

<details>
<summary><strong>Prompt sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Messages | `messages` |  |  |  |

</details>

| Simplify | `simplifyOutput` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Additional options to add | e.g. Add option | min:∞, max:2 |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Echo Prompt | `echo` | boolean | False | Whether the prompt should be echo back in addition to the completion |
| Frequency Penalty | `frequency_penalty` | number | 0 | Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim |
| Maximum Number of Tokens | `maxTokens` | number | 16 | The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768). |
| Number of Completions | `n` | number | 1 | How many completions to generate for each prompt. Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for max_tokens and stop. |
| Presence Penalty | `presence_penalty` | number | 0 | Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics |
| Sampling Temperature | `temperature` | number | 1 | Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive. |
| Top P | `topP` | number | 1 | Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both. |

</details>

| Operation | `operation` | options | create | ✗ | Create an image for a given text |  |
| Prompt | `prompt` | string |  | ✗ | A text description of the desired image(s). The maximum length is 1000 characters. | e.g. e.g. A cute cat eating a dinosaur |  |
| Model | `model` | options | dall-e-2 | ✗ | The model to use for image generation |  |
| Model | `imageModel` | options | dall-e-2 | ✗ | The model to use for image generation |  |
| Response Format | `responseFormat` | options | binaryData | ✗ | The format in which to return the image(s) |  |

**Response Format options:**

* **Binary File** (`binaryData`)
* **Image Url** (`imageUrl`)

| Options | `options` | collection | {} | ✗ | Additional options to add | e.g. Add option | min:1, max:10 |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Number of Images | `n` | number | 1 | Number of images to generate |
| Quality | `quality` | options | standard |  |
| Resolution | `size` | options | 1024x1024 |  |
| Resolution | `size` | options | 1024x1024 |  |
| Style | `style` | options | vivid |  |

</details>

| Operation | `operation` | options | complete | ✗ | Create one or more completions for a given text |  |
| Model | `model` | options | gpt-3.5-turbo-instruct | ✗ | The model which will generate the completion. <a href="https://beta.openai.com/docs/models/overview">Learn more</a>. |  |
| Prompt | `prompt` | string |  | ✗ | The prompt to generate completion(s) for | e.g. e.g. Say this is a test |  |
| Model | `model` | options | text-davinci-edit-001 | ✗ | The model which will generate the edited version. <a href="https://beta.openai.com/docs/models/overview">Learn more</a>. |  |

**Model options:**

* **code-davinci-edit-001** (`code-davinci-edit-001`)
* **text-davinci-edit-001** (`text-davinci-edit-001`)

| Input | `input` | string |  | ✗ | The input text to be edited | e.g. e.g. What day of the wek is it? |  |
| Instruction | `instruction` | string |  | ✗ | The instruction that tells the model how to edit the input text | e.g. e.g. Fix the spelling mistakes |  |
| Model | `model` | options | text-moderation-latest | ✗ | The model which will classify the text. <a href="https://beta.openai.com/docs/models/overview">Learn more</a>. |  |

**Model options:**

* **text-moderation-stable** (`text-moderation-stable`)
* **text-moderation-latest** (`text-moderation-latest`)

| Input | `input` | string |  | ✗ | The input text to classify | e.g. e.g. My cat is adorable ❤️❤️ |  |
| Simplify | `simplifyOutput` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Simplify | `simplifyOutput` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | Additional options to add | e.g. Add option | min:∞, max:2 |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Echo Prompt | `echo` | boolean | False | Whether the prompt should be echo back in addition to the completion |
| Frequency Penalty | `frequency_penalty` | number | 0 | Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim |
| Maximum Number of Tokens | `maxTokens` | number | 16 | The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768). |
| Number of Completions | `n` | number | 1 | How many completions to generate for each prompt. Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for max_tokens and stop. |
| Presence Penalty | `presence_penalty` | number | 0 | Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics |
| Sampling Temperature | `temperature` | number | 1 | Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive. |
| Top P | `topP` | number | 1 | Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both. |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{ $credentials.url?.split("/").slice(0,-1).join("/") ?? "https://api.openai.com" }}`
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
* Categories: Utility
* Aliases: ChatGPT, DallE

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: openAi
displayName: OpenAI
description: Consume Open AI
version:
- '1'
- '1.1'
nodeType: regular
group:
- transform
credentials:
- name: openAiApi
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: text
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: chat
      name: Chat
      description: ''
    - value: image
      name: Image
      description: ''
    - value: text
      name: Text
      description: ''
- id: operation
  name: Operation
  type: options
  default: complete
  required: false
  description: Create one or more completions for a given text
  validation: &id001
    displayOptions:
      show:
        resource:
        - text
  typeInfo: &id002
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: model
  name: Model
  type: options
  default: gpt-3.5-turbo
  required: false
  description: The model which will generate the completion. <a href="https://beta.openai.com/docs/models/overview">Learn
    more</a>.
  validation: &id005
    displayOptions:
      show:
        resource:
        - text
        operation:
        - moderate
  typeInfo: &id006
    type: options
    displayName: Model
    name: model
    possibleValues:
    - value: text-moderation-stable
      name: text-moderation-stable
      description: ''
    - value: text-moderation-latest
      name: text-moderation-latest
      description: ''
- id: chatModel
  name: Model
  type: options
  default: gpt-3.5-turbo
  required: false
  description: The model which will generate the completion. <a href="https://beta.openai.com/docs/models/overview">Learn
    more</a>.
  validation:
    displayOptions:
      show:
        operation:
        - complete
        resource:
        - chat
      hide: {}
  typeInfo:
    type: options
    displayName: Model
    name: chatModel
    possibleValues: []
- id: prompt
  name: Prompt
  type: fixedCollection
  default: {}
  required: false
  description: ''
  placeholder: Add Message
  validation: &id003
    displayOptions:
      show:
        resource:
        - text
        operation:
        - complete
  typeInfo: &id004
    type: string
    displayName: Prompt
    name: prompt
    typeOptions:
      rows: 2
- id: simplifyOutput
  name: Simplify
  type: boolean
  default: true
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  validation: &id011
    displayOptions:
      show:
        operation:
        - complete
        - edit
        resource:
        - text
  typeInfo: &id012
    type: boolean
    displayName: Simplify
    name: simplifyOutput
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Additional options to add
  placeholder: Add option
  validation: &id007
    displayOptions:
      show:
        operation:
        - complete
        - edit
        resource:
        - text
  typeInfo: &id008
    type: collection
    displayName: Options
    name: options
    typeOptions:
      maxValue: 2
      numberPrecision: 1
    subProperties:
    - displayName: Echo Prompt
      name: echo
      type: boolean
      description: Whether the prompt should be echo back in addition to the completion
      default: false
      displayOptions:
        show: {}
      routing: "\n\t\t\t\t\tsend: {\n\t\t\t\t\t\ttype: 'body',\n\t\t\t\t\t\tproperty:\
        \ 'echo',\n\t\t\t\t\t"
    - displayName: Frequency Penalty
      name: frequency_penalty
      type: number
      description: Positive values penalize new tokens based on their existing frequency
        in the text so far, decreasing the model's likelihood to repeat the same line
        verbatim
      default: 0
      typeOptions:
        maxValue: 2
        numberPrecision: 1
      routing: "\n\t\t\t\t\tsend: {\n\t\t\t\t\t\ttype: 'body',\n\t\t\t\t\t\tproperty:\
        \ 'frequency_penalty',\n\t\t\t\t\t"
    - displayName: Maximum Number of Tokens
      name: maxTokens
      type: number
      description: The maximum number of tokens to generate in the completion. Most
        models have a context length of 2048 tokens (except for the newest models,
        which support 32,768).
      default: 16
      typeOptions:
        maxValue: 32768
      displayOptions:
        show: {}
      routing: "\n\t\t\t\t\tsend: {\n\t\t\t\t\t\ttype: 'body',\n\t\t\t\t\t\tproperty:\
        \ 'max_tokens',\n\t\t\t\t\t"
    - displayName: Number of Completions
      name: n
      type: number
      description: 'How many completions to generate for each prompt. Note: Because
        this parameter generates many completions, it can quickly consume your token
        quota. Use carefully and ensure that you have reasonable settings for max_tokens
        and stop.'
      default: 1
      routing: "\n\t\t\t\t\tsend: {\n\t\t\t\t\t\ttype: 'body',\n\t\t\t\t\t\tproperty:\
        \ 'n',\n\t\t\t\t\t"
    - displayName: Presence Penalty
      name: presence_penalty
      type: number
      description: Positive values penalize new tokens based on whether they appear
        in the text so far, increasing the model's likelihood to talk about new topics
      default: 0
      typeOptions:
        maxValue: 2
        numberPrecision: 1
      routing: "\n\t\t\t\t\tsend: {\n\t\t\t\t\t\ttype: 'body',\n\t\t\t\t\t\tproperty:\
        \ 'presence_penalty',\n\t\t\t\t\t"
    - displayName: Sampling Temperature
      name: temperature
      type: number
      description: 'Controls randomness: Lowering results in less random completions.
        As the temperature approaches zero, the model will become deterministic and
        repetitive.'
      default: 1
      typeOptions:
        minValue: 0
        maxValue: 1
        numberPrecision: 1
      routing: "\n\t\t\t\t\tsend: {\n\t\t\t\t\t\ttype: 'body',\n\t\t\t\t\t\tproperty:\
        \ 'temperature',\n\t\t\t\t\t"
    - displayName: Top P
      name: topP
      type: number
      description: 'Controls diversity via nucleus sampling: 0.5 means half of all
        likelihood-weighted options are considered. We generally recommend altering
        this or temperature but not both.'
      default: 1
      typeOptions:
        minValue: 0
        maxValue: 1
        numberPrecision: 1
      routing: "\n\t\t\t\t\tsend: {\n\t\t\t\t\t\ttype: 'body',\n\t\t\t\t\t\tproperty:\
        \ 'top_p',\n\t\t\t\t\t"
- id: operation
  name: Operation
  type: options
  default: create
  required: false
  description: Create an image for a given text
  validation: *id001
  typeInfo: *id002
- id: prompt
  name: Prompt
  type: string
  default: ''
  required: false
  description: A text description of the desired image(s). The maximum length is 1000
    characters.
  placeholder: e.g. A cute cat eating a dinosaur
  validation: *id003
  typeInfo: *id004
- id: model
  name: Model
  type: options
  default: dall-e-2
  required: false
  description: The model to use for image generation
  validation: *id005
  typeInfo: *id006
- id: imageModel
  name: Model
  type: options
  default: dall-e-2
  required: false
  description: The model to use for image generation
  validation:
    displayOptions:
      show:
        resource:
        - image
        operation:
        - create
      hide: {}
  typeInfo:
    type: options
    displayName: Model
    name: imageModel
    possibleValues: []
- id: responseFormat
  name: Response Format
  type: options
  default: binaryData
  required: false
  description: The format in which to return the image(s)
  validation:
    displayOptions:
      show:
        resource:
        - image
        operation:
        - create
  typeInfo:
    type: options
    displayName: Response Format
    name: responseFormat
    possibleValues:
    - value: binaryData
      name: Binary File
      description: ''
    - value: imageUrl
      name: Image Url
      description: ''
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Additional options to add
  placeholder: Add option
  validation: *id007
  typeInfo: *id008
- id: operation
  name: Operation
  type: options
  default: complete
  required: false
  description: Create one or more completions for a given text
  validation: *id001
  typeInfo: *id002
- id: model
  name: Model
  type: options
  default: gpt-3.5-turbo-instruct
  required: false
  description: The model which will generate the completion. <a href="https://beta.openai.com/docs/models/overview">Learn
    more</a>.
  validation: *id005
  typeInfo: *id006
- id: prompt
  name: Prompt
  type: string
  default: ''
  required: false
  description: The prompt to generate completion(s) for
  placeholder: e.g. Say this is a test
  validation: *id003
  typeInfo: *id004
- id: model
  name: Model
  type: options
  default: text-davinci-edit-001
  required: false
  description: The model which will generate the edited version. <a href="https://beta.openai.com/docs/models/overview">Learn
    more</a>.
  validation: *id005
  typeInfo: *id006
- id: input
  name: Input
  type: string
  default: ''
  required: false
  description: The input text to be edited
  placeholder: e.g. What day of the wek is it?
  validation: &id009
    displayOptions:
      show:
        resource:
        - text
        operation:
        - moderate
  typeInfo: &id010
    type: string
    displayName: Input
    name: input
- id: instruction
  name: Instruction
  type: string
  default: ''
  required: false
  description: The instruction that tells the model how to edit the input text
  placeholder: e.g. Fix the spelling mistakes
  validation:
    displayOptions:
      show:
        resource:
        - text
        operation:
        - edit
  typeInfo:
    type: string
    displayName: Instruction
    name: instruction
- id: model
  name: Model
  type: options
  default: text-moderation-latest
  required: false
  description: The model which will classify the text. <a href="https://beta.openai.com/docs/models/overview">Learn
    more</a>.
  validation: *id005
  typeInfo: *id006
- id: input
  name: Input
  type: string
  default: ''
  required: false
  description: The input text to classify
  placeholder: e.g. My cat is adorable ❤️❤️
  validation: *id009
  typeInfo: *id010
- id: simplifyOutput
  name: Simplify
  type: boolean
  default: true
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  validation: *id011
  typeInfo: *id012
- id: simplifyOutput
  name: Simplify
  type: boolean
  default: true
  required: false
  description: Whether to return a simplified version of the response instead of the
    raw data
  validation: *id011
  typeInfo: *id012
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Additional options to add
  placeholder: Add option
  validation: *id007
  typeInfo: *id008
common_expressions:
- ={{ $credentials.url?.split("/").slice(0,-1).join("/") ?? "https://api.openai.com"
  }}
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: oldVersionNotice
    text: <strong>New node version available:</strong> get the latest version with
      added features from the nodes panel.
    conditions: null
  tooltips: []
  placeholders:
  - field: prompt
    text: Add Message
  - field: options
    text: Add option
  - field: prompt
    text: e.g. A cute cat eating a dinosaur
  - field: options
    text: Add option
  - field: prompt
    text: e.g. Say this is a test
  - field: input
    text: e.g. What day of the wek is it?
  - field: instruction
    text: e.g. Fix the spelling mistakes
  - field: input
    text: e.g. My cat is adorable ❤️❤️
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
  "$id": "https://n8n.io/schemas/nodes/openAi.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "OpenAI Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "chat",
            "image",
            "text"
          ],
          "default": "text"
        },
        "operation": {
          "description": "Create one or more completions for a given text",
          "type": "string",
          "default": "complete"
        },
        "model": {
          "description": "The model which will classify the text. <a href=\"https://beta.openai.com/docs/models/overview\">Learn more</a>.",
          "type": "string",
          "enum": [
            "text-moderation-stable",
            "text-moderation-latest"
          ],
          "default": "text-moderation-latest"
        },
        "chatModel": {
          "description": "The model which will generate the completion. <a href=\"https://beta.openai.com/docs/models/overview\">Learn more</a>.",
          "type": "string",
          "default": "gpt-3.5-turbo"
        },
        "prompt": {
          "description": "The prompt to generate completion(s) for",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Say this is a test"
          ]
        },
        "simplifyOutput": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "options": {
          "description": "Additional options to add",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "imageModel": {
          "description": "The model to use for image generation",
          "type": "string",
          "default": "dall-e-2"
        },
        "responseFormat": {
          "description": "The format in which to return the image(s)",
          "type": "string",
          "enum": [
            "binaryData",
            "imageUrl"
          ],
          "default": "binaryData"
        },
        "input": {
          "description": "The input text to classify",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. My cat is adorable \u2764\ufe0f\u2764\ufe0f"
          ]
        },
        "instruction": {
          "description": "The instruction that tells the model how to edit the input text",
          "type": "string",
          "default": "",
          "examples": [
            "e.g. Fix the spelling mistakes"
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
      "1.1"
    ]
  },
  "credentials": [
    {
      "name": "openAiApi",
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
