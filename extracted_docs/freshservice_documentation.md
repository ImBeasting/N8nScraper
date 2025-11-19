---
title: "Node: Freshservice"
slug: "node-freshservice"
version: "1"
updated: "2025-11-13"
summary: "Consume the Freshservice API"
node_type: "regular"
group: "['transform']"
---

# Node: Freshservice

**Purpose.** Consume the Freshservice API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:freshservice.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **freshserviceApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `freshserviceApi` | ✓ | - |

---

## Operations

### Ticket Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a ticket |
| Delete | `delete` | Delete a ticket |
| Get | `get` | Retrieve a ticket |
| Get Many | `getAll` | Retrieve many tickets |
| Update | `update` | Update a ticket |

### Agent Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an agent |
| Delete | `delete` | Delete an agent |
| Get | `get` | Retrieve an agent |
| Get Many | `getAll` | Retrieve many agents |
| Update | `update` | Update an agent |

### Agentgroup Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an agent group |
| Delete | `delete` | Delete an agent group |
| Get | `get` | Retrieve an agent group |
| Get Many | `getAll` | Retrieve many agent groups |
| Update | `update` | Update an agent group |

### Agentrole Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve an agent role |
| Get Many | `getAll` | Retrieve many agent roles |

### Announcement Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an announcement |
| Delete | `delete` | Delete an announcement |
| Get | `get` | Retrieve an announcement |
| Get Many | `getAll` | Retrieve many announcements |
| Update | `update` | Update an announcement |

### Assettype Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an asset type |
| Delete | `delete` | Delete an asset type |
| Get | `get` | Retrieve an asset type |
| Get Many | `getAll` | Retrieve many asset types |
| Update | `update` | Update an asset type |

### Change Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a change |
| Delete | `delete` | Delete a change |
| Get | `get` | Retrieve a change |
| Get Many | `getAll` | Retrieve many changes |
| Update | `update` | Update a change |

### Department Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a department |
| Delete | `delete` | Delete a department |
| Get | `get` | Retrieve a department |
| Get Many | `getAll` | Retrieve many departments |
| Update | `update` | Update a department |

### Location Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a location |
| Delete | `delete` | Delete a location |
| Get | `get` | Retrieve a location |
| Get Many | `getAll` | Retrieve many locations |
| Update | `update` | Update a location |

### Problem Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a problem |
| Delete | `delete` | Delete a problem |
| Get | `get` | Retrieve a problem |
| Get Many | `getAll` | Retrieve many problems |
| Update | `update` | Update a problem |

### Product Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a product |
| Delete | `delete` | Delete a product |
| Get | `get` | Retrieve a product |
| Get Many | `getAll` | Retrieve many products |
| Update | `update` | Update a product |

### Release Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a release |
| Delete | `delete` | Delete a release |
| Get | `get` | Retrieve a release |
| Get Many | `getAll` | Retrieve many releases |
| Update | `update` | Update a release |

### Requester Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a requester |
| Delete | `delete` | Delete a requester |
| Get | `get` | Retrieve a requester |
| Get Many | `getAll` | Retrieve many requesters |
| Update | `update` | Update a requester |

### Requestergroup Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a requester group |
| Delete | `delete` | Delete a requester group |
| Get | `get` | Retrieve a requester group |
| Get Many | `getAll` | Retrieve many requester groups |
| Update | `update` | Update a requester group |

### Software Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a software application |
| Delete | `delete` | Delete a software application |
| Get | `get` | Retrieve a software application |
| Get Many | `getAll` | Retrieve many software applications |
| Update | `update` | Update a software application |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | agent | ✗ | Resource to operate on |  |

**Resource options:**

