---
title: "Node: Slack"
slug: "node-slack"
version: "['2', '2.1', '2.2', '2.3']"
updated: "2025-11-13"
summary: "Consume Slack API"
node_type: "regular"
group: "['output']"
---

# Node: Slack

**Purpose.** Consume Slack API
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:slack.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **slackApi**: N/A
- **slackOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

**Node-Specific Tips:**

- **noticeAttachments** when operation=['post'], resource=['message'], messageType=['attachment']: This is a legacy Slack feature. Slack advises to instead use Blocks.

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `slackApi` | ✓ | {'show': {'authentication': ['accessToken']}} |
| `slackOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## Operations

### Channel Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Archive | `archive` | Archives a conversation |
| Close | `close` | Closes a direct message or multi-person direct message |
| Create | `create` | Initiates a public or private channel-based conversation |
| Get | `get` | Get information about a channel |
| Get Many | `getAll` | Get many channels in a Slack team |
| History | `history` | Get a conversation's history of messages and events |
| Invite | `invite` | Invite a user to a channel |
| Join | `join` | Joins an existing conversation |
| Kick | `kick` | Removes a user from a channel |
| Leave | `leave` | Leaves a conversation |
| Member | `member` | List members of a conversation |
| Open | `open` | Opens or resumes a direct message or multi-person direct message |
| Rename | `rename` | Renames a conversation |
| Replies | `replies` | Get a thread of messages posted to a channel |
| Set Purpose | `setPurpose` | Sets the purpose for a conversation |
| Set Topic | `setTopic` | Sets the topic for a conversation |
| Unarchive | `unarchive` | Unarchives a conversation |

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a message |
| Get Permalink | `getPermalink` | Get a message permalink |
| Search | `search` | Search for messages |
| Send | `post` | Send a message |
| Send and Wait for Response | `` | Send message and wait for response |
| Update | `update` | Update a message |

### Star Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a star to an item |
| Delete | `delete` | Delete a star from an item |
| Get Many | `getAll` | Get many stars of autenticated user |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a file |
| Get Many | `getAll` | Get & filters team files |
| Upload | `upload` | Create or upload an existing file |

### Reaction Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Adds a reaction to a message |
| Get | `get` | Get the reactions of a message |
| Remove | `remove` | Remove a reaction of a message |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `info` | Get information about a user |
| Get Many | `getAll` | Get a list of many users |
| Get User's Profile | `getProfile` | Get a user's profile |
| Get User's Status | `getPresence` | Get online status of a user |
| Update User's Profile | `updateProfile` | Update a user's profile |

### Usergroup Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a user group |
| Disable | `disable` | Disable a user group |
| Enable | `enable` | Enable a user group |
| Get Many | `getAll` | Get many user groups |
| Update | `update` | Update a user group |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Resource to operate on |  |

**Resource options:**

* **Channel** (`channel`)
* **File** (`file`)
* **Message** (`message`)
* **Reaction** (`reaction`)
* **Star** (`star`)
* **User** (`user`)
* **User Group** (`userGroup`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Archives a conversation |  |

**Operation options:**

* **Archive** (`archive`) - Archives a conversation
* **Close** (`close`) - Closes a direct message or multi-person direct message
* **Create** (`create`) - Initiates a public or private channel-based conversation
* **Get** (`get`) - Get information about a channel
* **Get Many** (`getAll`) - Get many channels in a Slack team
* **History** (`history`) - Get a conversation's history of messages and events
* **Invite** (`invite`) - Invite a user to a channel
* **Join** (`join`) - Joins an existing conversation
* **Kick** (`kick`) - Removes a user from a channel
* **Leave** (`leave`) - Leaves a conversation
* **Member** (`member`) - List members of a conversation
* **Open** (`open`) - Opens or resumes a direct message or multi-person direct message
* **Rename** (`rename`) - Renames a conversation
* **Replies** (`replies`) - Get a thread of messages posted to a channel
* **Set Purpose** (`setPurpose`) - Sets the purpose for a conversation
* **Set Topic** (`setTopic`) - Sets the topic for a conversation
* **Unarchive** (`unarchive`) - Unarchives a conversation

---

### Archive parameters (`archive`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✗ | The Slack channel to archive | e.g. Select a channel... |  |

### Close parameters (`close`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to close | e.g. Select a channel... |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | string |  | ✓ | e.g. Channel name |  |
| Channel Visibility | `channelVisibility` | options | public | ✓ | Whether to create a Public or a Private Slack channel. <a href="https://slack.com/help/articles/360017938993-What-is-a-channel">More info</a>. |  |

**Channel Visibility options:**

* **Public Channel** (`public`)
* **Private Channel** (`private`)

| Name | `name` | string |  | ✓ | A name for the User Group. Must be unique among User Groups. |  |
| Options | `Options` | collection | {} | ✗ | A comma-separated string of encoded channel IDs for which the User Group uses as a default. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Channel Names or IDs | `channelIds` | multiOptions | [] | A comma-separated string of encoded channel IDs for which the User Group uses as a default. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | A short description of the User Group |
| Handle | `handle` | string |  | A mention handle. Must be unique among channels, users and User Groups. |
| Include Count | `include_count` | boolean | True | Whether to include the number of users in each User Group |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to get | e.g. Select a channel... |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Num of Members | `includeNumMembers` | boolean | False |  |

</details>

| File ID | `fileId` | string |  | ✗ |  |  |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to get the reactions from | e.g. Select a channel... |  |
| Message Timestamp | `timestamp` | number |  | ✓ | Timestamp of the message to add, get or remove | e.g. 1663233118.856619 |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Whether to exclude archived channels from the list | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Archived | `excludeArchived` | boolean | False | Whether to exclude archived channels from the list |
| Types | `types` | multiOptions |  | Mix and match channel types |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Channel containing the file to be listed. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Channel Name or ID | `channelId` | options |  | Channel containing the file to be listed. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Show Files Hidden By Limit | `showFilesHidden` | boolean | False | Whether to show truncated file info for files hidden due to being too old, and the team who owns the file being over the file limit |
| Message Timestamp From | `tsFrom` | string |  | Filter files created after this timestamp (inclusive) |
| Message Timestamp To | `tsTo` | string |  | Filter files created before this timestamp (inclusive) |
| Types | `types` | multiOptions |  | Filter files by type |
| User Name or ID | `userId` | options |  | Filter files created by a single user. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Whether to include the number of users in each User Group | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Count | `include_count` | boolean | True | Whether to include the number of users in each User Group |
| Include Disabled | `include_disabled` | boolean | True | Whether to include disabled User Groups |
| Include Users | `include_users` | boolean | True | Whether to include the list of users for each User Group |

</details>


### History parameters (`history`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to get the history from | e.g. Select a channel... |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Whether to include messages with latest or oldest timestamp in results only when either timestamp is specified | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Inclusive | `inclusive` | boolean | False | Whether to include messages with latest or oldest timestamp in results only when either timestamp is specified |
| Latest | `latest` | dateTime |  | End of time range of messages to include in results |
| Oldest | `oldest` | dateTime |  | Start of time range of messages to include in results |

</details>


### Invite parameters (`invite`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to invite to | e.g. Select a channel... |  |
| User Names or IDs | `userIds` | multiOptions | [] | ✓ | The ID of the user to invite into channel. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |

### Join parameters (`join`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to join | e.g. Select a channel... |  |

### Kick parameters (`kick`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to kick the user from | e.g. Select a channel... |  |
| User Name or ID | `userId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

