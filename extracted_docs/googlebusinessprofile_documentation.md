---
title: "Node: Google Business Profile"
slug: "node-googlebusinessprofile"
version: "1"
updated: "2025-11-13"
summary: "Consume Google Business Profile API"
node_type: "regular"
group: "['input']"
---

# Node: Google Business Profile

**Purpose.** Consume Google Business Profile API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:googleBusinessProfile.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **googleBusinessProfileOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice** when resource=['post'], operation=['update']: Make sure that the updated options are supported by the post type. <a target='_blank' href='https://developers.google.com/my-business/reference/rest/v4/accounts.locations.localPosts#resource:-localpost'>More info</a>.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `googleBusinessProfileOAuth2Api` | ✓ | - |

---

## API Patterns

**Common Endpoints:**
- `callToAction.url`

**Headers Used:** Content-Type

---

## Operations

### Post Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

### Review Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | post | ✗ | Resource to operate on |  |

**Resource options:**

* **Post** (`post`)
* **Review** (`review`)

---

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | post | ✗ |  |  |

**Resource options:**

* **Post** (`post`)
* **Review** (`review`)

| Operation | `operation` | options | create | ✗ | Create a new post on Google Business Profile |  |
| Account | `account` | resourceLocator |  | ✓ | The Google Business Profile account | e.g. e.g. accounts/0123456789 |  |
| Location | `location` | resourceLocator |  | ✓ | The specific location or business associated with the account | e.g. e.g. locations/0123456789 |  |
| Post Type | `postType` | options | STANDARD | ✓ | The type of post to create (standard, event, offer, or alert) |  |

**Post Type options:**

* **Standard** (`STANDARD`)
* **Event** (`EVENT`)
* **Offer** (`OFFER`)
* **Alert** (`ALERT`)

| Summary | `summary` | string |  | ✓ | The main text of the post |  |
| Title | `title` | string |  | ✓ | E.g. Sales this week. |  |
| Start Date and Time | `startDateTime` | dateTime |  | ✓ | The start date and time of the event |  |
| End Date and Time | `endDateTime` | dateTime |  | ✓ | The end date and time of the event |  |
| Title | `title` | string |  | ✓ | E.g. 20% off in store or online. |  |
| Start Date | `startDate` | string |  | ✓ | The start date of the offer | e.g. YYYY-MM-DD |  |
| End Date | `endDate` | string |  | ✓ | The end date of the offer | e.g. YYYY-MM-DD |  |
| Alert Type | `alertType` | options | COVID_19 | ✓ | The sub-type of the alert |  |

**Alert Type options:**

* **Covid 19** (`COVID_19`) - This alert is related to the 2019 Coronavirus Disease pandemic

| Options | `additionalOptions` | collection | {} | ✗ | The language code of the post content. <a href="https://cloud.google.com/translate/docs/languages" target="_blank">More info</a>. | e.g. Add Option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Language | `languageCode` | string |  | The language code of the post content. <a href="https://cloud.google.com/translate/docs/languages" target="_blank">More info</a>. |
| Call to Action Type | `callToActionType` | options | ACTION_TYPE_UNSPECIFIED | The type of call to action |
| Call to Action Url | `url` | string |  | The URL that users are sent to when clicking through the promotion |
| Coupon Code | `couponCode` | string |  | The coupon code for the offer |
| Redeem Online Url | `redeemOnlineUrl` | string |  | Link to redeem the offer |
| Terms and Conditions | `termsConditions` | string |  | The terms and conditions of the offer |

</details>

