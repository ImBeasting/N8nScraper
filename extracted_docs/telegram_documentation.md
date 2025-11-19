---
title: "Node: Telegram"
slug: "node-telegram"
version: "['1', '1.1', '1.2']"
updated: "2025-11-13"
summary: "Sends data to Telegram"
node_type: "regular"
group: "['output']"
---

# Node: Telegram

**Purpose.** Sends data to Telegram
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `bot`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **telegramApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `telegramApi` | ✓ | - |

---

## Operations

### // 				'Bot Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Info | `info` | Get information about the bot associated with the access token. |

### // Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Info | `info` | Get information about the bot associated with the access token. |

### Chat Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get up to date information about a chat |
| Get Administrators | `administrators` | Get the Administrators of a chat |
| Get Member | `member` | Get the member of a chat |
| Leave | `leave` | Leave a group, supergroup or channel |
| Set Description | `setDescription` | Set the description of a chat |
| Set Title | `setTitle` | Set the title of a chat |

### Callback Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Answer Query | `answerQuery` | Send answer to callback query sent from inline keyboard |
| Answer Inline Query | `answerInlineQuery` | Send answer to callback query sent from inline bot |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a file |

### Message Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete Chat Message | `deleteMessage` | Delete a chat message |
| Edit Message Text | `editMessageText` | Edit a text message |
| Pin Chat Message | `pinChatMessage` | Pin a chat message |
| Send Animation | `sendAnimation` | Send an animated file |
| Send Audio | `sendAudio` | Send a audio file |
| Send Chat Action | `sendChatAction` | Send a chat action |
| Send Document | `sendDocument` | Send a document |
| Send Location | `sendLocation` | Send a location |
| Send Media Group | `sendMediaGroup` | Send group of photos or videos to album |
| Send Message | `sendMessage` | Send a text message |
| Send and Wait for Response | `` | Send a message and wait for response |
| Send Photo | `sendPhoto` | Send a photo |
| Send Sticker | `sendSticker` | Send a sticker |
| Send Video | `sendVideo` | Send a video |
| Unpin Chat Message | `unpinChatMessage` | Unpin a chat message |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | message | ✗ | Resource to operate on |  |

**Resource options:**

