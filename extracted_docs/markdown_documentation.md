---
title: "Node: Markdown"
slug: "node-markdown"
version: "1"
updated: "2025-11-13"
summary: "Convert data between Markdown and HTML"
node_type: "regular"
group: "['output']"
---

# Node: Markdown

**Purpose.** Convert data between Markdown and HTML
**Subtitle.** ={{$parameter["mode"]==="markdownToHtml" ? "Markdown to HTML" : "HTML to Markdown"}}


---

## Node Details

- **Icon:** `{'light': 'file:markdown.svg', 'dark': 'file:markdown.dark.svg'}`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Mode | `mode` | options | htmlToMarkdown | ✗ | Convert data from Markdown to HTML |  |

**Mode options:**

* **Markdown to HTML** (`markdownToHtml`) - Convert data from Markdown to HTML
* **HTML to Markdown** (`htmlToMarkdown`) - Convert data from HTML to Markdown

| HTML | `html` | string |  | ✓ | The HTML to be converted to markdown |  |
| Markdown | `markdown` | string |  | ✓ | The Markdown to be converted to html |  |
| Destination Key | `destinationKey` | string | data | ✓ | The field to put the output in. Specify nested fields using dots, e.g."level1.level2.newKey". |  |
| Options | `options` | collection | {} | ✗ | Specify bullet marker, default * | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Bullet Marker | `bulletMarker` | string | * | Specify bullet marker, default * |
| Code Block Fence | `codeFence` | string | ``` | Specify code block fence, default ``` |
| Emphasis Delimiter | `emDelimiter` | string | _ | Specify emphasis delimiter, default _ |
| Global Escape Pattern | `globalEscape` | fixedCollection | {} | Setting this will override the default escape settings, you might want to use textReplace option instead |
| Ignored Elements | `ignore` | string |  | Supplied elements will be ignored (ignores inner text does not parse children) |
| Keep Images With Data | `keepDataImages` | boolean | False | Whether to keep images with data: URI (Note: These can be up to 1MB each), e.g. &lt;img src="data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSK.../"&gt; |
| Line Start Escape Pattern | `lineStartEscape` | fixedCollection | {} | Setting this will override the default escape settings, you might want to use textReplace option instead |
| Max Consecutive New Lines | `maxConsecutiveNewlines` | number | 3 | Specify max consecutive new lines allowed |
| Place URLs At The Bottom | `useLinkReferenceDefinitions` | boolean | False | Whether to Place URLS at the bottom and format links using link reference definitions |
| Strong Delimiter | `strongDelimiter` | string | ** | Specify strong delimiter, default ** |
| Style For Code Block | `codeBlockStyle` | options | fence | Specify style for code block, default "fence" |
| Text Replacement Pattern | `textReplace` | fixedCollection | [] | User-defined text replacement pattern (Replaces matching text retrieved from nodes) |
| Treat As Blocks | `blockElements` | string |  | Supplied elements will be treated as blocks (surrounded with blank lines) |

</details>