| Account | `account` | resourceLocator |  | ✓ | The Google Business Profile account | e.g. e.g. accounts/0123456789 |  |
| Location | `location` | resourceLocator |  | ✓ | The specific location or business associated with the account | e.g. e.g. locations/0123456789 |  |
| Post | `post` | resourceLocator |  | ✗ | Select the post to retrieve its details | e.g. e.g. accounts/123/locations/123/localPosts/123 |  |
| Account | `account` | resourceLocator |  | ✓ | The Google Business Profile account | e.g. e.g. accounts/0123456789 |  |
| Location | `location` | resourceLocator |  | ✓ | The specific location or business associated with the account | e.g. e.g. locations/0123456789 |  |
| Post | `post` | resourceLocator |  | ✗ | Select the post to retrieve its details | e.g. e.g. accounts/123/locations/123/localPosts/123 |  |
| Account | `account` | resourceLocator |  | ✓ | The Google Business Profile account | e.g. e.g. accounts/0123456789 |  |
| Location | `location` | resourceLocator |  | ✓ | The specific location or business associated with the account | e.g. e.g. locations/0123456789 |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✗ | Max number of results to return | min:1, max:∞ |
| Account | `account` | resourceLocator |  | ✓ | The Google Business Profile account | e.g. e.g. accounts/0123456789 |  |
| Location | `location` | resourceLocator |  | ✓ | The specific location or business associated with the account | e.g. e.g. locations/0123456789 |  |
| Post | `post` | resourceLocator |  | ✗ | Select the post to retrieve its details | e.g. e.g. accounts/123/locations/123/localPosts/123 |  |
| Options | `additionalOptions` | collection | {} | ✗ | The main text of the post | e.g. Add Option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Summary | `summary` | string |  | The main text of the post |
| Language | `languageCode` | string |  | The language code of the post content. <a href="https://cloud.google.com/translate/docs/languages" target="_blank">More info</a>. |
| Call to Action Type | `callToActionType` | options | ACTION_TYPE_UNSPECIFIED | The type of call to action |
| Call to Action Url | `url` | string |  | The URL that users are sent to when clicking through the promotion |
| Start Date and Time | `startDateTime` | dateTime |  | The start date and time of the event |
| End Date and Time | `endDateTime` | dateTime |  | The end date and time of the event |
| Title | `title` | string |  | E.g. 20% off in store or online. |
| Start Date | `startDate` | string |  | The start date of the offer |
| End Date | `endDate` | string |  | The end date of the offer |
| Coupon Code | `couponCode` | string |  | The coupon code for the offer |
| Redeem Online Url | `redeemOnlineUrl` | string |  | Link to redeem the offer |
| Terms and Conditions | `termsConditions` | string |  | The terms and conditions of the offer |

</details>

| Operation | `operation` | options | get | ✗ | Delete a reply to a review |  |
| Account | `account` | resourceLocator |  | ✓ | The Google Business Profile account | e.g. e.g. accounts/0123456789 |  |
| Location | `location` | resourceLocator |  | ✓ | The specific location or business associated with the account | e.g. e.g. locations/0123456789 |  |
| Review | `review` | resourceLocator |  | ✓ | Select the review to retrieve its details | e.g. e.g. ABC123_review-ID_456xyz |  |
| Account | `account` | resourceLocator |  | ✓ | The Google Business Profile account | e.g. e.g. accounts/0123456789 |  |
| Location | `location` | resourceLocator |  | ✓ | The specific location or business associated with the account | e.g. e.g. locations/0123456789 |  |
| Review | `review` | resourceLocator |  | ✓ | Select the review to retrieve its details | e.g. e.g. ABC123_review-ID_456xyz |  |
| Account | `account` | resourceLocator |  | ✓ | The Google Business Profile account | e.g. e.g. accounts/0123456789 |  |
| Location | `location` | resourceLocator |  | ✓ | The specific location or business associated with the account | e.g. e.g. locations/0123456789 |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 20 | ✓ | Max number of results to return | min:1, max:∞ |
| Account | `account` | resourceLocator |  | ✓ | The Google Business Profile account | e.g. e.g. accounts/0123456789 |  |
| Location | `location` | resourceLocator |  | ✓ | The specific location or business associated with the account | e.g. e.g. locations/0123456789 |  |
| Review | `review` | resourceLocator |  | ✓ | Select the review to retrieve its details | e.g. e.g. ABC123_review-ID_456xyz |  |
| Reply | `reply` | string |  | ✗ | The body of the reply (up to 4096 characters) |  |

