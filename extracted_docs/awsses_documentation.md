---
title: "Node: AWS SES"
slug: "node-awsses"
version: "1"
updated: "2025-11-13"
summary: "Sends data to AWS SES"
node_type: "regular"
group: "['output']"
---

# Node: AWS SES

**Purpose.** Sends data to AWS SES
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:ses.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **aws**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `aws` | ✓ | - |

---

## Operations

### Customverificationemail Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new custom verification email template |
| Delete | `delete` | Delete an existing custom verification email template |
| Get | `get` | Get the custom email verification template |
| Get Many | `getAll` | Get many of the existing custom verification email templates for your account |
| Send | `send` | Add an email address to the list of identities |
| Update | `update` | Update an existing custom verification email template |

### Email Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Send | `send` | Send an email |
| Send Template | `sendTemplate` | Send an email based on a template |

### Template Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a template |
| Delete | `delete` | Delete a template |
| Get | `get` | Get a template |
| Get Many | `getAll` | Get many templates |
| Update | `update` | Update a template |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | email | ✗ | Resource to operate on |  |

**Resource options:**

* **Custom Verification Email** (`customVerificationEmail`)
* **Email** (`email`)
* **Template** (`template`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new custom verification email template |  |

**Operation options:**

* **Create** (`create`) - Create a new custom verification email template
* **Delete** (`delete`) - Delete an existing custom verification email template
* **Get** (`get`) - Get the custom email verification template
* **Get Many** (`getAll`) - Get many of the existing custom verification email templates for your account
* **Send** (`send`) - Add an email address to the list of identities
* **Update** (`update`) - Update an existing custom verification email template

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| From Email | `fromEmailAddress` | string |  | ✓ | The email address that the custom verification email is sent from | email |
| Template Name | `templateName` | string |  | ✗ | The name of the custom verification email template |  |
| Template Content | `templateContent` | string |  | ✗ | The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML |  |
| Template Subject | `templateSubject` | string |  | ✓ | The subject line of the custom verification email |  |
| Success Redirection URL | `successRedirectionURL` | string |  | ✓ | The URL that the recipient of the verification email is sent to if his or her address is successfully verified | url |
| Failure Redirection URL | `failureRedirectionURL` | string |  | ✓ | The URL that the recipient of the verification email is sent to if his or her address is not successfully verified | url |
| Template Name | `templateName` | string |  | ✓ | The name of the template |  |
| Subject Part | `subjectPart` | string |  | ✗ | The subject line of the email |  |
| Html Part | `htmlPart` | string |  | ✗ | The HTML body of the email |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The email body that will be visible to recipients whose email clients do not display HTML | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Text Part | `textPart` | string |  | The email body that will be visible to recipients whose email clients do not display HTML |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Template Name | `templateName` | string |  | ✗ | The name of the custom verification email template |  |
| Template Name | `templateName` | string |  | ✓ | The name of the template |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Template Name | `templateName` | string |  | ✗ | The name of the custom verification email template |  |
| Template Name | `templateName` | string |  | ✓ | The name of the template |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | The email address to verify | e.g. name@email.com | email |
| Template Name | `templateName` | string |  | ✓ | The name of the custom verification email template to use when sending the verification email |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of a configuration set to use when sending the verification email | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Configuration Set Name | `configurationSetName` | string |  | Name of a configuration set to use when sending the verification email |

</details>

| Is Body HTML | `isBodyHtml` | boolean | False | ✗ | Whether body is HTML or simple text |  |
| Subject | `subject` | string |  | ✓ |  |  |
| Body | `body` | string |  | ✓ | The message to be sent |  |
| From Email | `fromEmail` | string |  | ✓ | Email address of the sender | e.g. admin@example.com | email |
| To Addresses | `toAddresses` | string | [] | ✗ | Email addresses of the recipients | e.g. info@example.com |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Bcc Recipients of the email | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Bcc Addresses | `bccAddresses` | string | [] | Bcc Recipients of the email |
| Cc Addresses | `ccAddresses` | string | [] | Cc recipients of the email |
| Configuration Set Name | `configurationSetName` | string |  | Name of the configuration set to use when you send an email using send |
| Reply To Addresses | `replyToAddresses` | string | [] | Reply-to email address(es) for the message |
| Return Path | `returnPath` | string |  | Email address that bounces and complaints will be forwarded to when feedback forwarding is enabled |
| Return Path ARN | `returnPathArn` | string |  | This parameter is used only for sending authorization |
| Source ARN | `sourceArn` | string |  | This parameter is used only for sending authorization |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Template Name | `templateName` | string |  | ✗ | The name of the custom verification email template |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The URL that the recipient of the verification email is sent to if his or her address is not successfully verified | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Failure Redirection URL | `failureRedirectionURL` | string |  | The URL that the recipient of the verification email is sent to if his or her address is not successfully verified |
| From Email | `fromEmailAddress` | string |  | The email address that the custom verification email is sent from |
| Success Redirection URL | `successRedirectionURL` | string |  | The URL that the recipient of the verification email is sent to if his or her address is successfully verified |
| Template Content | `templateContent` | string |  | The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML |
| Template Subject | `templateSubject` | string |  | The subject line of the custom verification email |

</details>

| Template Name | `templateName` | string |  | ✓ | The name of the template |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The email body that will be visible to recipients whose email clients do not display HTML | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Text Part | `textPart` | string |  | The email body that will be visible to recipients whose email clients do not display HTML |
| Subject Part | `subjectPart` | string |  | The subject line of the email |
| Html Part | `htmlPart` | string |  | The HTML body of the email |

</details>


### Send Template parameters (`sendTemplate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Template Name or ID | `templateName` | options |  | ✗ | The ARN of the template to use when sending this email. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| From Email | `fromEmail` | string |  | ✓ | Email address of the sender | e.g. admin@example.com | email |
| To Addresses | `toAddresses` | string | [] | ✗ | Email addresses of the recipients | e.g. info@example.com |  |
| Template Data | `templateDataUi` | fixedCollection | {} | ✗ | e.g. Add Data |  |

<details>
<summary><strong>Template Data sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Data | `templateDataValues` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Bcc Recipients of the email | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Bcc Addresses | `bccAddresses` | string | [] | Bcc Recipients of the email |
| Cc Addresses | `ccAddresses` | string | [] | Cc recipients of the email |
| Configuration Set Name | `configurationSetName` | string |  | Name of the configuration set to use when you send an email using send |
| Reply To Addresses | `replyToAddresses` | string | [] | Reply-to email address(es) for the message |
| Return Path | `returnPath` | string |  | Email address that bounces and complaints will be forwarded to when feedback forwarding is enabled |
| Return Path ARN | `returnPathArn` | string |  | This parameter is used only for sending authorization |
| Source ARN | `sourceArn` | string |  | This parameter is used only for sending authorization |

</details>


---

## Load Options Methods

- `getTemplates`
- `for`
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
* Categories: Communication, Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: awsSes
displayName: AWS SES
description: Sends data to AWS SES
version: '1'
nodeType: regular
group:
- output
credentials:
- name: aws
  required: true
operations:
- id: create
  name: Create
  description: Create a new custom verification email template
  params:
  - id: fromEmailAddress
    name: From Email
    type: string
    default: ''
    required: true
    description: The email address that the custom verification email is sent from
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - customVerificationEmail
          operation:
          - create
    typeInfo:
      type: string
      displayName: From Email
      name: fromEmailAddress
  - id: templateName
    name: Template Name
    type: string
    default: ''
    required: false
    description: The name of the custom verification email template
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - template
          operation:
          - update
          - create
          - get
          - delete
    typeInfo: &id002
      type: string
      displayName: Template Name
      name: templateName
  - id: templateContent
    name: Template Content
    type: string
    default: ''
    required: false
    description: The content of the custom verification email. The total size of the
      email must be less than 10 MB. The message body may contain HTML
    validation:
      displayOptions:
        show:
          resource:
          - customVerificationEmail
          operation:
          - create
    typeInfo:
      type: string
      displayName: Template Content
      name: templateContent
  - id: templateSubject
    name: Template Subject
    type: string
    default: ''
    required: true
    description: The subject line of the custom verification email
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - customVerificationEmail
          operation:
          - create
    typeInfo:
      type: string
      displayName: Template Subject
      name: templateSubject
  - id: successRedirectionURL
    name: Success Redirection URL
    type: string
    default: ''
    required: true
    description: The URL that the recipient of the verification email is sent to if
      his or her address is successfully verified
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - customVerificationEmail
          operation:
          - create
    typeInfo:
      type: string
      displayName: Success Redirection URL
      name: successRedirectionURL
  - id: failureRedirectionURL
    name: Failure Redirection URL
    type: string
    default: ''
    required: true
    description: The URL that the recipient of the verification email is sent to if
      his or her address is not successfully verified
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - customVerificationEmail
          operation:
          - create
    typeInfo:
      type: string
      displayName: Failure Redirection URL
      name: failureRedirectionURL
  - id: templateName
    name: Template Name
    type: string
    default: ''
    required: true
    description: The name of the template
    validation: *id001
    typeInfo: *id002
  - id: subjectPart
    name: Subject Part
    type: string
    default: ''
    required: false
    description: The subject line of the email
    validation:
      displayOptions:
        show:
          resource:
          - template
          operation:
          - create
    typeInfo:
      type: string
      displayName: Subject Part
      name: subjectPart
  - id: htmlPart
    name: Html Part
    type: string
    default: ''
    required: false
    description: The HTML body of the email
    validation:
      displayOptions:
        show:
          resource:
          - template
          operation:
          - create
    typeInfo:
      type: string
      displayName: Html Part
      name: htmlPart
- id: delete
  name: Delete
  description: Delete an existing custom verification email template
  params:
  - id: templateName
    name: Template Name
    type: string
    default: ''
    required: false
    description: The name of the custom verification email template
    validation: *id001
    typeInfo: *id002
  - id: templateName
    name: Template Name
    type: string
    default: ''
    required: true
    description: The name of the template
    validation: *id001
    typeInfo: *id002
- id: get
  name: Get
  description: Get the custom email verification template
  params:
  - id: templateName
    name: Template Name
    type: string
    default: ''
    required: false
    description: The name of the custom verification email template
    validation: *id001
    typeInfo: *id002
  - id: templateName
    name: Template Name
    type: string
    default: ''
    required: true
    description: The name of the template
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many of the existing custom verification email templates for your
    account
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id003
      displayOptions:
        show:
          resource:
          - template
          operation:
          - getAll
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 20
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          resource:
          - template
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 20
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: send
  name: Send
  description: Add an email address to the list of identities
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email address to verify
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - customVerificationEmail
          operation:
          - send
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: templateName
    name: Template Name
    type: string
    default: ''
    required: true
    description: The name of the custom verification email template to use when sending
      the verification email
    validation: *id001
    typeInfo: *id002
  - id: isBodyHtml
    name: Is Body HTML
    type: boolean
    default: false
    required: false
    description: Whether body is HTML or simple text
    validation:
      displayOptions:
        show:
          resource:
          - email
          operation:
          - send
    typeInfo:
      type: boolean
      displayName: Is Body HTML
      name: isBodyHtml
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - email
          operation:
          - send
    typeInfo:
      type: string
      displayName: Subject
      name: subject
  - id: body
    name: Body
    type: string
    default: ''
    required: true
    description: The message to be sent
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - email
          operation:
          - send
    typeInfo:
      type: string
      displayName: Body
      name: body
  - id: fromEmail
    name: From Email
    type: string
    default: ''
    required: true
    description: Email address of the sender
    placeholder: admin@example.com
    validation: &id007
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - email
          operation:
          - sendTemplate
    typeInfo: &id008
      type: string
      displayName: From Email
      name: fromEmail
  - id: toAddresses
    name: To Addresses
    type: string
    default: []
    required: false
    description: Email addresses of the recipients
    placeholder: info@example.com
    validation: &id009
      displayOptions:
        show:
          resource:
          - email
          operation:
          - sendTemplate
    typeInfo: &id010
      type: string
      displayName: To Addresses
      name: toAddresses
      typeOptions:
        multipleValues: true
- id: update
  name: Update
  description: Update an existing custom verification email template
  params:
  - id: templateName
    name: Template Name
    type: string
    default: ''
    required: false
    description: The name of the custom verification email template
    validation: *id001
    typeInfo: *id002
  - id: templateName
    name: Template Name
    type: string
    default: ''
    required: true
    description: The name of the template
    validation: *id001
    typeInfo: *id002
- id: sendTemplate
  name: Send Template
  description: ''
  params:
  - id: templateName
    name: Template Name or ID
    type: options
    default: ''
    required: false
    description: The ARN of the template to use when sending this email. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: fromEmail
    name: From Email
    type: string
    default: ''
    required: true
    description: Email address of the sender
    placeholder: admin@example.com
    validation: *id007
    typeInfo: *id008
  - id: toAddresses
    name: To Addresses
    type: string
    default: []
    required: false
    description: Email addresses of the recipients
    placeholder: info@example.com
    validation: *id009
    typeInfo: *id010
  - id: templateDataUi
    name: Template Data
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Data
    validation:
      displayOptions:
        show:
          resource:
          - email
          operation:
          - sendTemplate
    typeInfo:
      type: fixedCollection
      displayName: Template Data
      name: templateDataUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: templateDataValues
        displayName: Data
        values:
        - displayName: Key
          name: key
          type: string
          default: ''
        - displayName: Value
          name: value
          type: string
          default: ''
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: fromEmail
    text: admin@example.com
  - field: toAddresses
    text: info@example.com
  - field: fromEmail
    text: admin@example.com
  - field: toAddresses
    text: info@example.com
  - field: templateDataUi
    text: Add Data
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/awsSes.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AWS SES Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "delete",
        "get",
        "getAll",
        "send",
        "update",
        "sendTemplate"
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
            "customVerificationEmail",
            "email",
            "template"
          ],
          "default": "email"
        },
        "operation": {
          "description": "Create a template",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "fromEmailAddress": {
          "description": "The email address that the custom verification email is sent from",
          "type": "string",
          "default": "",
          "format": "email"
        },
        "templateName": {
          "description": "The name of the template",
          "type": "string",
          "default": ""
        },
        "templateContent": {
          "description": "The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML",
          "type": "string",
          "default": ""
        },
        "templateSubject": {
          "description": "The subject line of the custom verification email",
          "type": "string",
          "default": ""
        },
        "successRedirectionURL": {
          "description": "The URL that the recipient of the verification email is sent to if his or her address is successfully verified",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "failureRedirectionURL": {
          "description": "The URL that the recipient of the verification email is sent to if his or her address is not successfully verified",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "email": {
          "description": "The email address to verify",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "additionalFields": {
          "description": "The email body that will be visible to recipients whose email clients do not display HTML",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "The email body that will be visible to recipients whose email clients do not display HTML",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
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
        },
        "isBodyHtml": {
          "description": "Whether body is HTML or simple text",
          "type": "boolean",
          "default": false
        },
        "subject": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "body": {
          "description": "The message to be sent",
          "type": "string",
          "default": ""
        },
        "fromEmail": {
          "description": "Email address of the sender",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "admin@example.com"
          ]
        },
        "toAddresses": {
          "description": "Email addresses of the recipients",
          "type": "string",
          "default": [],
          "examples": [
            "info@example.com"
          ]
        },
        "templateDataUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Data"
          ]
        },
        "subjectPart": {
          "description": "The subject line of the email",
          "type": "string",
          "default": ""
        },
        "htmlPart": {
          "description": "The HTML body of the email",
          "type": "string",
          "default": ""
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
      "name": "aws",
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
