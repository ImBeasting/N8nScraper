---
title: "Node: YouTube"
slug: "node-youtube"
version: "1"
updated: "2025-11-13"
summary: "Consume YouTube API"
node_type: "regular"
group: "['input']"
---

# Node: YouTube

**Purpose.** Consume YouTube API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:youTube.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **youTubeOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `youTubeOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Channel Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Retrieve a channel |
| Get Many | `getAll` | Retrieve many channels |
| Update | `update` | Update a channel |
| Upload Banner | `uploadBanner` | Upload a channel banner |

### Playlist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a playlist |
| Delete | `delete` | Delete a playlist |
| Get | `get` | Get a playlist |
| Get Many | `getAll` | Retrieve many playlists |
| Update | `update` | Update a playlist |

### Playlistitem Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add an item to a playlist |
| Delete | `delete` | Delete a item from a playlist |
| Get | `get` | Get a playlist's item |
| Get Many | `getAll` | Retrieve many playlist items |

### Video Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a video |
| Get | `get` | Get a video |
| Get Many | `getAll` | Retrieve many videos |
| Rate | `rate` | Rate a video |
| Update | `update` | Update a video |
| Upload | `upload` | Upload a video |

### Videocategory Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Retrieve many video categories |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | channel | ✗ | Resource to operate on |  |

**Resource options:**

* **Channel** (`channel`)
* **Playlist** (`playlist`)
* **Playlist Item** (`playlistItem`)
* **Video** (`video`)
* **Video Category** (`videoCategory`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Retrieve a channel |  |

**Operation options:**

* **Get** (`get`) - Retrieve a channel
* **Get Many** (`getAll`) - Retrieve many channels
* **Update** (`update`) - Update a channel
* **Upload Banner** (`uploadBanner`) - Upload a channel banner

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel ID | `channelId` | string |  | ✓ | ID of the channel |  |
| Fields | `part` | multiOptions |  | ✓ | The fields parameter specifies a comma-separated list of one or more channel resource properties that the API response will include |  |

**Fields options:**

* ***** (`*`)
* **Branding Settings** (`brandingSettings`)
* **Content Details** (`contentDetails`)
* **Content Owner Details** (`contentOwnerDetails`)
* **ID** (`id`)
* **Localizations** (`localizations`)
* **Snippet** (`snippet`)
* **Statistics** (`statistics`)
* **Status** (`status`)
* **Topic Details** (`topicDetails`)

| Playlist ID | `playlistId` | string |  | ✓ |  |  |
| Fields | `part` | multiOptions |  | ✓ | The fields parameter specifies a comma-separated list of one or more playlist resource properties that the API response will include |  |

**Fields options:**

* ***** (`*`)
* **Content Details** (`contentDetails`)
* **ID** (`id`)
* **Localizations** (`localizations`)
* **Player** (`player`)
* **Snippet** (`snippet`)
* **Status** (`status`)

| Options | `options` | collection | {} | ✗ | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |
| On Behalf Of Content Owner Channel | `onBehalfOfContentOwnerChannel` | string |  | The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added |

</details>

| Playlist Item ID | `playlistItemId` | string |  | ✓ |  |  |
| Fields | `part` | multiOptions |  | ✓ | The fields parameter specifies a comma-separated list of one or more playlistItem resource properties that the API response will include |  |

**Fields options:**

* ***** (`*`)
* **Content Details** (`contentDetails`)
* **ID** (`id`)
* **Snippet** (`snippet`)
* **Status** (`status`)

| Options | `options` | collection | {} | ✗ | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |

</details>

| Video ID | `videoId` | string |  | ✓ |  |  |
| Fields | `part` | multiOptions |  | ✓ | The fields parameter specifies a comma-separated list of one or more video resource properties that the API response will include |  |

**Fields options:**

* ***** (`*`)
* **Content Details** (`contentDetails`)
* **ID** (`id`)
* **Live Streaming Details** (`liveStreamingDetails`)
* **Localizations** (`localizations`)
* **Player** (`player`)
* **Recording Details** (`recordingDetails`)
* **Snippet** (`snippet`)
* **Statistics** (`statistics`)
* **Status** (`status`)
* **Topic Details** (`topicDetails`)

| Options | `options` | collection | {} | ✗ | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Fields | `part` | multiOptions |  | ✓ | The fields parameter specifies a comma-separated list of one or more channel resource properties that the API response will include |  |

**Fields options:**

* ***** (`*`)
* **Branding Settings** (`brandingSettings`)
* **Content Details** (`contentDetails`)
* **Content Owner Details** (`contentOwnerDetails`)
* **ID** (`id`)
* **Localizations** (`localizations`)
* **Snippet** (`snippet`)
* **Statistics** (`statistics`)
* **Status** (`status`)
* **Topic Details** (`topicDetails`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 25 | ✗ | Max number of results to return | min:1, max:50 |
| Filters | `filters` | collection | {} | ✗ | The categoryId parameter specifies a YouTube guide category, thereby requesting YouTube channels associated with that category | e.g. Add option |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Category ID | `categoryId` | string |  | The categoryId parameter specifies a YouTube guide category, thereby requesting YouTube channels associated with that category |
| For Username | `forUsername` | string |  | The forUsername parameter specifies a YouTube username, thereby requesting the channel associated with that username |
| ID | `id` | string |  | The ID parameter specifies a comma-separated list of the YouTube channel ID(s) for the resource(s) that are being retrieved. In a channel resource, the ID property specifies the channel's YouTube channel ID. |
| Managed By Me | `managedByMe` | boolean | False | Whether to instruct the API to only return channels managed by the content owner that the onBehalfOfContentOwner parameter specifies |

</details>

| Options | `options` | collection | {} | ✗ | The hl parameter instructs the API to retrieve localized resource metadata for a specific application language that the YouTube website supports. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Language Code | `h1` | options |  | The hl parameter instructs the API to retrieve localized resource metadata for a specific application language that the YouTube website supports. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |

</details>

| Fields | `part` | multiOptions |  | ✓ | The fields parameter specifies a comma-separated list of one or more playlist resource properties that the API response will include |  |

**Fields options:**

* ***** (`*`)
* **Content Details** (`contentDetails`)
* **ID** (`id`)
* **Localizations** (`localizations`)
* **Player** (`player`)
* **Snippet** (`snippet`)
* **Status** (`status`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 25 | ✗ | Max number of results to return | min:1, max:50 |
| Filters | `filters` | collection | {} | ✗ | This value indicates that the API should only return the specified channel's playlists | e.g. Add option |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Channel ID | `channelId` | string |  | This value indicates that the API should only return the specified channel's playlists |
| ID | `id` | string |  | The ID parameter specifies a comma-separated list of the YouTube playlist ID(s) for the resource(s) that are being retrieved. In a playlist resource, the ID property specifies the playlist's YouTube playlist ID. |

</details>

| Options | `options` | collection | {} | ✗ | The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| On Behalf Of Content Owner Channel | `onBehalfOfContentOwnerChannel` | string |  | The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |

</details>

| Playlist Name or ID | `playlistId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Fields | `part` | multiOptions |  | ✓ | The fields parameter specifies a comma-separated list of one or more playlistItem resource properties that the API response will include |  |