---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"] + ": " + $parameter["resource"]}}`
- `={{$parameter["resource"] === "post" && $parameter["operation"] === "update" && Object.keys($parameter["additionalOptions"]).length === 0}}`

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
* Categories: Marketing, Productivity
* Aliases: Google My Business, GMB, My Business

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: googleBusinessProfile
displayName: Google Business Profile
description: Consume Google Business Profile API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: googleBusinessProfileOAuth2Api
  required: true
params:
- id: resource
  name: Resource
  type: options
  default: post
  required: false
  description: ''
  typeInfo:
    type: options
    displayName: Resource
    name: resource
    possibleValues:
    - value: post
      name: Post
      description: ''
    - value: review
      name: Review
      description: ''
- id: operation
  name: Operation
  type: options
  default: create
  required: false
  description: Create a new post on Google Business Profile
  validation: &id011
    displayOptions:
      show:
        resource:
        - review
  typeInfo: &id012
    type: options
    displayName: Operation
    name: operation
    possibleValues: []
- id: account
  name: Account
  type: resourceLocator
  default: ''
  required: true
  description: The Google Business Profile account
  hint: Enter the account name
  placeholder: e.g. accounts/0123456789
  validation: &id003
    required: true
    displayOptions:
      show:
        resource:
        - review
        operation:
        - reply
  typeInfo: &id004
    type: resourceLocator
    displayName: Account
    name: account
- id: location
  name: Location
  type: resourceLocator
  default: ''
  required: true
  description: The specific location or business associated with the account
  hint: Enter the location name
  placeholder: e.g. locations/0123456789
  validation: &id005
    required: true
    displayOptions:
      show:
        resource:
        - review
        operation:
        - reply
  typeInfo: &id006
    type: resourceLocator
    displayName: Location
    name: location
- id: postType
  name: Post Type
  type: options
  default: STANDARD
  required: true
  description: The type of post to create (standard, event, offer, or alert)
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - post
        operation:
        - create
  typeInfo:
    type: options
    displayName: Post Type
    name: postType
    possibleValues:
    - value: STANDARD
      name: Standard
      description: ''
    - value: EVENT
      name: Event
      description: ''
    - value: OFFER
      name: Offer
      description: ''
    - value: ALERT
      name: Alert
      description: ''
- id: summary
  name: Summary
  type: string
  default: ''
  required: true
  description: The main text of the post
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - post
        operation:
        - create
  typeInfo:
    type: string
    displayName: Summary
    name: summary
- id: title
  name: Title
  type: string
  default: ''
  required: true
  description: E.g. Sales this week.
  validation: &id001
    required: true
    displayOptions:
      show:
        resource:
        - post
        operation:
        - create
        postType:
        - OFFER
  typeInfo: &id002
    type: string
    displayName: Title
    name: title
- id: startDateTime
  name: Start Date and Time
  type: dateTime
  default: ''
  required: true
  description: The start date and time of the event
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - post
        operation:
        - create
        postType:
        - EVENT
  typeInfo:
    type: dateTime
    displayName: Start Date and Time
    name: startDateTime
- id: endDateTime
  name: End Date and Time
  type: dateTime
  default: ''
  required: true
  description: The end date and time of the event
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - post
        operation:
        - create
        postType:
        - EVENT
  typeInfo:
    type: dateTime
    displayName: End Date and Time
    name: endDateTime
- id: title
  name: Title
  type: string
  default: ''
  required: true
  description: E.g. 20% off in store or online.
  validation: *id001
  typeInfo: *id002
- id: startDate
  name: Start Date
  type: string
  default: ''
  required: true
  description: The start date of the offer
  placeholder: YYYY-MM-DD
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - post
        operation:
        - create
        postType:
        - OFFER
  typeInfo:
    type: string
    displayName: Start Date
    name: startDate
- id: endDate
  name: End Date
  type: string
  default: ''
  required: true
  description: The end date of the offer
  placeholder: YYYY-MM-DD
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - post
        operation:
        - create
        postType:
        - OFFER
  typeInfo:
    type: string
    displayName: End Date
    name: endDate
