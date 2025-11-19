---
title: "Node: Spotify"
slug: "node-spotify"
version: "1"
updated: "2025-11-13"
summary: "Access public song data via the Spotify API"
node_type: "regular"
group: "['input']"
---

# Node: Spotify

**Purpose.** Access public song data via the Spotify API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:spotify.svg`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **spotifyOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `spotifyOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type, User-Agent

---

## Operations

### Player Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Song to Queue | `addSongToQueue` | Add a song to your queue |
| Currently Playing | `currentlyPlaying` | Get your currently playing track |
| Next Song | `nextSong` | Skip to your next track |
| Pause | `pause` | Pause your music |
| Previous Song | `previousSong` | Skip to your previous song |
| Recently Played | `recentlyPlayed` | Get your recently played tracks |
| Resume | `resume` | Resume playback on the current active device |
| Set Volume | `volume` | Set volume on the current active device |
| Start Music | `startMusic` | Start playing a playlist, artist, or album |

### Album Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get an album by URI or ID |
| Get New Releases | `getNewReleases` | Get a list of new album releases |
| Get Tracks | `getTracks` | Get an album's tracks by URI or ID |
| Search | `search` | Search albums by keyword |

### Artist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get an artist by URI or ID |
| Get Albums | `getAlbums` | Get an artist's albums by URI or ID |
| Get Related Artists | `getRelatedArtists` | Get an artist's related artists by URI or ID |
| Get Top Tracks | `getTopTracks` | Get an artist's top tracks by URI or ID |
| Search | `search` | Search artists by keyword |

### Playlist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add an Item | `add` | Add tracks to a playlist by track and playlist URI or ID |
| Create a Playlist | `create` | Create a new playlist |
| Get | `get` | Get a playlist by URI or ID |
| Get the User's Playlists | `getUserPlaylists` | Get a user's playlists |
| Get Tracks | `getTracks` | Get a playlist's tracks by URI or ID |
| Remove an Item | `delete` | Remove tracks from a playlist by track and playlist URI or ID |
| Search | `search` | Search playlists by keyword |

### Track Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a track by its URI or ID |
| Get Audio Features | `getAudioFeatures` | Get audio features for a track by URI or ID |
| Search | `search` | Search tracks by keyword |

### Library Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Liked Tracks | `getLikedTracks` | Get the user's liked tracks |

### Mydata Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Following Artists | `getFollowingArtists` | Get your followed artists |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | player | ✗ | Resource to operate on |  |

**Resource options:**

