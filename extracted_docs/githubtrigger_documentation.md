---
title: "Node: Github Trigger"
slug: "node-githubtrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Github events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Github Trigger

**Purpose.** Starts the workflow when Github events occur
**Subtitle.** ={{$parameter["owner"] + "/" + $parameter["repository"] + ": " + $parameter["events"].join(", ")}}


---

## Node Details

- **Icon:** `{'light': 'file:github.svg', 'dark': 'file:github.dark.svg'}`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **githubApi**: N/A
- **githubOAuth2Api**: N/A


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **notice**: Only members with owner privileges for an organization or admin privileges for a repository can set up the webhooks this node requires.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `githubApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `githubOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**Headers Used:** User-Agent

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Authentication | `authentication` | options | accessToken | ✗ |  |  |

**Authentication options:**

* **Access Token** (`accessToken`)
* **OAuth2** (`oAuth2`)

| Repository Owner | `owner` | resourceLocator |  | ✓ | e.g. Select an owner... |  |
| Repository Name | `repository` | resourceLocator |  | ✓ | e.g. Select an Repository... |  |
| Events | `events` | multiOptions | [] | ✓ | Any time any event is triggered (Wildcard Event) |  |

**Events options:**

* ***** (`*`) - Any time any event is triggered (Wildcard Event)
* **Check Run** (`check_run`) - Triggered when a check run is created, rerequested, completed, or has a requested_action
* **Check Suite** (`check_suite`) - Triggered when a check suite is completed, requested, or rerequested
* **Commit Comment** (`commit_comment`) - Triggered when a commit comment is created
* **Create** (`create`) - Represents a created repository, branch, or tag
* **Delete** (`delete`) - Represents a deleted branch or tag
* **Deploy Key** (`deploy_key`) - Triggered when a deploy key is added or removed from a repository
* **Deployment** (`deployment`) - Represents a deployment
* **Deployment Status** (`deployment_status`) - Represents a deployment status
* **Fork** (`fork`) - Triggered when a user forks a repository
* **Github App Authorization** (`github_app_authorization`) - Triggered when someone revokes their authorization of a GitHub App
* **Gollum** (`gollum`) - Triggered when a Wiki page is created or updated
* **Installation** (`installation`) - Triggered when someone installs (created), uninstalls (deleted), or accepts new permissions (new_permissions_accepted) for a GitHub App. When a GitHub App owner requests new permissions, the person who installed the GitHub App must accept the new permissions request.
* **Installation Repositories** (`installation_repositories`) - Triggered when a repository is added or removed from an installation
* **Issue Comment** (`issue_comment`) - Triggered when an issue comment is created, edited, or deleted
* **Issues** (`issues`) - Triggered when an issue is opened, edited, deleted, transferred, pinned, unpinned, closed, reopened, assigned, unassigned, labeled, unlabeled, locked, unlocked, milestoned, or demilestoned
* **Label** (`label`) - Triggered when a repository's label is created, edited, or deleted
* **Marketplace Purchase** (`marketplace_purchase`) - Triggered when someone purchases a GitHub Marketplace plan, cancels their plan, upgrades their plan (effective immediately), downgrades a plan that remains pending until the end of the billing cycle, or cancels a pending plan change
* **Member** (`member`) - Triggered when a user accepts an invitation or is removed as a collaborator to a repository, or has their permissions changed
* **Membership** (`membership`) - Triggered when a user is added or removed from a team. Organization hooks only.
* **Meta** (`meta`) - Triggered when the webhook that this event is configured on is deleted
* **Milestone** (`milestone`) - Triggered when a milestone is created, closed, opened, edited, or deleted
* **Org Block** (`org_block`) - Triggered when an organization blocks or unblocks a user. Organization hooks only.
* **Organization** (`organization`) - Triggered when an organization is deleted and renamed, and when a user is added, removed, or invited to an organization. Organization hooks only.
* **Page Build** (`page_build`) - Triggered on push to a GitHub Pages enabled branch (gh-pages for project pages, master for user and organization pages)
* **Project** (`project`) - Triggered when a project is created, updated, closed, reopened, or deleted
* **Project Card** (`project_card`) - Triggered when a project card is created, edited, moved, converted to an issue, or deleted
* **Project Column** (`project_column`) - Triggered when a project column is created, updated, moved, or deleted
* **Public** (`public`) - Triggered when a private repository is open sourced
* **Pull Request** (`pull_request`) - Triggered when a pull request is assigned, unassigned, labeled, unlabeled, opened, edited, closed, reopened, synchronize, ready_for_review, locked, unlocked, a pull request review is requested, or a review request is removed
* **Pull Request Review** (`pull_request_review`) - Triggered when a pull request review is submitted into a non-pending state, the body is edited, or the review is dismissed
* **Pull Request Review Comment** (`pull_request_review_comment`) - Triggered when a comment on a pull request's unified diff is created, edited, or deleted (in the Files Changed tab)
* **Push** (`push`) - Triggered on a push to a repository branch. Branch pushes and repository tag pushes also trigger webhook push events. This is the default event.
* **Release** (`release`) - Triggered when a release is published, unpublished, created, edited, deleted, or prereleased
* **Repository** (`repository`) - Triggered when a repository is created, archived, unarchived, renamed, edited, transferred, made public, or made private. Organization hooks are also triggered when a repository is deleted.
* **Repository Import** (`repository_import`) - Triggered when a successful, cancelled, or failed repository import finishes for a GitHub organization or a personal repository
* **Repository Vulnerability Alert** (`repository_vulnerability_alert`) - Triggered when a security alert is created, dismissed, or resolved
* **Security Advisory** (`security_advisory`) - Triggered when a new security advisory is published, updated, or withdrawn
* **Star** (`star`) - Triggered when a star is added or removed from a repository
* **Status** (`status`) - Triggered when the status of a Git commit changes
* **Team** (`team`) - Triggered when an organization's team is created, deleted, edited, added_to_repository, or removed_from_repository. Organization hooks only.
* **Team Add** (`team_add`) - Triggered when a repository is added to a team
* **Watch** (`watch`) - Triggered when someone stars a repository