**Fields options:**

* ***** (`*`)
* **Content Details** (`contentDetails`)
* **ID** (`id`)
* **Snippet** (`snippet`)
* **Status** (`status`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 25 | ✗ | Max number of results to return | min:1, max:50 |
| Options | `options` | collection | {} | ✗ | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 25 | ✗ | Max number of results to return | min:1, max:50 |
| Filters | `filters` | collection | {} | ✗ | The channelId parameter indicates that the API response should only contain resources created by the channel | e.g. Add option |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Channel ID | `channelId` | string |  | The channelId parameter indicates that the API response should only contain resources created by the channel |
| For Developer | `forDeveloper` | boolean | False | Whether to restrict the search to only retrieve videos uploaded via the developer's application or website |
| Published After | `publishedAfter` | dateTime |  | The publishedAfter parameter indicates that the API response should only contain resources created at or after the specified time |
| Published Before | `publishedBefore` | dateTime |  | The publishedBefore parameter indicates that the API response should only contain resources created before or at the specified time |
| Query | `q` | string |  | The q parameter specifies the query term to search for |
| Region Code | `regionCode` | options |  | The regionCode parameter instructs the API to select a video chart available in the specified region. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Related To Video ID | `relatedToVideoId` | string |  | The relatedToVideoId parameter retrieves a list of videos that are related to the video that the parameter value identifies |
| Video Category ID | `videoCategoryId` | string |  | The videoCategoryId parameter identifies the video category for which the chart should be retrieved |
| Video Syndicated | `videoSyndicated` | boolean | False | Whether to restrict a search to only videos that can be played outside youtube.com |
| Video Type | `videoType` | options |  | The videoType parameter lets you restrict a search to a particular type of videos |

</details>

| Options | `options` | collection | {} | ✗ | YouTube will filter some content from search results and, at the least, will filter content that is restricted in your locale | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Order | `order` | options | relevance |  |
| Safe Search | `safeSearch` | options |  | YouTube will filter some content from search results and, at the least, will filter content that is restricted in your locale |

</details>

| Region Code | `regionCode` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 25 | ✗ | Max number of results to return | min:1, max:50 |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel ID | `channelId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Encapsulates information about the branding of the channel | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Branding Settings | `brandingSettingsUi` | fixedCollection | {} | Encapsulates information about the branding of the channel |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  |  |

</details>

| Playlist ID | `playlistId` | string |  | ✓ | The playlist's title |  |
| Title | `title` | string |  | ✓ | The playlist's title |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The language of the text in the playlist resource's title and description properties. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Default Language Name or ID | `defaultLanguage` | options |  | The language of the text in the playlist resource's title and description properties. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | The playlist's description |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |
| Privacy Status | `privacyStatus` | options |  | The playlist's privacy status |
| Tags | `tags` | string |  | Keyword tags associated with the playlist. Mulplie can be defined separated by comma. |

</details>

| Video ID | `videoId` | string |  | ✓ |  |  |
| Title | `title` | string |  | ✓ |  |  |
| Region Code | `regionCode` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Category Name or ID | `categoryId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The language of the text in the playlist resource's title and description properties. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Default Language Name or ID | `defaultLanguage` | options |  | The language of the text in the playlist resource's title and description properties. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | The playlist's description |
| Embeddable | `embeddable` | boolean | False | Whether the video can be embedded on another website |
| License | `license` | options |  | The video's license |
| Notify Subscribers | `notifySubscribers` | boolean | False | Whether YouTube should send a notification about the new video to users who subscribe to the video's channel |
| Privacy Status | `privacyStatus` | options |  | The playlist's privacy status |
| Public Stats Viewable | `publicStatsViewable` | boolean | True | Whether the extended video statistics on the video's watch page are publicly viewable |
| Publish At | `publishAt` | dateTime |  | If you set a value for this property, you must also set the status.privacyStatus property to private |
| Recording Date | `recordingDate` | dateTime |  | The date and time when the video was recorded |
| Self Declared Made For Kids | `selfDeclaredMadeForKids` | boolean | False | Whether the video is designated as child-directed, and it contains the current "made for kids" status of the video |
| Tags | `tags` | string |  | Keyword tags associated with the playlist. Mulplie can be defined separated by comma. |

</details>


### Upload Banner parameters (`uploadBanner`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Channel ID | `channelId` | string |  | ✓ | ID of the channel |  |
| Input Binary Field | `binaryProperty` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | The playlist's title |  |
| Options | `options` | collection | {} | ✗ | The playlist's description | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | The playlist's description |
| Privacy Status | `privacyStatus` | options |  | The playlist's privacy status |
| Tags | `tags` | string |  | Keyword tags associated with the playlist. Mulplie can be defined separated by comma. |
| Default Language Name or ID | `defaultLanguage` | options |  | The language of the text in the playlist resource's title and description properties. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| On Behalf Of Content Owner Channel | `onBehalfOfContentOwnerChannel` | string |  | The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Playlist ID | `playlistId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |

</details>

| Playlist Item ID | `playlistItemId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |

</details>

| Video ID | `videoId` | string |  | ✓ | ID of the video |  |
| Options | `options` | collection | {} | ✗ | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Playlist Name or ID | `playlistId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Video ID | `videoId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | The time, measured in seconds from the start of the video, when the video should stop playing | e.g. Add option | min:0, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| End At | `endAt` | dateTime |  | The time, measured in seconds from the start of the video, when the video should stop playing |
| Note | `note` | string |  | A user-generated note for this item. The property value has a maximum length of 280 characters. |
| On Behalf Of Content Owner | `onBehalfOfContentOwner` | string |  | The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value |
| Position | `position` | number |  | The order in which the item appears in the playlist. The value uses a zero-based index, so the first item has a position of 0, the second item has a position of 1, and so forth. |
| Start At | `startAt` | dateTime |  | The time, measured in seconds from the start of the video, when the video should start playing |

</details>


### Rate parameters (`rate`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Video ID | `videoId` | string |  | ✓ |  |  |
| Rating | `rating` | options |  | ✗ | Records that the authenticated user disliked the video |  |

**Rating options:**

* **Dislike** (`dislike`) - Records that the authenticated user disliked the video
* **Like** (`like`) - Records that the authenticated user liked the video
* **None** (`none`) - Removes any rating that the authenticated user had previously set for the video


### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ |  |  |
| Region Code | `regionCode` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Category Name or ID | `categoryId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Input Binary Field | `binaryProperty` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |
| Options | `options` | collection | {} | ✗ | The language of the text in the playlist resource's title and description properties. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Default Language Name or ID | `defaultLanguage` | options |  | The language of the text in the playlist resource's title and description properties. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | The playlist's description |
| Embeddable | `embeddable` | boolean | False | Whether the video can be embedded on another website |
| License | `license` | options |  | The video's license |
| Notify Subscribers | `notifySubscribers` | boolean | False | Whether YouTube should send a notification about the new video to users who subscribe to the video's channel |
| Privacy Status | `privacyStatus` | options |  | The playlist's privacy status |
| Public Stats Viewable | `publicStatsViewable` | boolean | True | Whether the extended video statistics on the video's watch page are publicly viewable |
| Publish At | `publishAt` | dateTime |  | If you set a value for this property, you must also set the status.privacyStatus property to private |
| Recording Date | `recordingDate` | dateTime |  | The date and time when the video was recorded |
| Self Declared Made For Kids | `selfDeclaredMadeForKids` | boolean | False | Whether the video is designated as child-directed, and it contains the current "made for kids" status of the video |
| Tags | `tags` | string |  | Keyword tags associated with the playlist. Mulplie can be defined separated by comma. |

</details>


---

## Load Options Methods

- `getLanguages`
- `for`
- `name`
- `value`

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: YouTube

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "playlistItem",
  "operation": "getAll",
  "playlistId": "PLXXXXFAKEPLAYLISTID01",
  "limit": 3,
  "options": {}
}
```

**Credentials:**
- youTubeOAuth2Api: `YouTube OAuth2 creds`

### Example 2: YouTube1

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "playlistItem",
  "operation": "get",
  "playlistItemId": "fakePlaylistItemId1",
  "options": {}
}
```