* **Album** (`album`)
* **Artist** (`artist`)
* **Library** (`library`)
* **My Data** (`myData`)
* **Player** (`player`)
* **Playlist** (`playlist`)
* **Track** (`track`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | addSongToQueue | ✗ | Add a song to your queue |  |

**Operation options:**

* **Add Song to Queue** (`addSongToQueue`) - Add a song to your queue
* **Currently Playing** (`currentlyPlaying`) - Get your currently playing track
* **Next Song** (`nextSong`) - Skip to your next track
* **Pause** (`pause`) - Pause your music
* **Previous Song** (`previousSong`) - Skip to your previous song
* **Recently Played** (`recentlyPlayed`) - Get your recently played tracks
* **Resume** (`resume`) - Resume playback on the current active device
* **Set Volume** (`volume`) - Set volume on the current active device
* **Start Music** (`startMusic`) - Start playing a playlist, artist, or album

---

### Add Song to Queue parameters (`addSongToQueue`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Track ID | `id` | string |  | ✓ | Enter a track URI or ID | e.g. spotify:track:0xE4LEFzSNGsz1F6kvXsHU |  |

### Recently Played parameters (`recentlyPlayed`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✓ | Max number of results to return | min:1, max:50 |

### Set Volume parameters (`volume`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Volume | `volumePercent` | number | 50 | ✓ | The volume percentage to set | min:0, max:100 |

### Start Music parameters (`startMusic`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource ID | `id` | string |  | ✓ | Enter a playlist, artist, or album URI or ID | e.g. spotify:album:1YZ3k65Mqw3G8FzYlW1mmp |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Album ID | `id` | string |  | ✓ | The album's Spotify URI or ID | e.g. spotify:album:1YZ3k65Mqw3G8FzYlW1mmp |  |
| Playlist ID | `id` | string |  | ✓ | The playlist's Spotify URI or its ID | e.g. spotify:playlist:37i9dQZF1DWUhI3iC1khPH |  |

### Get New Releases parameters (`getNewReleases`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✓ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | Country to filter new releases by | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Country | `country` | options | US | Country to filter new releases by |

</details>


### Get Tracks parameters (`getTracks`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Album ID | `id` | string |  | ✓ | The album's Spotify URI or ID | e.g. spotify:album:1YZ3k65Mqw3G8FzYlW1mmp |  |
| Playlist ID | `id` | string |  | ✓ | The playlist's Spotify URI or its ID | e.g. spotify:playlist:37i9dQZF1DWUhI3iC1khPH |  |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✓ | Max number of results to return | min:1, max:100 |

### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Search Keyword | `query` | string |  | ✓ | The keyword term to search for |  |
| Search Keyword | `query` | string |  | ✓ | The keyword term to search for |  |
| Search Keyword | `query` | string |  | ✓ | The keyword term to search for |  |
| Search Keyword | `query` | string |  | ✓ | The keyword term to search for |  |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✓ | Max number of results to return | min:1, max:100 |
| Filters | `filters` | collection | {} | ✗ | If a country code is specified, only content that is playable in that market is returned | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Country | `market` | options |  | If a country code is specified, only content that is playable in that market is returned |

</details>


### Get Albums parameters (`getAlbums`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✓ | Max number of results to return | min:1, max:100 |

### Get Top Tracks parameters (`getTopTracks`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Country | `country` | string | US | ✓ | Top tracks in which country? Enter the postal abbreviation | e.g. US |  |

### Add an Item parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Playlist ID | `id` | string |  | ✓ | The playlist's Spotify URI or its ID | e.g. spotify:playlist:37i9dQZF1DWUhI3iC1khPH |  |
| Track ID | `trackID` | string |  | ✓ | The track's Spotify URI or its ID. The track to add/delete from the playlist. | e.g. spotify:track:0xE4LEFzSNGsz1F6kvXsHU |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The new track's position in the playlist | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Position | `position` | number | 0 | The new track's position in the playlist |

</details>


### Create a Playlist parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ | Name of the playlist to create | e.g. Favorite Songs |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Description for the playlist to create | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Description for the playlist to create |
| Public | `public` | boolean | True | Whether the playlist is publicly accessible |

</details>


### Get the User's Playlists parameters (`getUserPlaylists`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✓ | Max number of results to return | min:1, max:100 |

### Remove an Item parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Playlist ID | `id` | string |  | ✓ | The playlist's Spotify URI or its ID | e.g. spotify:playlist:37i9dQZF1DWUhI3iC1khPH |  |
| Track ID | `trackID` | string |  | ✓ | The track's Spotify URI or its ID. The track to add/delete from the playlist. | e.g. spotify:track:0xE4LEFzSNGsz1F6kvXsHU |  |

### Get Liked Tracks parameters (`getLikedTracks`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✓ | Max number of results to return | min:1, max:100 |

### Get Following Artists parameters (`getFollowingArtists`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✓ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✓ | Max number of results to return | min:1, max:50 |

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Spotify

**From workflow:** [TEST] Spotify

**Parameters:**
```json
{
  "resource": "album",
  "operation": "search",
  "query": "From Xero",
  "limit": 2,
  "filters": {}
}
```

**Credentials:**
- spotifyOAuth2Api: `Spotify account`

### Example 2: Spotify1

**From workflow:** [TEST] Spotify

**Parameters:**
```json
{
  "resource": "album",
  "operation": "getNewReleases",
  "limit": 2,
  "filters": {}
}
```

**Credentials:**
- spotifyOAuth2Api: `Spotify account`

### Example 3: Spotify2

**From workflow:** [TEST] Spotify

**Parameters:**
```json
{
  "resource": "album",
  "operation": "getTracks",
  "id": "spotify:album:4R6FV9NSzhPihHR0h4pI93",
  "returnAll": true
}
```

**Credentials:**
- spotifyOAuth2Api: `Spotify account`

### Example 4: Spotify4

**From workflow:** [TEST] Spotify

**Parameters:**
```json
{
  "resource": "album",
  "id": "4R6FV9NSzhPihHR0h4pI93"
}
```

**Credentials:**
- spotifyOAuth2Api: `Spotify account`


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
* Categories: Miscellaneous
* Aliases: Music, Song

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: spotify
displayName: Spotify
description: Access public song data via the Spotify API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: spotifyOAuth2Api
  required: true
operations:
- id: addSongToQueue
  name: Add Song to Queue
  description: Add a song to your queue
  params:
  - id: id
    name: Track ID
    type: string
    default: ''
    required: true
    description: Enter a track URI or ID
    placeholder: spotify:track:0xE4LEFzSNGsz1F6kvXsHU
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - track
        hide:
          operation:
          - search
    typeInfo: &id002
      type: string
      displayName: Track ID
      name: id
- id: currentlyPlaying
  name: Currently Playing
  description: Get your currently playing track
- id: nextSong
  name: Next Song
  description: Skip to your next track
- id: pause
  name: Pause
  description: Pause your music
- id: previousSong
  name: Previous Song
  description: Skip to your previous song
- id: recentlyPlayed
  name: Recently Played
  description: Get your recently played tracks
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - album
          - artist
          - library
          - myData
          - playlist
          - track
          - player
          operation:
          - getTracks
          - getAlbums
          - getUserPlaylists
          - getNewReleases
          - getLikedTracks
          - getFollowingArtists
          - search
          - recentlyPlayed
          - ''
    typeInfo: &id004
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: true
    description: Max number of results to return
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - myData
          - player
          operation:
          - getFollowingArtists
          - recentlyPlayed
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 50
- id: resume
  name: Resume
  description: Resume playback on the current active device
- id: volume
  name: Set Volume
  description: Set volume on the current active device
  params:
  - id: volumePercent
    name: Volume
    type: number
    default: 50
    required: true
    description: The volume percentage to set
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - player
          operation:
          - volume
    typeInfo:
      type: number
      displayName: Volume
      name: volumePercent
      typeOptions:
        minValue: 0
        maxValue: 100
- id: startMusic
  name: Start Music
  description: Start playing a playlist, artist, or album
  params:
  - id: id
    name: Resource ID
    type: string
    default: ''
    required: true
    description: Enter a playlist, artist, or album URI or ID
    placeholder: spotify:album:1YZ3k65Mqw3G8FzYlW1mmp
    validation: *id001
    typeInfo: *id002
- id: get
  name: Get
  description: Get an album by URI or ID
  params:
  - id: id
    name: Album ID
    type: string
    default: ''
    required: true
    description: The album's Spotify URI or ID
    placeholder: spotify:album:1YZ3k65Mqw3G8FzYlW1mmp
    validation: *id001
    typeInfo: *id002
  - id: id
    name: Playlist ID
    type: string
    default: ''
    required: true
    description: The playlist's Spotify URI or its ID
    placeholder: spotify:playlist:37i9dQZF1DWUhI3iC1khPH
    validation: *id001
    typeInfo: *id002
- id: getNewReleases
  name: Get New Releases
  description: Get a list of new album releases
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: true
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: getTracks
  name: Get Tracks
  description: Get an album's tracks by URI or ID
  params:
  - id: id
    name: Album ID
    type: string
    default: ''
    required: true
    description: The album's Spotify URI or ID
    placeholder: spotify:album:1YZ3k65Mqw3G8FzYlW1mmp
    validation: *id001
    typeInfo: *id002
  - id: id
    name: Playlist ID
    type: string
    default: ''
    required: true
    description: The playlist's Spotify URI or its ID
    placeholder: spotify:playlist:37i9dQZF1DWUhI3iC1khPH
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: true
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: search
  name: Search
  description: Search albums by keyword
  params:
  - id: query
    name: Search Keyword
    type: string
    default: ''
    required: true
    description: The keyword term to search for
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - track
          operation:
          - search
    typeInfo: &id008
      type: string
      displayName: Search Keyword
      name: query
  - id: query
    name: Search Keyword
    type: string
    default: ''
    required: true
    description: The keyword term to search for
    validation: *id007
    typeInfo: *id008
  - id: query
    name: Search Keyword
    type: string
    default: ''
    required: true
    description: The keyword term to search for
    validation: *id007
    typeInfo: *id008
  - id: query
    name: Search Keyword
    type: string
    default: ''
    required: true
    description: The keyword term to search for
    validation: *id007
    typeInfo: *id008
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: true
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: getAlbums
  name: Get Albums
  description: Get an artist's albums by URI or ID
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: true
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: getRelatedArtists
  name: Get Related Artists
  description: Get an artist's related artists by URI or ID
- id: getTopTracks
  name: Get Top Tracks
  description: Get an artist's top tracks by URI or ID
  params:
  - id: country
    name: Country
    type: string
    default: US
    required: true
    description: Top tracks in which country? Enter the postal abbreviation
    placeholder: US
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - artist
          operation:
          - getTopTracks
    typeInfo:
      type: string
      displayName: Country
      name: country
- id: add
  name: Add an Item
  description: Add tracks to a playlist by track and playlist URI or ID
  params:
  - id: id
    name: Playlist ID
    type: string
    default: ''
    required: true
    description: The playlist's Spotify URI or its ID
    placeholder: spotify:playlist:37i9dQZF1DWUhI3iC1khPH
    validation: *id001
    typeInfo: *id002
  - id: trackID
    name: Track ID
    type: string
    default: ''
    required: true
    description: The track's Spotify URI or its ID. The track to add/delete from the
      playlist.
    placeholder: spotify:track:0xE4LEFzSNGsz1F6kvXsHU
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - playlist
          operation:
          - add
          - delete
    typeInfo: &id010
      type: string
      displayName: Track ID
      name: trackID
- id: create
  name: Create a Playlist
  description: Create a new playlist
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the playlist to create
    placeholder: Favorite Songs
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - playlist
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
- id: getUserPlaylists
  name: Get the User's Playlists
  description: Get a user's playlists
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: true
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: delete
  name: Remove an Item
  description: Remove tracks from a playlist by track and playlist URI or ID
  params:
  - id: id
    name: Playlist ID
    type: string
    default: ''
    required: true
    description: The playlist's Spotify URI or its ID
    placeholder: spotify:playlist:37i9dQZF1DWUhI3iC1khPH
    validation: *id001
    typeInfo: *id002
  - id: trackID
    name: Track ID
    type: string
    default: ''
    required: true
    description: The track's Spotify URI or its ID. The track to add/delete from the
      playlist.
    placeholder: spotify:track:0xE4LEFzSNGsz1F6kvXsHU
    validation: *id009
    typeInfo: *id010
- id: getAudioFeatures
  name: Get Audio Features
  description: Get audio features for a track by URI or ID
- id: getLikedTracks
  name: Get Liked Tracks
  description: Get the user's liked tracks
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: true
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
- id: getFollowingArtists
  name: Get Following Artists
  description: Get your followed artists
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: true
    description: Whether to return all results or only up to a given limit
    validation: *id003
    typeInfo: *id004
  - id: limit
    name: Limit
    type: number
    default: 50
    required: true
    description: Max number of results to return
    validation: *id005
    typeInfo: *id006
examples:
- name: Spotify
  parameters:
    resource: album
    operation: search
    query: From Xero
    limit: 2
    filters: {}
  workflow: '[TEST] Spotify'
- name: Spotify1
  parameters:
    resource: album
    operation: getNewReleases
    limit: 2
    filters: {}
  workflow: '[TEST] Spotify'
- name: Spotify2
  parameters:
    resource: album
    operation: getTracks
    id: spotify:album:4R6FV9NSzhPihHR0h4pI93
    returnAll: true
  workflow: '[TEST] Spotify'
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - Content-Type
  - User-Agent
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: id
    text: spotify:album:1YZ3k65Mqw3G8FzYlW1mmp
  - field: id
    text: spotify:track:0xE4LEFzSNGsz1F6kvXsHU
  - field: id
    text: spotify:album:1YZ3k65Mqw3G8FzYlW1mmp
  - field: id
    text: spotify:artist:4LLpKhyESsyAXpc4laK94U
  - field: country
    text: US
  - field: id
    text: spotify:playlist:37i9dQZF1DWUhI3iC1khPH
  - field: name
    text: Favorite Songs
  - field: additionalFields
    text: Add Field
  - field: trackID
    text: spotify:track:0xE4LEFzSNGsz1F6kvXsHU
  - field: additionalFields
    text: Add Field
  - field: id
    text: spotify:track:0xE4LEFzSNGsz1F6kvXsHU
  - field: filters
    text: Add Filter
  - field: filters
    text: Add Filter
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
  "$id": "https://n8n.io/schemas/nodes/spotify.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Spotify Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "addSongToQueue",
        "currentlyPlaying",
        "nextSong",
        "pause",
        "previousSong",
        "recentlyPlayed",
        "resume",
        "volume",
        "startMusic",
        "get",
        "getNewReleases",
        "getTracks",
        "search",
        "getAlbums",
        "getRelatedArtists",
        "getTopTracks",
        "add",
        "create",
        "getUserPlaylists",
        "delete",
        "getAudioFeatures",
        "getLikedTracks",
        "getFollowingArtists"
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
            "album",
            "artist",
            "library",
            "myData",
            "player",
            "playlist",
            "track"
          ],
          "default": "player"
        },
        "operation": {
          "description": "Get your followed artists",
          "type": "string",
          "enum": [
            "getFollowingArtists"
          ],
          "default": "getFollowingArtists"
        },
        "id": {
          "description": "The track's Spotify URI or ID",
          "type": "string",
          "default": "",
          "examples": [
            "spotify:track:0xE4LEFzSNGsz1F6kvXsHU"
          ]
        },
        "query": {
          "description": "The keyword term to search for",
          "type": "string",
          "default": ""
        },
        "country": {
          "description": "Top tracks in which country? Enter the postal abbreviation",
          "type": "string",
          "default": "US",
          "examples": [
            "US"
          ]
        },
        "name": {
          "description": "Name of the playlist to create",
          "type": "string",
          "default": "",
          "examples": [
            "Favorite Songs"
          ]
        },
        "additionalFields": {
          "description": "The new track's position in the playlist",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "trackID": {
          "description": "The track's Spotify URI or its ID. The track to add/delete from the playlist.",
          "type": "string",
          "default": "",
          "examples": [
            "spotify:track:0xE4LEFzSNGsz1F6kvXsHU"
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
          "default": 50
        },
        "volumePercent": {
          "description": "The volume percentage to set",
          "type": "number",
          "default": 50
        },
        "filters": {
          "description": "If a country code is specified, only content that is playable in that market is returned",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
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
  },
  "credentials": [
    {
      "name": "spotifyOAuth2Api",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Spotify",
      "value": {
        "resource": "album",
        "operation": "search",
        "query": "From Xero",
        "limit": 2,
        "filters": {}
      }
    },
    {
      "description": "Spotify1",
      "value": {
        "resource": "album",
        "operation": "getNewReleases",
        "limit": 2,
        "filters": {}
      }
    },
    {
      "description": "Spotify2",
      "value": {
        "resource": "album",
        "operation": "getTracks",
        "id": "spotify:album:4R6FV9NSzhPihHR0h4pI93",
        "returnAll": true
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