- id: alertType
  name: Alert Type
  type: options
  default: COVID_19
  required: true
  description: The sub-type of the alert
  validation:
    required: true
    displayOptions:
      show:
        resource:
        - post
        operation:
        - create
        postType:
        - ALERT
  typeInfo:
    type: options
    displayName: Alert Type
    name: alertType
    possibleValues:
    - value: COVID_19
      name: Covid 19
      description: This alert is related to the 2019 Coronavirus Disease pandemic
- id: additionalOptions
  name: Options
  type: collection
  default: {}
  required: false
  description: The language code of the post content. <a href="https://cloud.google.com/translate/docs/languages"
    target="_blank">More info</a>.
  placeholder: Add Option
  validation: &id009
    displayOptions:
      show:
        resource:
        - post
        operation:
        - update
  typeInfo: &id010
    type: collection
    displayName: Options
    name: additionalOptions
    subProperties:
    - displayName: Summary
      name: summary
      type: string
      description: The main text of the post
      default: ''
      routing: ' send: { type: ''body'', property: ''summary'' '
    - displayName: Language
      name: languageCode
      type: string
      description: The language code of the post content. <a href="https://cloud.google.com/translate/docs/languages"
        target="_blank">More info</a>.
      placeholder: e.g. en
      default: ''
      routing: ' send: { type: ''body'', property: ''languageCode'' '
    - displayName: Call to Action Type
      name: callToActionType
      type: options
      description: The type of call to action
      value: ACTION_TYPE_UNSPECIFIED
      default: ACTION_TYPE_UNSPECIFIED
      options:
      - name: Action Type Unspecified
        description: Type unspecified
        value: ACTION_TYPE_UNSPECIFIED
        displayName: Action Type Unspecified
      - name: Book
        description: This post wants a user to book an appointment/table/etc
        value: BOOK
        displayName: Book
      - name: Get Offer
        description: Deprecated. Use OFFER in LocalPostTopicType to create a post
          with offer content.
        value: GET_OFFER
        displayName: Get Offer
      - name: Learn More
        description: This post wants a user to learn more (at their website)
        value: LEARN_MORE
        displayName: Learn More
      - name: Order
        description: This post wants a user to order something
        value: ORDER
        displayName: Order
      - name: Shop
        description: This post wants a user to browse a product catalog
        value: SHOP
        displayName: Shop
      - name: Sign Up
        description: This post wants a user to register/sign up/join something
        value: SIGN_UP
        displayName: Sign Up
      routing: "\n\t\t\t\t\tsend: { type: 'body', property: 'callToAction.actionType' "
    - displayName: Call to Action Url
      name: url
      type: string
      description: The URL that users are sent to when clicking through the promotion
      default: ''
      routing: "\n\t\t\t\t\tsend: { type: 'body', property: 'callToAction.url' "
    - displayName: Start Date and Time
      name: startDateTime
      type: dateTime
      description: The start date and time of the event
      default: ''
    - displayName: End Date and Time
      name: endDateTime
      type: dateTime
      description: The end date and time of the event
      default: ''
    - displayName: Title
      name: title
      type: string
      description: E.g. 20% off in store or online.
      default: ''
      routing: ' send: { type: ''body'', property: ''event.title'' '
    - displayName: Start Date
      name: startDate
      type: string
      description: The start date of the offer
      placeholder: YYYY-MM-DD
      default: ''
    - displayName: End Date
      name: endDate
      type: string
      description: The end date of the offer
      placeholder: YYYY-MM-DD
      default: ''
    - displayName: Coupon Code
      name: couponCode
      type: string
      description: The coupon code for the offer
      default: ''
      routing: "\n\t\t\t\t\tsend: { type: 'body', property: 'offer.couponCode' "
    - displayName: Redeem Online Url
      name: redeemOnlineUrl
      type: string
      description: Link to redeem the offer
      default: ''
      routing: "\n\t\t\t\t\tsend: { type: 'body', property: 'offer.redeemOnlineUrl' "
    - displayName: Terms and Conditions
      name: termsConditions
      type: string
      description: The terms and conditions of the offer
      default: ''
      routing: "\n\t\t\t\t\tsend: { type: 'body', property: 'offer.termsConditions' "
