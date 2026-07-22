# Python `emoji` Module — Complete Reference
**Status:** ~85% complete — core functions documented; some advanced edge cases and library internals need further exploration

---

## Table of Contents
1. [Overview](#overview)
2. [Core Functions](#core-functions)
   - [`emojize()` — Text to Emoji](#emojize--text-to-emoji)
   - [`demojize()` — Emoji to Text](#demojize--emoji-to-text)
   - [`emoji_list()` — Locate Emojis in a String](#emoji_list--locate-emojis-in-a-string)
   - [`replace_emoji()` — Remove or Replace Emojis](#replace_emoji--remove-or-replace-emojis)
   - [`is_emoji()` — Validate a Character](#is_emoji--validate-a-character)
   - [`emoji_count()` — Count Emojis](#emoji_count--count-emojis)
3. [Data Structures](#data-structures)
   - [`EMOJI_DATA` Dictionary](#emoji_data-dictionary)
4. [Understanding Emoji Length & Indices](#understanding-emoji-length--indices)
5. [Common Errors & Fixes](#common-errors--fixes)
6. [Multilingual Support](#multilingual-support)
7. [Practical Examples](#practical-examples)

---

## Overview

The `emoji` Python library handles conversion between emoji characters and their text shortcodes, plus utilities for locating, counting, and manipulating emojis in strings.

**Installation:**
```bash
pip install emoji
```

**Import:**
```python
import emoji
```

---

## Core Functions

### `emojize()` — Text to Emoji

Converts text shortcodes into actual emoji characters.

**Syntax:**
```python
emoji.emojize(string, language='en', delimiters=(':', ':'))
```

| Parameter | Purpose | Default |
|-----------|---------|---------|
| `string` | Text containing shortcodes to convert | Required |
| `language` | Shortcode language: `'en'` (official names), `'alias'` (aliases), or language codes like `'es'`, `'fr'` | `'en'` |
| `delimiters` | Characters wrapping shortcodes | `(':', ':')` |

**Key Difference — `language='en'` vs `language='alias'`:**

| Setting | Works For | Example |
|---------|-----------|---------|
| `language='en'` (default) | Official Unicode names only | `:thumbs_up:` ✅, `:thumbsup:` ❌ |
| `language='alias'` | Both official names and aliases | `:thumbs_up:` ✅, `:thumbsup:` ✅ |

**Example:**
```python
import emoji

# Default — only official names
print(emoji.emojize("Python is :thumbs_up:"))
# Output: Python is 👍

# With aliases enabled
print(emoji.emojize("Python is :thumbsup:", language='alias'))
# Output: Python is 👍
```

> **Tricky Doubt:** Why doesn't `:thumbsup:` work by default? The library follows Unicode Consortium naming. `:thumbs_up:` is the official name. `:thumbsup:` is a non-standard alias used by platforms like Slack and Discord. Pass `language='alias'` to enable these alternative shortcodes.

---

### `demojize()` — Emoji to Text

Converts emoji characters back into their text shortcodes.

**Syntax:**
```python
emoji.demojize(string, language='en', delimiters=(':', ':'))
```

**Example:**
```python
import emoji

text = emoji.demojize("Python is 👍")
print(text)
# Output: Python is :thumbs_up:
```

**Use case:** Data processing, text analytics, or storing emojis as readable text in databases.

---

### `emoji_list()` — Locate Emojis in a String

Finds all emojis in a string and returns their exact positions and characters.

**Syntax:**
```python
emoji.emoji_list(string)
```

**Returns:** A list of dictionaries, each containing:

| Key | Meaning |
|-----|---------|
| `match_start` | Index where the emoji begins (inclusive) |
| `match_end` | Index where the emoji ends (exclusive) |
| `emoji` | The actual emoji character(s) found |

**Example:**
```python
import emoji

text = "Python is 👍 and very 🚀!"

results = emoji.emoji_list(text)
print(results)
# Output: [
#     {'match_start': 10, 'match_end': 11, 'emoji': '👍'},
#     {'match_start': 21, 'match_end': 22, 'emoji': '🚀'}
# ]
```

**Why `match_end` exists — complex emojis span multiple indices:**

| Emoji Type | Characters | Python Length |
|------------|------------|---------------|
| Simple emoji (`👍`) | 1 character | `match_end - match_start = 1` |
| Skin tone modifier (`👍🏽`) | 2 characters (base + skin tone) | `match_end - match_start = 2` |
| Country flag (`🇺🇸`) | 2 regional indicators | `match_end - match_start = 2` |
| ZWJ family (`👨‍👩‍👧‍👦`) | 7 characters (4 people + 3 ZWJs) | `match_end - match_start = 7` |

```python
import emoji

text = "👍 🇺🇸 👨‍👩‍👧‍👦"

for item in emoji.emoji_list(text):
    length = item['match_end'] - item['match_start']
    print(f"Emoji: {item['emoji']} | Length: {length}")

# Output:
# Emoji: 👍 | Length: 1
# Emoji: 🇺🇸 | Length: 2
# Emoji: 👨‍👩‍👧‍👦 | Length: 7
```

> **Common Misconception:** "An emoji is always one character." This is false for flags, skin tones, and ZWJ sequences. Using `match_end - match_start` is the only safe way to determine emoji length.

**Practical use — extract metadata for all emojis in text:**
```python
import emoji

text = 'welcome to jungle 👍 🇺🇸 👨‍👩‍👧‍👦'

found_emojis = emoji.emoji_list(text)

for item in found_emojis:
    char = item['emoji']
    metadata = emoji.EMOJI_DATA[char]
    print(f"Emoji: {char} | Shortcode: {metadata['en']}")
```

---

### `replace_emoji()` — Remove or Replace Emojis

Strips emojis from text or replaces them with a specified string.

**Syntax:**
```python
emoji.replace_emoji(string, replace='')
```

| Parameter | Purpose |
|-----------|---------|
| `string` | Text to process |
| `replace` | String to insert in place of each emoji (default: empty string = remove) |

**Example:**
```python
import emoji

text = "Welcome to the jungle 🦁🌴!"
clean = emoji.replace_emoji(text, replace="")
print(clean)
# Output: Welcome to the jungle !

labeled = emoji.replace_emoji(text, replace="[EMOJI]")
print(labeled)
# Output: Welcome to the jungle [EMOJI][EMOJI]!
```

---

### `is_emoji()` — Validate a Character

Checks whether a single character or string is exactly one emoji.

**Syntax:**
```python
emoji.is_emoji(char)
```

**Returns:** `True` or `False`

**Example:**
```python
import emoji

print(emoji.is_emoji("👍"))   # True
print(emoji.is_emoji("A"))    # False
print(emoji.is_emoji("ab"))   # False (string of two non-emoji chars)
```

---

### `emoji_count()` — Count Emojis

Returns the number of emojis in a string.

**Syntax:**
```python
emoji.emoji_count(string)
```

**Example:**
```python
import emoji

text = "Hello! 👋0️⃣🚀"
print(emoji.emoji_count(text))
# Output: 3
```

---

## Data Structures

### `EMOJI_DATA` Dictionary

A dictionary where:
- **Keys** are single emoji characters (e.g., `"👍"`)
- **Values** are dictionaries containing metadata

**Access pattern:**
```python
import emoji

metadata = emoji.EMOJI_DATA["👍"]
print(metadata)
```

**Metadata structure:**
```python
{
    'en': ':thumbs_up:',           # English shortcode
    'status': 2,                   # Fully-qualified emoji status
    'E': 0.6,                      # Emoji presentation score
    'alias': [':thumbsup:', '+1'], # Alternative shortcodes
    'es': ':pulgar_hacia_arriba:', # Spanish
    'fr': ':pouce_vers_le_haut:',  # French
    # ... more languages
}
```

**Useful operations:**

| Task | Code |
|------|------|
| Count total emojis | `len(emoji.EMOJI_DATA)` |
| Look up a character | `emoji.EMOJI_DATA[char]` |
| Check if char is in dict | `char in emoji.EMOJI_DATA` |
| Search by keyword | Loop through and check `data['en']` |

**Search by keyword example:**
```python
import emoji

keyword = "heart"
for char, data in emoji.EMOJI_DATA.items():
    if keyword in data['en']:
        print(f"{char} -> {data['en']}")
```

> **Common Error:** `TypeError: 'dict' object is not callable` — You used parentheses `EMOJI_DATA()` instead of square brackets `EMOJI_DATA[char]`. Dictionaries are accessed with `[]`, not `()`.

> **Common Error:** `KeyError` — You tried to look up an entire sentence or a non-emoji string in the dictionary. Keys must be individual emoji characters. Extract emojis first with `emoji_list()`, then look them up.

---

## Understanding Emoji Length & Indices

### Why `match_end` Is Not Always `match_start + 1`

Emojis in Unicode can be composed of multiple code points:

| Composition | Characters | Example | Length |
|-------------|------------|---------|--------|
| Base emoji | 1 | `👍` | 1 |
| Base + skin tone modifier | 2 | `👍🏽` | 2 |
| Flag (regional indicators) | 2 | `🇺🇸` | 2 |
| ZWJ sequence (family) | Up to 7+ | `👨‍👩‍👧‍👦` | 7 |
| Keycap sequence | 2+ZWJ | `0️⃣` | 3 |

### Zero-Width Joiner (ZWJ)

The ZWJ character (`\u200d`) acts as invisible glue, joining separate emojis into a single displayed glyph. Python sees the individual characters; the rendering engine displays them as one image.

> **Key Fact:** Never assume `len(emoji_char) == 1`. Always use `emoji_list()` to safely identify emoji boundaries.

---

## Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `:thumbsup:` not converting | Default `language='en'` doesn't include aliases | Use `language='alias'` |
| `TypeError: 'dict' object is not callable` | Used `EMOJI_DATA()` (parentheses) | Use `EMOJI_DATA[char]` (square brackets) |
| `KeyError` on dictionary lookup | Trying to look up a full sentence | Use `emoji_list()` first, then look up individual chars |
| f-string syntax error with nested quotes | `f"...{emoji.emojize("...")}"` | Use single quotes inside: `f"...{emoji.emojize('...')}"` |

---

## Multilingual Support

The `language` parameter in `emojize()` and `demojize()` supports multiple languages.

```python
import emoji

# Spanish
print(emoji.emojize(":pulgar_hacia_arriba:", language="es"))
# Output: 👍

# French
print(emoji.emojize(":pouce_vers_le_haut:", language="fr"))
# Output: 👍
```

Available languages are stored in each emoji's metadata inside `EMOJI_DATA`.

---

## Practical Examples

### CS50P Emojize Problem — Fixed

```python
import emoji

# Fixed: language='alias' enables :thumbsup:
# Fixed: single quotes inside f-string double quotes
print(f"Output: {emoji.emojize(input('Input: '), language='alias')}")
```

### Extract All Emojis with Metadata

```python
import emoji

text = input("Enter text: ")
found = emoji.emoji_list(text)

for item in found:
    char = item['emoji']
    data = emoji.EMOJI_DATA[char]
    print(f"Emoji: {char}")
    print(f"  English: {data['en']}")
    print(f"  Aliases: {data.get('alias', [])}")
    print()
```

### Remove Emojis for Clean Text Processing

```python
import emoji

raw = "User feedback: Great app! 👍👍👍 Needs dark mode 🌙"
clean = emoji.replace_emoji(raw)
print(clean)
# Output: User feedback: Great app! Needs dark mode
```

---

## Quick Reference

| Function | Purpose | Example |
|----------|---------|---------|
| `emojize(s, language='alias')` | Text → Emoji | `emoji.emojize(':thumbsup:', language='alias')` |
| `demojize(s)` | Emoji → Text | `emoji.demojize('👍')` |
| `emoji_list(s)` | Locate emojis | `emoji.emoji_list('Hello 👍')` |
| `replace_emoji(s, replace='')` | Remove/Replace emojis | `emoji.replace_emoji('Hi 👍', '')` |
| `is_emoji(c)` | Validate character | `emoji.is_emoji('👍')` |
| `emoji_count(s)` | Count emojis | `emoji.emoji_count('a👍b🚀c')` |
| `EMOJI_DATA[c]` | Metadata lookup | `emoji.EMOJI_DATA['👍']['en']` |

---

## Remaining Gaps `[TODO]`

- [ ] How `status` values in `EMOJI_DATA` work — fully-qualified vs. minimally-qualified vs. unqualified emojis
- [ ] The `E` (Emoji Presentation) score — what range means "always emoji" vs. "text default"
- [ ] How the library handles newer Unicode emoji versions — update frequency and backward compatibility
- [ ] Performance comparison: `emoji_list()` vs manual regex for very large text corpora
- [ ] Custom delimiters — using `{ }` or `[ ]` instead of `: :` for shortcodes