# CoinCap API — Bitcoin Price Fetcher in Python
**Status:** ~85% complete — v3 API integration documented; error handling, rate limiting, and CS50 check50 compatibility need practical testing

---

## Table of Contents
1. [What is CoinCap API](#what-is-coincap-api)
2. [Free Tier & API Key Setup](#free-tier--api-key-setup)
3. [API Versions: v2 vs v3](#api-versions-v2-vs-v3)
4. [Authentication Methods](#authentication-methods)
5. [Making Requests in Python](#making-requests-in-python)
6. [Common Errors & Fixes](#common-errors--fixes)
7. [`requests.RequestException` — Error Handling](#requestsrequestexception--error-handling)
8. [CS50P Bitcoin Problem Set Note](#cs50p-bitcoin-problem-set-note)
9. [Quick Reference](#quick-reference)

---

## What is CoinCap API

CoinCap is a free public REST API providing real-time and historical cryptocurrency data for over 1,000 digital assets.

| Feature | Detail |
|---------|--------|
| **Cost** | Free (no credit card required) |
| **Data** | Prices, market cap, supply, 24h change, exchange volumes |
| **Format** | JSON |
| **Update Frequency** | Rolling 24-hour Volume-Weighted Average Price (VWAP) |
| **Use Cases** | Portfolio trackers, price tickers, trading bots, financial dashboards |

### CoinCap vs MetaMask

| | CoinCap API | MetaMask |
|---|-------------|----------|
| **Purpose** | Fetches market data | Stores and manages crypto assets |
| **Holds funds?** | No | Yes (real wallet) |
| **Auth required?** | API key for higher limits | Seed phrase / password |
| **Developer tool** | REST API | JavaScript `window.ethereum` provider |

---

## Free Tier & API Key Setup

1. Go to [coincap.io](https://coincap.io) and create an account.
2. Navigate to the **API Manager** dashboard.
3. Click **Add New Key** to generate your API key.

### Rate Limits

| Tier | Limit |
|------|-------|
| **No API key** | Low, anonymous access only |
| **Free API key** | Higher limits (sufficient for personal projects) |
| **Exceeded?** | Server returns error — `data` key disappears from response |

> **Key Fact:** When rate-limited, CoinCap returns `{"error": "Too Many Requests"}` instead of the normal data structure. This is why `o["data"]` raises `KeyError` — the `"data"` key doesn't exist in error responses.

---

## API Versions: v2 vs v3

| | v2 | v3 |
|---|----|----|
| **Base URL** | `https://api.coincap.io/v2` | `https://rest.coincap.io/v3` |
| **Status** | Legacy, still functional | Active, recommended |
| **Auth method** | Authorization header | Query parameter `?apiKey=` |
| **MCP support** | No | Yes (`/mcp` endpoint for AI agents) |

---

## Authentication Methods

### Method 1: Query Parameter (v3)

API key appended directly to the URL:

```python
url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_KEY"
response = requests.get(url)
```

| Pro | Con |
|-----|-----|
| Simple, works in browser | Key visible in URL — may appear in server logs |

### Method 2: Authorization Header (v2/v3)

API key hidden in HTTP headers:

```python
url = "https://api.coincap.io/v2/assets/bitcoin"
headers = {"Authorization": "Bearer YOUR_KEY"}
response = requests.get(url, headers=headers)
```

| Pro | Con |
|-----|-----|
| Key not in URL — more secure | Slightly more code |

> **Key Fact:** Both methods work. v3 documentation primarily shows query parameter style. Headers are preferred for production code to avoid leaking keys in logs.

---

## Making Requests in Python

### Basic Bitcoin Price Fetch (v3)

```python
import requests

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_KEY"
response = requests.get(url)
o = response.json()
price = float(o["data"]["priceUsd"])
print(f"BTC Price: ${price:,.2f}")
```

### Command-Line Portfolio Calculator

Takes Bitcoin amount as a command-line argument and calculates total value:

```python
import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Usage: python bitcoin.py <amount>")

try:
    units = float(sys.argv[1])
except ValueError:
    sys.exit("Amount must be a number")

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_KEY"
response = requests.get(url)
o = response.json()
price = float(o["data"]["priceUsd"])
print(f"${price * units:,.4f}")
```

### Polling Live Price Sequence

```python
import time
import requests

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_KEY"

while True:
    response = requests.get(url)
    if response.status_code == 200:
        price = float(response.json()["data"]["priceUsd"])
        print(f"[{time.strftime('%H:%M:%S')}] BTC: ${price:,.2f}")
    time.sleep(10)
```

### JSON Response Structure

```json
{
  "data": {
    "id": "bitcoin",
    "rank": "1",
    "symbol": "BTC",
    "name": "Bitcoin",
    "priceUsd": "65906.45728",
    "changePercent24Hr": "1.23",
    "marketCapUsd": "1290000000000",
    "supply": "19500000.000000"
  }
}
```

> **Note:** `priceUsd` is returned as a **string** to avoid floating-point rounding errors. Always cast to `float()` before math operations.

---

## Common Errors & Fixes

### `KeyError: 'data'`

| Cause | Why |
|-------|-----|
| Rate limit exceeded | API returns `{"error": "Too Many Requests"}` — no `"data"` key |
| Invalid API key | Returns error structure instead of normal data |
| Server error | API returns error page, not the expected JSON |

**Fix — check for `"data"` before accessing:**

```python
o = response.json()
if "data" in o:
    price = float(o["data"]["priceUsd"])
else:
    sys.exit(f"API Error: {o.get('error', 'Unknown')}")
```

### `response.raise_for_status()` — HTTP Error Detection

```python
response = requests.get(url)
response.raise_for_status()  # Raises HTTPError on 4xx/5xx status codes
```

This converts HTTP errors (429, 500, 404) into exceptions you can catch.

### `len(sys.argv) < 1` Bug

`sys.argv[0]` is always the script name. Length is never less than 1. Use `len(sys.argv) < 2` to check for missing arguments.

---

## `requests.RequestException` — Error Handling

`requests.RequestException` is the **base exception class** for all errors in the `requests` library. Catching it handles every possible network failure.

### Exception Hierarchy

```
requests.RequestException (base — catches everything below)
├── requests.ConnectionError      # DNS failure, no internet
├── requests.HTTPError            # 4xx/5xx status codes (requires raise_for_status())
├── requests.Timeout              # Server took too long
└── requests.TooManyRedirects     # Infinite redirect loop
```

### Basic Usage

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.RequestException as e:
    sys.exit(f"Network error: {e}")
```

### Granular Error Handling

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

except requests.Timeout:
    sys.exit("Server too slow. Try again.")

except requests.HTTPError as e:
    sys.exit(f"HTTP error: {e}")

except requests.RequestException as e:
    sys.exit(f"Network failure: {e}")
```

| Exception | Trigger |
|-----------|---------|
| `ConnectionError` | DNS failure, Wi-Fi disconnected, server unreachable |
| `HTTPError` | 404, 429 (rate limit), 500 (server crash) — requires `raise_for_status()` |
| `Timeout` | Server didn't respond within specified seconds |
| `TooManyRedirects` | URL redirects in an infinite loop |

---

## CS50P Bitcoin Problem Set Note

The CS50P assignment uses a **different API** than CoinCap:

| | CS50P Official | CoinCap (This Document) |
|---|---|---|
| **Endpoint** | `https://api.coindesk.com/v1/bpi/currentprice.json` | `https://rest.coincap.io/v3/assets/bitcoin` |
| **API key?** | Not required | Required for v3 |
| **JSON path** | `o["bpi"]["USD"]["rate_float"]` | `o["data"]["priceUsd"]` |
| **check50** | Expects CoinDesk endpoint | Will **fail** if using CoinCap |

### CoinDesk Price Fetch

```python
import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()
rate = o["bpi"]["USD"]["rate_float"]
print(f"${rate:,.4f}")
```

---

## Quick Reference

| Task | Code |
|------|------|
| Fetch BTC price (v3) | `requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=KEY")` |
| Access price | `float(o["data"]["priceUsd"])` |
| Check for errors | `response.raise_for_status()` |
| Safe key access | `if "data" in o:` before `o["data"]` |
| Catch all network errors | `except requests.RequestException:` |
| Format as currency | `f"${value:,.2f}"` |
| Polling loop | `while True: ... time.sleep(10)` |

---

## Remaining Gaps `[TODO]`

- [ ] CoinCap WebSocket API for real-time streaming prices — how to use `websockets` library.
- [ ] Historical data endpoint — fetching daily OHLCV data over date ranges.
- [ ] Multi-asset request — fetching prices for multiple cryptocurrencies in a single call.
- [ ] Rate limit exact numbers — how many requests per minute does the free tier allow?
- [ ] CoinCap v3 MCP endpoint — how AI agents consume it via Model Context Protocol.