| Options | `options` | collection | {} | ✗ | Whether to open all links in new windows (by adding the attribute target="_blank" to <a> tags) | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Add Blank To Links | `openLinksInNewWindow` | boolean | False | Whether to open all links in new windows (by adding the attribute target="_blank" to <a> tags) |
| Automatic Linking to URLs | `simplifiedAutoLink` | boolean | False | Whether to enable automatic linking to URLs |
| Backslash Escapes HTML Tags | `backslashEscapesHTMLTags` | boolean | False | Whether to support for HTML Tag escaping ex: &lt;div&gt;foo&lt;/div&gt; |
| Complete HTML Document | `completeHTMLDocument` | boolean | False | Whether to output a complete html document, including &lt;html&gt;, &lt;head&gt; and &lt;body&gt; tags instead of an HTML fragment |
| Customized Header ID | `customizedHeaderId` | boolean | False | Whether to use text in curly braces as header ID |
| Emoji Support | `emoji` | boolean | False | Whether to enable emoji support. Ex: this is a :smile: emoji For more info on available emojis, see https://github.com/showdownjs/showdown/wiki/Emojis. |
| Encode Emails | `encodeEmails` | boolean | True | Whether to enable e-mail addresses encoding through the use of Character Entities, transforming ASCII e-mail addresses into its equivalent decimal entities |
| Exclude Trailing Punctuation From URLs | `excludeTrailingPunctuationFromURLs` | boolean | False | Whether to exclude trailing punctuation from autolinking URLs. Punctuation excluded: . ! ? ( ). Only applies if simplifiedAutoLink option is set to true. |
| GitHub Code Blocks | `ghCodeBlocks` | boolean | True | Whether to enable support for GFM code block style |
| GitHub Compatible Header IDs | `ghCompatibleHeaderId` | boolean | False | Whether to generate header IDs compatible with github style (spaces are replaced with dashes and a bunch of non alphanumeric chars are removed) |
| GitHub Mention Link | `ghMentionsLink` | string | https://github.com/{u} | Whether to change the link generated by @mentions. Showdown will replace {u} with the username. Only applies if ghMentions option is enabled. |
| GitHub Mentions | `ghMentions` | boolean | False | Whether to enable github @mentions, which link to the username mentioned |
| GitHub Task Lists | `tasklists` | boolean | False | Whether to enable support for GFM tasklists |
| Header Level Start | `headerLevelStart` | number | 1 | Whether to set the header starting level |
| Mandatory Space Before Header | `requireSpaceBeforeHeadingText` | boolean | False | Whether to make adding a space between # and the header text mandatory |
| Middle Word Asterisks | `literalMidWordAsterisks` | boolean | False | Whether to stop showdown from interpreting asterisks in the middle of words as <em> and <strong> and instead treat them as literal asterisks |
| Middle Word Underscores | `literalMidWordUnderscores` | boolean | False | Whether to stop showdown from interpreting underscores in the middle of words as <em> and <strong> and instead treat them as literal underscores |
| No Header ID | `noHeaderId` | boolean | False | Whether to disable the automatic generation of header IDs |
| Parse Image Dimensions | `parseImgDimensions` | boolean | False | Whether to enable support for setting image dimensions from within markdown syntax |
| Prefix Header ID | `prefixHeaderId` | string | section | Add a prefix to the generated header IDs |
| Raw Header ID | `rawHeaderId` | boolean | False | Whether to remove only spaces, ' and " from generated header IDs (including prefixes), replacing them with dashes (-) |
| Raw Prefix Header ID | `rawPrefixHeaderId` | boolean | False | Whether to prevent showdown from modifying the prefix |
| Simple Line Breaks | `simpleLineBreaks` | boolean | False | Whether to parse line breaks as &lt;br&gt;, like GitHub does, without needing 2 spaces at the end of the line |
| Smart Indentation Fix | `smartIndentationFix` | boolean | False | Whether to try to smartly fix indentation problems related to es6 template strings in the midst of indented code |
| Spaces Indented Sublists | `disableForced4SpacesIndentedSublists` | boolean | False | Whether to disable the requirement of indenting sublists by 4 spaces for them to be nested, effectively reverting to the old behavior where 2 or 3 spaces were enough |
| Split Adjacent Blockquotes | `splitAdjacentBlockquotes` | boolean | False | Whether to split adjacent blockquote blocks |
| Strikethrough | `strikethrough` | boolean | False | Whether to enable support for strikethrough syntax |
| Tables Header ID | `tablesHeaderId` | boolean | False | Whether to add an ID property to table headers tags |
| Tables Support | `tables` | boolean | False | Whether to enable support for tables syntax |

</details>


---

## Common Expression Patterns

These expression patterns are commonly used with this node:

- `={{$parameter["mode"]==="markdownToHtml" ? "Markdown to HTML" : "HTML to Markdown"}}`

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
* Categories: Core Nodes

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: markdown
displayName: Markdown
description: Convert data between Markdown and HTML
version: '1'
nodeType: regular
group:
- output
params:
- id: mode
  name: Mode
  type: options
  default: htmlToMarkdown
  required: false
  description: Convert data from Markdown to HTML
  typeInfo:
    type: options
    displayName: Mode
    name: mode
    possibleValues:
    - value: markdownToHtml
      name: Markdown to HTML
      description: Convert data from Markdown to HTML
    - value: htmlToMarkdown
      name: HTML to Markdown
      description: Convert data from HTML to Markdown