- id: account
  name: Account
  type: resourceLocator
  default: ''
  required: true
  description: The Google Business Profile account
  hint: Enter the account name
  placeholder: e.g. accounts/0123456789
  validation: *id003
  typeInfo: *id004
- id: location
  name: Location
  type: resourceLocator
  default: ''
  required: true
  description: The specific location or business associated with the account
  hint: Enter the location name
  placeholder: e.g. locations/0123456789
  validation: *id005
  typeInfo: *id006
- id: post
  name: Post
  type: resourceLocator
  default: ''
  required: false
  description: Select the post to retrieve its details
  placeholder: e.g. accounts/123/locations/123/localPosts/123
  validation: &id007
    displayOptions:
      show:
        resource:
        - post
        operation:
        - update
  typeInfo: &id008
    type: resourceLocator
    displayName: Post
    name: post
- id: account
  name: Account
  type: resourceLocator
  default: ''
  required: true
  description: The Google Business Profile account
  hint: Enter the account name
  placeholder: e.g. accounts/0123456789
  validation: *id003
  typeInfo: *id004
- id: location
  name: Location
  type: resourceLocator
  default: ''
  required: true
  description: The specific location or business associated with the account
  hint: Enter the location name
  placeholder: e.g. locations/0123456789
  validation: *id005
  typeInfo: *id006
- id: post
  name: Post
  type: resourceLocator
  default: ''
  required: false
  description: Select the post to retrieve its details
  placeholder: e.g. accounts/123/locations/123/localPosts/123
  validation: *id007
  typeInfo: *id008
- id: account
  name: Account
  type: resourceLocator
  default: ''
  required: true
  description: The Google Business Profile account
  hint: Enter the account name
  placeholder: e.g. accounts/0123456789
  validation: *id003
  typeInfo: *id004
- id: location
  name: Location
  type: resourceLocator
  default: ''
  required: true
  description: The specific location or business associated with the account
  hint: Enter the location name
  placeholder: e.g. locations/0123456789
  validation: *id005
  typeInfo: *id006
- id: returnAll
  name: Return All
  type: boolean
  default: false
  required: false
  description: Whether to return all results or only up to a given limit
  validation: &id015
    displayOptions:
      show:
        resource:
        - review
        operation:
        - getAll
  typeInfo: &id016
    type: boolean
    displayName: Return All
    name: returnAll
- id: limit
  name: Limit
  type: number
  default: 20
  required: false
  description: Max number of results to return
  validation: &id017
    required: true
    displayOptions:
      show:
        resource:
        - review
        operation:
        - getAll
        returnAll:
        - false
  typeInfo: &id018
    type: number
    displayName: Limit
    name: limit
    typeOptions:
      minValue: 1
- id: account
  name: Account
  type: resourceLocator
  default: ''
  required: true
  description: The Google Business Profile account
  hint: Enter the account name
  placeholder: e.g. accounts/0123456789
  validation: *id003
  typeInfo: *id004
- id: location
  name: Location
  type: resourceLocator
  default: ''
  required: true
  description: The specific location or business associated with the account
  hint: Enter the location name
  placeholder: e.g. locations/0123456789
  validation: *id005
  typeInfo: *id006
- id: post
  name: Post
  type: resourceLocator
  default: ''
  required: false
  description: Select the post to retrieve its details
  placeholder: e.g. accounts/123/locations/123/localPosts/123
  validation: *id007
  typeInfo: *id008
- id: additionalOptions
  name: Options
  type: collection
  default: {}
  required: false
  description: The main text of the post
  placeholder: Add Option
  validation: *id009
  typeInfo: *id010
- id: operation
  name: Operation
  type: options
  default: get
  required: false
  description: Delete a reply to a review
  validation: *id011
  typeInfo: *id012
- id: account
  name: Account
  type: resourceLocator
  default: ''
  required: true
  description: The Google Business Profile account
  hint: Enter the account name
  placeholder: e.g. accounts/0123456789
  validation: *id003
  typeInfo: *id004
- id: location
  name: Location
  type: resourceLocator
  default: ''
  required: true
  description: The specific location or business associated with the account
  hint: Enter the location name
  placeholder: e.g. locations/0123456789
  validation: *id005
  typeInfo: *id006