### Leave parameters (`leave`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to leave from | e.g. Select a channel... |  |

### Member parameters (`member`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to get the members from | e.g. Select a channel... |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | e.g. Limit | min:1, max:∞ |
| Resolve Data | `resolveData` | boolean | False | ✗ | Whether to resolve the data automatically. By default the response only contain the ID to resource. |  |

### Open parameters (`open`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Options | `options` | collection | {} | ✗ | Resume a conversation by supplying an im or mpim's ID. Or provide the users field instead. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Channel ID | `channelId` | string |  | Resume a conversation by supplying an im or mpim's ID. Or provide the users field instead. |
| Return IM | `returnIm` | boolean | False | Whether you want the full IM channel definition in the response |
| User Names or IDs | `users` | multiOptions | [] | If only one user is included, this creates a 1:1 DM. The ordering of the users is preserved whenever a multi-person direct message is returned. Supply a channel when not supplying users. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Rename parameters (`rename`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to rename | e.g. Select a channel... |  |
| Name | `name` | string |  | ✓ | New name for conversation |  |

### Replies parameters (`replies`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to replies to | e.g. Select a channel... |  |
| Message Timestamp | `ts` | number |  | ✓ | Timestamp of the message to reply | e.g. 1663233118.856619 |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Whether to include messages with latest or oldest timestamp in results only when either timestamp is specified | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Inclusive | `inclusive` | boolean | False | Whether to include messages with latest or oldest timestamp in results only when either timestamp is specified |
| Latest | `latest` | string |  | End of time range of messages to include in results |
| Oldest | `oldest` | string |  | Start of time range of messages to include in results |

</details>


### Set Purpose parameters (`setPurpose`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to set the purpose of | e.g. Select a channel... |  |
| Purpose | `purpose` | string |  | ✓ | A new, specialer purpose |  |

### Set Topic parameters (`setTopic`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to set the topic of | e.g. Select a channel... |  |
| Topic | `topic` | string |  | ✓ |  |  |

### Unarchive parameters (`unarchive`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to unarchive | e.g. Select a channel... |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Delete Message From | `select` | options |  | ✓ | e.g. Select... |  |

**Delete Message From options:**

* **Channel** (`channel`)
* **User** (`user`)

| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to delete the message from | e.g. Select a channel... |  |
| User | `user` | resourceLocator |  | ✗ | e.g. Select a user... |  |
| Message Timestamp | `timestamp` | number |  | ✓ | Timestamp of the message to delete | e.g. 1663233118.856619 |  |
| Options | `options` | collection | {} | ✗ | Options to set | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Channel Name or ID | `channelId` | options |  | Channel to add star to, or channel where the message to add star to was posted (used with timestamp). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| File ID | `fileId` | string |  | File to add star to |
| File Comment | `fileComment` | string |  | File comment to add star to |
| Message Timestamp | `timestamp` | number | 0 | Timestamp of the message to delete |

</details>


### Get Permalink parameters (`getPermalink`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✗ | The Slack channel to get the message permalink from | e.g. Select a channel... |  |
| Message Timestamp | `timestamp` | number |  | ✓ | Timestamp of the message to message | e.g. 1663233118.856619 |  |

### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Search Query | `query` | string |  | ✓ | The text to search for within messages |  |
| Sort By | `sort` | options | desc | ✗ | How search results should be sorted. You can sort by. |  |

**Sort By options:**

* **Newest** (`desc`)
* **Oldest** (`asc`)
* **Relevance Score** (`relevance`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 25 | ✗ | Max number of results to return | min:1, max:50 |
| Options | `options` | collection | [] | ✗ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Search in Channel | `searchChannel` | multiOptions | [] | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>


### Send parameters (`post`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message Type | `messageType` | options | text | ✗ | Whether to send a simple text message, or use Slack’s Blocks UI builder for more sophisticated messages that include form fields, sections and more |  |

**Message Type options:**

* **Simple Text Message** (`text`) - Supports basic Markdown
* **Blocks** (`block`) - Combine text, buttons, form elements, dividers and more in Slack 's visual builder
* **Attachments** (`attachment`)

| Message Text | `text` | string |  | ✓ | The message text to post. Supports <a href="https://api.slack.com/reference/surfaces/formatting">markdown</a> by default - this can be disabled in "Options". |  |
| Blocks | `blocksUi` | string |  | ✓ | Enter the JSON output from Slack's visual Block Kit Builder here. You can then use expressions to add variable content to your blocks. To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's Block Kit Builder</a> | e.g. To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's Block Kit Builder</a> |  |
| Notification Text | `text` | string |  | ✗ | Fallback text to display in slack notifications. Supports <a href="https://api.slack.com/reference/surfaces/formatting">markdown</a> by default - this can be disabled in "Options". |  |
| Attachments | `attachments` | collection | {} | ✗ | Required plain-text summary of the attachment | e.g. Add attachment item |  |

<details>
<summary><strong>Attachments sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fallback Text | `fallback` | string |  | Required plain-text summary of the attachment |
| Text | `text` | string |  |  |
| Title | `title` | string |  |  |
| Title Link | `title_link` | string |  |  |
| Color | `color` | color | #ff0000 | Color of the line left of text |
| Pretext | `pretext` | string |  | Text which appears before the message block |
| Author Name | `author_name` | string |  | Name that should appear |
| Author Link | `author_link` | string |  |  |
| Author Icon | `author_icon` | string |  | Icon which should appear for the user |
| Image URL | `image_url` | string |  |  |
| Thumbnail URL | `thumb_url` | string |  |  |
| Footer | `footer` | string |  | Text of footer to add |
| Footer Icon | `footer_icon` | string |  | Icon which should appear next to footer |
| Message Timestamp | `ts` | number | 0 | Timestamp of the message to post |
| Fields | `fields` | fixedCollection | {} | Fields to add to message |

</details>

| Options | `otherOptions` | collection | {} | ✗ | Other options to set | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Link to Workflow | `includeLinkToWorkflow` | boolean | True | Whether to append a link to this workflow at the end of the message. This is helpful if you have many workflows sending Slack messages. |
| Custom Bot Profile Photo | `botProfile` | fixedCollection |  | Set an image or an emoji as the Profile Photo (avatar) of the bot sending the message. Will not be used if sending message as a user. |
| Link User and Channel Names | `link_names` | boolean | False | Whether to turn @users and #channels in message text into clickable links |
| Reply to a Message | `thread_ts` | fixedCollection | {} | Provide another message's Timestamp value to make this message a reply |
| Use Markdown? | `mrkdwn` | boolean | True | Whether to use Slack Markdown to format the message |
| Unfurl Links | `unfurl_links` | boolean | False | Whether to enable unfurling of primarily text-based content |
| Unfurl Media | `unfurl_media` | boolean | True | Whether to disable unfurling of media content |
| Send as Ephemeral Message | `ephemeral` | fixedCollection | {} | Whether to send a temporary, ephemeral message |
| Send as Ephemeral Message | `ephemeral` | boolean | True | Whether to send a temporary, ephemeral message |
| Send as User | `sendAsUser` | string |  | The message will be sent from this username (i.e. as if this individual sent the message). Add chat:write.customize scope on Slack API |

</details>

| Send Message To | `select` | options |  | ✓ | e.g. Select... |  |

**Send Message To options:**

* **Channel** (`channel`)
* **User** (`user`)


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to update the message from | e.g. Select a channel... |  |
| Message Timestamp | `ts` | number |  | ✓ | Timestamp of the message to update | e.g. 1663233118.856619 |  |
| Message Type | `messageType` | options | text | ✗ | Whether to send a simple text message, or use Slack’s Blocks UI builder for more sophisticated messages that include form fields, sections and more |  |

**Message Type options:**

* **Simple Text Message** (`text`) - Supports basic Markdown
* **Blocks** (`block`) - Combine text, buttons, form elements, dividers and more in Slack 's visual builder
* **Attachments** (`attachment`)

| Blocks | `blocksUi` | string |  | ✓ | Enter the JSON output from Slack's visual Block Kit Builder here. You can then use expressions to add variable content to your blocks. To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's Block Kit Builder</a> | e.g. To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's Block Kit Builder</a> |  |
| Notification Text | `text` | string |  | ✗ | Fallback text to display in slack notifications. Supports <a href="https://api.slack.com/reference/surfaces/formatting">markdown</a> by default - this can be disabled in "Options". |  |
| Message Text | `text` | string |  | ✗ | The message text to update. Supports <a href="https://api.slack.com/reference/surfaces/formatting/">markdown</a> by default - this can be disabled in "Options". |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Whether to find and link channel names and usernames | e.g. Add option |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Link User and Channel Names | `link_names` | boolean | False | Whether to find and link channel names and usernames |
| Parse | `parse` | options | client | Change how messages are treated |

</details>

| Options | `otherOptions` | collection | {} | ✗ | Other options to set | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Link to Workflow | `includeLinkToWorkflow` | boolean | True | Whether to append a link to this workflow at the end of the message. This is helpful if you have many workflows sending Slack messages. |

</details>

| User Group ID | `userGroupId` | string |  | ✓ | The encoded ID of the User Group to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | A comma-separated string of encoded channel IDs for which the User Group uses as a default. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Channel Names or IDs | `channels` | multiOptions | [] | A comma-separated string of encoded channel IDs for which the User Group uses as a default. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | A short description of the User Group |
| Handle | `handle` | string |  | A mention handle. Must be unique among channels, users and User Groups. |
| Include Count | `include_count` | boolean | True | Whether to include the number of users in each User Group |
| Name | `name` | string |  | A name for the User Group. Must be unique among User Groups. |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Item to Add Star | `target` | options |  | ✓ | Choose whether to add a star to a message or a file | e.g. Select... |  |

**Item to Add Star options:**

* **Message** (`message`)
* **File** (`file`)

| Channel | `channelId` | resourceLocator |  | ✗ | The Slack channel to add a star to | e.g. Select a channel... |  |
| File ID | `fileId` | string |  | ✗ | File to add star to |  |
| Message Timestamp | `timestamp` | number |  | ✗ | Timestamp of the message to add | e.g. 1663233118.856619 |  |
| Options | `options` | collection | {} | ✗ | Options to set | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Comment | `fileComment` | string |  | File comment to add star to |

</details>

| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to get the reactions from | e.g. Select a channel... |  |
| Message Timestamp | `timestamp` | number |  | ✓ | Timestamp of the message to add, get or remove | e.g. 1663233118.856619 |  |
| Emoji Code | `name` | string |  | ✓ | Emoji code to use for the message reaction. Use emoji codes like +1, not an actual emoji like 👍. <a target="_blank" href=" https://www.webfx.com/tools/emoji-cheat-sheet/">List of common emoji codes</a> | e.g. +1 |  |

### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Binary File | `binaryData` | boolean | False | ✗ | Whether the data to upload should be taken from binary field |  |
| File Content | `fileContent` | string |  | ✗ |  |  |
| File Property | `binaryPropertyName` | string | data | ✓ | Name of the binary property which contains the data for the file to be uploaded |  |
| File Property | `binaryPropertyName` | string | data | ✓ | Name of the binary property which contains the data for the file to be uploaded |  |
| Options | `options` | collection | {} | ✗ | Other options to set | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Channel Names or IDs | `channelIds` | multiOptions | [] | The channels to send the file to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Channel Name or ID | `channelId` | options | [] | The channel to send the file to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| File Name | `fileName` | string |  |  |
| Initial Comment | `initialComment` | string |  | The message text introducing the file in specified channels |
| Thread Timestamp | `threadTs` | string |  | Provide another message's Timestamp value to upload this file as a reply. Never use a reply's Timestamp value; use its parent instead. |
| Title | `title` | string |  |  |

</details>


### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel | `channelId` | resourceLocator |  | ✓ | The Slack channel to get the reactions from | e.g. Select a channel... |  |
| Message Timestamp | `timestamp` | number |  | ✓ | Timestamp of the message to add, get or remove | e.g. 1663233118.856619 |  |
| Emoji Code | `name` | string |  | ✓ | Emoji code to use for the message reaction. Use emoji codes like +1, not an actual emoji like 👍. <a target="_blank" href=" https://www.webfx.com/tools/emoji-cheat-sheet/">List of common emoji codes</a> | e.g. +1 |  |

### Get parameters (`info`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User | `user` | resourceLocator |  | ✗ | The ID of the user to get information about | e.g. Select a user... |  |

### Get User's Profile parameters (`getProfile`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User | `user` | resourceLocator |  | ✗ | The ID of the user to get information about | e.g. Select a user... |  |

### Get User's Status parameters (`getPresence`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User | `user` | resourceLocator |  | ✗ | The ID of the user to get the online status of | e.g. Select a user... |  |

### Update User's Profile parameters (`updateProfile`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Options | `options` | collection | {} | ✗ | ID of the field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `customFieldUi` | fixedCollection | {} | ID of the field to set. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Email | `email` | string |  | This field can only be changed by admins for users on paid teams |
| First Name | `first_name` | string |  |  |
| Last Name | `last_name` | string |  |  |
| Set Status | `status` | fixedCollection | {} | Is a string referencing an emoji enabled for the Slack team, such as :mountain_railway: |
| User ID | `user` | string |  | ID of user to change. This argument may only be specified by team admins on paid teams. |

</details>


### Disable parameters (`disable`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User Group ID | `userGroupId` | string |  | ✓ | The encoded ID of the User Group to update |  |
| Options | `options` | collection | {} | ✗ | Whether to include the number of users in each User Group | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Count | `include_count` | boolean | True | Whether to include the number of users in each User Group |

</details>


### Enable parameters (`enable`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User Group ID | `userGroupId` | string |  | ✓ | The encoded ID of the User Group to update |  |
| Options | `option` | collection | {} | ✗ | Whether to include the number of users in each User Group | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Count | `include_count` | boolean | True | Whether to include the number of users in each User Group |

</details>


---

## Load Options Methods

- `getUsers`
- `for`
- `name`
- `value`

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

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: Slack
displayName: Slack
description: Consume Slack API
version:
- '2'
- '2.1'
- '2.2'
- '2.3'
nodeType: regular
group:
- output
credentials:
- name: slackApi
  required: true
- name: slackOAuth2Api
  required: true
operations:
- id: archive
  name: Archive
  description: Archives a conversation
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: false
    description: The Slack channel to archive
    placeholder: Select a channel...
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - reaction
          operation:
          - add
          - get
          - remove
    typeInfo: &id002
      type: resourceLocator
      displayName: Channel
      name: channelId
- id: close
  name: Close
  description: Closes a direct message or multi-person direct message
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to close
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
- id: create
  name: Create
  description: Initiates a public or private channel-based conversation
  params:
  - id: channelId
    name: Channel
    type: string
    default: ''
    required: true
    description: ''
    placeholder: Channel name
    validation: *id001
    typeInfo: *id002
  - id: channelVisibility
    name: Channel Visibility
    type: options
    default: public
    required: true
    description: Whether to create a Public or a Private Slack channel. <a href="https://slack.com/help/articles/360017938993-What-is-a-channel">More
      info</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - channel
    typeInfo:
      type: options
      displayName: Channel Visibility
      name: channelVisibility
      possibleValues:
      - value: public
        name: Public Channel
        description: ''
      - value: private
        name: Private Channel
        description: ''
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: A name for the User Group. Must be unique among User Groups.
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - userGroup
    typeInfo: &id008
      type: string
      displayName: Name
      name: name
- id: get
  name: Get
  description: Get information about a channel
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to get
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id021
      displayOptions:
        show:
          resource:
          - file
          operation:
          - get
    typeInfo: &id022
      type: string
      displayName: File ID
      name: fileId
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to get the reactions from
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: timestamp
    name: Message Timestamp
    type: number
    default: ''
    required: true
    description: Timestamp of the message to add, get or remove
    placeholder: '1663233118.856619'
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - reaction
          operation:
          - add
          - get
          - remove
    typeInfo: &id010
      type: number
      displayName: Message Timestamp
      name: timestamp
- id: getAll
  name: Get Many
  description: Get many channels in a Slack team
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
          operation:
          - getAll
          resource:
          - userGroup
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - userGroup
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: history
  name: History
  description: Get a conversation's history of messages and events
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to get the history from
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: invite
  name: Invite
  description: Invite a user to a channel
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to invite to
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: userIds
    name: User Names or IDs
    type: multiOptions
    default: []
    required: true
    description: The ID of the user to invite into channel. Choose from the list,
      or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - invite
          resource:
          - channel
    typeInfo:
      type: multiOptions
      displayName: User Names or IDs
      name: userIds
      typeOptions:
        loadOptionsMethod: getUsers
      possibleValues: []
- id: join
  name: Join
  description: Joins an existing conversation
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to join
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
- id: kick
  name: Kick
  description: Removes a user from a channel
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to kick the user from
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: userId
    name: User Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      displayOptions:
        show:
          operation:
          - kick
          resource:
          - channel
    typeInfo:
      type: options
      displayName: User Name or ID
      name: userId
      typeOptions:
        loadOptionsMethod: getUsers
      possibleValues: []
- id: leave
  name: Leave
  description: Leaves a conversation
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to leave from
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
- id: member
  name: Member
  description: List members of a conversation
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to get the members from
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
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
    default: 100
    required: false
    description: Max number of results to return
    placeholder: Limit
    validation: *id005
    typeInfo: *id006
  - id: resolveData
    name: Resolve Data
    type: boolean
    default: false
    required: false
    description: Whether to resolve the data automatically. By default the response
      only contain the ID to resource.
    validation:
      displayOptions:
        show:
          resource:
          - channel
          operation:
          - member
    typeInfo:
      type: boolean
      displayName: Resolve Data
      name: resolveData
- id: open
  name: Open
  description: Opens or resumes a direct message or multi-person direct message
  params: []
- id: rename
  name: Rename
  description: Renames a conversation
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to rename
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: New name for conversation
    validation: *id007
    typeInfo: *id008
- id: replies
  name: Replies
  description: Get a thread of messages posted to a channel
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to replies to
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: ts
    name: Message Timestamp
    type: number
    default: ''
    required: true
    description: Timestamp of the message to reply
    placeholder: '1663233118.856619'
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - update
    typeInfo: &id016
      type: number
      displayName: Message Timestamp
      name: ts
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
    default: 50
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: setPurpose
  name: Set Purpose
  description: Sets the purpose for a conversation
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to set the purpose of
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: purpose
    name: Purpose
    type: string
    default: ''
    required: true
    description: A new, specialer purpose
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - setPurpose
          resource:
          - channel
    typeInfo:
      type: string
      displayName: Purpose
      name: purpose
- id: setTopic
  name: Set Topic
  description: Sets the topic for a conversation
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to set the topic of
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: topic
    name: Topic
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - setTopic
          resource:
          - channel
    typeInfo:
      type: string
      displayName: Topic
      name: topic
- id: unarchive
  name: Unarchive
  description: Unarchives a conversation
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to unarchive
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete
  description: ''
  params:
  - id: select
    name: Delete Message From
    type: options
    default: ''
    required: true
    description: ''
    placeholder: Select...
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - post
    typeInfo: &id014
      type: options
      displayName: Send Message To
      name: select
      possibleValues:
      - value: channel
        name: Channel
        description: ''
      - value: user
        name: User
        description: ''
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to delete the message from
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: user
    name: User
    type: resourceLocator
    default: ''
    required: false
    description: ''
    placeholder: Select a user...
    validation: &id025
      displayOptions:
        show:
          operation:
          - getPresence
          resource:
          - user
    typeInfo: &id026
      type: resourceLocator
      displayName: User
      name: user
  - id: timestamp
    name: Message Timestamp
    type: number
    default: ''
    required: true
    description: Timestamp of the message to delete
    placeholder: '1663233118.856619'
    validation: *id009
    typeInfo: *id010
- id: getPermalink
  name: Get Permalink
  description: ''
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: false
    description: The Slack channel to get the message permalink from
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: timestamp
    name: Message Timestamp
    type: number
    default: ''
    required: true
    description: Timestamp of the message to message
    placeholder: '1663233118.856619'
    validation: *id009
    typeInfo: *id010
- id: search
  name: Search
  description: ''
  params:
  - id: query
    name: Search Query
    type: string
    default: ''
    required: true
    description: The text to search for within messages
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - message
          operation:
          - search
    typeInfo:
      type: string
      displayName: Search Query
      name: query
  - id: sort
    name: Sort By
    type: options
    default: desc
    required: false
    description: How search results should be sorted. You can sort by.
    validation:
      displayOptions:
        show:
          resource:
          - message
          operation:
          - search
    typeInfo:
      type: options
      displayName: Sort By
      name: sort
      possibleValues:
      - value: desc
        name: Newest
        description: ''
      - value: asc
        name: Oldest
        description: ''
      - value: relevance
        name: Relevance Score
        description: ''
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
    default: 25
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: post
  name: Send
  description: ''
  params:
  - id: messageType
    name: Message Type
    type: options
    default: text
    required: false
    description: Whether to send a simple text message, or use Slack’s Blocks UI builder
      for more sophisticated messages that include form fields, sections and more
    validation: &id017
      displayOptions:
        show:
          operation:
          - update
          resource:
          - message
    typeInfo: &id018
      type: options
      displayName: Message Type
      name: messageType
      possibleValues:
      - value: text
        name: Simple Text Message
        description: Supports basic Markdown
      - value: block
        name: Blocks
        description: Combine text, buttons, form elements, dividers and more in Slack
          's visual builder
      - value: attachment
        name: Attachments
        description: ''
  - id: text
    name: Message Text
    type: string
    default: ''
    required: true
    description: The message text to post. Supports <a href="https://api.slack.com/reference/surfaces/formatting">markdown</a>
      by default - this can be disabled in "Options".
    validation: &id011
      displayOptions:
        show:
          resource:
          - message
          operation:
          - update
          messageType:
          - text
    typeInfo: &id012
      type: string
      displayName: Message Text
      name: text
  - id: blocksUi
    name: Blocks
    type: string
    default: ''
    required: true
    description: Enter the JSON output from Slack's visual Block Kit Builder here.
      You can then use expressions to add variable content to your blocks. To create
      blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's
      Block Kit Builder</a>
    hint: To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's
      Block Kit Builder</a>
    validation: &id019
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - message
          messageType:
          - block
    typeInfo: &id020
      type: string
      displayName: Blocks
      name: blocksUi
      typeOptions:
        rows: 3
  - id: text
    name: Notification Text
    type: string
    default: ''
    required: false
    description: Fallback text to display in slack notifications. Supports <a href="https://api.slack.com/reference/surfaces/formatting">markdown</a>
      by default - this can be disabled in "Options".
    validation: *id011
    typeInfo: *id012
  - id: select
    name: Send Message To
    type: options
    default: ''
    required: true
    description: ''
    placeholder: Select...
    validation: *id013
    typeInfo: *id014
- id: ''
  name: Send and Wait for Response
  description: ''
- id: update
  name: Update
  description: ''
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to update the message from
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: ts
    name: Message Timestamp
    type: number
    default: ''
    required: true
    description: Timestamp of the message to update
    placeholder: '1663233118.856619'
    validation: *id015
    typeInfo: *id016
  - id: messageType
    name: Message Type
    type: options
    default: text
    required: false
    description: Whether to send a simple text message, or use Slack’s Blocks UI builder
      for more sophisticated messages that include form fields, sections and more
    validation: *id017
    typeInfo: *id018
  - id: blocksUi
    name: Blocks
    type: string
    default: ''
    required: true
    description: Enter the JSON output from Slack's visual Block Kit Builder here.
      You can then use expressions to add variable content to your blocks. To create
      blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's
      Block Kit Builder</a>
    hint: To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's
      Block Kit Builder</a>
    validation: *id019
    typeInfo: *id020
  - id: text
    name: Notification Text
    type: string
    default: ''
    required: false
    description: Fallback text to display in slack notifications. Supports <a href="https://api.slack.com/reference/surfaces/formatting">markdown</a>
      by default - this can be disabled in "Options".
    validation: *id011
    typeInfo: *id012
  - id: text
    name: Message Text
    type: string
    default: ''
    required: false
    description: The message text to update. Supports <a href="https://api.slack.com/reference/surfaces/formatting/">markdown</a>
      by default - this can be disabled in "Options".
    validation: *id011
    typeInfo: *id012
  - id: userGroupId
    name: User Group ID
    type: string
    default: ''
    required: true
    description: The encoded ID of the User Group to update
    validation: &id027
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - userGroup
    typeInfo: &id028
      type: string
      displayName: User Group ID
      name: userGroupId
- id: add
  name: Add
  description: Add a star to an item
  params:
  - id: target
    name: Item to Add Star
    type: options
    default: ''
    required: true
    description: Choose whether to add a star to a message or a file
    placeholder: Select...
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - add
          resource:
          - star
    typeInfo:
      type: options
      displayName: Item to Add Star
      name: target
      possibleValues:
      - value: message
        name: Message
        description: ''
      - value: file
        name: File
        description: ''
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: false
    description: The Slack channel to add a star to
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: false
    description: File to add star to
    validation: *id021
    typeInfo: *id022
  - id: timestamp
    name: Message Timestamp
    type: number
    default: ''
    required: false
    description: Timestamp of the message to add
    placeholder: '1663233118.856619'
    validation: *id009
    typeInfo: *id010
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to get the reactions from
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: timestamp
    name: Message Timestamp
    type: number
    default: ''
    required: true
    description: Timestamp of the message to add, get or remove
    placeholder: '1663233118.856619'
    validation: *id009
    typeInfo: *id010
  - id: name
    name: Emoji Code
    type: string
    default: ''
    required: true
    description: Emoji code to use for the message reaction. Use emoji codes like
      +1, not an actual emoji like 👍. <a target="_blank" href=" https://www.webfx.com/tools/emoji-cheat-sheet/">List
      of common emoji codes</a>
    placeholder: '+1'
    validation: *id007
    typeInfo: *id008
- id: upload
  name: Upload
  description: Create or upload an existing file
  params:
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: false
    description: Whether the data to upload should be taken from binary field
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo:
      type: boolean
      displayName: Binary File
      name: binaryData
  - id: fileContent
    name: File Content
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
          binaryData:
          - false
    typeInfo:
      type: string
      displayName: File Content
      name: fileContent
  - id: binaryPropertyName
    name: File Property
    type: string
    default: data
    required: true
    description: Name of the binary property which contains the data for the file
      to be uploaded
    validation: &id023
      required: true
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo: &id024
      type: string
      displayName: File Property
      name: binaryPropertyName
  - id: binaryPropertyName
    name: File Property
    type: string
    default: data
    required: true
    description: Name of the binary property which contains the data for the file
      to be uploaded
    validation: *id023
    typeInfo: *id024
- id: remove
  name: Remove
  description: Remove a reaction of a message
  params:
  - id: channelId
    name: Channel
    type: resourceLocator
    default: ''
    required: true
    description: The Slack channel to get the reactions from
    placeholder: Select a channel...
    validation: *id001
    typeInfo: *id002
  - id: timestamp
    name: Message Timestamp
    type: number
    default: ''
    required: true
    description: Timestamp of the message to add, get or remove
    placeholder: '1663233118.856619'
    validation: *id009
    typeInfo: *id010
  - id: name
    name: Emoji Code
    type: string
    default: ''
    required: true
    description: Emoji code to use for the message reaction. Use emoji codes like
      +1, not an actual emoji like 👍. <a target="_blank" href=" https://www.webfx.com/tools/emoji-cheat-sheet/">List
      of common emoji codes</a>
    placeholder: '+1'
    validation: *id007
    typeInfo: *id008
- id: info
  name: Get
  description: Get information about a user
  params:
  - id: user
    name: User
    type: resourceLocator
    default: ''
    required: false
    description: The ID of the user to get information about
    placeholder: Select a user...
    validation: *id025
    typeInfo: *id026
- id: getProfile
  name: Get User's Profile
  description: Get a user's profile
  params:
  - id: user
    name: User
    type: resourceLocator
    default: ''
    required: false
    description: The ID of the user to get information about
    placeholder: Select a user...
    validation: *id025
    typeInfo: *id026
- id: getPresence
  name: Get User's Status
  description: Get online status of a user
  params:
  - id: user
    name: User
    type: resourceLocator
    default: ''
    required: false
    description: The ID of the user to get the online status of
    placeholder: Select a user...
    validation: *id025
    typeInfo: *id026
- id: updateProfile
  name: Update User's Profile
  description: Update a user's profile
  params: []
- id: disable
  name: Disable
  description: ''
  params:
  - id: userGroupId
    name: User Group ID
    type: string
    default: ''
    required: true
    description: The encoded ID of the User Group to update
    validation: *id027
    typeInfo: *id028
- id: enable
  name: Enable
  description: ''
  params:
  - id: userGroupId
    name: User Group ID
    type: string
    default: ''
    required: true
    description: The encoded ID of the User Group to update
    validation: *id027
    typeInfo: *id028
api_patterns:
  http_methods: []
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices:
  - name: noticeAttachments
    text: This is a legacy Slack feature. Slack advises to instead use Blocks.
    conditions:
      show:
        operation:
        - post
        resource:
        - message
        messageType:
        - attachment
  tooltips: []
  placeholders:
  - field: channelId
    text: Select a channel...
  - field: channelId
    text: Select a channel...
  - field: channelId
    text: Channel name
  - field: channelId
    text: Select a channel...
  - field: channelId
    text: Select a channel...
  - field: options
    text: Add Field
  - field: channelId
    text: Select a channel...
  - field: channelId
    text: Select a channel...
  - field: filters
    text: Add Field
  - field: channelId
    text: Select a channel...
  - field: filters
    text: Add Field
  - field: channelId
    text: Select a channel...
  - field: channelId
    text: Select a channel...
  - field: limit
    text: Limit
  - field: options
    text: Add Field
  - field: channelId
    text: Select a channel...
  - field: channelId
    text: Select a channel...
  - field: ts
    text: '1663233118.856619'
  - field: filters
    text: Add Field
  - field: channelId
    text: Select a channel...
  - field: channelId
    text: Select a channel...
  - field: channelId
    text: Select a channel...
  - field: channelId
    text: Select a channel...
  - field: timestamp
    text: '1663233118.856619'
  - field: attachments
    text: Add attachment item
  - field: otherOptions
    text: Add option
  - field: channelId
    text: Select a channel...
  - field: ts
    text: '1663233118.856619'
  - field: updateFields
    text: Add option
  - field: otherOptions
    text: Add option
  - field: select
    text: Select...
  - field: channelId
    text: Select a channel...
  - field: user
    text: Select a user...
  - field: timestamp
    text: '1663233118.856619'
  - field: options
    text: Add option
  - field: select
    text: Select...
  - field: channelId
    text: Select a channel...
  - field: user
    text: Select a user...
  - field: target
    text: Select...
  - field: channelId
    text: Select a channel...
  - field: timestamp
    text: '1663233118.856619'
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: filters
    text: Add Field
  - field: channelId
    text: Select a channel...
  - field: timestamp
    text: '1663233118.856619'
  - field: name
    text: '+1'
  - field: user
    text: Select a user...
  - field: user
    text: Select a user...
  - field: options
    text: Add Field
  - field: Options
    text: Add Field
  - field: options
    text: Add Field
  - field: option
    text: Add Field
  - field: options
    text: Add Field
  - field: updateFields
    text: Add Field
  hints:
  - field: blocksUi
    text: To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's
      Block Kit Builder</a>
  - field: blocksUi
    text: To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's
      Block Kit Builder</a>
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
  "$id": "https://n8n.io/schemas/nodes/Slack.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Slack Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "archive",
        "close",
        "create",
        "get",
        "getAll",
        "history",
        "invite",
        "join",
        "kick",
        "leave",
        "member",
        "open",
        "rename",
        "replies",
        "setPurpose",
        "setTopic",
        "unarchive",
        "delete",
        "getPermalink",
        "search",
        "post",
        "",
        "update",
        "add",
        "upload",
        "remove",
        "info",
        "getProfile",
        "getPresence",
        "updateProfile",
        "disable",
        "enable"
      ],
      "description": "Operation to perform"
    },
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
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "channel",
            "file",
            "message",
            "reaction",
            "star",
            "user",
            "userGroup"
          ],
          "default": "message"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "create",
            "disable",
            "enable",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "channelId": {
          "description": "The Slack channel to get the reactions from",
          "type": "string",
          "examples": [
            "Select a channel..."
          ]
        },
        "channelVisibility": {
          "description": "Whether to create a Public or a Private Slack channel. <a href=\"https://slack.com/help/articles/360017938993-What-is-a-channel\">More info</a>.",
          "type": "string",
          "enum": [
            "public",
            "private"
          ],
          "default": "public"
        },
        "userIds": {
          "description": "The ID of the user to invite into channel. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "options": {
          "description": "Whether to include the number of users in each User Group",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "userId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
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
          "default": 100
        },
        "filters": {
          "description": "Channel containing the file to be listed. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "resolveData": {
          "description": "Whether to resolve the data automatically. By default the response only contain the ID to resource.",
          "type": "boolean",
          "default": false
        },
        "name": {
          "description": "A name for the User Group. Must be unique among User Groups.",
          "type": "string",
          "default": ""
        },
        "ts": {
          "description": "Timestamp of the message to update",
          "type": "number",
          "examples": [
            "1663233118.856619"
          ]
        },
        "purpose": {
          "description": "A new, specialer purpose",
          "type": "string",
          "default": ""
        },
        "topic": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "timestamp": {
          "description": "Timestamp of the message to add, get or remove",
          "type": "number",
          "examples": [
            "1663233118.856619"
          ]
        },
        "messageType": {
          "description": "Whether to send a simple text message, or use Slack\u2019s Blocks UI builder for more sophisticated messages that include form fields, sections and more",
          "type": "string",
          "enum": [
            "text",
            "block",
            "attachment"
          ],
          "default": "text"
        },
        "text": {
          "description": "The message text to update. Supports <a href=\"https://api.slack.com/reference/surfaces/formatting/\">markdown</a> by default - this can be disabled in \"Options\".",
          "type": "string",
          "default": ""
        },
        "blocksUi": {
          "description": "Enter the JSON output from Slack's visual Block Kit Builder here. You can then use expressions to add variable content to your blocks. To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's Block Kit Builder</a>",
          "type": "string",
          "default": ""
        },
        "attachments": {
          "description": "Required plain-text summary of the attachment",
          "type": "string",
          "default": {},
          "examples": [
            "Add attachment item"
          ]
        },
        "otherOptions": {
          "description": "Other options to set",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "updateFields": {
          "description": "A comma-separated string of encoded channel IDs for which the User Group uses as a default. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "select": {
          "description": "",
          "type": "string",
          "enum": [
            "channel",
            "user"
          ],
          "default": "",
          "examples": [
            "Select..."
          ]
        },
        "user": {
          "description": "The ID of the user to get the online status of",
          "type": "string",
          "examples": [
            "Select a user..."
          ]
        },
        "query": {
          "description": "The text to search for within messages",
          "type": "string",
          "default": ""
        },
        "sort": {
          "description": "How search results should be sorted. You can sort by.",
          "type": "string",
          "enum": [
            "desc",
            "asc",
            "relevance"
          ],
          "default": "desc"
        },
        "target": {
          "description": "Choose whether to add a star to a message or a file",
          "type": "string",
          "enum": [
            "message",
            "file"
          ],
          "default": "",
          "examples": [
            "Select..."
          ]
        },
        "fileId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "binaryData": {
          "description": "Whether the data to upload should be taken from binary field",
          "type": "boolean",
          "default": false
        },
        "fileContent": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "binaryPropertyName": {
          "description": "Name of the binary property which contains the data for the file to be uploaded",
          "type": "string",
          "default": "data"
        },
        "Options": {
          "description": "A comma-separated string of encoded channel IDs for which the User Group uses as a default. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "userGroupId": {
          "description": "The encoded ID of the User Group to update",
          "type": "string",
          "default": ""
        },
        "option": {
          "description": "Whether to include the number of users in each User Group",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "default": {
          "description": "",
          "type": "string"
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
      "2",
      "2.1",
      "2.2",
      "2.3"
    ]
  },
  "credentials": [
    {
      "name": "slackApi",
      "required": true
    },
    {
      "name": "slackOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2', '2.1', '2.2', '2.3'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
