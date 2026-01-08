---
title: "Node: SurveyMonkey Trigger"
slug: "node-surveymonkeytrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when Survey Monkey events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: SurveyMonkey Trigger

**Purpose.** Starts the workflow when Survey Monkey events occur


---

## Node Details

- **Icon:** `file:surveyMonkey.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **surveyMonkeyApi**: N/A
- **surveyMonkeyOAuth2Api**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `surveyMonkeyApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `surveyMonkeyOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** Content-Type

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | accessToken | ✗ |  |  |

**Authentication options:**

* **Access Token** (`accessToken`)
* **OAuth2** (`oAuth2`)

| Type | `objectType` | options |  | ✓ |  |  |

**Type options:**

* **Collector** (`collector`)
* **Survey** (`survey`)

| Event | `event` | options |  | ✓ | A collector is created |  |

**Event options:**

* **Collector Created** (`collector_created`) - A collector is created
* **Collector Deleted** (`collector_deleted`) - A collector is deleted
* **Collector Updated** (`collector_updated`) - A collector is updated
* **Response Completed** (`response_completed`) - A survey response is completed
* **Response Created** (`response_created`) - A respondent begins a survey
* **Response Deleted** (`response_deleted`) - A response is deleted
* **Response Disqualified** (`response_disqualified`) - A survey response is disqualified
* **Response Overquota** (`response_overquota`) - A response is over a survey’s quota
* **Response Updated** (`response_updated`) - A survey response is updated
* **Survey Created** (`survey_created`) - A survey is created
* **Survey Deleted** (`survey_deleted`) - A survey is deleted
* **Survey Updated** (`survey_updated`) - A survey is updated

| Event | `event` | options |  | ✓ | A collector is deleted |  |

**Event options:**

* **Collector Deleted** (`collector_deleted`) - A collector is deleted
* **Collector Updated** (`collector_updated`) - A collector is updated
* **Response Completed** (`response_completed`) - A survey response is completed
* **Response Created** (`response_created`) - A respondent begins a survey
* **Response Deleted** (`response_deleted`) - A response is deleted
* **Response Disqualified** (`response_disqualified`) - A survey response is disqualified
* **Response Overquota** (`response_overquota`) - A response is over a survey’s quota
* **Response Updated** (`response_updated`) - A survey response is updated

| Survey Names or IDs | `surveyIds` | multiOptions | [] | ✓ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Survey Name or ID | `surveyId` | options | [] | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Collector Names or IDs | `collectorIds` | multiOptions | [] | ✓ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Resolve Data | `resolveData` | boolean | True | ✗ | By default the webhook-data only contain the IDs. If this option gets activated, it will resolve the data automatically. |  |
| Only Answers | `onlyAnswers` | boolean | True | ✗ | Whether to return only the answers of the form and not any of the other data |  |

---

## Load Options Methods

- `getCollectors`

---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Marketing, Communication
* Aliases: Form

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: surveyMonkeyTrigger
displayName: SurveyMonkey Trigger
description: Starts the workflow when Survey Monkey events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: surveyMonkeyApi
  required: true
- name: surveyMonkeyOAuth2Api
  required: true
params:
- id: authentication
  name: Authentication
  type: options
  default: accessToken
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Authentication
    name: authentication
    possibleValues:
    - value: accessToken
      name: Access Token
      description: ''
    - value: oAuth2
      name: OAuth2
      description: ''
- id: objectType
  name: Type
  type: options
  default: ''
  required: true
  description: ''
  validation:
    required: true
  typeInfo:
    type: options
    displayName: Type
    name: objectType
    possibleValues:
    - value: collector
      name: Collector
      description: ''
    - value: survey
      name: Survey
      description: ''
- id: event
  name: Event
  type: options
  default: ''
  required: true
  description: A collector is created
  validation: &id001
    required: true
    displayOptions:
      show:
        objectType:
        - collector
  typeInfo: &id002
    type: options
    displayName: Event
    name: event
    possibleValues:
    - value: collector_deleted
      name: Collector Deleted
      description: A collector is deleted
    - value: collector_updated
      name: Collector Updated
      description: A collector is updated
    - value: response_completed
      name: Response Completed
      description: A survey response is completed
    - value: response_created
      name: Response Created
      description: A respondent begins a survey
    - value: response_deleted
      name: Response Deleted
      description: A response is deleted
    - value: response_disqualified
      name: Response Disqualified
      description: A survey response is disqualified
    - value: response_overquota
      name: Response Overquota
      description: A response is over a survey’s quota
    - value: response_updated
      name: Response Updated
      description: A survey response is updated
- id: event
  name: Event
  type: options
  default: ''
  required: true
  description: A collector is deleted
  validation: *id001
  typeInfo: *id002
- id: surveyIds
  name: Survey Names or IDs
  type: multiOptions
  default: []
  required: true
  description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
    displayOptions:
      show:
        objectType:
        - survey
      hide:
        event:
        - survey_created
  typeInfo:
    type: multiOptions
    displayName: Survey Names or IDs
    name: surveyIds
    typeOptions:
      loadOptionsMethod: getSurveys
    possibleValues: []
- id: surveyId
  name: Survey Name or ID
  type: options
  default: []
  required: true
  description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
    displayOptions:
      show:
        objectType:
        - collector
  typeInfo:
    type: options
    displayName: Survey Name or ID
    name: surveyId
    typeOptions:
      loadOptionsMethod: getSurveys
    possibleValues: []
- id: collectorIds
  name: Collector Names or IDs
  type: multiOptions
  default: []
  required: true
  description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
  validation:
    required: true
    displayOptions:
      show:
        objectType:
        - collector
  typeInfo:
    type: multiOptions
    displayName: Collector Names or IDs
    name: collectorIds
    typeOptions:
      loadOptionsMethod: getCollectors
    possibleValues: []
- id: resolveData
  name: Resolve Data
  type: boolean
  default: true
  required: false
  description: By default the webhook-data only contain the IDs. If this option gets
    activated, it will resolve the data automatically.
  validation:
    displayOptions:
      show:
        event:
        - response_completed
  typeInfo:
    type: boolean
    displayName: Resolve Data
    name: resolveData
- id: onlyAnswers
  name: Only Answers
  type: boolean
  default: true
  required: false
  description: Whether to return only the answers of the form and not any of the other
    data
  validation:
    displayOptions:
      show:
        resolveData:
        - true
        event:
        - response_completed
  typeInfo:
    type: boolean
    displayName: Only Answers
    name: onlyAnswers
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders: []
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/surveyMonkeyTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SurveyMonkey Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "",
          "type": "string",
          "enum": [
            "accessToken",
            "oAuth2"
          ],
          "default": "accessToken"
        },
        "objectType": {
          "description": "",
          "type": "string",
          "enum": [
            "collector",
            "survey"
          ],
          "default": ""
        },
        "event": {
          "description": "A collector is deleted",
          "type": "string",
          "enum": [
            "collector_deleted",
            "collector_updated",
            "response_completed",
            "response_created",
            "response_deleted",
            "response_disqualified",
            "response_overquota",
            "response_updated"
          ],
          "default": ""
        },
        "surveyIds": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "surveyId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "collectorIds": {
          "description": "Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "resolveData": {
          "description": "By default the webhook-data only contain the IDs. If this option gets activated, it will resolve the data automatically.",
          "type": "boolean",
          "default": true
        },
        "onlyAnswers": {
          "description": "Whether to return only the answers of the form and not any of the other data",
          "type": "boolean",
          "default": true
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
    "version": "1"
  },
  "credentials": [
    {
      "name": "surveyMonkeyApi",
      "required": true
    },
    {
      "name": "surveyMonkeyOAuth2Api",
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