- id: review
  name: Review
  type: resourceLocator
  default: ''
  required: true
  description: Select the review to retrieve its details
  placeholder: e.g. ABC123_review-ID_456xyz
  validation: &id013
    required: true
    displayOptions:
      show:
        resource:
        - review
        operation:
        - reply
  typeInfo: &id014
    type: resourceLocator
    displayName: Review
    name: review
- id: account
  name: Account
  type: resourceLocator
  default: ''
  required: true
  description: The Google Business Profile account
  hint: Enter the account name
  placeholder: e.g. accounts/0123456789
  validation: *id003
  typeInfo: *id004
- id: location
  name: Location
  type: resourceLocator
  default: ''
  required: true
  description: The specific location or business associated with the account
  hint: Enter the location name
  placeholder: e.g. locations/0123456789
  validation: *id005
  typeInfo: *id006
- id: review
  name: Review
  type: resourceLocator
  default: ''
  required: true
  description: Select the review to retrieve its details
  placeholder: e.g. ABC123_review-ID_456xyz
  validation: *id013
  typeInfo: *id014
- id: account
  name: Account
  type: resourceLocator
  default: ''
  required: true
  description: The Google Business Profile account
  hint: Enter the account name
  placeholder: e.g. accounts/0123456789
  validation: *id003
  typeInfo: *id004
- id: location
  name: Location
  type: resourceLocator
  default: ''
  required: true
  description: The specific location or business associated with the account
  hint: Enter the location name
  placeholder: e.g. locations/0123456789
  validation: *id005
  typeInfo: *id006
- id: returnAll
  name: Return All
  type: boolean
  default: false
  required: false
  description: Whether to return all results or only up to a given limit
  validation: *id015
  typeInfo: *id016
- id: limit
  name: Limit
  type: number
  default: 20
  required: true
  description: Max number of results to return
  validation: *id017
  typeInfo: *id018
- id: account
  name: Account
  type: resourceLocator
  default: ''
  required: true
  description: The Google Business Profile account
  hint: Enter the account name
  placeholder: e.g. accounts/0123456789
  validation: *id003
  typeInfo: *id004
- id: location
  name: Location
  type: resourceLocator
  default: ''
  required: true
  description: The specific location or business associated with the account
  hint: Enter the location name
  placeholder: e.g. locations/0123456789
  validation: *id005
  typeInfo: *id006
- id: review
  name: Review
  type: resourceLocator
  default: ''
  required: true
  description: Select the review to retrieve its details
  placeholder: e.g. ABC123_review-ID_456xyz
  validation: *id013
  typeInfo: *id014
- id: reply
  name: Reply
  type: string
  default: ''
  required: false
  description: The body of the reply (up to 4096 characters)
  validation:
    displayOptions:
      show:
        resource:
        - review
        operation:
        - reply
  typeInfo:
    type: string
    displayName: Reply
    name: reply
    typeOptions:
      rows: 5
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
- ={{$parameter["resource"] === "post" && $parameter["operation"] === "update" &&
  Object.keys($parameter["additionalOptions"]).length === 0}}
