---
title: "Node: SecurityScorecard"
slug: "node-securityscorecard"
version: "1"
updated: "2026-01-08"
summary: "Consume SecurityScorecard API"
node_type: "regular"
group: "['transform']"
---

# Node: SecurityScorecard

**Purpose.** Consume SecurityScorecard API
**Subtitle.** ={{$parameter["operation"]}} : {{$parameter["resource"]}}


---

## Node Details

- **Icon:** `file:securityScorecard.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **securityScorecardApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `securityScorecardApi` | ✓ | - |

---

## Operations

### Company Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Factor Scores | `getFactor` | Get company factor scores and issue counts |
| Get Historical Factor Scores | `getFactorHistorical` | Get company's historical factor scores |
| Get Historical Scores | `getHistoricalScore` | Get company's historical scores |
| Get Information and Scorecard | `getScorecard` | Get company information and summary of their scorecard |
| Get Score Plan | `getScorePlan` | Get company's score improvement plan |

### Industry Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Factor Scores | `getFactor` | Get factor scores for an industry |
| Get Historical Factor Scores | `getFactorHistorical` | Get historical factor scores for an industry |
| Get Score | `getScore` | Get the score for an industry |

### Invite Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an invite for a company/user |

### Portfolio Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a portfolio |
| Delete | `delete` | Delete a portfolio |
| Get Many | `getAll` | Get many portfolios |
| Update | `update` | Update a portfolio |

### Portfoliocompany Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a company to portfolio |
| Get Many | `getAll` | Get many companies in a portfolio |
| Remove | `remove` | Remove a company from portfolio |

### Report Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Download | `download` | Download a generated report |
| Generate | `generate` | Generate a report |
| Get Many | `getAll` | Get list of recently generated report |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | company | ✓ | Resource to operate on |  |

**Resource options:**

* **Company** (`company`)
* **Industry** (`industry`)
* **Invite** (`invite`)
* **Portfolio** (`portfolio`)
* **Portfolio Company** (`portfolioCompany`)
* **Report** (`report`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getFactor | ✓ | Get company factor scores and issue counts |  |

**Operation options:**

* **Get Factor Scores** (`getFactor`) - Get company factor scores and issue counts
* **Get Historical Factor Scores** (`getFactorHistorical`) - Get company's historical factor scores
* **Get Historical Scores** (`getHistoricalScore`) - Get company's historical scores
* **Get Information and Scorecard** (`getScorecard`) - Get company information and summary of their scorecard
* **Get Score Plan** (`getScorePlan`) - Get company's score improvement plan

---

### Get Factor Scores parameters (`getFactor`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Scorecard Identifier | `scorecardIdentifier` | string |  | ✓ | Primary identifier of a company or scorecard, i.e. domain. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Filter issues by comma-separated severity list | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Severity | `severity` | string |  |  |
| Severity In | `severity_in` | string |  | Filter issues by comma-separated severity list |

</details>

| Industry | `industry` | options | food | ✓ |  |  |

**Industry options:**

* **Food** (`food`)
* **Healthcare** (`healthcare`)
* **Manofacturing** (`manofacturing`)
* **Retail** (`retail`)
* **Technology** (`technology`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |

### Get Historical Factor Scores parameters (`getFactorHistorical`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Scorecard Identifier | `scorecardIdentifier` | string |  | ✓ | Primary identifier of a company or scorecard, i.e. domain. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | History start date | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date From | `date_from` | dateTime |  | History start date |
| Date To | `date_to` | dateTime |  | History end date |
| Timing | `timing` | options | daily | Date granularity |

</details>

| Industry | `industry` | options | food | ✓ |  |  |

**Industry options:**

* **Food** (`food`)
* **Healthcare** (`healthcare`)
* **Manofacturing** (`manofacturing`)
* **Retail** (`retail`)
* **Technology** (`technology`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | History start date | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date From | `from` | dateTime |  | History start date |
| Date To | `to` | dateTime |  | History end date |

</details>


### Get Historical Scores parameters (`getHistoricalScore`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Scorecard Identifier | `scorecardIdentifier` | string |  | ✓ | Primary identifier of a company or scorecard, i.e. domain. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Options | `options` | collection | {} | ✗ | History start date | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Date From | `date_from` | dateTime |  | History start date |
| Date To | `date_to` | dateTime |  | History end date |
| Timing | `timing` | options | daily | Date granularity |

</details>


### Get Information and Scorecard parameters (`getScorecard`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Scorecard Identifier | `scorecardIdentifier` | string |  | ✓ | Primary identifier of a company or scorecard, i.e. domain. |  |

### Get Score Plan parameters (`getScorePlan`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Scorecard Identifier | `scorecardIdentifier` | string |  | ✓ | Primary identifier of a company or scorecard, i.e. domain. |  |
| Score | `score` | number | 0 | ✓ | Score target |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |

### Get Score parameters (`getScore`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Industry | `industry` | options | food | ✓ |  |  |

**Industry options:**

* **Food** (`food`)
* **Healthcare** (`healthcare`)
* **Manofacturing** (`manofacturing`)
* **Retail** (`retail`)
* **Technology** (`technology`)


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | e.g. name@email.com | email |
| First Name | `firstName` | string |  | ✓ |  |  |
| Last Name | `lastName` | string |  | ✓ |  |  |
| Message | `message` | string |  | ✓ | Message for the invitee |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Minimum days to resolve a scorecard issue | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Days to Resolve Issue | `days_to_resolve_issue` | number | 0 | Minimum days to resolve a scorecard issue |
| Domain | `domain` | string |  | Invitee company domain |
| Grade to Maintain | `grade_to_maintain` | string |  | Request the invitee's organisation to maintain a minimum grade |
| Is Organisation Point of Contact | `is_organization_point_of_contact` | boolean | False | Is the invitee organisation's point of contact |
| Issue Description | `issue_desc` | string |  |  |
| Issue Title | `issue_title` | string |  |  |
| Issue Type | `issue_type` | string |  |  |
| Send Me a Copy | `sendme_copy` | boolean | False | Whether to send a copy of the invite to the requesting user |
| Target URL | `target_url` | string |  | Optional URL to take the invitee to when arriving to the platform |

</details>

| Portfolio Name | `name` | string |  | ✓ | Name of the portfolio |  |
| Description | `description` | string |  | ✗ |  |  |
| Privacy | `privacy` | options | shared | ✗ | Only visible to you |  |

**Privacy options:**

* **Private** (`private`) - Only visible to you
* **Shared** (`shared`) - Visible to everyone in your company
* **Team** (`team`) - Visible to the people on your team


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Portfolio ID | `portfolioId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Portfolio ID | `portfolioId` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Company score grade filter | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Grade | `grade` | string |  | Company score grade filter |
| Industry | `industry` | string |  | Industry filter |
| Issue Type | `issueType` | string |  | Issue type filter |
| Status | `status` | options |  |  |
| Vulnerability | `vulnerability` | string |  | CVE vulnerability filter |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Portfolio ID | `portfolioId` | string |  | ✓ |  |  |
| Portfolio Name | `name` | string |  | ✓ | Name of the portfolio |  |
| Description | `description` | string |  | ✗ |  |  |
| Privacy | `privacy` | options | shared | ✗ | Only visible to you |  |