| Options | `options` | collection | {} | ✗ | Whether the SSL certificate of the n8n host be verified by GitHub when delivering payloads | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Insecure SSL | `insecureSSL` | boolean | False | Whether the SSL certificate of the n8n host be verified by GitHub when delivering payloads |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["owner"] + "/" + $parameter["repository"] + ": " + $parameter["events"].join(", ")}}`

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
* Categories: Development

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: githubTrigger
displayName: Github Trigger
description: Starts the workflow when Github events occur
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: githubApi
  required: true
- name: githubOAuth2Api
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
- id: owner
  name: Repository Owner
  type: resourceLocator
  default: ''
  required: true
  description: ''
  placeholder: Select an owner...
  validation:
    required: true
  typeInfo:
    type: resourceLocator
    displayName: Repository Owner
    name: owner
- id: repository
  name: Repository Name
  type: resourceLocator
  default: ''
  required: true
  description: ''
  placeholder: Select an Repository...
  validation:
    required: true
  typeInfo:
    type: resourceLocator
    displayName: Repository Name
    name: repository
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: Any time any event is triggered (Wildcard Event)
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: '*'
      name: '*'
      description: Any time any event is triggered (Wildcard Event)
    - value: check_run
      name: Check Run
      description: Triggered when a check run is created, rerequested, completed,
        or has a requested_action
    - value: check_suite
      name: Check Suite
      description: Triggered when a check suite is completed, requested, or rerequested
    - value: commit_comment
      name: Commit Comment
      description: Triggered when a commit comment is created
    - value: create
      name: Create
      description: Represents a created repository, branch, or tag
    - value: delete
      name: Delete
      description: Represents a deleted branch or tag
    - value: deploy_key
      name: Deploy Key
      description: Triggered when a deploy key is added or removed from a repository
    - value: deployment
      name: Deployment
      description: Represents a deployment
    - value: deployment_status
      name: Deployment Status
      description: Represents a deployment status
    - value: fork
      name: Fork
      description: Triggered when a user forks a repository
    - value: github_app_authorization
      name: Github App Authorization
      description: Triggered when someone revokes their authorization of a GitHub
        App
    - value: gollum
      name: Gollum
      description: Triggered when a Wiki page is created or updated
    - value: installation
      name: Installation
      description: Triggered when someone installs (created), uninstalls (deleted),
        or accepts new permissions (new_permissions_accepted) for a GitHub App. When
        a GitHub App owner requests new permissions, the person who installed the
        GitHub App must accept the new permissions request.
    - value: installation_repositories
      name: Installation Repositories
      description: Triggered when a repository is added or removed from an installation
    - value: issue_comment
      name: Issue Comment
      description: Triggered when an issue comment is created, edited, or deleted
    - value: issues
      name: Issues
      description: Triggered when an issue is opened, edited, deleted, transferred,
        pinned, unpinned, closed, reopened, assigned, unassigned, labeled, unlabeled,
        locked, unlocked, milestoned, or demilestoned
    - value: label
      name: Label
      description: Triggered when a repository's label is created, edited, or deleted
    - value: marketplace_purchase
      name: Marketplace Purchase
      description: Triggered when someone purchases a GitHub Marketplace plan, cancels
        their plan, upgrades their plan (effective immediately), downgrades a plan
        that remains pending until the end of the billing cycle, or cancels a pending
        plan change
    - value: member
      name: Member
      description: Triggered when a user accepts an invitation or is removed as a
        collaborator to a repository, or has their permissions changed
    - value: membership
      name: Membership
      description: Triggered when a user is added or removed from a team. Organization
        hooks only.
    - value: meta
      name: Meta
      description: Triggered when the webhook that this event is configured on is
        deleted
    - value: milestone
      name: Milestone
      description: Triggered when a milestone is created, closed, opened, edited,
        or deleted
    - value: org_block
      name: Org Block
      description: Triggered when an organization blocks or unblocks a user. Organization
        hooks only.
    - value: organization
      name: Organization
      description: Triggered when an organization is deleted and renamed, and when
        a user is added, removed, or invited to an organization. Organization hooks
        only.
    - value: page_build
      name: Page Build
      description: Triggered on push to a GitHub Pages enabled branch (gh-pages for
        project pages, master for user and organization pages)
    - value: project
      name: Project
      description: Triggered when a project is created, updated, closed, reopened,
        or deleted
    - value: project_card
      name: Project Card
      description: Triggered when a project card is created, edited, moved, converted
        to an issue, or deleted
    - value: project_column
      name: Project Column
      description: Triggered when a project column is created, updated, moved, or
        deleted
    - value: public
      name: Public
      description: Triggered when a private repository is open sourced
    - value: pull_request
      name: Pull Request
      description: Triggered when a pull request is assigned, unassigned, labeled,
        unlabeled, opened, edited, closed, reopened, synchronize, ready_for_review,
        locked, unlocked, a pull request review is requested, or a review request
        is removed
    - value: pull_request_review
      name: Pull Request Review
      description: Triggered when a pull request review is submitted into a non-pending
        state, the body is edited, or the review is dismissed
    - value: pull_request_review_comment
      name: Pull Request Review Comment
      description: Triggered when a comment on a pull request's unified diff is created,
        edited, or deleted (in the Files Changed tab)
    - value: push
      name: Push
      description: Triggered on a push to a repository branch. Branch pushes and repository
        tag pushes also trigger webhook push events. This is the default event.
    - value: release
      name: Release
      description: Triggered when a release is published, unpublished, created, edited,
        deleted, or prereleased
    - value: repository
      name: Repository
      description: Triggered when a repository is created, archived, unarchived, renamed,
        edited, transferred, made public, or made private. Organization hooks are
        also triggered when a repository is deleted.
    - value: repository_import
      name: Repository Import
      description: Triggered when a successful, cancelled, or failed repository import
        finishes for a GitHub organization or a personal repository
    - value: repository_vulnerability_alert
      name: Repository Vulnerability Alert
      description: Triggered when a security alert is created, dismissed, or resolved
    - value: security_advisory
      name: Security Advisory
      description: Triggered when a new security advisory is published, updated, or
        withdrawn
    - value: star
      name: Star
      description: Triggered when a star is added or removed from a repository
    - value: status
      name: Status
      description: Triggered when the status of a Git commit changes
    - value: team
      name: Team
      description: Triggered when an organization's team is created, deleted, edited,
        added_to_repository, or removed_from_repository. Organization hooks only.
    - value: team_add
      name: Team Add
      description: Triggered when a repository is added to a team
    - value: watch
      name: Watch
      description: Triggered when someone stars a repository
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether the SSL certificate of the n8n host be verified by GitHub when
    delivering payloads
  placeholder: Add option
  typeInfo:
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Insecure SSL
      name: insecureSSL
      type: boolean
      description: Whether the SSL certificate of the n8n host be verified by GitHub
        when delivering payloads
      default: false
common_expressions:
- '={{$parameter["owner"] + "/" + $parameter["repository"] + ": " + $parameter["events"].join(",
  ")}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - User-Agent
  query_params: []
ui_elements:
  notices:
  - name: notice
    text: Only members with owner privileges for an organization or admin privileges
      for a repository can set up the webhooks this node requires.
    conditions: null
  tooltips: []
  placeholders:
  - field: owner
    text: Select an owner...
  - field: repository
    text: Select an Repository...
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/githubTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Github Trigger Node",
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
        "owner": {
          "description": "",
          "type": "string",
          "examples": [
            "Select an owner..."
          ]
        },
        "repository": {
          "description": "",
          "type": "string",
          "examples": [
            "Select an Repository..."
          ]
        },
        "events": {
          "description": "Any time any event is triggered (Wildcard Event)",
          "type": "string",
          "default": []
        },
        "options": {
          "description": "Whether the SSL certificate of the n8n host be verified by GitHub when delivering payloads",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
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
      "name": "githubApi",
      "required": true
    },
    {
      "name": "githubOAuth2Api",
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