**Credentials:**
- youTubeOAuth2Api: `YouTube OAuth2 creds`

### Example 3: YouTube2

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "playlistItem",
  "playlistId": "PLXXXXFAKEPLAYLISTID01",
  "videoId": "FAKEVIDID1",
  "options": {}
}
```

**Credentials:**
- youTubeOAuth2Api: `YouTube OAuth2 creds`

### Example 4: YouTube3

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "resource": "playlistItem",
  "operation": "delete",
  "playlistItemId": "UExWUDRtV2RxbGFhNWlwZEJRWXZVaFgyNk9RTENJRlV2cS41NkI0NEY2RDEwNTU3Q0M2",
  "options": {}
}
```

**Credentials:**
- youTubeOAuth2Api: `YouTube OAuth2 creds`

### Example 5: YouTube

**From workflow:** Unnamed workflow

**Parameters:**
```json
{
  "filters": {},
  "options": {}
}
```

**Credentials:**
- youTubeOAuth2Api: `YouTube OAuth2 creds`


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
* Categories: Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: youTube
displayName: YouTube
description: Consume YouTube API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: youTubeOAuth2Api
  required: true
operations:
- id: get
  name: Get
  description: Retrieve a channel
  params:
  - id: channelId
    name: Channel ID
    type: string
    default: ''
    required: true
    description: ID of the channel
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - uploadBanner
          resource:
          - channel
    typeInfo: &id010
      type: string
      displayName: Channel ID
      name: channelId
  - id: part
    name: Fields
    type: multiOptions
    default: ''
    required: true
    description: The fields parameter specifies a comma-separated list of one or more
      channel resource properties that the API response will include
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - video
    typeInfo: &id002
      type: multiOptions
      displayName: Fields
      name: part
      possibleValues:
      - value: '*'
        name: '*'
        description: ''
      - value: contentDetails
        name: Content Details
        description: ''
      - value: id
        name: ID
        description: ''
      - value: liveStreamingDetails
        name: Live Streaming Details
        description: ''
      - value: localizations
        name: Localizations
        description: ''
      - value: player
        name: Player
        description: ''
      - value: recordingDetails
        name: Recording Details
        description: ''
      - value: snippet
        name: Snippet
        description: ''
      - value: statistics
        name: Statistics
        description: ''
      - value: status
        name: Status
        description: ''
      - value: topicDetails
        name: Topic Details
        description: ''
  - id: playlistId
    name: Playlist ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - playlistItem
    typeInfo: &id008
      type: options
      displayName: Playlist Name or ID
      name: playlistId
      typeOptions:
        loadOptionsMethod: getPlaylists
      possibleValues: []
  - id: part
    name: Fields
    type: multiOptions
    default: ''
    required: true
    description: The fields parameter specifies a comma-separated list of one or more
      playlist resource properties that the API response will include
    validation: *id001
    typeInfo: *id002
  - id: playlistItemId
    name: Playlist Item ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id017
      required: true
      displayOptions:
        show:
          operation:
          - delete
          resource:
          - playlistItem
    typeInfo: &id018
      type: string
      displayName: Playlist Item ID
      name: playlistItemId
  - id: part
    name: Fields
    type: multiOptions
    default: ''
    required: true
    description: The fields parameter specifies a comma-separated list of one or more
      playlistItem resource properties that the API response will include
    validation: *id001
    typeInfo: *id002
  - id: videoId
    name: Video ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - video
    typeInfo: &id012
      type: string
      displayName: Video ID
      name: videoId
  - id: part
    name: Fields
    type: multiOptions
    default: ''
    required: true
    description: The fields parameter specifies a comma-separated list of one or more
      video resource properties that the API response will include
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Retrieve many channels
  params:
  - id: part
    name: Fields
    type: multiOptions
    default: ''
    required: true
    description: The fields parameter specifies a comma-separated list of one or more
      channel resource properties that the API response will include
    validation: *id001
    typeInfo: *id002
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
          - videoCategory
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 25
    required: false
    description: Max number of results to return
    validation: &id005
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - videoCategory
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 50
  - id: part
    name: Fields
    type: multiOptions
    default: ''
    required: true
    description: The fields parameter specifies a comma-separated list of one or more
      playlist resource properties that the API response will include
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
    default: 25
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: playlistId
    name: Playlist Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: part
    name: Fields
    type: multiOptions
    default: ''
    required: true
    description: The fields parameter specifies a comma-separated list of one or more
      playlistItem resource properties that the API response will include
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
    default: 25
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
    default: 25
    required: false
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
  - id: regionCode
    name: Region Code
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id015
      required: true
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - videoCategory
    typeInfo: &id016
      type: options
      displayName: Region Code
      name: regionCode
      typeOptions:
        loadOptionsMethod: getCountriesCodes
      possibleValues: []
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
- id: update
  name: Update
  description: Update a channel
  params:
  - id: channelId
    name: Channel ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: playlistId
    name: Playlist ID
    type: string
    default: ''
    required: true
    description: The playlist's title
    validation: *id007
    typeInfo: *id008
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The playlist's title
    validation: &id013
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - video
    typeInfo: &id014
      type: string
      displayName: Title
      name: title
  - id: videoId
    name: Video ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: ''
    validation: *id013
    typeInfo: *id014
  - id: regionCode
    name: Region Code
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id015
    typeInfo: *id016
  - id: categoryId
    name: Category Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id019
      displayOptions:
        show:
          operation:
          - update
          resource:
          - video
    typeInfo: &id020
      type: options
      displayName: Category Name or ID
      name: categoryId
      typeOptions:
        loadOptionsMethod: getVideoCategories
      possibleValues: []