**Privacy options:**

* **Private** (`private`) - Only visible to you
* **Shared** (`shared`) - Visible to everyone in your company
* **Team** (`team`) - Visible to the people on your team


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Portfolio ID | `portfolioId` | string |  | ✓ |  |  |
| Domain | `domain` | string |  | ✓ | Company's domain name |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Portfolio ID | `portfolioId` | string |  | ✓ |  |  |
| Domain | `domain` | string |  | ✓ | Company's domain name |  |

### Download parameters (`download`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Report URL | `url` | string |  | ✓ | URL to a generated report | url |
| Put Output File in Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |

### Generate parameters (`generate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Report | `report` | options | detailed | ✓ |  |  |

**Report options:**

* **Company Detailed** (`detailed`)
* **Company Events** (`events-json`)
* **Company Issues** (`issues`)
* **Company Partnership** (`partnership`)
* **Company Summary** (`summary`)
* **Full Scorecard** (`full-scorecard-json`)
* **Portfolio** (`portfolio`)
* **Scorecard Footprint** (`scorecard-footprint`)

| Scorecard Identifier | `scorecardIdentifier` | string |  | ✓ | Primary identifier of a company or scorecard, i.e. domain. |  |
| Portfolio ID | `portfolioId` | string |  | ✓ |  |  |
| Branding | `branding` | options | securityscorecard | ✗ |  |  |