api_patterns:
  http_methods: []
  endpoints:
  - callToAction.url
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices:
  - name: notice
    text: Make sure that the updated options are supported by the post type. <a target='_blank'
      href='https://developers.google.com/my-business/reference/rest/v4/accounts.locations.localPosts#resource:-localpost'>More
      info</a>.
    conditions:
      show:
        resource:
        - post
        operation:
        - update
  tooltips: []
  placeholders:
  - field: account
    text: e.g. accounts/0123456789
  - field: location
    text: e.g. locations/0123456789
  - field: startDate
    text: YYYY-MM-DD
  - field: endDate
    text: YYYY-MM-DD
  - field: additionalOptions
    text: Add Option
  - field: account
    text: e.g. accounts/0123456789
  - field: location
    text: e.g. locations/0123456789
  - field: post
    text: e.g. accounts/123/locations/123/localPosts/123
  - field: account
    text: e.g. accounts/0123456789
  - field: location
    text: e.g. locations/0123456789
  - field: post
    text: e.g. accounts/123/locations/123/localPosts/123
  - field: account
    text: e.g. accounts/0123456789
  - field: location
    text: e.g. locations/0123456789
  - field: account
    text: e.g. accounts/0123456789
  - field: location
    text: e.g. locations/0123456789
  - field: post
    text: e.g. accounts/123/locations/123/localPosts/123
  - field: additionalOptions
    text: Add Option
  - field: account
    text: e.g. accounts/0123456789
  - field: location
    text: e.g. locations/0123456789
  - field: review
    text: e.g. ABC123_review-ID_456xyz
  - field: account
    text: e.g. accounts/0123456789
  - field: location
    text: e.g. locations/0123456789
  - field: review
    text: e.g. ABC123_review-ID_456xyz
  - field: account
    text: e.g. accounts/0123456789
  - field: location
    text: e.g. locations/0123456789
  - field: account
    text: e.g. accounts/0123456789
  - field: location
    text: e.g. locations/0123456789
  - field: review
    text: e.g. ABC123_review-ID_456xyz
  hints:
  - field: account
    text: Enter the account name
  - field: location
    text: Enter the location name
  - field: account
    text: Enter the account name
  - field: location
    text: Enter the location name
  - field: account
    text: Enter the account name
  - field: location
    text: Enter the location name
  - field: account
    text: Enter the account name
  - field: location
    text: Enter the location name
  - field: account
    text: Enter the account name
  - field: location
    text: Enter the location name
  - field: account
    text: Enter the account name
  - field: location
    text: Enter the location name
  - field: account
    text: Enter the account name
  - field: location
    text: Enter the location name
  - field: account
    text: Enter the account name
  - field: location
    text: Enter the location name
  - field: account
    text: Enter the account name
  - field: location
    text: Enter the location name
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
  "$id": "https://n8n.io/schemas/nodes/googleBusinessProfile.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Google Business Profile Node",
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
            "post",
            "review"
          ],
          "default": "post"
        },
        "operation": {
          "description": "Delete a reply to a review",
          "type": "string",
          "default": "get"
        },
        "account": {
          "description": "The Google Business Profile account",
          "type": "string",
          "examples": [
            "e.g. accounts/0123456789"
          ]
        },
        "location": {
          "description": "The specific location or business associated with the account",
          "type": "string",
          "examples": [
            "e.g. locations/0123456789"
          ]
        },
        "postType": {
          "description": "The type of post to create (standard, event, offer, or alert)",
          "type": "string",
          "enum": [
            "STANDARD",
            "EVENT",
            "OFFER",
            "ALERT"
          ],
          "default": "STANDARD"
        },
        "summary": {
          "description": "The main text of the post",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "E.g. 20% off in store or online.",
          "type": "string",
          "default": ""
        },
        "startDateTime": {
          "description": "The start date and time of the event",
          "type": "string",
          "default": ""
        },
        "endDateTime": {
          "description": "The end date and time of the event",
          "type": "string",
          "default": ""
        },
        "startDate": {
          "description": "The start date of the offer",
          "type": "string",
          "default": "",
          "examples": [
            "YYYY-MM-DD"
          ]
        },
        "endDate": {
          "description": "The end date of the offer",
          "type": "string",
          "default": "",
          "examples": [
            "YYYY-MM-DD"
          ]
        },
        "alertType": {
          "description": "The sub-type of the alert",
          "type": "string",
          "enum": [
            "COVID_19"
          ],
          "default": "COVID_19"
        },
        "additionalOptions": {
          "description": "The main text of the post",
          "type": "string",
          "default": {},
          "examples": [
            "Add Option"
          ]
        },
        "post": {
          "description": "Select the post to retrieve its details",
          "type": "string",
          "examples": [
            "e.g. accounts/123/locations/123/localPosts/123"
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
        "review": {
          "description": "Select the review to retrieve its details",
          "type": "string",
          "examples": [
            "e.g. ABC123_review-ID_456xyz"
          ]
        },
        "reply": {
          "description": "The body of the reply (up to 4096 characters)",
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
      "name": "googleBusinessProfileOAuth2Api",
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