- id: html
  name: HTML
  type: string
  default: ''
  required: true
  description: The HTML to be converted to markdown
  validation:
    required: true
    displayOptions:
      show:
        mode:
        - htmlToMarkdown
  typeInfo:
    type: string
    displayName: HTML
    name: html
- id: markdown
  name: Markdown
  type: string
  default: ''
  required: true
  description: The Markdown to be converted to html
  validation:
    required: true
    displayOptions:
      show:
        mode:
        - markdownToHtml
  typeInfo:
    type: string
    displayName: Markdown
    name: markdown
- id: destinationKey
  name: Destination Key
  type: string
  default: data
  required: true
  description: The field to put the output in. Specify nested fields using dots, e.g."level1.level2.newKey".
  validation:
    required: true
    displayOptions:
      show:
        mode:
        - markdownToHtml
        - htmlToMarkdown
  typeInfo:
    type: string
    displayName: Destination Key
    name: destinationKey
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Specify bullet marker, default *
  hint: Comma separated elements
  placeholder: Add option
  validation: &id001
    displayOptions:
      show:
        mode:
        - markdownToHtml
  typeInfo: &id002
    type: collection
    displayName: Options
    name: options
    subProperties:
    - displayName: Add Blank To Links
      name: openLinksInNewWindow
      type: boolean
      description: Whether to open all links in new windows (by adding the attribute
        target="_blank" to <a> tags)
      default: false
    - displayName: Automatic Linking to URLs
      name: simplifiedAutoLink
      type: boolean
      description: Whether to enable automatic linking to URLs
      default: false
    - displayName: Backslash Escapes HTML Tags
      name: backslashEscapesHTMLTags
      type: boolean
      description: 'Whether to support for HTML Tag escaping ex: &lt;div&gt;foo&lt;/div&gt;'
      default: false
    - displayName: Complete HTML Document
      name: completeHTMLDocument
      type: boolean
      description: Whether to output a complete html document, including &lt;html&gt;,
        &lt;head&gt; and &lt;body&gt; tags instead of an HTML fragment
      default: false
    - displayName: Customized Header ID
      name: customizedHeaderId
      type: boolean
      description: Whether to use text in curly braces as header ID
      default: false
    - displayName: Emoji Support
      name: emoji
      type: boolean
      description: 'Whether to enable emoji support. Ex: this is a :smile: emoji For
        more info on available emojis, see https://github.com/showdownjs/showdown/wiki/Emojis.'
      default: false
    - displayName: Encode Emails
      name: encodeEmails
      type: boolean
      description: Whether to enable e-mail addresses encoding through the use of
        Character Entities, transforming ASCII e-mail addresses into its equivalent
        decimal entities
      default: true
    - displayName: Exclude Trailing Punctuation From URLs
      name: excludeTrailingPunctuationFromURLs
      type: boolean
      description: 'Whether to exclude trailing punctuation from autolinking URLs.
        Punctuation excluded: . ! ? ( ). Only applies if simplifiedAutoLink option
        is set to true.'
      default: false
    - displayName: GitHub Code Blocks
      name: ghCodeBlocks
      type: boolean
      description: Whether to enable support for GFM code block style
      default: true
    - displayName: GitHub Compatible Header IDs
      name: ghCompatibleHeaderId
      type: boolean
      description: Whether to generate header IDs compatible with github style (spaces
        are replaced with dashes and a bunch of non alphanumeric chars are removed)
      default: false
    - displayName: GitHub Mention Link
      name: ghMentionsLink
      type: string
      description: Whether to change the link generated by @mentions. Showdown will
        replace {u} with the username. Only applies if ghMentions option is enabled.
      default: https://github.com/{u}
    - displayName: GitHub Mentions
      name: ghMentions
      type: boolean
      description: Whether to enable github @mentions, which link to the username
        mentioned
      default: false
    - displayName: GitHub Task Lists
      name: tasklists
      type: boolean
      description: Whether to enable support for GFM tasklists
      default: false
    - displayName: Header Level Start
      name: headerLevelStart
      type: number
      description: Whether to set the header starting level
      default: 1
    - displayName: Mandatory Space Before Header
      name: requireSpaceBeforeHeadingText
      type: boolean
      description: 'Whether to make adding a space between # and the header text mandatory'
      default: false
    - displayName: Middle Word Asterisks
      name: literalMidWordAsterisks
      type: boolean
      description: Whether to stop showdown from interpreting asterisks in the middle
        of words as <em> and <strong> and instead treat them as literal asterisks
      default: false
    - displayName: Middle Word Underscores
      name: literalMidWordUnderscores
      type: boolean
      description: Whether to stop showdown from interpreting underscores in the middle
        of words as <em> and <strong> and instead treat them as literal underscores
      default: false
    - displayName: No Header ID
      name: noHeaderId
      type: boolean
      description: Whether to disable the automatic generation of header IDs
      default: false
    - displayName: Parse Image Dimensions
      name: parseImgDimensions
      type: boolean
      description: Whether to enable support for setting image dimensions from within
        markdown syntax
      default: false
    - displayName: Prefix Header ID
      name: prefixHeaderId
      type: string
      description: Add a prefix to the generated header IDs
      default: section
    - displayName: Raw Header ID
      name: rawHeaderId
      type: boolean
      description: Whether to remove only spaces, ' and " from generated header IDs
        (including prefixes), replacing them with dashes (-)
      default: false
    - displayName: Raw Prefix Header ID
      name: rawPrefixHeaderId
      type: boolean
      description: Whether to prevent showdown from modifying the prefix
      default: false
    - displayName: Simple Line Breaks
      name: simpleLineBreaks
      type: boolean
      description: Whether to parse line breaks as &lt;br&gt;, like GitHub does, without
        needing 2 spaces at the end of the line
      default: false
    - displayName: Smart Indentation Fix
      name: smartIndentationFix
      type: boolean
      description: Whether to try to smartly fix indentation problems related to es6
        template strings in the midst of indented code
      default: false
    - displayName: Spaces Indented Sublists
      name: disableForced4SpacesIndentedSublists
      type: boolean
      description: Whether to disable the requirement of indenting sublists by 4 spaces
        for them to be nested, effectively reverting to the old behavior where 2 or
        3 spaces were enough
      default: false
    - displayName: Split Adjacent Blockquotes
      name: splitAdjacentBlockquotes
      type: boolean
      description: Whether to split adjacent blockquote blocks
      default: false
    - displayName: Strikethrough
      name: strikethrough
      type: boolean
      description: Whether to enable support for strikethrough syntax
      default: false
    - displayName: Tables Header ID
      name: tablesHeaderId
      type: boolean
      description: Whether to add an ID property to table headers tags
      default: false
    - displayName: Tables Support
      name: tables
      type: boolean
      description: Whether to enable support for tables syntax
      default: false
- id: options
  name: Options
  type: collection
  default: {}
  required: false
  description: Whether to open all links in new windows (by adding the attribute target="_blank"
    to <a> tags)
  placeholder: Add option
  validation: *id001
  typeInfo: *id002
common_expressions:
- '={{$parameter["mode"]==="markdownToHtml" ? "Markdown to HTML" : "HTML to Markdown"}}'
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: options
    text: Add option
  - field: options
    text: Add option
  hints:
  - field: options
    text: Comma separated elements
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
  "$id": "https://n8n.io/schemas/nodes/markdown.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Markdown Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "mode": {
          "description": "Convert data from Markdown to HTML",
          "type": "string",
          "enum": [
            "markdownToHtml",
            "htmlToMarkdown"
          ],
          "default": "htmlToMarkdown"
        },
        "html": {
          "description": "The HTML to be converted to markdown",
          "type": "string",
          "default": ""
        },
        "markdown": {
          "description": "The Markdown to be converted to html",
          "type": "string",
          "default": ""
        },
        "destinationKey": {
          "description": "The field to put the output in. Specify nested fields using dots, e.g.\"level1.level2.newKey\".",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "Whether to open all links in new windows (by adding the attribute target=\"_blank\" to <a> tags)",
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
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