* **Agent** (`agent`)
* **Agent Group** (`agentGroup`)
* **Agent Role** (`agentRole`)
* **Announcement** (`announcement`)
* **Asset** (`asset`)
* **Asset Type** (`assetType`)
* **Change** (`change`)
* **Department** (`department`)
* **Location** (`location`)
* **Problem** (`problem`)
* **Product** (`product`)
* **Release** (`release`)
* **Requester** (`requester`)
* **Requester Group** (`requesterGroup`)
* **Software** (`software`)
* **Ticket** (`ticket`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a ticket |  |

**Operation options:**

* **Create** (`create`) - Create a ticket
* **Delete** (`delete`) - Delete a ticket
* **Get** (`get`) - Retrieve a ticket
* **Get Many** (`getAll`) - Retrieve many tickets
* **Update** (`update`) - Update a ticket

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | Email address of the ticket author | e.g. name@email.com | email |
| Subject | `subject` | string |  | ✗ |  |  |
| Description | `description` | string |  | ✗ | HTML supported |  |
| Priority | `priority` | options | 1 | ✗ |  |  |

**Priority options:**

* **Low** (``)
* **Medium** (``)
* **High** (``)
* **Urgent** (``)

| Status | `status` | options | 2 | ✗ |  |  |

**Status options:**

* **Open** (``)
* **Pending** (``)
* **Resolved** (``)
* **Closed** (``)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Comma-separated email addresses to add in the CC field of the ticket email | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| CC Emails | `cc_emails` | string |  | Comma-separated email addresses to add in the CC field of the ticket email |
| Department Name or ID | `department_id` | options |  | ID of the department to which this ticket belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Group Name or ID | `group_id` | options |  | ID of the group to which the ticket has been assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Impact | `impact` | options | 1 |  |
| Name | `name` | string |  | Name of the ticket author |
| Requester Name or ID | `requester_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Email | `email` | string |  | ✓ | e.g. name@email.com | email |
| First Name | `firstName` | string |  | ✓ |  |  |
| Roles | `roles` | fixedCollection | {} | ✓ | Role to assign to the agent | e.g. Add Role |  |

<details>
<summary><strong>Roles sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Role Properties | `roleProperties` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | IDs of the departments to which the agent belongs. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  |  |
| Background Information | `background_information` | string |  |  |
| Department Names or IDs | `department_ids` | multiOptions | [] | IDs of the departments to which the agent belongs. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Job Title | `job_title` | string |  |  |
| Language | `language` | options |  |  |
| Last Name | `last_name` | string |  |  |
| Location Name or ID | `location_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Group Names or IDs | `member_of` | multiOptions | [] | Comma-separated IDs of the groups that the agent is a member of. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Mobile Phone | `mobile_phone_number` | string |  |  |
| Observer of Group Names/IDs | `observer_of` | multiOptions | [] | Comma-separated IDs of the groups that the agent is an observer of. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Scoreboard Level ID | `scoreboard_level_id` | options | 1 | ID of the level of the agent in the Arcade |
| Time Format | `time_format` | options | 12h |  |
| Work Phone | `work_phone_number` | string |  |  |

</details>

| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the user to whom an escalation email is sent if a ticket in this group is unassigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Escalate to Agent Name or ID | `escalate_to` | options |  | ID of the user to whom an escalation email is sent if a ticket in this group is unassigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Member Names or IDs | `members` | multiOptions | [] | Comma-separated IDs of agents who are members of this group. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Observer Names or IDs | `observers` | multiOptions | [] | Comma-separated agent IDs who are observers of this group. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Unassigned For | `unassigned_for` | options | 30m | Time after which an escalation email is sent if a ticket in the group remains unassigned |

</details>

| Title | `title` | string |  | ✓ |  |  |
| Body | `bodyHtml` | string |  | ✓ | HTML supported |  |
| Visibility | `visibility` | options | everyone | ✓ |  |  |

**Visibility options:**

* **Agents Only** (`agents_only`)
* **Agents and Groups** (`grouped_visibility`)
* **Everyone** (`everyone`)

| Visible From | `visibleFrom` | dateTime |  | ✓ | Timestamp at which announcement becomes active |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Comma-separated additional email addresses to which the announcement needs to be sent | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Additional Emails | `additional_emails` | string |  | Comma-separated additional email addresses to which the announcement needs to be sent |
| Department Names or IDs | `departments` | multiOptions | [] | Comma-separated IDs of departments that may view this announcement. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Visible From | `visible_from` | dateTime |  | Timestamp at which announcement is active |
| Visible Until | `visible_till` | dateTime |  | Timestamp until which announcement is active |

</details>

| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Parent Asset Type Name or ID | `parent_asset_type_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Requester Name or ID | `requesterId` | options |  | ✓ | ID of the requester of the change. Choose from the list or specify an ID. You can also specify the ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Subject | `subject` | string |  | ✓ |  |  |
| Planned Start Date | `plannedStartDate` | dateTime |  | ✓ |  |  |
| Planned End Date | `plannedEndDate` | dateTime |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the agent to whom the change is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Agent Name or ID | `agent_id` | options |  | ID of the agent to whom the change is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Change Type | `change_type` | options | 1 |  |
| Department Name or ID | `department_id` | options |  | ID of the department requesting the change. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | HTML supported |
| Group Name or ID | `group_id` | options |  | ID of the agent group to which the change is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Impact | `impact` | options | 1 |  |
| Priority | `priority` | options | 1 |  |
| Risk | `risk` | options | 1 |  |
| Status | `status` | options | 1 |  |
| Subject | `subject` | string |  |  |

</details>

| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Comma-separated email domains associated with the department | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Domains | `domains` | string |  | Comma-separated email domains associated with the department |

</details>

| Name | `name` | string |  | ✓ | Name of the location |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | fixedCollection | {} |  |

</details>

| Subject | `subject` | string |  | ✓ |  |  |
| Requester Name or ID | `requesterId` | options |  | ✓ | ID of the initiator of the problem. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Due By | `dueBy` | dateTime |  | ✗ | Date when the problem is due to be solved |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the agent to whom the problem is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Agent Name or ID | `agent_id` | options |  | ID of the agent to whom the problem is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Department Name or ID | `department_id` | options |  | ID of the department initiating the problem. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | HTML supported |
| Group Name or ID | `group_id` | options |  | ID of the agent group to which the problem is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Impact | `impact` | options | 1 |  |
| Priority | `priority` | options | 1 |  |
| Status | `status` | options | 1 |  |

</details>

| Asset Type Name or ID | `assetTypeId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | HTML supported | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | HTML supported |
| Manufacturer | `manufacturer` | string |  |  |
| Mode of Procurement | `mode_of_procurement` | options | Buy |  |
| Status | `status` | options | In Production |  |

</details>

| Subject | `subject` | string |  | ✓ |  |  |
| Release Type | `releaseType` | options | 1 | ✗ |  |  |

**Release Type options:**

* **Minor** (``)
* **Standard** (``)
* **Major** (``)
* **Emergency** (``)

| Priority | `priority` | options | 1 | ✗ |  |  |

**Priority options:**

* **Low** (``)
* **Medium** (``)
* **High** (``)
* **Urgent** (``)

| Status | `status` | options | 1 | ✗ |  |  |

**Status options:**

* **Open** (``)
* **On Hold** (``)
* **In Progress** (``)
* **Incomplete** (``)
* **Completed** (``)

| Planned Start Date | `plannedStartDate` | dateTime |  | ✓ |  |  |
| Planned End Date | `plannedEndDate` | dateTime |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the department initiating the release. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Department Name or ID | `department_id` | options |  | ID of the department initiating the release. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | HTML supported |
| Group Name or ID | `group_id` | options |  | ID of the agent group to which the release is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| First Name | `firstName` | string |  | ✓ |  |  |
| Primary Email | `primaryEmail` | string |  | ✗ |  | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Comma-separated IDs of the departments associated with the requester. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  |  |
| Background Information | `background_information` | string |  |  |
| Department Names or IDs | `department_ids` | multiOptions | [] | Comma-separated IDs of the departments associated with the requester. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Job Title | `job_title` | string |  |  |
| Language | `language` | options |  |  |
| Last Name | `last_name` | string |  |  |
| Location Name or ID | `location_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Mobile Phone | `mobile_phone_number` | string |  |  |
| Secondary Emails | `secondary_emails` | string |  | Comma-separated secondary emails associated with the requester |
| Time Format | `time_format` | options | 12h |  |
| Work Phone | `work_phone_number` | string |  |  |

</details>

| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |

</details>

| Application Type | `applicationType` | options | desktop | ✓ |  |  |

**Application Type options:**

* **Desktop** (`desktop`)
* **Mobile** (`mobile`)
* **SaaS** (`saas`)

| Name | `name` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Notes | `notes` | string |  |  |
| Status | `status` | options | managed |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Ticket ID | `ticketId` | string |  | ✓ | ID of the ticket to delete |  |
| Agent ID | `agentId` | string |  | ✓ | ID of the agent to delete |  |
| Agent Group ID | `agentGroupId` | string |  | ✓ | ID of the agent group to delete |  |
| Announcement ID | `announcementId` | string |  | ✓ | ID of the announcement to delete |  |
| Asset Type ID | `assetTypeId` | string |  | ✓ | ID of the asset type to delete |  |
| Change ID | `changeId` | string |  | ✓ | ID of the change to delete |  |
| Department ID | `departmentId` | string |  | ✓ | ID of the department to delete |  |
| Location ID | `locationId` | string |  | ✓ | ID of the location to delete |  |
| Problem ID | `problemId` | string |  | ✓ | ID of the problem to delete |  |
| Product ID | `productId` | string |  | ✓ | ID of the product to delete |  |
| Release ID | `releaseId` | string |  | ✓ | ID of the release to delete |  |
| Requester ID | `requesterId` | string |  | ✓ | ID of the requester to delete |  |
| Requester Group ID | `requesterGroupId` | string |  | ✓ | ID of the requester group to delete |  |
| Software ID | `softwareId` | string |  | ✓ | ID of the software application to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Ticket ID | `ticketId` | string |  | ✓ | ID of the ticket to retrieve |  |
| Agent ID | `agentId` | string |  | ✓ | ID of the agent to retrieve |  |
| Agent Group ID | `agentGroupId` | string |  | ✓ | ID of the agent group to retrieve |  |
| Agent Role ID | `agentRoleId` | string |  | ✓ | ID of the agent role to retrieve |  |
| Announcement ID | `announcementId` | string |  | ✓ | ID of the announcement to retrieve |  |
| Asset Type ID | `assetTypeId` | string |  | ✓ | ID of the asset type to retrieve |  |
| Change ID | `changeId` | string |  | ✓ | ID of the change to retrieve |  |
| Department ID | `departmentId` | string |  | ✓ | ID of the department to retrieve |  |
| Location ID | `locationId` | string |  | ✓ | ID of the location to retrieve |  |
| Problem ID | `problemId` | string |  | ✓ | ID of the problem to retrieve |  |
| Product ID | `productId` | string |  | ✓ | ID of the product to retrieve |  |
| Release ID | `releaseId` | string |  | ✓ | ID of the release to retrieve |  |
| Requester ID | `requesterId` | string |  | ✓ | ID of the requester to retrieve |  |
| Requester Group ID | `requesterGroupId` | string |  | ✓ | ID of the requester group to retrieve |  |
| Software ID | `softwareId` | string |  | ✓ | ID of the software application to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | ID of the agent to whom the tickets have been assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Agent Name or ID | `agent_id` | options |  | ID of the agent to whom the tickets have been assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Group Name or ID | `group_id` | options |  | ID of the group to which the tickets have been assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Impact | `impact` | options | 1 |  |
| Priority | `priority` | options | 1 |  |
| Status | `status` | options | 2 |  |
| Created On | `created_at` | dateTime |  | Date when the ticket was created |
| Due By | `due_by` | dateTime |  | Date when the ticket is due to be resolved |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | ID of the department to which the agent belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Department Name or ID | `department_id` | options |  | ID of the department to which the agent belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Email | `email` | string |  |  |
| First Name | `first_name` | string |  |  |
| Job Title | `job_title` | string |  |  |
| Language | `language` | options |  |  |
| Last Name | `last_name` | string |  |  |
| Location Name or ID | `location_id` | options |  | Choose from the list or specify an ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Mobile Phone Number | `mobile_phone_number` | string |  |  |
| Work Phone Number | `work_phone_number` | string |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Predefined Filters | `filter` | options | my_open |  |
| Sort Order | `sort_by` | options | asc |  |
| Updated Since | `updated_since` | dateTime |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Name of the department | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | Name of the department |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Department Name or ID | `department_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| First Name | `first_name` | string |  |  |
| Job Title | `job_title` | string |  |  |
| Language | `language` | options |  |  |
| Last Name | `last_name` | string |  |  |
| Location Name or ID | `location_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Mobile Phone Number | `mobile_phone_number` | string |  |  |
| Primary Email | `primary_email` | string |  |  |
| Work Phone Number | `work_phone_number` | string |  |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Ticket ID | `ticketId` | string |  | ✓ | ID of the ticket to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the department to which this ticket has been assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Department Name or ID | `department_id` | options |  | ID of the department to which this ticket has been assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | HTML supported |
| Email | `email` | string |  | Email address of the ticket author |
| Group Name or ID | `group_id` | options |  | ID of the group to which the ticket has been assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Impact | `impact` | options | 1 |  |
| Name | `name` | string |  | Name of the ticket author |
| Phone | `phone` | string |  |  |
| Priority | `priority` | options | 1 | Priority of the ticket |
| Status | `status` | options | 2 |  |
| Subject | `subject` | string |  |  |

</details>

| Agent ID | `agentId` | string |  | ✓ | ID of the agent to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | IDs of the departments to which the agent belongs. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  |  |
| Background Information | `background_information` | string |  |  |
| Department Names or IDs | `department_ids` | multiOptions | [] | IDs of the departments to which the agent belongs. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Email | `email` | string |  |  |
| First Name | `first_name` | string |  |  |
| Job Title | `job_title` | string |  |  |
| Language | `language` | options |  |  |
| Last Name | `last_name` | string |  |  |
| Location Name or ID | `location_id` | options |  | Choose from the list or specify an ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Group Names or IDs | `member_of` | multiOptions | [] | Comma-separated IDs of the groups that the agent is a member of. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Mobile Phone | `mobile_phone_number` | string |  |  |
| Observer of Group Names/IDs | `observer_of` | multiOptions | [] | Comma-separated IDs of the groups that the agent is an observer of. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Scoreboard Level ID | `scoreboard_level_id` | options | 1 | ID of the level of the agent in the Arcade |
| Time Format | `time_format` | options | 12h |  |
| Work Phone | `work_phone_number` | string |  |  |

</details>

| Agent Group ID | `agentGroupId` | string |  | ✓ | ID of the agent group to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the agent to whom an escalation email is sent if a ticket in this group is unassigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Escalate to Agent Name or ID | `escalate_to` | options |  | ID of the agent to whom an escalation email is sent if a ticket in this group is unassigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Member Names or IDs | `members` | multiOptions | [] | Comma-separated IDs of agents who are members of this group. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Name | `name` | string |  |  |
| Observer Names or IDs | `observers` | multiOptions | [] | Comma-separated agent user IDs who are observers of this group. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Unassigned For | `unassigned_for` | options | 30m | Time after which an escalation email is sent if a ticket in the group remains unassigned |

</details>

| Announcement ID | `announcementId` | string |  | ✓ | ID of the announcement to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Comma-separated additional email addresses to which the announcement needs to be sent | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Additional Emails | `additional_emails` | string |  | Comma-separated additional email addresses to which the announcement needs to be sent |
| Body | `body_html` | string |  | HTML supported |
| Department Names or IDs | `departments` | multiOptions | [] | Comma-separated IDs of departments that may view this announcement. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Title | `title` | string |  |  |
| Visibility | `visibility` | options | everyone |  |

</details>

| Asset Type ID | `assetTypeId` | string |  | ✓ | ID of the asset type to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Name | `name` | string |  |  |

</details>

| Change ID | `changeId` | string |  | ✓ | ID of the change to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the agent to whom the change is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Agent Name or ID | `agent_id` | options |  | ID of the agent to whom the change is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Change Type | `change_type` | options | 1 |  |
| Department Name or ID | `department_id` | options |  | ID of the department requesting the change. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | HTML supported |
| Group Name or ID | `group_id` | options |  | ID of the agent group to which the change is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Impact | `impact` | options | 1 | Impact of the change |
| Priority | `priority` | options | 1 |  |
| Requester Name or ID | `requester_id` | options |  | ID of the requester of the change. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Risk | `risk` | options | 1 |  |
| Status | `status` | options | 1 |  |
| Subject | `subject` | string |  |  |

</details>

| Department ID | `departmentId` | string |  | ✓ | ID of the department to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Comma-separated email domains associated with the department | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  |  |
| Domains | `domains` | string |  | Comma-separated email domains associated with the department |
| Name | `name` | string |  |  |

</details>

| Location ID | `locationId` | string |  | ✓ | ID of the location to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  |  |
| Address | `address` | fixedCollection | {} |  |

</details>

| Problem ID | `problemId` | string |  | ✓ | ID of the problem to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the agent to whom the problem is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Agent Name or ID | `agent_id` | options |  | ID of the agent to whom the problem is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Department Name or ID | `department_id` | options |  | ID of the department initiating the problem. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | HTML supported |
| Due By | `due_by` | dateTime |  | Date when the problem is due to be solved |
| Group Name or ID | `group_id` | options |  | ID of the agent group to which the problem is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Impact | `impact` | options | 1 |  |
| Priority | `priority` | options | 1 |  |
| Requester Name or ID | `requester_id` | options |  | ID of the initiator of the problem. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Status | `status` | options | 1 |  |
| Subject | `subject` | string |  |  |

</details>

| Product ID | `productId` | string |  | ✓ | ID of the product to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Asset Type Name or ID | `asset_type_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Description | `description` | string |  | HTML supported |
| Manufacturer | `manufacturer` | string |  |  |
| Mode of Procurement | `mode_of_procurement` | options | Buy |  |
| Name | `name` | string |  |  |
| Status | `status` | options | In Production |  |

</details>

| Release ID | `releaseId` | string |  | ✓ | ID of the release to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the department initiating the release. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Department Name or ID | `department_id` | options |  | ID of the department initiating the release. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | HTML supported |
| Group Name or ID | `group_id` | options |  | ID of the agent group to which the release is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Priority | `priority` | options | 1 |  |
| Release Type | `release_type` | options | 1 |  |
| Status | `status` | options | 1 |  |
| Subject | `subject` | string |  |  |

</details>

| Requester ID | `requesterId` | string |  | ✓ | ID of the requester to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Comma-separated IDs of the departments associated with the requester. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  |  |
| Background Information | `background_information` | string |  |  |
| Department Names or IDs | `department_ids` | multiOptions | [] | Comma-separated IDs of the departments associated with the requester. Choose from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| First Name | `first_name` | string |  |  |
| Job Title | `job_title` | string |  |  |
| Language | `language` | options |  |  |
| Last Name | `last_name` | string |  |  |
| Location Name or ID | `location_id` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Mobile Phone | `mobile_phone_number` | string |  |  |
| Primary Email | `primary_email` | string |  |  |
| Secondary Emails | `secondary_emails` | string |  | Comma-separated secondary emails associated with the requester |
| Time Format | `time_format` | options | 12h |  |
| Work Phone | `work_phone_number` | string |  |  |

</details>

| Requester Group ID | `requesterGroupId` | string |  | ✓ | ID of the requester group to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Description of the requester group | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Description of the requester group |
| Name | `name` | string |  | Name of the requester group |

</details>

| Software ID | `softwareId` | string |  | ✓ | ID of the software application to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Type of the software | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Application Type | `application_type` | options | desktop | Type of the software |
| Description | `description` | string |  |  |
| Name | `name` | string |  |  |
| Notes | `notes` | string |  |  |
| Status | `status` | options | managed |  |

</details>


---

## Load Options Methods

- `getAgents`

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
* Categories: Productivity
* Aliases: Freshdesk

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: freshservice
displayName: Freshservice
description: Consume the Freshservice API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: freshserviceApi
  required: true
operations:
- id: create
  name: Create
  description: Create a ticket
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: Email address of the ticket author
    placeholder: name@email.com
    validation: &id001
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - agent
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Email
      name: email
  - id: subject
    name: Subject
    type: string
    default: ''
    required: false
    description: ''
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - release
          operation:
          - create
    typeInfo: &id006
      type: string
      displayName: Subject
      name: subject
  - id: description
    name: Description
    type: string
    default: ''
    required: false
    description: HTML supported
    validation:
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - create
    typeInfo:
      type: string
      displayName: Description
      name: description
  - id: priority
    name: Priority
    type: options
    default: 1
    required: false
    description: ''
    validation: &id009
      displayOptions:
        show:
          resource:
          - release
          operation:
          - create
    typeInfo: &id010
      type: options
      displayName: Priority
      name: priority
      possibleValues:
      - value: Low
        name: Low
        description: ''
      - value: Medium
        name: Medium
        description: ''
      - value: High
        name: High
        description: ''
      - value: Urgent
        name: Urgent
        description: ''
  - id: status
    name: Status
    type: options
    default: 2
    required: false
    description: ''
    validation: &id011
      displayOptions:
        show:
          resource:
          - release
          operation:
          - create
    typeInfo: &id012
      type: options
      displayName: Status
      name: status
      possibleValues:
      - value: Open
        name: Open
        description: ''
      - value: On Hold
        name: On Hold
        description: ''
      - value: In Progress
        name: In Progress
        description: ''
      - value: Incomplete
        name: Incomplete
        description: ''
      - value: Completed
        name: Completed
        description: ''
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: ''
    placeholder: name@email.com
    validation: *id001
    typeInfo: *id002
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - requester
          operation:
          - create
    typeInfo: &id018
      type: string
      displayName: First Name
      name: firstName
  - id: roles
    name: Roles
    type: fixedCollection
    default: {}
    required: true
    description: Role to assign to the agent
    placeholder: Add Role
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - agent
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Roles
      name: roles
      typeOptions:
        multipleValues: true
      subProperties:
      - name: roleProperties
        displayName: Role Properties
        values:
        - displayName: Role Name or ID
          name: role
          type: options
          description: Name of the role to assign to the agent. Choose from the list,
            or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: ''
          required: true
          typeOptions:
            loadOptionsMethod: getAgentRoles
        - displayName: Scope
          name: assignment_scope
          type: options
          description: Scope in which the agent may use the permissions granted by
            the role
          value: entire_helpdesk
          default: specified_groups
          required: true
          options:
          - name: Entire Helpdesk
            value: entire_helpdesk
            displayName: Entire Helpdesk
          - name: Member Groups
            value: member_groups
            displayName: Member Groups
          - name: Specified Groups
            value: specified_groups
            displayName: Specified Groups
          - name: Assigned Items
            value: assigned_items
            displayName: Assigned Items
        - displayName: Group Names or IDs
          name: groups
          type: multiOptions
          description: Groups in which the permissions granted by the role apply.
            Required only when Scope is Specified Groups - ignored otherwise. Choose
            from the list or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
            Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: []
          typeOptions:
            loadOptionsMethod: getAgentGroups
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - software
          operation:
          - create
    typeInfo: &id004
      type: string
      displayName: Name
      name: name
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - announcement
          operation:
          - create
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: bodyHtml
    name: Body
    type: string
    default: ''
    required: true
    description: HTML supported
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - announcement
          operation:
          - create
    typeInfo:
      type: string
      displayName: Body
      name: bodyHtml
  - id: visibility
    name: Visibility
    type: options
    default: everyone
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - announcement
          operation:
          - create
    typeInfo:
      type: options
      displayName: Visibility
      name: visibility
      possibleValues:
      - value: agents_only
        name: Agents Only
        description: ''
      - value: grouped_visibility
        name: Agents and Groups
        description: ''
      - value: everyone
        name: Everyone
        description: ''
  - id: visibleFrom
    name: Visible From
    type: dateTime
    default: ''
    required: true
    description: Timestamp at which announcement becomes active
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - announcement
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Visible From
      name: visibleFrom
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: requesterId
    name: Requester Name or ID
    type: options
    default: ''
    required: true
    description: ID of the requester of the change. Choose from the list or specify
      an ID. You can also specify the ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - requester
          operation:
          - update
    typeInfo: &id008
      type: string
      displayName: Requester ID
      name: requesterId
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: plannedStartDate
    name: Planned Start Date
    type: dateTime
    default: ''
    required: true
    description: ''
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - release
          operation:
          - create
    typeInfo: &id014
      type: dateTime
      displayName: Planned Start Date
      name: plannedStartDate
  - id: plannedEndDate
    name: Planned End Date
    type: dateTime
    default: ''
    required: true
    description: ''
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - release
          operation:
          - create
    typeInfo: &id016
      type: dateTime
      displayName: Planned End Date
      name: plannedEndDate
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the location
    validation: *id003
    typeInfo: *id004
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: requesterId
    name: Requester Name or ID
    type: options
    default: ''
    required: true
    description: ID of the initiator of the problem. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: dueBy
    name: Due By
    type: dateTime
    default: ''
    required: false
    description: Date when the problem is due to be solved
    validation:
      displayOptions:
        show:
          resource:
          - problem
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Due By
      name: dueBy
  - id: assetTypeId
    name: Asset Type Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - product
          operation:
          - create
    typeInfo: &id020
      type: options
      displayName: Asset Type Name or ID
      name: assetTypeId
      typeOptions:
        loadOptionsMethod: getAssetTypes
      possibleValues: []
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: releaseType
    name: Release Type
    type: options
    default: 1
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - release
          operation:
          - create
    typeInfo:
      type: options
      displayName: Release Type
      name: releaseType
      possibleValues:
      - value: Minor
        name: Minor
        description: ''
      - value: Standard
        name: Standard
        description: ''
      - value: Major
        name: Major
        description: ''
      - value: Emergency
        name: Emergency
        description: ''
  - id: priority
    name: Priority
    type: options
    default: 1
    required: false
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: status
    name: Status
    type: options
    default: 1
    required: false
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: plannedStartDate
    name: Planned Start Date
    type: dateTime
    default: ''
    required: true
    description: ''
    validation: *id013
    typeInfo: *id014
  - id: plannedEndDate
    name: Planned End Date
    type: dateTime
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: primaryEmail
    name: Primary Email
    type: string
    default: ''
    required: false
    description: ''
    validation:
      format: email
      displayOptions:
        show:
          resource:
          - requester
          operation:
          - create
    typeInfo:
      type: string
      displayName: Primary Email
      name: primaryEmail
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: applicationType
    name: Application Type
    type: options
    default: desktop
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - software
          operation:
          - create
    typeInfo:
      type: options
      displayName: Application Type
      name: applicationType
      possibleValues:
      - value: desktop
        name: Desktop
        description: ''
      - value: mobile
        name: Mobile
        description: ''
      - value: saas
        name: SaaS
        description: ''
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
- id: delete
  name: Delete
  description: Delete a ticket
  params:
  - id: ticketId
    name: Ticket ID
    type: string
    default: ''
    required: true
    description: ID of the ticket to delete
    validation: &id021
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - update
    typeInfo: &id022
      type: string
      displayName: Ticket ID
      name: ticketId
  - id: agentId
    name: Agent ID
    type: string
    default: ''
    required: true
    description: ID of the agent to delete
    validation: &id023
      required: true
      displayOptions:
        show:
          resource:
          - agent
          operation:
          - update
    typeInfo: &id024
      type: string
      displayName: Agent ID
      name: agentId
  - id: agentGroupId
    name: Agent Group ID
    type: string
    default: ''
    required: true
    description: ID of the agent group to delete
    validation: &id025
      required: true
      displayOptions:
        show:
          resource:
          - agentGroup
          operation:
          - update
    typeInfo: &id026
      type: string
      displayName: Agent Group ID
      name: agentGroupId
  - id: announcementId
    name: Announcement ID
    type: string
    default: ''
    required: true
    description: ID of the announcement to delete
    validation: &id027
      required: true
      displayOptions:
        show:
          resource:
          - announcement
          operation:
          - update
    typeInfo: &id028
      type: string
      displayName: Announcement ID
      name: announcementId
  - id: assetTypeId
    name: Asset Type ID
    type: string
    default: ''
    required: true
    description: ID of the asset type to delete
    validation: *id019
    typeInfo: *id020
  - id: changeId
    name: Change ID
    type: string
    default: ''
    required: true
    description: ID of the change to delete
    validation: &id029
      required: true
      displayOptions:
        show:
          resource:
          - change
          operation:
          - update
    typeInfo: &id030
      type: string
      displayName: Change ID
      name: changeId
  - id: departmentId
    name: Department ID
    type: string
    default: ''
    required: true
    description: ID of the department to delete
    validation: &id031
      required: true
      displayOptions:
        show:
          resource:
          - department
          operation:
          - update
    typeInfo: &id032
      type: string
      displayName: Department ID
      name: departmentId
  - id: locationId
    name: Location ID
    type: string
    default: ''
    required: true
    description: ID of the location to delete
    validation: &id033
      required: true
      displayOptions:
        show:
          resource:
          - location
          operation:
          - update
    typeInfo: &id034
      type: string
      displayName: Location ID
      name: locationId
  - id: problemId
    name: Problem ID
    type: string
    default: ''
    required: true
    description: ID of the problem to delete
    validation: &id035
      required: true
      displayOptions:
        show:
          resource:
          - problem
          operation:
          - update
    typeInfo: &id036
      type: string
      displayName: Problem ID
      name: problemId
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: true
    description: ID of the product to delete
    validation: &id037
      required: true
      displayOptions:
        show:
          resource:
          - product
          operation:
          - update
    typeInfo: &id038
      type: string
      displayName: Product ID
      name: productId
  - id: releaseId
    name: Release ID
    type: string
    default: ''
    required: true
    description: ID of the release to delete
    validation: &id039
      required: true
      displayOptions:
        show:
          resource:
          - release
          operation:
          - update
    typeInfo: &id040
      type: string
      displayName: Release ID
      name: releaseId
  - id: requesterId
    name: Requester ID
    type: string
    default: ''
    required: true
    description: ID of the requester to delete
    validation: *id007
    typeInfo: *id008
  - id: requesterGroupId
    name: Requester Group ID
    type: string
    default: ''
    required: true
    description: ID of the requester group to delete
    validation: &id041
      required: true
      displayOptions:
        show:
          resource:
          - requesterGroup
          operation:
          - update
    typeInfo: &id042
      type: string
      displayName: Requester Group ID
      name: requesterGroupId
  - id: softwareId
    name: Software ID
    type: string
    default: ''
    required: true
    description: ID of the software application to delete
    validation: &id043
      required: true
      displayOptions:
        show:
          resource:
          - software
          operation:
          - update
    typeInfo: &id044
      type: string
      displayName: Software ID
      name: softwareId
- id: get
  name: Get
  description: Retrieve a ticket
  params:
  - id: ticketId
    name: Ticket ID
    type: string
    default: ''
    required: true
    description: ID of the ticket to retrieve
    validation: *id021
    typeInfo: *id022
  - id: agentId
    name: Agent ID
    type: string
    default: ''
    required: true
    description: ID of the agent to retrieve
    validation: *id023
    typeInfo: *id024
  - id: agentGroupId
    name: Agent Group ID
    type: string
    default: ''
    required: true
    description: ID of the agent group to retrieve
    validation: *id025
    typeInfo: *id026
  - id: agentRoleId
    name: Agent Role ID
    type: string
    default: ''
    required: true
    description: ID of the agent role to retrieve
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - agentRole
          operation:
          - get
    typeInfo:
      type: string
      displayName: Agent Role ID
      name: agentRoleId
  - id: announcementId
    name: Announcement ID
    type: string
    default: ''
    required: true
    description: ID of the announcement to retrieve
    validation: *id027
    typeInfo: *id028
  - id: assetTypeId
    name: Asset Type ID
    type: string
    default: ''
    required: true
    description: ID of the asset type to retrieve
    validation: *id019
    typeInfo: *id020
  - id: changeId
    name: Change ID
    type: string
    default: ''
    required: true
    description: ID of the change to retrieve
    validation: *id029
    typeInfo: *id030
  - id: departmentId
    name: Department ID
    type: string
    default: ''
    required: true
    description: ID of the department to retrieve
    validation: *id031
    typeInfo: *id032
  - id: locationId
    name: Location ID
    type: string
    default: ''
    required: true
    description: ID of the location to retrieve
    validation: *id033
    typeInfo: *id034
  - id: problemId
    name: Problem ID
    type: string
    default: ''
    required: true
    description: ID of the problem to retrieve
    validation: *id035
    typeInfo: *id036
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: true
    description: ID of the product to retrieve
    validation: *id037
    typeInfo: *id038
  - id: releaseId
    name: Release ID
    type: string
    default: ''
    required: true
    description: ID of the release to retrieve
    validation: *id039
    typeInfo: *id040
  - id: requesterId
    name: Requester ID
    type: string
    default: ''
    required: true
    description: ID of the requester to retrieve
    validation: *id007
    typeInfo: *id008
  - id: requesterGroupId
    name: Requester Group ID
    type: string
    default: ''
    required: true
    description: ID of the requester group to retrieve
    validation: *id041
    typeInfo: *id042
  - id: softwareId
    name: Software ID
    type: string
    default: ''
    required: true
    description: ID of the software application to retrieve
    validation: *id043
    typeInfo: *id044
- id: getAll
  name: Get Many
  description: Retrieve many tickets
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id045
      displayOptions:
        show:
          resource:
          - software
          operation:
          - getAll
    typeInfo: &id046
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id047
      displayOptions:
        show:
          resource:
          - software
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id048
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
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id045
    typeInfo: *id046
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id047
    typeInfo: *id048
- id: update
  name: Update
  description: Update a ticket
  params:
  - id: ticketId
    name: Ticket ID
    type: string
    default: ''
    required: true
    description: ID of the ticket to update
    validation: *id021
    typeInfo: *id022
  - id: agentId
    name: Agent ID
    type: string
    default: ''
    required: true
    description: ID of the agent to update
    validation: *id023
    typeInfo: *id024
  - id: agentGroupId
    name: Agent Group ID
    type: string
    default: ''
    required: true
    description: ID of the agent group to update
    validation: *id025
    typeInfo: *id026
  - id: announcementId
    name: Announcement ID
    type: string
    default: ''
    required: true
    description: ID of the announcement to update
    validation: *id027
    typeInfo: *id028
  - id: assetTypeId
    name: Asset Type ID
    type: string
    default: ''
    required: true
    description: ID of the asset type to update
    validation: *id019
    typeInfo: *id020
  - id: changeId
    name: Change ID
    type: string
    default: ''
    required: true
    description: ID of the change to update
    validation: *id029
    typeInfo: *id030
  - id: departmentId
    name: Department ID
    type: string
    default: ''
    required: true
    description: ID of the department to update
    validation: *id031
    typeInfo: *id032
  - id: locationId
    name: Location ID
    type: string
    default: ''
    required: true
    description: ID of the location to update
    validation: *id033
    typeInfo: *id034
  - id: problemId
    name: Problem ID
    type: string
    default: ''
    required: true
    description: ID of the problem to update
    validation: *id035
    typeInfo: *id036
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: true
    description: ID of the product to update
    validation: *id037
    typeInfo: *id038
  - id: releaseId
    name: Release ID
    type: string
    default: ''
    required: true
    description: ID of the release to update
    validation: *id039
    typeInfo: *id040
  - id: requesterId
    name: Requester ID
    type: string
    default: ''
    required: true
    description: ID of the requester to update
    validation: *id007
    typeInfo: *id008
  - id: requesterGroupId
    name: Requester Group ID
    type: string
    default: ''
    required: true
    description: ID of the requester group to update
    validation: *id041
    typeInfo: *id042
  - id: softwareId
    name: Software ID
    type: string
    default: ''
    required: true
    description: ID of the software application to update
    validation: *id043
    typeInfo: *id044
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
  - field: filters
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: roles
    text: Add Role
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
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
  "$id": "https://n8n.io/schemas/nodes/freshservice.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Freshservice Node",
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
        "update"
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
            "agent",
            "agentGroup",
            "agentRole",
            "announcement",
            "asset",
            "assetType",
            "change",
            "department",
            "location",
            "problem",
            "product",
            "release",
            "requester",
            "requesterGroup",
            "software",
            "ticket"
          ],
          "default": "agent"
        },
        "operation": {
          "description": "Create a software application",
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
        "email": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "subject": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "description": {
          "description": "HTML supported",
          "type": "string",
          "default": ""
        },
        "priority": {
          "description": "",
          "type": "string",
          "enum": [
            "Low",
            "Medium",
            "High",
            "Urgent"
          ],
          "default": 1
        },
        "status": {
          "description": "",
          "type": "string",
          "enum": [
            "Open",
            "On Hold",
            "In Progress",
            "Incomplete",
            "Completed"
          ],
          "default": 1
        },
        "additionalFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "ticketId": {
          "description": "ID of the ticket to update",
          "type": "string",
          "default": ""
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 50
        },
        "filters": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "updateFields": {
          "description": "Type of the software",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "firstName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "roles": {
          "description": "Role to assign to the agent",
          "type": "string",
          "default": {},
          "examples": [
            "Add Role"
          ]
        },
        "agentId": {
          "description": "ID of the agent to update",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "agentGroupId": {
          "description": "ID of the agent group to update",
          "type": "string",
          "default": ""
        },
        "agentRoleId": {
          "description": "ID of the agent role to retrieve",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "bodyHtml": {
          "description": "HTML supported",
          "type": "string",
          "default": ""
        },
        "visibility": {
          "description": "",
          "type": "string",
          "enum": [
            "agents_only",
            "grouped_visibility",
            "everyone"
          ],
          "default": "everyone"
        },
        "visibleFrom": {
          "description": "Timestamp at which announcement becomes active",
          "type": "string",
          "default": ""
        },
        "announcementId": {
          "description": "ID of the announcement to update",
          "type": "string",
          "default": ""
        },
        "assetTypeId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "requesterId": {
          "description": "ID of the requester to update",
          "type": "string",
          "default": ""
        },
        "plannedStartDate": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "plannedEndDate": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "changeId": {
          "description": "ID of the change to update",
          "type": "string",
          "default": ""
        },
        "departmentId": {
          "description": "ID of the department to update",
          "type": "string",
          "default": ""
        },
        "locationId": {
          "description": "ID of the location to update",
          "type": "string",
          "default": ""
        },
        "dueBy": {
          "description": "Date when the problem is due to be solved",
          "type": "string",
          "default": ""
        },
        "problemId": {
          "description": "ID of the problem to update",
          "type": "string",
          "default": ""
        },
        "productId": {
          "description": "ID of the product to update",
          "type": "string",
          "default": ""
        },
        "releaseType": {
          "description": "",
          "type": "string",
          "enum": [
            "Minor",
            "Standard",
            "Major",
            "Emergency"
          ],
          "default": 1
        },
        "releaseId": {
          "description": "ID of the release to update",
          "type": "string",
          "default": ""
        },
        "primaryEmail": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email"
        },
        "requesterGroupId": {
          "description": "ID of the requester group to update",
          "type": "string",
          "default": ""
        },
        "applicationType": {
          "description": "",
          "type": "string",
          "enum": [
            "desktop",
            "mobile",
            "saas"
          ],
          "default": "desktop"
        },
        "softwareId": {
          "description": "ID of the software application to update",
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
      "name": "freshserviceApi",
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