- id: uploadBanner
  name: Upload Banner
  description: Upload a channel banner
  params:
  - id: channelId
    name: Channel ID
    type: string
    default: ''
    required: true
    description: ID of the channel
    validation: *id009
    typeInfo: *id010
  - id: binaryProperty
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be uploaded
    validation: &id021
      required: true
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - video
    typeInfo: &id022
      type: string
      displayName: Input Binary Field
      name: binaryProperty
- id: create
  name: Create
  description: Create a playlist
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The playlist's title
    validation: *id013
    typeInfo: *id014
- id: delete
  name: Delete
  description: Delete a playlist
  params:
  - id: playlistId
    name: Playlist ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: playlistItemId
    name: Playlist Item ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: videoId
    name: Video ID
    type: string
    default: ''
    required: true
    description: ID of the video
    validation: *id011
    typeInfo: *id012
- id: add
  name: Add
  description: Add an item to a playlist
  params:
  - id: playlistId
    name: Playlist Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id007
    typeInfo: *id008
  - id: videoId
    name: Video ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
- id: rate
  name: Rate
  description: Rate a video
  params:
  - id: videoId
    name: Video ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: rating
    name: Rating
    type: options
    default: ''
    required: false
    description: Records that the authenticated user disliked the video
    validation:
      displayOptions:
        show:
          operation:
          - rate
          resource:
          - video
    typeInfo:
      type: options
      displayName: Rating
      name: rating
      possibleValues:
      - value: dislike
        name: Dislike
        description: Records that the authenticated user disliked the video
      - value: like
        name: Like
        description: Records that the authenticated user liked the video
      - value: none
        name: None
        description: Removes any rating that the authenticated user had previously
          set for the video
