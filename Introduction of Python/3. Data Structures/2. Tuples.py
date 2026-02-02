# ==========================================
# 1️⃣ Creating Tuples
# ==========================================

# Basic tuple
numbers = (1, 2, 3)

# Mixed data types
mixed = (1, "Python", True, 3.14)

# Single element tuple (IMPORTANT: must use comma)
single = (5,)

print(numbers)
# Output: (1, 2, 3)

print(mixed)
# Output: (1, 'Python', True, 3.14)

print(single)
# Output: (5,)


# ==========================================
# 2️⃣ Accessing Tuples (Indexing & Slicing)
# ==========================================

print(numbers[0])
# First element
# Output: 1

print(numbers[-1])
# Last element
# Output: 3

print(numbers[0:2])
# Slicing from index 0 to 1
# Output: (1, 2)


# ==========================================
# 3️⃣ Tuple Unpacking
# ==========================================

person = ("Frank", 22, "Student")

name, age, profession = person

print(name)
# Output: Frank

print(age)
# Output: 22

print(profession)
# Output: Student


# 🔹 Using * (star unpacking)

data = (10, 20, 30, 40, 50)

first, *middle, last = data

print(first)
# Output: 10

print(middle)
# Output: [20, 30, 40]

print(last)
# Output: 50


# ==========================================
# 4️⃣ Understanding Immutability
# ==========================================

nums = (1, 2, 3)

# Tuples CANNOT be changed
# nums[0] = 100   ❌ This will cause an error:
# TypeError: 'tuple' object does not support item assignment

print(nums)
# Output: (1, 2, 3)


# But if tuple contains a mutable object (like list),
# that object CAN be modified

example = (1, [2, 3], 4)

example[1].append(5)

print(example)
# Output: (1, [2, 3, 5], 4)
# The tuple itself is unchanged, but the list inside it changed


# ==========================================
# 5️⃣ Tuple Methods
# ==========================================

values = (1, 2, 2, 3, 4)

print(values.count(2))
# Counts how many times 2 appears
# Output: 2

print(values.index(3))
# Finds index of value 3
# Output: 3