* **Bot** (`bot`)
* **Chat** (`chat`)
* **Callback** (`callback`)
* **File** (`file`)
* **Message** (`message`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | info | ✗ | Get information about the bot associated with the access token. |  |

**Operation options:**

* **Info** (`info`) - Get information about the bot associated with the access token.

---

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| File ID | `fileId` | string |  | ✓ | The ID of the file |  |
| Download | `download` | boolean | True | ✗ | Whether to download the file |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The MIME type of the file. If not specified, the MIME type will be determined by the file extension. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| MIME Type | `mimeType` | string |  | The MIME type of the file. If not specified, the MIME type will be determined by the file extension. |

</details>


### Get Administrators parameters (`administrators`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |

### Get Member parameters (`member`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| User ID | `userId` | string |  | ✓ | Unique identifier of the target user |  |

### Leave parameters (`leave`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |

### Set Description parameters (`setDescription`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Description | `description` | string |  | ✓ | New chat description, 0-255 characters |  |

### Set Title parameters (`setTitle`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Title | `title` | string |  | ✓ | New chat title, 1-255 characters |  |

### Answer Query parameters (`answerQuery`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Query ID | `queryId` | string |  | ✓ | Unique identifier for the query to be answered |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The maximum amount of time in seconds that the result of the callback query may be cached client-side | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Cache Time | `cache_time` | number | 0 | The maximum amount of time in seconds that the result of the callback query may be cached client-side |
| Show Alert | `show_alert` | boolean | False | Whether an alert will be shown by the client instead of a notification at the top of the chat screen |
| Text | `text` | string |  | Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters. |
| URL | `url` | string |  | URL that will be opened by the user's client |

</details>


### Answer Inline Query parameters (`answerInlineQuery`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Query ID | `queryId` | string |  | ✓ | Unique identifier for the answered query |  |
| Results | `results` | string |  | ✓ | A JSON-serialized array of results for the inline query |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The maximum amount of time in seconds that the result of the callback query may be cached client-side | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Cache Time | `cache_time` | number | 0 | The maximum amount of time in seconds that the result of the callback query may be cached client-side |
| Show Alert | `show_alert` | boolean | False | Whether an alert will be shown by the client instead of a notification at the top of the chat screen |
| Text | `text` | string |  | Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters. |
| URL | `url` | string |  | URL that will be opened by the user's client |

</details>


### Delete Chat Message parameters (`deleteMessage`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Message ID | `messageId` | string |  | ✓ | Unique identifier of the message to delete |  |

### Edit Message Text parameters (`editMessageText`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Message Type | `messageType` | options | message | ✗ | The type of the message to edit |  |

**Message Type options:**

* **Inline Message** (`inlineMessage`)
* **Message** (`message`)

| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Message ID | `messageId` | string |  | ✓ | Unique identifier of the message to edit |  |
| Inline Message ID | `inlineMessageId` | string |  | ✓ | Unique identifier of the inline message to edit |  |
| Reply Markup | `replyMarkup` | options | none | ✗ | Additional interface options |  |

**Reply Markup options:**

* **None** (`none`)
* **Inline Keyboard** (`inlineKeyboard`)

| Text | `text` | string |  | ✓ | Text of the message to be sent |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the phrase “This message was sent automatically with n8n” to the end of the message | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Caption | `caption` | string |  | Caption text to set, 0-1024 characters |
| Disable Notification | `disable_notification` | boolean | False | Whether to send the message silently. Users will receive a notification with no sound. |
| Disable WebPage Preview | `disable_web_page_preview` | boolean | False | Whether to disable link previews for links in this message |
| Duration | `duration` | number | 0 | Duration of clip in seconds |
| File Name | `fileName` | string |  |  |
| Height | `height` | number | 0 | Height of the video |
| Parse Mode | `parse_mode` | options | HTML | How to parse the text |
| Performer | `performer` | string |  | Name of the performer |
| Reply To Message ID | `reply_to_message_id` | number | 0 | If the message is a reply, ID of the original message |
| Message Thread ID | `message_thread_id` | number | 0 | The unique identifier of the forum topic |
| Title | `title` | string |  | Title of the track |
| Thumbnail | `thumb` | string |  | Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. |
| Width | `width` | number | 0 | Width of the video |

</details>


### Pin Chat Message parameters (`pinChatMessage`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Message ID | `messageId` | string |  | ✓ | Unique identifier of the message to pin or unpin |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to send a notification to all chat members about the new pinned message | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Disable Notification | `disable_notification` | boolean | False | Whether to send a notification to all chat members about the new pinned message |

</details>


### Send Animation parameters (`sendAnimation`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | Name of the binary property that contains the data to upload | e.g. The name of the input binary field containing the file to be written |  |
| Animation | `file` | string |  | ✗ | Animation to send. Pass a file_id to send an animation that exists on the Telegram servers (recommended), an HTTP URL for Telegram to get an animation from the Internet. |  |
| Reply Markup | `replyMarkup` | options | none | ✗ | Additional interface options |  |

**Reply Markup options:**

* **Force Reply** (`forceReply`)
* **Inline Keyboard** (`inlineKeyboard`)
* **None** (`none`)
* **Reply Keyboard** (`replyKeyboard`)
* **Reply Keyboard Remove** (`replyKeyboardRemove`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the phrase “This message was sent automatically with n8n” to the end of the message | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Caption | `caption` | string |  | Caption text to set, 0-1024 characters |
| Disable Notification | `disable_notification` | boolean | False | Whether to send the message silently. Users will receive a notification with no sound. |
| Disable WebPage Preview | `disable_web_page_preview` | boolean | False | Whether to disable link previews for links in this message |
| Duration | `duration` | number | 0 | Duration of clip in seconds |
| File Name | `fileName` | string |  |  |
| Height | `height` | number | 0 | Height of the video |
| Parse Mode | `parse_mode` | options | HTML | How to parse the text |
| Performer | `performer` | string |  | Name of the performer |
| Reply To Message ID | `reply_to_message_id` | number | 0 | If the message is a reply, ID of the original message |
| Message Thread ID | `message_thread_id` | number | 0 | The unique identifier of the forum topic |
| Title | `title` | string |  | Title of the track |
| Thumbnail | `thumb` | string |  | Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. |
| Width | `width` | number | 0 | Width of the video |

</details>


### Send Audio parameters (`sendAudio`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | Name of the binary property that contains the data to upload | e.g. The name of the input binary field containing the file to be written |  |
| Audio | `file` | string |  | ✗ | Audio file to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), an HTTP URL for Telegram to get a file from the Internet. |  |
| Reply Markup | `replyMarkup` | options | none | ✗ | Additional interface options |  |

**Reply Markup options:**

* **Force Reply** (`forceReply`)
* **Inline Keyboard** (`inlineKeyboard`)
* **None** (`none`)
* **Reply Keyboard** (`replyKeyboard`)
* **Reply Keyboard Remove** (`replyKeyboardRemove`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the phrase “This message was sent automatically with n8n” to the end of the message | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Caption | `caption` | string |  | Caption text to set, 0-1024 characters |
| Disable Notification | `disable_notification` | boolean | False | Whether to send the message silently. Users will receive a notification with no sound. |
| Disable WebPage Preview | `disable_web_page_preview` | boolean | False | Whether to disable link previews for links in this message |
| Duration | `duration` | number | 0 | Duration of clip in seconds |
| File Name | `fileName` | string |  |  |
| Height | `height` | number | 0 | Height of the video |
| Parse Mode | `parse_mode` | options | HTML | How to parse the text |
| Performer | `performer` | string |  | Name of the performer |
| Reply To Message ID | `reply_to_message_id` | number | 0 | If the message is a reply, ID of the original message |
| Message Thread ID | `message_thread_id` | number | 0 | The unique identifier of the forum topic |
| Title | `title` | string |  | Title of the track |
| Thumbnail | `thumb` | string |  | Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. |
| Width | `width` | number | 0 | Width of the video |

</details>


### Send Chat Action parameters (`sendChatAction`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Action | `action` | options | typing | ✗ | Type of action to broadcast. Choose one, depending on what the user is about to receive. The status is set for 5 seconds or less (when a message arrives from your bot). |  |

**Action options:**

* **Find Location** (`find_location`) - Find location
* **Record Audio** (`record_audio`) - Record audio
* **Record Video** (`record_video`) - Record video
* **Record Video Note** (`record_video_note`) - Record video note
* **Typing** (`typing`) - Typing a message
* **Upload Audio** (`upload_audio`) - Upload audio
* **Upload Document** (`upload_document`) - Upload document
* **Upload Photo** (`upload_photo`) - Upload photo
* **Upload Video** (`upload_video`) - Upload video
* **Upload Video Note** (`upload_video_note`) - Upload video note


### Send Document parameters (`sendDocument`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | Name of the binary property that contains the data to upload | e.g. The name of the input binary field containing the file to be written |  |
| Document | `file` | string |  | ✗ | Document to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), an HTTP URL for Telegram to get a file from the Internet. |  |
| Reply Markup | `replyMarkup` | options | none | ✗ | Additional interface options |  |

**Reply Markup options:**

* **Force Reply** (`forceReply`)
* **Inline Keyboard** (`inlineKeyboard`)
* **None** (`none`)
* **Reply Keyboard** (`replyKeyboard`)
* **Reply Keyboard Remove** (`replyKeyboardRemove`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the phrase “This message was sent automatically with n8n” to the end of the message | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Caption | `caption` | string |  | Caption text to set, 0-1024 characters |
| Disable Notification | `disable_notification` | boolean | False | Whether to send the message silently. Users will receive a notification with no sound. |
| Disable WebPage Preview | `disable_web_page_preview` | boolean | False | Whether to disable link previews for links in this message |
| Duration | `duration` | number | 0 | Duration of clip in seconds |
| File Name | `fileName` | string |  |  |
| Height | `height` | number | 0 | Height of the video |
| Parse Mode | `parse_mode` | options | HTML | How to parse the text |
| Performer | `performer` | string |  | Name of the performer |
| Reply To Message ID | `reply_to_message_id` | number | 0 | If the message is a reply, ID of the original message |
| Message Thread ID | `message_thread_id` | number | 0 | The unique identifier of the forum topic |
| Title | `title` | string |  | Title of the track |
| Thumbnail | `thumb` | string |  | Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. |
| Width | `width` | number | 0 | Width of the video |

</details>


### Send Location parameters (`sendLocation`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Latitude | `latitude` | number | 0 | ✗ | Location latitude | min:∞, max:90 |
| Longitude | `longitude` | number | 0 | ✗ | Location longitude | min:∞, max:180 |
| Reply Markup | `replyMarkup` | options | none | ✗ | Additional interface options |  |

**Reply Markup options:**

* **Force Reply** (`forceReply`)
* **Inline Keyboard** (`inlineKeyboard`)
* **None** (`none`)
* **Reply Keyboard** (`replyKeyboard`)
* **Reply Keyboard Remove** (`replyKeyboardRemove`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the phrase “This message was sent automatically with n8n” to the end of the message | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Caption | `caption` | string |  | Caption text to set, 0-1024 characters |
| Disable Notification | `disable_notification` | boolean | False | Whether to send the message silently. Users will receive a notification with no sound. |
| Disable WebPage Preview | `disable_web_page_preview` | boolean | False | Whether to disable link previews for links in this message |
| Duration | `duration` | number | 0 | Duration of clip in seconds |
| File Name | `fileName` | string |  |  |
| Height | `height` | number | 0 | Height of the video |
| Parse Mode | `parse_mode` | options | HTML | How to parse the text |
| Performer | `performer` | string |  | Name of the performer |
| Reply To Message ID | `reply_to_message_id` | number | 0 | If the message is a reply, ID of the original message |
| Message Thread ID | `message_thread_id` | number | 0 | The unique identifier of the forum topic |
| Title | `title` | string |  | Title of the track |
| Thumbnail | `thumb` | string |  | Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. |
| Width | `width` | number | 0 | Width of the video |

</details>


### Send Media Group parameters (`sendMediaGroup`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Media | `media` | fixedCollection | {} | ✗ | The media to add | e.g. Add Media |  |

<details>
<summary><strong>Media sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Media | `media` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the phrase “This message was sent automatically with n8n” to the end of the message | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Caption | `caption` | string |  | Caption text to set, 0-1024 characters |
| Disable Notification | `disable_notification` | boolean | False | Whether to send the message silently. Users will receive a notification with no sound. |
| Disable WebPage Preview | `disable_web_page_preview` | boolean | False | Whether to disable link previews for links in this message |
| Duration | `duration` | number | 0 | Duration of clip in seconds |
| File Name | `fileName` | string |  |  |
| Height | `height` | number | 0 | Height of the video |
| Parse Mode | `parse_mode` | options | HTML | How to parse the text |
| Performer | `performer` | string |  | Name of the performer |
| Reply To Message ID | `reply_to_message_id` | number | 0 | If the message is a reply, ID of the original message |
| Message Thread ID | `message_thread_id` | number | 0 | The unique identifier of the forum topic |
| Title | `title` | string |  | Title of the track |
| Thumbnail | `thumb` | string |  | Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. |
| Width | `width` | number | 0 | Width of the video |

</details>


### Send Message parameters (`sendMessage`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Text | `text` | string |  | ✓ | Text of the message to be sent |  |
| Reply Markup | `replyMarkup` | options | none | ✗ | Additional interface options |  |

**Reply Markup options:**

* **Force Reply** (`forceReply`)
* **Inline Keyboard** (`inlineKeyboard`)
* **None** (`none`)
* **Reply Keyboard** (`replyKeyboard`)
* **Reply Keyboard Remove** (`replyKeyboardRemove`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the phrase “This message was sent automatically with n8n” to the end of the message | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Caption | `caption` | string |  | Caption text to set, 0-1024 characters |
| Disable Notification | `disable_notification` | boolean | False | Whether to send the message silently. Users will receive a notification with no sound. |
| Disable WebPage Preview | `disable_web_page_preview` | boolean | False | Whether to disable link previews for links in this message |
| Duration | `duration` | number | 0 | Duration of clip in seconds |
| File Name | `fileName` | string |  |  |
| Height | `height` | number | 0 | Height of the video |
| Parse Mode | `parse_mode` | options | HTML | How to parse the text |
| Performer | `performer` | string |  | Name of the performer |
| Reply To Message ID | `reply_to_message_id` | number | 0 | If the message is a reply, ID of the original message |
| Message Thread ID | `message_thread_id` | number | 0 | The unique identifier of the forum topic |
| Title | `title` | string |  | Title of the track |
| Thumbnail | `thumb` | string |  | Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. |
| Width | `width` | number | 0 | Width of the video |

</details>


### Send and Wait for Response parameters (``)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | Name of the binary property that contains the data to upload | e.g. The name of the input binary field containing the file to be written |  |
| Reply Markup | `replyMarkup` | options | none | ✗ | Additional interface options |  |

**Reply Markup options:**

* **Force Reply** (`forceReply`)
* **Inline Keyboard** (`inlineKeyboard`)
* **None** (`none`)
* **Reply Keyboard** (`replyKeyboard`)
* **Reply Keyboard Remove** (`replyKeyboardRemove`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the phrase “This message was sent automatically with n8n” to the end of the message | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Caption | `caption` | string |  | Caption text to set, 0-1024 characters |
| Disable Notification | `disable_notification` | boolean | False | Whether to send the message silently. Users will receive a notification with no sound. |
| Disable WebPage Preview | `disable_web_page_preview` | boolean | False | Whether to disable link previews for links in this message |
| Duration | `duration` | number | 0 | Duration of clip in seconds |
| File Name | `fileName` | string |  |  |
| Height | `height` | number | 0 | Height of the video |
| Parse Mode | `parse_mode` | options | HTML | How to parse the text |
| Performer | `performer` | string |  | Name of the performer |
| Reply To Message ID | `reply_to_message_id` | number | 0 | If the message is a reply, ID of the original message |
| Message Thread ID | `message_thread_id` | number | 0 | The unique identifier of the forum topic |
| Title | `title` | string |  | Title of the track |
| Thumbnail | `thumb` | string |  | Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. |
| Width | `width` | number | 0 | Width of the video |

</details>


### Send Photo parameters (`sendPhoto`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | Name of the binary property that contains the data to upload | e.g. The name of the input binary field containing the file to be written |  |
| Photo | `file` | string |  | ✗ | Photo to send. Pass a file_id to send a photo that exists on the Telegram servers (recommended), an HTTP URL for Telegram to get a photo from the Internet. |  |
| Reply Markup | `replyMarkup` | options | none | ✗ | Additional interface options |  |

**Reply Markup options:**

* **Force Reply** (`forceReply`)
* **Inline Keyboard** (`inlineKeyboard`)
* **None** (`none`)
* **Reply Keyboard** (`replyKeyboard`)
* **Reply Keyboard Remove** (`replyKeyboardRemove`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the phrase “This message was sent automatically with n8n” to the end of the message | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Caption | `caption` | string |  | Caption text to set, 0-1024 characters |
| Disable Notification | `disable_notification` | boolean | False | Whether to send the message silently. Users will receive a notification with no sound. |
| Disable WebPage Preview | `disable_web_page_preview` | boolean | False | Whether to disable link previews for links in this message |
| Duration | `duration` | number | 0 | Duration of clip in seconds |
| File Name | `fileName` | string |  |  |
| Height | `height` | number | 0 | Height of the video |
| Parse Mode | `parse_mode` | options | HTML | How to parse the text |
| Performer | `performer` | string |  | Name of the performer |
| Reply To Message ID | `reply_to_message_id` | number | 0 | If the message is a reply, ID of the original message |
| Message Thread ID | `message_thread_id` | number | 0 | The unique identifier of the forum topic |
| Title | `title` | string |  | Title of the track |
| Thumbnail | `thumb` | string |  | Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. |
| Width | `width` | number | 0 | Width of the video |

</details>


### Send Sticker parameters (`sendSticker`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | Name of the binary property that contains the data to upload | e.g. The name of the input binary field containing the file to be written |  |
| Sticker | `file` | string |  | ✗ | Sticker to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), an HTTP URL for Telegram to get a .webp file from the Internet. |  |
| Reply Markup | `replyMarkup` | options | none | ✗ | Additional interface options |  |

**Reply Markup options:**

* **Force Reply** (`forceReply`)
* **Inline Keyboard** (`inlineKeyboard`)
* **None** (`none`)
* **Reply Keyboard** (`replyKeyboard`)
* **Reply Keyboard Remove** (`replyKeyboardRemove`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the phrase “This message was sent automatically with n8n” to the end of the message | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Caption | `caption` | string |  | Caption text to set, 0-1024 characters |
| Disable Notification | `disable_notification` | boolean | False | Whether to send the message silently. Users will receive a notification with no sound. |
| Disable WebPage Preview | `disable_web_page_preview` | boolean | False | Whether to disable link previews for links in this message |
| Duration | `duration` | number | 0 | Duration of clip in seconds |
| File Name | `fileName` | string |  |  |
| Height | `height` | number | 0 | Height of the video |
| Parse Mode | `parse_mode` | options | HTML | How to parse the text |
| Performer | `performer` | string |  | Name of the performer |
| Reply To Message ID | `reply_to_message_id` | number | 0 | If the message is a reply, ID of the original message |
| Message Thread ID | `message_thread_id` | number | 0 | The unique identifier of the forum topic |
| Title | `title` | string |  | Title of the track |
| Thumbnail | `thumb` | string |  | Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. |
| Width | `width` | number | 0 | Width of the video |

</details>


### Send Video parameters (`sendVideo`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Binary File | `binaryData` | boolean | False | ✓ | Whether the data to upload should be taken from binary field |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | Name of the binary property that contains the data to upload | e.g. The name of the input binary field containing the file to be written |  |
| Video | `file` | string |  | ✗ | Video file to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), an HTTP URL for Telegram to get a file from the Internet. |  |
| Reply Markup | `replyMarkup` | options | none | ✗ | Additional interface options |  |

**Reply Markup options:**

* **Force Reply** (`forceReply`)
* **Inline Keyboard** (`inlineKeyboard`)
* **None** (`none`)
* **Reply Keyboard** (`replyKeyboard`)
* **Reply Keyboard Remove** (`replyKeyboardRemove`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to include the phrase “This message was sent automatically with n8n” to the end of the message | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Caption | `caption` | string |  | Caption text to set, 0-1024 characters |
| Disable Notification | `disable_notification` | boolean | False | Whether to send the message silently. Users will receive a notification with no sound. |
| Disable WebPage Preview | `disable_web_page_preview` | boolean | False | Whether to disable link previews for links in this message |
| Duration | `duration` | number | 0 | Duration of clip in seconds |
| File Name | `fileName` | string |  |  |
| Height | `height` | number | 0 | Height of the video |
| Parse Mode | `parse_mode` | options | HTML | How to parse the text |
| Performer | `performer` | string |  | Name of the performer |
| Reply To Message ID | `reply_to_message_id` | number | 0 | If the message is a reply, ID of the original message |
| Message Thread ID | `message_thread_id` | number | 0 | The unique identifier of the forum topic |
| Title | `title` | string |  | Title of the track |
| Thumbnail | `thumb` | string |  | Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. |
| Width | `width` | number | 0 | Width of the video |

</details>


### Unpin Chat Message parameters (`unpinChatMessage`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Chat ID | `chatId` | string |  | ✓ | Unique identifier for the target chat or username, To find your chat ID ask @get_id_bot |  |
| Message ID | `messageId` | string |  | ✓ | Unique identifier of the message to pin or unpin |  |

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
* Categories: Communication, HITL
* Aliases: human, form, wait, hitl, approval

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: telegram
displayName: Telegram
description: Sends data to Telegram
version:
- '1'
- '1.1'
- '1.2'
nodeType: regular
group:
- output
credentials:
- name: telegramApi
  required: true
operations:
- id: info
  name: Info
  description: Get information about the bot associated with the access token.
- id: get
  name: Get
  description: Get up to date information about a chat
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: &id001
      required: true
    typeInfo: &id002
      type: string
      displayName: Chat ID
      name: chatId
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: true
    description: The ID of the file
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - file
    typeInfo:
      type: string
      displayName: File ID
      name: fileId
  - id: download
    name: Download
    type: boolean
    default: true
    required: false
    description: Whether to download the file
    validation:
      displayOptions:
        show:
          operation:
          - get
          resource:
          - file
    typeInfo:
      type: boolean
      displayName: Download
      name: download
- id: administrators
  name: Get Administrators
  description: Get the Administrators of a chat
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
- id: member
  name: Get Member
  description: Get the member of a chat
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the target user
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - member
          resource:
          - chat
    typeInfo:
      type: string
      displayName: User ID
      name: userId
- id: leave
  name: Leave
  description: Leave a group, supergroup or channel
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
- id: setDescription
  name: Set Description
  description: Set the description of a chat
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: description
    name: Description
    type: string
    default: ''
    required: true
    description: New chat description, 0-255 characters
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - setDescription
          resource:
          - chat
    typeInfo:
      type: string
      displayName: Description
      name: description
- id: setTitle
  name: Set Title
  description: Set the title of a chat
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: New chat title, 1-255 characters
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - setTitle
          resource:
          - chat
    typeInfo:
      type: string
      displayName: Title
      name: title
- id: answerQuery
  name: Answer Query
  description: Send answer to callback query sent from inline keyboard
  params:
  - id: queryId
    name: Query ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the query to be answered
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - answerInlineQuery
          resource:
          - callback
    typeInfo: &id004
      type: string
      displayName: Query ID
      name: queryId
- id: answerInlineQuery
  name: Answer Inline Query
  description: Send answer to callback query sent from inline bot
  params:
  - id: queryId
    name: Query ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the answered query
    validation: *id003
    typeInfo: *id004
  - id: results
    name: Results
    type: string
    default: ''
    required: true
    description: A JSON-serialized array of results for the inline query
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - answerInlineQuery
          resource:
          - callback
    typeInfo:
      type: string
      displayName: Results
      name: results
- id: deleteMessage
  name: Delete Chat Message
  description: Delete a chat message
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the message to delete
    validation: &id005
      required: true
      displayOptions:
        show:
          messageType:
          - message
          operation:
          - editMessageText
          resource:
          - message
    typeInfo: &id006
      type: string
      displayName: Message ID
      name: messageId
- id: editMessageText
  name: Edit Message Text
  description: Edit a text message
  params:
  - id: messageType
    name: Message Type
    type: options
    default: message
    required: false
    description: The type of the message to edit
    validation:
      displayOptions:
        show:
          operation:
          - editMessageText
          resource:
          - message
    typeInfo:
      type: options
      displayName: Message Type
      name: messageType
      possibleValues:
      - value: inlineMessage
        name: Inline Message
        description: ''
      - value: message
        name: Message
        description: ''
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the message to edit
    validation: *id005
    typeInfo: *id006
  - id: inlineMessageId
    name: Inline Message ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the inline message to edit
    validation:
      required: true
      displayOptions:
        show:
          messageType:
          - inlineMessage
          operation:
          - editMessageText
          resource:
          - message
    typeInfo:
      type: string
      displayName: Inline Message ID
      name: inlineMessageId
  - id: replyMarkup
    name: Reply Markup
    type: options
    default: none
    required: false
    description: Additional interface options
    validation: &id007
      displayOptions:
        show:
          operation:
          - sendAnimation
          - sendDocument
          - sendMessage
          - sendPhoto
          - sendSticker
          - sendVideo
          - sendAudio
          - sendLocation
          - ''
          resource:
          - message
    typeInfo: &id008
      type: options
      displayName: Reply Markup
      name: replyMarkup
      possibleValues:
      - value: forceReply
        name: Force Reply
        description: ''
      - value: inlineKeyboard
        name: Inline Keyboard
        description: ''
      - value: none
        name: None
        description: ''
      - value: replyKeyboard
        name: Reply Keyboard
        description: ''
      - value: replyKeyboardRemove
        name: Reply Keyboard Remove
        description: ''
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: Text of the message to be sent
    validation: &id015
      required: true
      displayOptions:
        show:
          operation:
          - editMessageText
          - sendMessage
          resource:
          - message
    typeInfo: &id016
      type: string
      displayName: Text
      name: text
- id: pinChatMessage
  name: Pin Chat Message
  description: Pin a chat message
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the message to pin or unpin
    validation: *id005
    typeInfo: *id006
- id: sendAnimation
  name: Send Animation
  description: Send an animated file
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - sendAnimation
          - sendAudio
          - sendDocument
          - sendPhoto
          - sendVideo
          - sendSticker
          - ''
          resource:
          - message
    typeInfo: &id010
      type: boolean
      displayName: Binary File
      name: binaryData
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: Name of the binary property that contains the data to upload
    hint: The name of the input binary field containing the file to be written
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - sendAnimation
          - sendAudio
          - sendDocument
          - sendPhoto
          - sendVideo
          - sendSticker
          - ''
          resource:
          - message
          binaryData:
          - true
    typeInfo: &id012
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
  - id: file
    name: Animation
    type: string
    default: ''
    required: false
    description: Animation to send. Pass a file_id to send an animation that exists
      on the Telegram servers (recommended), an HTTP URL for Telegram to get an animation
      from the Internet.
    validation: &id013
      displayOptions:
        show:
          operation:
          - sendVideo
          resource:
          - message
          binaryData:
          - false
    typeInfo: &id014
      type: string
      displayName: Video
      name: file
  - id: replyMarkup
    name: Reply Markup
    type: options
    default: none
    required: false
    description: Additional interface options
    validation: *id007
    typeInfo: *id008
- id: sendAudio
  name: Send Audio
  description: Send a audio file
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation: *id009
    typeInfo: *id010
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: Name of the binary property that contains the data to upload
    hint: The name of the input binary field containing the file to be written
    validation: *id011
    typeInfo: *id012
  - id: file
    name: Audio
    type: string
    default: ''
    required: false
    description: Audio file to send. Pass a file_id to send a file that exists on
      the Telegram servers (recommended), an HTTP URL for Telegram to get a file from
      the Internet.
    validation: *id013
    typeInfo: *id014
  - id: replyMarkup
    name: Reply Markup
    type: options
    default: none
    required: false
    description: Additional interface options
    validation: *id007
    typeInfo: *id008
- id: sendChatAction
  name: Send Chat Action
  description: Send a chat action
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: action
    name: Action
    type: options
    default: typing
    required: false
    description: Type of action to broadcast. Choose one, depending on what the user
      is about to receive. The status is set for 5 seconds or less (when a message
      arrives from your bot).
    validation:
      displayOptions:
        show:
          operation:
          - sendChatAction
          resource:
          - message
    typeInfo:
      type: options
      displayName: Action
      name: action
      possibleValues:
      - value: find_location
        name: Find Location
        description: ''
      - value: record_audio
        name: Record Audio
        description: ''
      - value: record_video
        name: Record Video
        description: ''
      - value: record_video_note
        name: Record Video Note
        description: ''
      - value: typing
        name: Typing
        description: ''
      - value: upload_audio
        name: Upload Audio
        description: ''
      - value: upload_document
        name: Upload Document
        description: ''
      - value: upload_photo
        name: Upload Photo
        description: ''
      - value: upload_video
        name: Upload Video
        description: ''
      - value: upload_video_note
        name: Upload Video Note
        description: ''
- id: sendDocument
  name: Send Document
  description: Send a document
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation: *id009
    typeInfo: *id010
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: Name of the binary property that contains the data to upload
    hint: The name of the input binary field containing the file to be written
    validation: *id011
    typeInfo: *id012
  - id: file
    name: Document
    type: string
    default: ''
    required: false
    description: Document to send. Pass a file_id to send a file that exists on the
      Telegram servers (recommended), an HTTP URL for Telegram to get a file from
      the Internet.
    validation: *id013
    typeInfo: *id014
  - id: replyMarkup
    name: Reply Markup
    type: options
    default: none
    required: false
    description: Additional interface options
    validation: *id007
    typeInfo: *id008
- id: sendLocation
  name: Send Location
  description: Send a location
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: latitude
    name: Latitude
    type: number
    default: 0
    required: false
    description: Location latitude
    validation:
      displayOptions:
        show:
          operation:
          - sendLocation
          resource:
          - message
    typeInfo:
      type: number
      displayName: Latitude
      name: latitude
      typeOptions:
        maxValue: 90
        numberPrecision: 10
  - id: longitude
    name: Longitude
    type: number
    default: 0
    required: false
    description: Location longitude
    validation:
      displayOptions:
        show:
          operation:
          - sendLocation
          resource:
          - message
    typeInfo:
      type: number
      displayName: Longitude
      name: longitude
      typeOptions:
        maxValue: 180
        numberPrecision: 10
  - id: replyMarkup
    name: Reply Markup
    type: options
    default: none
    required: false
    description: Additional interface options
    validation: *id007
    typeInfo: *id008
- id: sendMediaGroup
  name: Send Media Group
  description: Send group of photos or videos to album
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: media
    name: Media
    type: fixedCollection
    default: {}
    required: false
    description: The media to add
    placeholder: Add Media
    validation:
      displayOptions:
        show:
          operation:
          - sendMediaGroup
          resource:
          - message
    typeInfo:
      type: fixedCollection
      displayName: Media
      name: media
      typeOptions:
        multipleValues: true
      subProperties:
      - name: media
        displayName: Media
        values:
        - displayName: Type
          name: type
          type: options
          description: The type of the media to add
          value: photo
          default: photo
          options:
          - name: Photo
            value: photo
            displayName: Photo
          - name: Video
            value: video
            displayName: Video
        - displayName: Media File
          name: media
          type: string
          description: Media to send. Pass a file_id to send a file that exists on
            the Telegram servers (recommended) or pass an HTTP URL for Telegram to
            get a file from the Internet.
          default: ''
        - displayName: Additional Fields
          name: additionalFields
          type: collection
          description: Caption text to set, 0-1024 characters
          placeholder: Add Field
          value: Markdown
          default: {}
          options:
          - displayName: Caption
            name: caption
            type: string
            description: Caption text to set, 0-1024 characters
            default: ''
          - displayName: Parse Mode
            name: parse_mode
            type: options
            description: How to parse the text
            value: Markdown
            default: HTML
            options:
            - name: Markdown (Legacy)
              value: Markdown
              displayName: Markdown (legacy)
            - name: MarkdownV2
              value: MarkdownV2
              displayName: Markdown V2
            - name: HTML
              value: HTML
              displayName: Html
- id: sendMessage
  name: Send Message
  description: Send a text message
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: text
    name: Text
    type: string
    default: ''
    required: true
    description: Text of the message to be sent
    validation: *id015
    typeInfo: *id016
  - id: replyMarkup
    name: Reply Markup
    type: options
    default: none
    required: false
    description: Additional interface options
    validation: *id007
    typeInfo: *id008
- id: ''
  name: Send and Wait for Response
  description: Send a message and wait for response
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation: *id009
    typeInfo: *id010
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: Name of the binary property that contains the data to upload
    hint: The name of the input binary field containing the file to be written
    validation: *id011
    typeInfo: *id012
  - id: replyMarkup
    name: Reply Markup
    type: options
    default: none
    required: false
    description: Additional interface options
    validation: *id007
    typeInfo: *id008
- id: sendPhoto
  name: Send Photo
  description: Send a photo
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation: *id009
    typeInfo: *id010
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: Name of the binary property that contains the data to upload
    hint: The name of the input binary field containing the file to be written
    validation: *id011
    typeInfo: *id012
  - id: file
    name: Photo
    type: string
    default: ''
    required: false
    description: Photo to send. Pass a file_id to send a photo that exists on the
      Telegram servers (recommended), an HTTP URL for Telegram to get a photo from
      the Internet.
    validation: *id013
    typeInfo: *id014
  - id: replyMarkup
    name: Reply Markup
    type: options
    default: none
    required: false
    description: Additional interface options
    validation: *id007
    typeInfo: *id008
- id: sendSticker
  name: Send Sticker
  description: Send a sticker
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation: *id009
    typeInfo: *id010
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: Name of the binary property that contains the data to upload
    hint: The name of the input binary field containing the file to be written
    validation: *id011
    typeInfo: *id012
  - id: file
    name: Sticker
    type: string
    default: ''
    required: false
    description: Sticker to send. Pass a file_id to send a file that exists on the
      Telegram servers (recommended), an HTTP URL for Telegram to get a .webp file
      from the Internet.
    validation: *id013
    typeInfo: *id014
  - id: replyMarkup
    name: Reply Markup
    type: options
    default: none
    required: false
    description: Additional interface options
    validation: *id007
    typeInfo: *id008
- id: sendVideo
  name: Send Video
  description: Send a video
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: binaryData
    name: Binary File
    type: boolean
    default: false
    required: true
    description: Whether the data to upload should be taken from binary field
    validation: *id009
    typeInfo: *id010
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: Name of the binary property that contains the data to upload
    hint: The name of the input binary field containing the file to be written
    validation: *id011
    typeInfo: *id012
  - id: file
    name: Video
    type: string
    default: ''
    required: false
    description: Video file to send. Pass a file_id to send a file that exists on
      the Telegram servers (recommended), an HTTP URL for Telegram to get a file from
      the Internet.
    validation: *id013
    typeInfo: *id014
  - id: replyMarkup
    name: Reply Markup
    type: options
    default: none
    required: false
    description: Additional interface options
    validation: *id007
    typeInfo: *id008
- id: unpinChatMessage
  name: Unpin Chat Message
  description: Unpin a chat message
  params:
  - id: chatId
    name: Chat ID
    type: string
    default: ''
    required: true
    description: Unique identifier for the target chat or username, To find your chat
      ID ask @get_id_bot
    validation: *id001
    typeInfo: *id002
  - id: messageId
    name: Message ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the message to pin or unpin
    validation: *id005
    typeInfo: *id006
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
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: media
    text: Add Media
  - field: forceReply
    text: Add Field
  - field: inlineKeyboard
    text: Add Keyboard Row
  - field: replyKeyboard
    text: Add Reply Keyboard Row
  - field: replyKeyboardOptions
    text: Add option
  - field: replyKeyboardRemove
    text: Add Field
  - field: additionalFields
    text: Add Field
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be written
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
  "$id": "https://n8n.io/schemas/nodes/telegram.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Telegram Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "info",
        "get",
        "administrators",
        "member",
        "leave",
        "setDescription",
        "setTitle",
        "answerQuery",
        "answerInlineQuery",
        "deleteMessage",
        "editMessageText",
        "pinChatMessage",
        "sendAnimation",
        "sendAudio",
        "sendChatAction",
        "sendDocument",
        "sendLocation",
        "sendMediaGroup",
        "sendMessage",
        "",
        "sendPhoto",
        "sendSticker",
        "sendVideo",
        "unpinChatMessage"
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
            "bot",
            "chat",
            "callback",
            "file",
            "message"
          ],
          "default": "message"
        },
        "operation": {
          "description": "Delete a chat message",
          "type": "string",
          "enum": [
            "deleteMessage",
            "editMessageText",
            "pinChatMessage",
            "sendAnimation",
            "sendAudio",
            "sendChatAction",
            "sendDocument",
            "sendLocation",
            "sendMediaGroup",
            "sendMessage",
            "Send and Wait for Response",
            "sendPhoto",
            "sendSticker",
            "sendVideo",
            "unpinChatMessage"
          ],
          "default": "sendMessage"
        },
        "chatId": {
          "description": "Unique identifier for the target chat or username of the target channel (in the format @channelusername). To find your chat ID ask @get_id_bot.",
          "type": "string",
          "default": ""
        },
        "messageId": {
          "description": "Unique identifier of the message to edit",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Whether to include the phrase \u201cThis message was sent automatically with n8n\u201d to the end of the message",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "userId": {
          "description": "Unique identifier of the target user",
          "type": "string",
          "default": ""
        },
        "description": {
          "description": "New chat description, 0-255 characters",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "New chat title, 1-255 characters",
          "type": "string",
          "default": ""
        },
        "queryId": {
          "description": "Unique identifier for the answered query",
          "type": "string",
          "default": ""
        },
        "results": {
          "description": "A JSON-serialized array of results for the inline query",
          "type": "string",
          "default": ""
        },
        "fileId": {
          "description": "The ID of the file",
          "type": "string",
          "default": ""
        },
        "download": {
          "description": "Whether to download the file",
          "type": "boolean",
          "default": true
        },
        "messageType": {
          "description": "The type of the message to edit",
          "type": "string",
          "enum": [
            "inlineMessage",
            "message"
          ],
          "default": "message"
        },
        "binaryData": {
          "description": "Whether the data to upload should be taken from binary field",
          "type": "boolean",
          "default": false
        },
        "binaryPropertyName": {
          "description": "Name of the binary property that contains the data to upload",
          "type": "string",
          "default": "data"
        },
        "inlineMessageId": {
          "description": "Unique identifier of the inline message to edit",
          "type": "string",
          "default": ""
        },
        "replyMarkup": {
          "description": "Additional interface options",
          "type": "string",
          "enum": [
            "forceReply",
            "inlineKeyboard",
            "none",
            "replyKeyboard",
            "replyKeyboardRemove"
          ],
          "default": "none"
        },
        "file": {
          "description": "Video file to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), an HTTP URL for Telegram to get a file from the Internet.",
          "type": "string",
          "default": ""
        },
        "action": {
          "description": "Type of action to broadcast. Choose one, depending on what the user is about to receive. The status is set for 5 seconds or less (when a message arrives from your bot).",
          "type": "string",
          "enum": [
            "find_location",
            "record_audio",
            "record_video",
            "record_video_note",
            "typing",
            "upload_audio",
            "upload_document",
            "upload_photo",
            "upload_video",
            "upload_video_note"
          ],
          "default": "typing"
        },
        "latitude": {
          "description": "Location latitude",
          "type": "number",
          "default": 0
        },
        "longitude": {
          "description": "Location longitude",
          "type": "number",
          "default": 0
        },
        "media": {
          "description": "The media to add",
          "type": "string",
          "default": {},
          "examples": [
            "Add Media"
          ]
        },
        "text": {
          "description": "Text of the message to be sent",
          "type": "string",
          "default": ""
        },
        "forceReply": {
          "description": "Whether to show reply interface to the user, as if they manually selected the bot\u2018s message and tapped \u2019Reply",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "inlineKeyboard": {
          "description": "Adds an inline keyboard that appears right next to the message it belongs to",
          "type": "string",
          "default": {},
          "examples": [
            "Add Keyboard Row"
          ]
        },
        "replyKeyboard": {
          "description": "Adds a custom keyboard with reply options",
          "type": "string",
          "default": {},
          "examples": [
            "Add Reply Keyboard Row"
          ]
        },
        "replyKeyboardOptions": {
          "description": "Whether to request clients to resize the keyboard vertically for optimal fit",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "replyKeyboardRemove": {
          "description": "Whether to request clients to remove the custom keyboard",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "appendAttribution": {
          "description": "",
          "type": "boolean",
          "default": true
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
      "1",
      "1.1",
      "1.2"
    ]
  },
  "credentials": [
    {
      "name": "telegramApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '1.1', '1.2'] | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
