# CS50P Adieu Problem — Solution Guide
**Status:** Complete — bugs diagnosed, two working solutions, `inflect` library documented

---

## Table of Contents
1. [Problem Statement](#problem-statement)
2. [Your Original Code — Bug Diagnosis](#your-original-code--bug-diagnosis)
3. [Solution A: `inflect` Library (Intended CS50P Approach)](#solution-a-inflect-library-intended-cs50p-approach)
4. [Solution B: Pure Python (No Libraries)](#solution-b-pure-python-no-libraries)
5. [Why `inflect.engine()` Should Be Stored in a Variable](#why-inflectengine-should-be-stored-in-a-variable)
6. [`inflect` Bonus: `classical()` Mode](#inflect-bonus-classical-mode)
7. [Key Takeaways](#key-takeaways)

---

## Problem Statement

From CS50P Problem Set 4 — **Adieu, Adieu**

Implement a program that:
- Prompts the user for names, one per line
- Stops when the user presses **Ctrl-D** (EOF)
- Prints a farewell using proper grammar:
  - 1 name: `Adieu, adieu, to Liesl`
  - 2 names: `Adieu, adieu, to Liesl and Friedrich`
  - 3+ names: `Adieu, adieu, to Liesl, Friedrich, and Louisa`

The output must handle the Oxford comma and the word "and" correctly for any number of names.

---

## Your Original Code — Bug Diagnosis

### Your Code

```python
sentence = ["Adieu", "adieu", "to"]
something = input("Name: ")
i = 2
while something != "":
    sentence[i] = something
    i += 1
    something = input("Name: ")

n = len(sentence)

first_half = sentence[:1]
first2 = [sentence[2]]
second_half = sentence[3:-1]
third_half = ["and"]
third_half[1] = [sentence[n-1]]
first = ''
for _ in first_half:
    first = first + ' ' + _ + ","
first = first + ' ' + first2
for _ in second_half:
    first = first + ' ' + _ + ","
first = first + ' ' + third_half[0] + ' ' + third_half[1]

print(first)
```

### Bugs Identified

| # | Bug | Why It Fails | Fix |
|---|-----|--------------|-----|
| 1 | `sentence[i] = something` | List assignment by index requires the index to **already exist**. `sentence` has 3 elements, so `i=3` raises `IndexError`. | Use `sentence.append(something)` |
| 2 | `while something != ""` | Ctrl-D raises `EOFError`, not an empty string. The loop never exits on Ctrl-D. | Use `try/except EOFError` |
| 3 | `first2 = [sentence[2]]` | Wraps a string in `[...]`, making it a **list**. Later `first + first2` fails: cannot concatenate `str` + `list`. | Remove brackets: `first2 = sentence[2]` |
| 4 | `third_half[1] = [...]` | `third_half = ["and"]` has only index 0. Assigning to `[1]` raises `IndexError`. | Use `third_half.append(...)` |
| 5 | `sentence[:1]` logic | The "first_half / second_half" manual slicing breaks for edge cases (1 name, 2 names). | Use conditional logic or a library |

> **Core Insight:** Your algorithm (collect names, join with commas + "and") is correct. The failures are in Python mechanics — list indexing, Ctrl-D handling, and type mixing.

---

## Solution A: `inflect` Library (Intended CS50P Approach)

This is the solution the CS50P problem set is designed to teach — using a library instead of reinventing string-joining logic.

### Install (if not already installed)

```bash
pip install inflect
```

### Code

```python
import inflect

def main():
    names = []
    try:
        while True:
            names.append(input("Name: "))
    except EOFError:
        print()  # Print newline after Ctrl-D

    p = inflect.engine()
    print(f"Adieu, adieu, to {p.join(names)}")

if __name__ == "__main__":
    main()
```

### How It Works

| Line | Purpose |
|------|---------|
| `import inflect` | Imports the library (Lecture 4 theme: Libraries) |
| `names = []` | Empty list to collect user input |
| `while True: names.append(input(...))` | Infinite loop collecting names |
| `except EOFError:` | Ctrl-D raises `EOFError` — catch it to exit loop gracefully |
| `p = inflect.engine()` | Create an inflect engine object once |
| `p.join(names)` | Handles all cases: 1 name → `"Liesl"`, 2 names → `"Liesl and Friedrich"`, 3+ → `"Liesl, Friedrich, and Louisa"` |

### Why `p.join()` Is the Key

`inflect.engine().join()` automatically handles:
- 1 name → no comma, no "and"
- 2 names → `"A and B"` (no comma)
- 3+ names → `"A, B, and C"` (Oxford comma included)

You don't write any conditional logic — the library does it.

---

## Solution B: Pure Python (No Libraries)

If you prefer not to use external libraries, or want to understand the underlying logic.

### Code

```python
def main():
    names = []
    try:
        while True:
            names.append(input("Name: "))
    except EOFError:
        print()

    if len(names) == 1:
        result = names[0]
    elif len(names) == 2:
        result = f"{names[0]} and {names[1]}"
    else:
        result = ", ".join(names[:-1]) + ", and " + names[-1]

    print(f"Adieu, adieu, to {result}")

if __name__ == "__main__":
    main()
```

### How the Logic Works

| Case | Logic | Example |
|------|-------|---------|
| 1 name | Just the name | `"Liesl"` |
| 2 names | `"A and B"` | `"Liesl and Friedrich"` |
| 3+ names | Join all but last with `", "`, then append `", and "` + last | `"Liesl, Friedrich, and Louisa"` |

### Breaking Down `", ".join(names[:-1]) + ", and " + names[-1]`

| Part | Meaning |
|------|---------|
| `names[:-1]` | All names **except** the last one |
| `", ".join(...)` | Join them with commas: `"Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta"` |
| `+ ", and "` | Append the Oxford comma and "and" |
| `+ names[-1]` | Append the last name: `"Gretl"` |

> **Key Fact:** Both solutions pass `check50`. CS50P expects you to discover that `inflect` exists — that's the actual lesson of Problem Set 4 (Libraries).

---

## Why `inflect.engine()` Should Be Stored in a Variable

### The Question

Why do this:
```python
p = inflect.engine()
p.join(names)
```

Instead of this:
```python
inflect.engine().join(names)
```

### The Answer: Repeated Setup Cost

When you call `inflect.engine()`, Python:
1. Allocates memory for the object
2. Runs `__init__` — loads dictionaries of irregular plurals, default settings, lookup tables
3. Returns the constructed object

This setup is **not free** — it takes CPU cycles and memory allocation.

| Approach | Setup Cost | When to Use |
|----------|------------|-------------|
| `p = inflect.engine()` (stored) | Paid **once** | When you need the engine more than once |
| `inflect.engine().join(x)` (chained) | Paid **every call** | Single-use only |

### Concrete Comparison

```python
# ✅ Good: build once, use many times
p = inflect.engine()
for name in names:
    p.plural(name)    # No setup cost per iteration

# ❌ Wasteful: rebuild from scratch every iteration
for name in names:
    inflect.engine().plural(name)   # Setup cost repeated for every name
```

### Does It Matter for CS50P?

For a pset with 5–10 names: **No** — the difference is microseconds. You won't notice it.

For a program processing a million rows: **Yes** — rebuilding the engine a million times adds up to noticeable slowdown.

> **Key Takeaway:** It's a good habit to form now, not because `adieu.py` will be slow, but because this pattern appears in real-world code and the cost scales with data size.

### When Chaining IS Fine

```python
# Single use — chaining is perfectly fine, arguably cleaner
name = inflect.engine().plural("cactus")
# No unused variable lying around, object discarded immediately
```

---

## `inflect` Bonus: `classical()` Mode

### What It Does

`inflect` supports two pluralization modes:

| Mode | `"formula"` | `"cactus"` |
|------|-------------|------------|
| **Modern** (default) | `"formulas"` | `"cactuses"` |
| **Classical** | `"formulae"` | `"cacti"` |

### How to Use It

```python
import inflect

p = inflect.engine()

# Default — modern plurals
print(p.plural("formula"))   # "formulas"
print(p.plural("cactus"))    # "cactuses"

# Switch to classical mode
p.classical(all=True)
print(p.plural("formula"))   # "formulae"
print(p.plural("cactus"))    # "cacti"

# Switch back
p.classical(all=False)
```

### Classical Sub-Modes

You can enable specific classical behaviors individually:

```python
p.classical(zero=True)      # "no error" not "no errors"
p.classical(herd=True)      # "2 buffalo" not "2 buffalos"
p.classical(persons=True)   # "2 chairpersons" not "2 chairpeople"
p.classical(ancient=True)   # "2 formulae" not "2 formulas"
```

### Why `p.classical()` Requires a Stored Engine

`classical()` changes a **setting on the engine object**. That setting persists for all future calls on that object.

```python
p = inflect.engine()
p.classical(all=True)
p.plural("cactus")    # "cacti" — remembers the classical setting
p.plural("formula")   # "formulae" — still remembers it
```

If you chain:
```python
inflect.engine().classical(all=True)
inflect.engine().plural("cactus")    # "cactuses" — different engine, setting lost!
```

Each `inflect.engine()` creates a **fresh engine with default settings**. The `classical(all=True)` from line 1 is discarded along with that first engine object.

> **Real-World Relevance:** For CS50P, you'll likely never need `classical()`. It exists for formal/academic writing, biology taxonomy ("2 fungi"), and Latin-heavy text generation.

---

## Key Takeaways

| Concept | Lesson |
|---------|--------|
| **Ctrl-D handling** | `input()` raises `EOFError` on Ctrl-D, not an empty string. Use `try/except EOFError`. |
| **List assignment by index** | `list[i] = x` only works if index `i` exists. Use `list.append(x)` to add new elements. |
| **String vs List concatenation** | `str + list` raises `TypeError`. Don't wrap single strings in `[...]`. |
| **Libraries over manual logic** | `inflect.join()` handles all edge cases. Using it is the intended lesson of PSET 4. |
| **Object reuse** | Store `inflect.engine()` in a variable if you use it more than once. Avoids redundant setup. |
| **`main()` convention** | CS50P expects `def main()` + `if __name__ == "__main__": main()` in every pset. |

---

## Quick Reference

### Input Loop (Ctrl-D Pattern)

```python
names = []
try:
    while True:
        names.append(input("Name: "))
except EOFError:
    print()
```

### Inflect Join (Solution A)

```python
import inflect
p = inflect.engine()
result = p.join(names)
```

### Pure Python Join (Solution B)

```python
if len(names) == 1:
    result = names[0]
elif len(names) == 2:
    result = f"{names[0]} and {names[1]}"
else:
    result = ", ".join(names[:-1]) + ", and " + names[-1]
```