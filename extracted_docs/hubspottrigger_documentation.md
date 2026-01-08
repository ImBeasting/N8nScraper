---
title: "Node: HubSpot Trigger"
slug: "node-hubspottrigger"
version: "1"
updated: "2026-01-08"
summary: "Starts the workflow when HubSpot events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: HubSpot Trigger

**Purpose.** Starts the workflow when HubSpot events occur


---

## Node Details

- **Icon:** `file:hubspot.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **hubspotDeveloperApi**: N/A


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
| `hubspotDeveloperApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `eventsUi` | fixedCollection | {} | ✓ | To get notified if any company is created in a customer's account | e.g. Add Event |  |

<details>
<summary><strong>Events sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Event | `eventValues` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field | min:5, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Max Concurrent Requests | `maxConcurrentRequests` | number | 5 |  |

</details>


---

## Load Options Methods

- `getContactProperties`

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
* Categories: Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: hubspotTrigger
displayName: HubSpot Trigger
description: Starts the workflow when HubSpot events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: hubspotDeveloperApi
  required: true
params:
- id: eventsUi
  name: Events
  type: fixedCollection
  default: {}
  required: true
  description: To get notified if any company is created in a customer's account
  placeholder: Add Event
  validation:
    required: true
    displayOptions:
      show:
        name:
        - contact.propertyChange
  typeInfo:
    type: fixedCollection
    displayName: Events
    name: eventsUi
    typeOptions:
      multipleValues: true
    subProperties:
    - name: eventValues
      displayName: Event
      values:
      - displayName: Name
        name: name
        type: options
        description: To get notified if any company is created in a customer's account
        value: company.creation
        default: contact.creation
        required: true
        options:
        - name: Company Created
          description: To get notified if any company is created in a customer's account
          value: company.creation
          displayName: Company Created
        - name: Company Deleted
          description: To get notified if any company is deleted in a customer's account
          value: company.deletion
          displayName: Company Deleted
        - name: Company Property Changed
          description: To get notified if a specified property is changed for any
            company in a customer's account
          value: company.propertyChange
          displayName: Company Property Changed
        - name: Contact Created
          description: To get notified if any contact is created in a customer's account
          value: contact.creation
          displayName: Contact Created
        - name: Contact Deleted
          description: To get notified if any contact is deleted in a customer's account
          value: contact.deletion
          displayName: Contact Deleted
        - name: Contact Privacy Deleted
          description: To get notified if a contact is deleted for privacy compliance
            reasons
          value: contact.privacyDeletion
          displayName: Contact Privacy Deleted
        - name: Contact Property Changed
          description: To get notified if a specified property is changed for any
            contact in a customer's account
          value: contact.propertyChange
          displayName: Contact Property Changed
        - name: Conversation Creation
          description: To get notified if a new thread is created in an account
          value: conversation.creation
          displayName: Conversation Creation
        - name: Conversation Deletion
          description: To get notified if a thread is archived or soft-deleted in
            an account
          value: conversation.deletion
          displayName: Conversation Deletion
        - name: Conversation New Message
          description: To get notified if a new message on a thread has been received
          value: conversation.newMessage
          displayName: Conversation New Message
        - name: Conversation Privacy Deletion
          description: To get notified if a thread is permanently deleted in an account
          value: conversation.privacyDeletion
          displayName: Conversation Privacy Deletion
        - name: Conversation Property Change
          description: To get notified if a property on a thread has been changed
          value: conversation.propertyChange
          displayName: Conversation Property Change
        - name: Deal Created
          description: To get notified if any deal is created in a customer's account
          value: deal.creation
          displayName: Deal Created
        - name: Deal Deleted
          description: To get notified if any deal is deleted in a customer's account
          value: deal.deletion
          displayName: Deal Deleted
        - name: Deal Property Changed
          description: To get notified if a specified property is changed for any
            deal in a customer's account
          value: deal.propertyChange
          displayName: Deal Property Changed
        - name: Ticket Created
          description: To get notified if a ticket is created in a customer's account
          value: ticket.creation
          displayName: Ticket Created
        - name: Ticket Deleted
          description: To get notified if any ticket is deleted in a customer's account
          value: ticket.deletion
          displayName: Ticket Deleted
        - name: Ticket Property Changed
          description: To get notified if a specified property is changed for any
            ticket in a customer's account
          value: ticket.propertyChange
          displayName: Ticket Property Changed
      - displayName: Property Name or ID
        name: property
        type: options
        description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
        default: ''
        required: true
        typeOptions:
          loadOptionsMethod: getContactProperties
        displayOptions:
          show:
            name:
            - contact.propertyChange
      - displayName: Property Name or ID
        name: property
        type: options
        description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
        default: ''
        required: true
        typeOptions:
          loadOptionsMethod: getCompanyProperties
        displayOptions:
          show:
            name:
            - company.propertyChange
      - displayName: Property Name or ID
        name: property
        type: options
        description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
        default: ''
        required: true
        typeOptions:
          loadOptionsMethod: getDealProperties
        displayOptions:
          show:
            name:
            - deal.propertyChange
- id: additionalFields
  name: Additional Fields
  type: collection
  default: {}
  required: false
  description: ''
  placeholder: Add Field
  typeInfo:
    type: collection
    displayName: Additional Fields
    name: additionalFields
    typeOptions:
      minValue: 5
    subProperties:
    - displayName: Max Concurrent Requests
      name: maxConcurrentRequests
      type: number
      default: 5
      typeOptions:
        minValue: 5
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: eventsUi
    text: Add Event
  - field: additionalFields
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/hubspotTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HubSpot Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "eventsUi": {
          "description": "To get notified if any company is created in a customer's account",
          "type": "string",
          "default": {},
          "examples": [
            "Add Event"
          ]
        },
        "additionalFields": {
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
      "name": "hubspotDeveloperApi",
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