- id: upload
  name: Upload
  description: Upload a video
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: ''
    validation: *id013
    typeInfo: *id014
  - id: regionCode
    name: Region Code
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id015
    typeInfo: *id016
  - id: categoryId
    name: Category Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id019
    typeInfo: *id020
  - id: binaryProperty
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be uploaded
    validation: *id021
    typeInfo: *id022
examples:
- name: YouTube
  parameters:
    resource: playlistItem
    operation: getAll
    playlistId: PLXXXXFAKEPLAYLISTID01
    limit: 3
    options: {}
  workflow: Unnamed workflow
- name: YouTube1
  parameters:
    resource: playlistItem
    operation: get
    playlistItemId: fakePlaylistItemId1
    options: {}
  workflow: Unnamed workflow
- name: YouTube2
  parameters:
    resource: playlistItem
    playlistId: PLXXXXFAKEPLAYLISTID01
    videoId: FAKEVIDID1
    options: {}
  workflow: Unnamed workflow
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: filters
    text: Add option
  - field: options
    text: Add option
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: filters
    text: Add option
  - field: options
    text: Add option
  - field: updateFields
    text: Add Field
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: filters
    text: Add option
  - field: options
    text: Add option
  - field: updateFields
    text: Add option
  hints:
  - field: binaryProperty
    text: The name of the input binary field containing the file to be uploaded
  - field: binaryProperty
    text: The name of the input binary field containing the file to be uploaded
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
  "$id": "https://n8n.io/schemas/nodes/youTube.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "YouTube Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "get",
        "getAll",
        "update",
        "uploadBanner",
        "create",
        "delete",
        "add",
        "rate",
        "upload"
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
            "channel",
            "playlist",
            "playlistItem",
            "video",
            "videoCategory"
          ],
          "default": "channel"
        },
        "operation": {
          "description": "Retrieve many video categories",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "getAll"
        },
        "part": {
          "description": "The fields parameter specifies a comma-separated list of one or more video resource properties that the API response will include",
          "type": "string"
        },
        "returnAll": {
          "description": "Whether to return all results or only up to a given limit",
          "type": "boolean",
          "default": false
        },
        "limit": {
          "description": "Max number of results to return",
          "type": "number",
          "default": 25
        },
        "filters": {
          "description": "The channelId parameter indicates that the API response should only contain resources created by the channel",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "options": {
          "description": "YouTube will filter some content from search results and, at the least, will filter content that is restricted in your locale",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "channelId": {
          "description": "ID of the channel",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "The language of the text in the playlist resource's title and description properties. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "binaryProperty": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "title": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "playlistId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "videoId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "playlistItemId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "regionCode": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "categoryId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "rating": {
          "description": "Records that the authenticated user disliked the video",
          "type": "string",
          "enum": [
            "dislike",
            "like",
            "none"
          ],
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
      "name": "youTubeOAuth2Api",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "YouTube",
      "value": {
        "resource": "playlistItem",
        "operation": "getAll",
        "playlistId": "PLXXXXFAKEPLAYLISTID01",
        "limit": 3,
        "options": {}
      }
    },
    {
      "description": "YouTube1",
      "value": {
        "resource": "playlistItem",
        "operation": "get",
        "playlistItemId": "fakePlaylistItemId1",
        "options": {}
      }
    },
    {
      "description": "YouTube2",
      "value": {
        "resource": "playlistItem",
        "playlistId": "PLXXXXFAKEPLAYLISTID01",
        "videoId": "FAKEVIDID1",
        "options": {}
      }
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
