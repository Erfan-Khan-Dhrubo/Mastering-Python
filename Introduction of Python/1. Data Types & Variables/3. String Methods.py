text = "PythonProgramming"

# ------------------------------
# len()
# ------------------------------
print(len(text))
# Counts total characters → Output: 18


# ------------------------------
# INDEXING
# ------------------------------
print(text[0])
# First character → Output: P

print(text[-1])
# Last character using negative index → Output: g


# ------------------------------
# SLICING (ALL COMMON CASES)
# ------------------------------

print(text[0:6])
# Slice from index 0 to 5 → Output: Python

print(text[6:18])
# Slice from index 6 to end → Output: Programming

print(text[:6])
# Slice from start to index 5 → Output: Python

print(text[6:])
# Slice from index 6 to end → Output: Programming

print(text[:])
# Full string → Output: PythonProgramming

print(text[0:18:2])
# Slice with step 2 → Output: PtoPo rmn

print(text[::2])
# Entire string with step 2 → Output: PtoPo rmn

print(text[::3])
# Step of 3 → Output: PhPgmn

print(text[-11:-1])
# Negative slicing → Output: Programmin

print(text[-11:])
# From negative index to end → Output: Programming

print(text[::-1])
# Reverse string → Output: gnimmargorPnohtyP

print(text[5:0:-1])
# Reverse slice (index 5 to 1) → Output: nohty

print(text[-1:-7:-1])
# Reverse from end → Output: gnimmr


# ------------------------------
# ESCAPE SEQUENCES
# ------------------------------
print("Hello\nPython")
# New line → Output:
# Hello
# Python

print("Python\tProgramming")
# Tab space → Output: Python    Programming

print("He said \"Python\"")
# Escape double quote → Output: He said "Python"


# ------------------------------
# STRING METHODS
# ------------------------------
sample = "  hello python  "

print(sample.strip())
# Removes spaces → Output: hello python

print(sample.upper())
# Uppercase → Output:   HELLO PYTHON

print(sample.lower())
# Lowercase → Output:   hello python

print(sample.title())
# Title case → Output:   Hello Python

print(sample.find("python"))
# Finds index → Output: 8

print(sample.replace("python", "java"))
# Replace text → Output:   hello java


# ------------------------------
# NUMBER FUNCTIONS
# ------------------------------
num = 8.7654
print(round(num, 2))
# Round to 2 decimals → Output: 8.77

negative = -25
print(abs(negative))
# Absolute value → Output: 25
