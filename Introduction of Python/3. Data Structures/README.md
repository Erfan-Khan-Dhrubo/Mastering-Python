# 📘 Data Structures

This folder contains Python examples that demonstrate **lists, tuples, dictionaries, and sets**—the core built-in data structures for organizing and storing data.

---

## 📄 Lists

This file covers:

- Creating lists (numbers, strings, mixed types)
- Indexing lists (positive and negative indices)
- Slicing lists (`[start:end]`, `[:end]`, `[start:]`, `[:]`, step slicing)
- Reversing lists with `[::-1]`
- List methods:
  - `append()` — add element at end
  - `extend()` — add multiple elements
  - `insert()` — insert at index
  - `remove()` — remove first occurrence
  - `pop()` — remove by index or last element
- List comprehensions:
  - Basic form `[expr for x in iterable]`
  - With condition `[x for x in iterable if condition]`
  - With if-else `[a if cond else b for x in iterable]`
  - Nested list comprehensions (e.g., flattening a matrix)

---

## 📄 Tuples

This file covers:

- Creating tuples (basic, mixed types)
- Single-element tuple syntax (comma required: `(5,)`)
- Accessing tuples via indexing and slicing
- Tuple unpacking (assigning to multiple variables)
- Star unpacking (`first, *middle, last`) for capturing remaining elements
- Immutability (tuples cannot be changed after creation)
- Modifying mutable objects inside a tuple (e.g., list in tuple)
- Tuple methods: `count()` and `index()`

---

## 📄 Dictionaries

This file covers:

- Creating dictionaries (key-value pairs)
- Accessing values by key (`dict["key"]`) and with `get()` (safe, returns `None` if missing)
- Adding and modifying key-value pairs
- Deleting items with `del` and `pop()`
- Dictionary methods:
  - `keys()` — all keys
  - `values()` — all values
  - `items()` — key-value pairs as tuples
- Looping through dictionaries with `for key, value in dict.items()`
- Dictionary comprehensions:
  - Basic `{key: value for x in iterable}`
  - With condition and transforming existing dictionaries

---

## 📄 Sets

This file covers:

- Creating sets (curly braces and `set()` from iterables)
- Automatic removal of duplicates
- Add and remove: `add()`, `remove()` (error if missing), `discard()` (no error)
- Set operations:
  - Union (`|` or `union()`) — all unique elements
  - Intersection (`&` or `intersection()`) — common elements
  - Difference (`-`) — elements in one set but not the other
  - Symmetric difference (`^`) — elements in either set but not both
- Membership checking with `in` and `not in`
- Looping through sets (order not guaranteed)
- Set comprehensions (e.g., `{x**2 for x in range(5)}`)
