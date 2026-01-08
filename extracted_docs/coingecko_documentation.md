---
title: "Node: CoinGecko"
slug: "node-coingecko"
version: "1"
updated: "2026-01-08"
summary: "Consume CoinGecko API"
node_type: "regular"
group: "['output']"
---

# Node: CoinGecko

**Purpose.** Consume CoinGecko API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:coinGecko.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Coin Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Candlestick | `candlestick` | Get a candlestick open-high-low-close chart for the selected currency |
| Get | `get` | Get current data for a coin |
| Get Many | `getAll` | Get many coins |
| History | `history` | Get historical data (name, price, market, stats) at a given date for a coin |
| Market | `market` | Get prices and market related data for all trading pairs that match the selected currency |
| Market Chart | `marketChart` | Get historical market data include price, market cap, and 24h volume (granularity auto) |
| Price | `price` | Get the current price of any cryptocurrencies in any other supported currencies that you need |
| Ticker | `ticker` | Get coin tickers |

### Event Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many events |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | coin | ✗ | Resource to operate on |  |

**Resource options:**

* **Coin** (`coin`)
* **Event** (`event`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getAll | ✗ | Get a candlestick open-high-low-close chart for the selected currency |  |

**Operation options:**

* **Candlestick** (`candlestick`) - Get a candlestick open-high-low-close chart for the selected currency
* **Get** (`get`) - Get current data for a coin
* **Get Many** (`getAll`) - Get many coins
* **History** (`history`) - Get historical data (name, price, market, stats) at a given date for a coin
* **Market** (`market`) - Get prices and market related data for all trading pairs that match the selected currency
* **Market Chart** (`marketChart`) - Get historical market data include price, market cap, and 24h volume (granularity auto)
* **Price** (`price`) - Get the current price of any cryptocurrencies in any other supported currencies that you need
* **Ticker** (`ticker`) - Get coin tickers

---

### Candlestick parameters (`candlestick`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Base Currency Name or ID | `baseCurrency` | options |  | ✓ | The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Quote Currency Name or ID | `quoteCurrency` | options |  | ✓ | The second currency in the pair. For BTC:ETH this is ETH. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Range (Days) | `days` | options |  | ✓ | Return data for this many days in the past from now |  |

**Range (Days) options:**

* **1** (`1`)
* **7** (`7`)
* **14** (`14`)
* **30** (`30`)
* **90** (`90`)
* **180** (`180`)
* **365** (`365`)
* **Max** (`max`)


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Search By | `searchBy` | options | coinId | ✓ | Search by coin ID or contract address |  |

**Search By options:**

* **Coin ID** (`coinId`)
* **Contract Address** (`contractAddress`)

| Coin Name or ID | `coinId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. bitcoin |  |
| Platform ID | `platformId` | options | ethereum | ✓ | The ID of the platform issuing tokens |  |

**Platform ID options:**

* **Ethereum** (`ethereum`)

| Contract Address | `contractAddress` | string |  | ✓ | Token's contract address |  |
| Options | `options` | collection | {} | ✗ | Whether to include community data | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Community Data | `community_data` | boolean | False | Whether to include community data |
| Developer Data | `developer_data` | boolean | False | Whether to include developer data |
| Localization | `localization` | boolean | False | Whether to include all localized languages in response |
| Market Data | `market_data` | boolean | False | Whether to include market data |
| Sparkline | `sparkline` | boolean | False | Whether to include sparkline 7 days data (eg. true, false). |
| Tickers | `tickers` | boolean | False | Whether to include tickers data |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Country code of event. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Country Code | `country_code` | options |  | Country code of event. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| From Date | `from_date` | dateTime |  | Lists events after this date |
| To Date | `to_date` | dateTime |  | Lists events before this date |
| Type Name or ID | `type` | options |  | Type of event. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Upcoming Events Only | `upcoming_events_only` | boolean | True | Whether to list only upcoming events |

</details>


### History parameters (`history`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Coin Name or ID | `coinId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. bitcoin |  |
| Date | `date` | dateTime |  | ✓ | The date of data snapshot |  |
| Options | `options` | collection | {} | ✗ | Whether to exclude localized languages in response | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Localization | `localization` | boolean | True | Whether to exclude localized languages in response |

</details>


### Market parameters (`market`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Base Currency Name or ID | `baseCurrency` | options |  | ✓ | The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Filter results by comma-separated list of coin ID | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Coin IDs | `ids` | string |  | Filter results by comma-separated list of coin ID |
| Category | `category` | options | decentralized_finance_defi | Filter by coin category |
| Order | `order` | options |  | Sort results by field |
| Sparkline | `sparkline` | boolean | False | Whether to include sparkline 7 days data |
| Price Change Percentage | `price_change_percentage` | multiOptions | [] | Include price change percentage for specified times |

</details>


### Market Chart parameters (`marketChart`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Search By | `searchBy` | options | coinId | ✓ | Search by coin ID or contract address |  |

**Search By options:**

* **Coin ID** (`coinId`)
* **Contract Address** (`contractAddress`)

| Platform ID | `platformId` | options | ethereum | ✓ | The ID of the platform issuing tokens |  |

**Platform ID options:**

* **Ethereum** (`ethereum`)

| Contract Address | `contractAddress` | string |  | ✓ | Token's contract address |  |
| Base Currency Name or ID | `baseCurrency` | options |  | ✓ | The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Quote Currency Name or ID | `quoteCurrency` | options |  | ✓ | The second currency in the pair. For BTC:ETH this is ETH. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Range (Days) | `days` | options |  | ✓ | Return data for this many days in the past from now |  |

**Range (Days) options:**

* **1** (`1`)
* **7** (`7`)
* **14** (`14`)
* **30** (`30`)
* **90** (`90`)
* **180** (`180`)
* **365** (`365`)
* **Max** (`max`)


### Price parameters (`price`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Search By | `searchBy` | options | coinId | ✓ | Search by coin ID or contract address |  |

**Search By options:**

* **Coin ID** (`coinId`)
* **Contract Address** (`contractAddress`)

| Base Currency Names or IDs | `baseCurrencies` | multiOptions | [] | ✓ | The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. bitcoin |  |
| Platform ID | `platformId` | options | ethereum | ✓ | The ID of the platform issuing tokens |  |

**Platform ID options:**

* **Ethereum** (`ethereum`)

| Contract Addresses | `contractAddresses` | string |  | ✓ | The contract address of tokens, comma-separated |  |
| Quote Currency Names or IDs | `quoteCurrencies` | multiOptions | [] | ✓ | The second currency in the pair. For BTC:ETH this is ETH. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include 24hr Change | `include_24hr_change` | boolean | False |  |
| Include 24hr Vol | `include_24hr_vol` | boolean | False |  |
| Include Last Updated At | `include_last_updated_at` | boolean | False |  |
| Include Market Cap | `include_market_cap` | boolean | False |  |

</details>


### Ticker parameters (`ticker`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Coin Name or ID | `coinId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. bitcoin |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Filter results by exchange IDs. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exchange Names or IDs | `exchange_ids` | multiOptions | [] | Filter results by exchange IDs. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Include Exchange Logo | `include_exchange_logo` | boolean | False |  |
| Order | `order` | options | trust_score_desc | Sorts results by the selected rule |

</details>


---

## Load Options Methods

- `getCurrencies`
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
* Categories: Productivity, Finance & Accounting

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: coinGecko
displayName: CoinGecko
description: Consume CoinGecko API
version: '1'
nodeType: regular
group:
- output
operations:
- id: candlestick
  name: Candlestick
  description: Get a candlestick open-high-low-close chart for the selected currency
  params:
  - id: baseCurrency
    name: Base Currency Name or ID
    type: options
    default: ''
    required: true
    description: The first currency in the pair. For BTC:ETH this is BTC. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id007
      required: true
      displayOptions:
        show:
          operation:
          - marketChart
          resource:
          - coin
          searchBy:
          - coinId
        hide:
          searchBy:
          - contractAddress
    typeInfo: &id008
      type: options
      displayName: Base Currency Name or ID
      name: baseCurrency
      typeOptions:
        loadOptionsMethod: getCoins
      possibleValues: []
  - id: quoteCurrency
    name: Quote Currency Name or ID
    type: options
    default: ''
    required: true
    description: The second currency in the pair. For BTC:ETH this is ETH. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id015
      required: true
      displayOptions:
        show:
          operation:
          - candlestick
          - marketChart
          resource:
          - coin
    typeInfo: &id016
      type: options
      displayName: Quote Currency Name or ID
      name: quoteCurrency
      typeOptions:
        loadOptionsMethod: getCurrencies
      possibleValues: []
  - id: days
    name: Range (Days)
    type: options
    default: ''
    required: true
    description: Return data for this many days in the past from now
    validation: &id017
      required: true
      displayOptions:
        show:
          operation:
          - marketChart
          - candlestick
          resource:
          - coin
    typeInfo: &id018
      type: options
      displayName: Range (Days)
      name: days
      possibleValues:
      - value: '1'
        name: '1'
        description: ''
      - value: '7'
        name: '7'
        description: ''
      - value: '14'
        name: '14'
        description: ''
      - value: '30'
        name: '30'
        description: ''
      - value: '90'
        name: '90'
        description: ''
      - value: '180'
        name: '180'
        description: ''
      - value: '365'
        name: '365'
        description: ''
      - value: max
        name: Max
        description: ''
- id: get
  name: Get
  description: Get current data for a coin
  params:
  - id: searchBy
    name: Search By
    type: options
    default: coinId
    required: true
    description: Search by coin ID or contract address
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - get
          - marketChart
          - price
          resource:
          - coin
    typeInfo: &id010
      type: options
      displayName: Search By
      name: searchBy
      possibleValues:
      - value: coinId
        name: Coin ID
        description: ''
      - value: contractAddress
        name: Contract Address
        description: ''
  - id: coinId
    name: Coin Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: bitcoin
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - ticker
          - history
          resource:
          - coin
    typeInfo: &id006
      type: options
      displayName: Coin Name or ID
      name: coinId
      typeOptions:
        loadOptionsMethod: getCoins
      possibleValues: []
  - id: platformId
    name: Platform ID
    type: options
    default: ethereum
    required: true
    description: The ID of the platform issuing tokens
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - get
          - marketChart
          - price
          resource:
          - coin
          searchBy:
          - contractAddress
    typeInfo: &id012
      type: options
      displayName: Platform ID
      name: platformId
      possibleValues:
      - value: ethereum
        name: Ethereum
        description: ''
  - id: contractAddress
    name: Contract Address
    type: string
    default: ''
    required: true
    description: Token's contract address
    validation: &id013
      required: true
      displayOptions:
        show:
          operation:
          - get
          - marketChart
          resource:
          - coin
          searchBy:
          - contractAddress
    typeInfo: &id014
      type: string
      displayName: Contract Address
      name: contractAddress
- id: getAll
  name: Get Many
  description: Get many coins
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id001
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - event
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
          operation:
          - getAll
          resource:
          - event
          returnAll:
          - false
    typeInfo: &id004
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
- id: history
  name: History
  description: Get historical data (name, price, market, stats) at a given date for
    a coin
  params:
  - id: coinId
    name: Coin Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: bitcoin
    validation: *id005
    typeInfo: *id006
  - id: date
    name: Date
    type: dateTime
    default: ''
    required: true
    description: The date of data snapshot
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - history
          resource:
          - coin
    typeInfo:
      type: dateTime
      displayName: Date
      name: date
- id: market
  name: Market
  description: Get prices and market related data for all trading pairs that match
    the selected currency
  params:
  - id: baseCurrency
    name: Base Currency Name or ID
    type: options
    default: ''
    required: true
    description: The first currency in the pair. For BTC:ETH this is BTC. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
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
- id: marketChart
  name: Market Chart
  description: Get historical market data include price, market cap, and 24h volume
    (granularity auto)
  params:
  - id: searchBy
    name: Search By
    type: options
    default: coinId
    required: true
    description: Search by coin ID or contract address
    validation: *id009
    typeInfo: *id010
  - id: platformId
    name: Platform ID
    type: options
    default: ethereum
    required: true
    description: The ID of the platform issuing tokens
    validation: *id011
    typeInfo: *id012
  - id: contractAddress
    name: Contract Address
    type: string
    default: ''
    required: true
    description: Token's contract address
    validation: *id013
    typeInfo: *id014
  - id: baseCurrency
    name: Base Currency Name or ID
    type: options
    default: ''
    required: true
    description: The first currency in the pair. For BTC:ETH this is BTC. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id007
    typeInfo: *id008
  - id: quoteCurrency
    name: Quote Currency Name or ID
    type: options
    default: ''
    required: true
    description: The second currency in the pair. For BTC:ETH this is ETH. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id015
    typeInfo: *id016
  - id: days
    name: Range (Days)
    type: options
    default: ''
    required: true
    description: Return data for this many days in the past from now
    validation: *id017
    typeInfo: *id018
- id: price
  name: Price
  description: Get the current price of any cryptocurrencies in any other supported
    currencies that you need
  params:
  - id: searchBy
    name: Search By
    type: options
    default: coinId
    required: true
    description: Search by coin ID or contract address
    validation: *id009
    typeInfo: *id010
  - id: baseCurrencies
    name: Base Currency Names or IDs
    type: multiOptions
    default: []
    required: true
    description: The first currency in the pair. For BTC:ETH this is BTC. Choose from
      the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    placeholder: bitcoin
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - price
          resource:
          - coin
          searchBy:
          - coinId
    typeInfo:
      type: multiOptions
      displayName: Base Currency Names or IDs
      name: baseCurrencies
      typeOptions:
        loadOptionsMethod: getCoins
      possibleValues: []
  - id: platformId
    name: Platform ID
    type: options
    default: ethereum
    required: true
    description: The ID of the platform issuing tokens
    validation: *id011
    typeInfo: *id012
  - id: contractAddresses
    name: Contract Addresses
    type: string
    default: ''
    required: true
    description: The contract address of tokens, comma-separated
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - price
          resource:
          - coin
          searchBy:
          - contractAddress
    typeInfo:
      type: string
      displayName: Contract Addresses
      name: contractAddresses
  - id: quoteCurrencies
    name: Quote Currency Names or IDs
    type: multiOptions
    default: []
    required: true
    description: The second currency in the pair. For BTC:ETH this is ETH. Choose
      from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - price
          resource:
          - coin
    typeInfo:
      type: multiOptions
      displayName: Quote Currency Names or IDs
      name: quoteCurrencies
      typeOptions:
        loadOptionsMethod: getCurrencies
      possibleValues: []
- id: ticker
  name: Ticker
  description: Get coin tickers
  params:
  - id: coinId
    name: Coin Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: bitcoin
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
  - field: coinId
    text: bitcoin
  - field: coinId
    text: bitcoin
  - field: baseCurrencies
    text: bitcoin
  - field: options
    text: Add option
  - field: options
    text: Add Field
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: options
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/coinGecko.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CoinGecko Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "candlestick",
        "get",
        "getAll",
        "history",
        "market",
        "marketChart",
        "price",
        "ticker"
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
            "coin",
            "event"
          ],
          "default": "coin"
        },
        "operation": {
          "description": "Get many events",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "getAll"
        },
        "searchBy": {
          "description": "Search by coin ID or contract address",
          "type": "string",
          "enum": [
            "coinId",
            "contractAddress"
          ],
          "default": "coinId"
        },
        "coinId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": "",
          "examples": [
            "bitcoin"
          ]
        },
        "baseCurrency": {
          "description": "The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "baseCurrencies": {
          "description": "The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": [],
          "examples": [
            "bitcoin"
          ]
        },
        "platformId": {
          "description": "The ID of the platform issuing tokens",
          "type": "string",
          "enum": [
            "ethereum"
          ],
          "default": "ethereum"
        },
        "contractAddress": {
          "description": "Token's contract address",
          "type": "string",
          "default": ""
        },
        "contractAddresses": {
          "description": "The contract address of tokens, comma-separated",
          "type": "string",
          "default": ""
        },
        "quoteCurrency": {
          "description": "The second currency in the pair. For BTC:ETH this is ETH. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "quoteCurrencies": {
          "description": "The second currency in the pair. For BTC:ETH this is ETH. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "days": {
          "description": "Return data for this many days in the past from now",
          "type": "string",
          "enum": [
            "1",
            "7",
            "14",
            "30",
            "90",
            "180",
            "365",
            "max"
          ],
          "default": ""
        },
        "date": {
          "description": "The date of data snapshot",
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
        "options": {
          "description": "Country code of event. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
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
| 1 | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
