# 4. Functions & File Operations

This module introduces **functions** (defining, parameters, return values, scope) and **file I/O** (reading, writing, appending) in Python.

---

## Contents

### 1. Functions (`1. Functions.py`)

| Topic                      | Description                                           |
| -------------------------- | ----------------------------------------------------- |
| **Defining functions**     | Using `def` to create and call functions              |
| **Parameters**             | Positional, keyword, and default parameters           |
| **Return values**          | Using `return` to send values back to the caller      |
| **Variable scope**         | Local vs global variables; using the `global` keyword |
| **Multiple return values** | Returning tuples and unpacking multiple values        |

**Concepts covered:**

- `greet()`, `add(a, b)`, `introduce(name, country="Bangladesh")`
- `return x * y` and using returned values
- Accessing global variables inside functions; modifying with `global`
- `return sum_value, product` and `total, multiply_result = calculate(5, 6)`

---

### 2. File Operations (`2. File Operations.py`)

| Topic               | Description                                         |
| ------------------- | --------------------------------------------------- |
| **Opening files**   | Modes: `'r'` (read), `'w'` (write), `'a'` (append)  |
| **Writing**         | `write()` in `'w'` mode (creates/overwrites file)   |
| **Appending**       | `write()` in `'a'` mode (adds at end)               |
| **Reading**         | `read()`, `readline()`, `readlines()` in `'r'` mode |
| **Context manager** | Using `with open(...) as file:` (recommended)       |
| **writelines()**    | Writing a list of strings to a file                 |

**Concepts covered:**

- `open('example.txt', 'r')` and closing with `file.close()`
- `file.read()` (whole file), `file.readline()` (one line), `file.readlines()` (list of lines)
- `with open('example.txt', 'r') as file:` for automatic closing
- `file.writelines(lines)` for writing multiple lines (newlines must be in the strings)

---

## Running the code

From this folder:

```bash
python "1. Functions.py"
python "2. File Operations.py"
```

**Note:** Running `2. File Operations.py` creates `example.txt`, `example2.txt`, and `example3.txt` in the current directory.