**Branding options:**

* **SecurityScorecard** (`securityscorecard`)
* **Company and SecurityScorecard** (`company_and_securityscorecard`)
* **Company** (`company`)

| Date | `date` | dateTime |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Format | `format` | options | pdf |  |

</details>

| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Countries | `countries` | string | [] |  |
| Format | `format` | options | pdf |  |
| IPs | `ips` | string | [] |  |
| Subdomains | `subdomains` | string | [] |  |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["operation"]}}`

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
* Categories: Analytics

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: securityScorecard
displayName: SecurityScorecard
description: Consume SecurityScorecard API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: securityScorecardApi
  required: true
operations:
- id: getFactor
  name: Get Factor Scores
  description: Get company factor scores and issue counts
  params:
  - id: scorecardIdentifier
    name: Scorecard Identifier
    type: string
    default: ''
    required: true
    description: Primary identifier of a company or scorecard, i.e. domain.
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - report
          operation:
          - generate
          report:
          - detailed
          - events-json
          - full-scorecard-json
          - issues
          - partnership
          - scorecard-footprint
          - summary
          - ''
    typeInfo: &id006
      type: string
      displayName: Scorecard Identifier
      name: scorecardIdentifier
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id001
      displayOptions:
        show:
          resource:
          - report
          operation:
          - getAll
    typeInfo: &id002
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id003
      displayOptions:
        show:
          resource:
          - report
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id004
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: industry
    name: Industry
    type: options
    default: food
    required: true
    description: ''
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - industry
          operation:
          - getScore
          - getFactor
          - getFactorHistorical
    typeInfo: &id010
      type: options
      displayName: Industry
      name: industry
      possibleValues:
      - value: food
        name: Food
        description: ''
      - value: healthcare
        name: Healthcare
        description: ''
      - value: manofacturing
        name: Manofacturing
        description: ''
      - value: retail
        name: Retail
        description: ''
      - value: technology
        name: Technology
        description: ''
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: &id007
      displayOptions:
        show:
          resource:
          - industry
          operation:
          - getFactor
          - getFactorHistorical
    typeInfo: &id008
      type: boolean
      displayName: Simplify
      name: simple
- id: getFactorHistorical
  name: Get Historical Factor Scores
  description: Get company's historical factor scores
  params:
  - id: scorecardIdentifier
    name: Scorecard Identifier
    type: string
    default: ''
    required: true
    description: Primary identifier of a company or scorecard, i.e. domain.
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
  - id: industry
    name: Industry
    type: options
    default: food
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
- id: getHistoricalScore
  name: Get Historical Scores
  description: Get company's historical scores
  params:
  - id: scorecardIdentifier
    name: Scorecard Identifier
    type: string
    default: ''
    required: true
    description: Primary identifier of a company or scorecard, i.e. domain.
    validation: *id005
    typeInfo: *id006
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation: *id007
    typeInfo: *id008
- id: getScorecard
  name: Get Information and Scorecard
  description: Get company information and summary of their scorecard
  params:
  - id: scorecardIdentifier
    name: Scorecard Identifier
    type: string
    default: ''
    required: true
    description: Primary identifier of a company or scorecard, i.e. domain.
    validation: *id005
    typeInfo: *id006
- id: getScorePlan
  name: Get Score Plan
  description: Get company's score improvement plan
  params:
  - id: scorecardIdentifier
    name: Scorecard Identifier
    type: string
    default: ''
    required: true
    description: Primary identifier of a company or scorecard, i.e. domain.
    validation: *id005
    typeInfo: *id006
  - id: score
    name: Score
    type: number
    default: 0
    required: true
    description: Score target
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - company
          operation:
          - getScorePlan
    typeInfo:
      type: number
      displayName: Score
      name: score
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
- id: getScore
  name: Get Score
  description: ''
  params:
  - id: industry
    name: Industry
    type: options
    default: food
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
- id: create
  name: Create
  description: Create an invite for a company/user
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: ''
    placeholder: name@email.com
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - invite
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email
      name: email
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - invite
          operation:
          - create
    typeInfo:
      type: string
      displayName: First Name
      name: firstName
  - id: lastName
    name: Last Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - invite
          operation:
          - create
    typeInfo:
      type: string
      displayName: Last Name
      name: lastName
  - id: message
    name: Message
    type: string
    default: ''
    required: true
    description: Message for the invitee
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - invite
          operation:
          - create
    typeInfo:
      type: string
      displayName: Message
      name: message
  - id: name
    name: Portfolio Name
    type: string
    default: ''
    required: true
    description: Name of the portfolio
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - portfolio
          operation:
          - create
          - update
    typeInfo: &id014
      type: string
      displayName: Portfolio Name
      name: name
  - id: description
    name: Description
    type: string
    default: ''
    required: false
    description: ''
    validation: &id015
      displayOptions:
        show:
          resource:
          - portfolio
          operation:
          - create
          - update
    typeInfo: &id016
      type: string
      displayName: Description
      name: description
  - id: privacy
    name: Privacy
    type: options
    default: shared
    required: false
    description: Only visible to you
    validation: &id017
      displayOptions:
        show:
          resource:
          - portfolio
          operation:
          - create
          - update
    typeInfo: &id018
      type: options
      displayName: Privacy
      name: privacy
      possibleValues:
      - value: private
        name: Private
        description: Only visible to you
      - value: shared
        name: Shared
        description: Visible to everyone in your company
      - value: team
        name: Team
        description: Visible to the people on your team
- id: delete
  name: Delete
  description: Delete a portfolio
  params:
  - id: portfolioId
    name: Portfolio ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - report
          operation:
          - generate
          report:
          - portfolio
    typeInfo: &id012
      type: string
      displayName: Portfolio ID
      name: portfolioId
- id: getAll
  name: Get Many
  description: Get many portfolios
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: portfolioId
    name: Portfolio ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id001
    typeInfo: *id002
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id003
    typeInfo: *id004
- id: update
  name: Update
  description: Update a portfolio
  params:
  - id: portfolioId
    name: Portfolio ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: name
    name: Portfolio Name
    type: string
    default: ''
    required: true
    description: Name of the portfolio
    validation: *id013
    typeInfo: *id014
  - id: description
    name: Description
    type: string
    default: ''
    required: false
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: privacy
    name: Privacy
    type: options
    default: shared
    required: false
    description: Only visible to you
    validation: *id017
    typeInfo: *id018
- id: add
  name: Add
  description: Add a company to portfolio
  params:
  - id: portfolioId
    name: Portfolio ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: domain
    name: Domain
    type: string
    default: ''
    required: true
    description: Company's domain name
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - portfolioCompany
          operation:
          - add
          - remove
    typeInfo: &id020
      type: string
      displayName: Domain
      name: domain
- id: remove
  name: Remove
  description: Remove a company from portfolio
  params:
  - id: portfolioId
    name: Portfolio ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: domain
    name: Domain
    type: string
    default: ''
    required: true
    description: Company's domain name
    validation: *id019
    typeInfo: *id020
- id: download
  name: Download
  description: Download a generated report
  params:
  - id: url
    name: Report URL
    type: string
    default: ''
    required: true
    description: URL to a generated report
    validation:
      required: true
      format: url
      displayOptions:
        show:
          resource:
          - report
          operation:
          - download
    typeInfo:
      type: string
      displayName: Report URL
      name: url
  - id: binaryPropertyName
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - report
          operation:
          - download
    typeInfo:
      type: string
      displayName: Put Output File in Field
      name: binaryPropertyName
- id: generate
  name: Generate
  description: Generate a report
  params:
  - id: report
    name: Report
    type: options
    default: detailed
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - report
          operation:
          - generate
    typeInfo:
      type: options
      displayName: Report
      name: report
      possibleValues:
      - value: detailed
        name: Company Detailed
        description: ''
      - value: events-json
        name: Company Events
        description: ''
      - value: issues
        name: Company Issues
        description: ''
      - value: partnership
        name: Company Partnership
        description: ''
      - value: summary
        name: Company Summary
        description: ''
      - value: full-scorecard-json
        name: Full Scorecard
        description: ''
      - value: portfolio
        name: Portfolio
        description: ''
      - value: scorecard-footprint
        name: Scorecard Footprint
        description: ''
  - id: scorecardIdentifier
    name: Scorecard Identifier
    type: string
    default: ''
    required: true
    description: Primary identifier of a company or scorecard, i.e. domain.
    validation: *id005
    typeInfo: *id006
  - id: portfolioId
    name: Portfolio ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: branding
    name: Branding
    type: options
    default: securityscorecard
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - report
          operation:
          - generate
          report:
          - detailed
          - summary
    typeInfo:
      type: options
      displayName: Branding
      name: branding
      possibleValues:
      - value: securityscorecard
        name: SecurityScorecard
        description: ''
      - value: company_and_securityscorecard
        name: Company and SecurityScorecard
        description: ''
      - value: company
        name: Company
        description: ''
  - id: date
    name: Date
    type: dateTime
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - report
          operation:
          - generate
          report:
          - events-json
    typeInfo:
      type: dateTime
      displayName: Date
      name: date
common_expressions:
- ={{$parameter["operation"]}}
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: filters
    text: Add Filter
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  hints:
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
  "$id": "https://n8n.io/schemas/nodes/securityScorecard.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SecurityScorecard Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "getFactor",
        "getFactorHistorical",
        "getHistoricalScore",
        "getScorecard",
        "getScorePlan",
        "getScore",
        "create",
        "delete",
        "getAll",
        "update",
        "add",
        "remove",
        "download",
        "generate"
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
            "company",
            "industry",
            "invite",
            "portfolio",
            "portfolioCompany",
            "report"
          ],
          "default": "company"
        },
        "operation": {
          "description": "Download a generated report",
          "type": "string",
          "enum": [
            "download",
            "generate",
            "getAll"
          ],
          "default": "getAll"
        },
        "scorecardIdentifier": {
          "description": "Primary identifier of a company or scorecard, i.e. domain.",
          "type": "string",
          "default": ""
        },
        "score": {
          "description": "Score target",
          "type": "number",
          "default": 0
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 100
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "filters": {
          "description": "Company score grade filter",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "options": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "industry": {
          "description": "",
          "type": "string",
          "enum": [
            "food",
            "healthcare",
            "manofacturing",
            "retail",
            "technology"
          ],
          "default": "food"
        },
        "email": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "firstName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "lastName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "message": {
          "description": "Message for the invitee",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Minimum days to resolve a scorecard issue",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "portfolioId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "Name of the portfolio",
          "type": "string",
          "default": ""
        },
        "description": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "privacy": {
          "description": "Only visible to you",
          "type": "string",
          "enum": [
            "private",
            "shared",
            "team"
          ],
          "default": "shared"
        },
        "domain": {
          "description": "Company's domain name",
          "type": "string",
          "default": ""
        },
        "report": {
          "description": "",
          "type": "string",
          "enum": [
            "detailed",
            "events-json",
            "issues",
            "partnership",
            "summary",
            "full-scorecard-json",
            "portfolio",
            "scorecard-footprint"
          ],
          "default": "detailed"
        },
        "branding": {
          "description": "",
          "type": "string",
          "enum": [
            "securityscorecard",
            "company_and_securityscorecard",
            "company"
          ],
          "default": "securityscorecard"
        },
        "date": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "url": {
          "description": "URL to a generated report",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
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
      "name": "securityScorecardApi",
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
