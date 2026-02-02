# ==========================================
# 1️⃣ Creating Lists
# ==========================================

numbers = [1, 2, 3]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "Python", True, 3.14]

print(numbers)
# Output: [1, 2, 3]

print(names)
# Output: ['Alice', 'Bob', 'Charlie']

print(mixed)
# Output: [1, 'Python', True, 3.14]


# ==========================================
# 2️⃣ Indexing Lists
# ==========================================

print(numbers[0])
# First element
# Output: 1

print(numbers[-1])
# Last element using negative index
# Output: 3


# ==========================================
# 3️⃣ Slicing Lists
# ==========================================

nums = [10, 20, 30, 40, 50]

print(nums[1:4])
# From index 1 to 3
# Output: [20, 30, 40]

print(nums[:3])
# From start to index 2
# Output: [10, 20, 30]

print(nums[2:])
# From index 2 to end
# Output: [30, 40, 50]

print(nums[:])
# Full list copy
# Output: [10, 20, 30, 40, 50]

print(nums[::2])
# Step slicing (every 2nd element)
# Output: [10, 30, 50]

print(nums[::-1])
# Reverse list
# Output: [50, 40, 30, 20, 10]


# ==========================================
# 4️⃣ List Methods
# ==========================================

fruits = ["Apple", "Banana"]

# append()
fruits.append("Orange")
print(fruits)
# Adds element at end
# Output: ['Apple', 'Banana', 'Orange']


# extend()
fruits.extend(["Mango", "Grapes"])
print(fruits)
# Adds multiple elements
# Output: ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes']


# insert()
fruits.insert(1, "Pineapple")
print(fruits)
# Insert at index 1
# Output: ['Apple', 'Pineapple', 'Banana', 'Orange', 'Mango', 'Grapes']


# remove()
fruits.remove("Banana")
print(fruits)
# Removes first occurrence of 'Banana'
# Output: ['Apple', 'Pineapple', 'Orange', 'Mango', 'Grapes']


# pop()
fruits.pop()
print(fruits)
# Removes last element
# Output: ['Apple', 'Pineapple', 'Orange', 'Mango']

fruits.pop(1)
print(fruits)
# Removes element at index 1
# Output: ['Apple', 'Orange', 'Mango']


# ==========================================
# 5️⃣ List Comprehensions
# ==========================================

numbers = [1, 2, 3, 4, 5]

# Basic
doubled = [x * 2 for x in numbers]
print(doubled)
# Multiply each element by 2
# Output: [2, 4, 6, 8, 10]


# With condition
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
# Keep only even numbers
# Output: [2, 4]


# With if-else
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(labels)
# Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# Nested List Comprehension
matrix = [[1, 2], [3, 4]]

flat = [num for row in matrix for num in row]
print(flat)
# Flatten 2D list
# Output: [1, 2, 3, 4]
