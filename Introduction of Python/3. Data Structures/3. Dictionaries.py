# ==========================================
# 1️⃣ Creating Dictionaries
# ==========================================

# Basic dictionary
student = {
    "name": "Frank",
    "age": 22,
    "course": "Computer Science"
}

print(student)
# Output: {'name': 'Frank', 'age': 22, 'course': 'Computer Science'}


# ==========================================
# 2️⃣ Accessing Values
# ==========================================

print(student["name"])
# Access value using key
# Output: Frank

print(student.get("age"))
# Using get() method
# Output: 22

print(student.get("grade"))
# If key doesn't exist, returns None (no error)
# Output: None


# ==========================================
# 3️⃣ Adding and Modifying Items
# ==========================================

# Add new key-value pair
student["grade"] = "A"
print(student)
# Output: {'name': 'Frank', 'age': 22, 'course': 'Computer Science', 'grade': 'A'}

# Modify existing value
student["age"] = 23
print(student)
# Output: age updated to 23


# ==========================================
# 4️⃣ Deleting Items
# ==========================================

# Using del
del student["grade"]
print(student)
# 'grade' key removed

# Using pop()
removed = student.pop("course")
print(removed)
# Output: Computer Science

print(student)
# 'course' removed


# ==========================================
# 5️⃣ Dictionary Methods
# ==========================================

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person.keys())
# Returns all keys
# Output: dict_keys(['name', 'age', 'city'])

print(person.values())
# Returns all values
# Output: dict_values(['Alice', 25, 'New York'])

print(person.items())
# Returns key-value pairs as tuples
# Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])


# Loop through dictionary
for key, value in person.items():
    print(key, value)
# Output:
# name Alice
# age 25
# city New York


# ==========================================
# 6️⃣ Dictionary Comprehension
# ==========================================

# Basic dictionary comprehension
numbers = [1, 2, 3, 4, 5]

squares = {x: x**2 for x in numbers}
print(squares)
# Creates dictionary with number and its square
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# With condition
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(even_squares)
# Keeps only even numbers
# Output: {2: 4, 4: 16}


# Using existing dictionary
prices = {"apple": 100, "banana": 50, "orange": 80}

discounted = {key: value * 0.9 for key, value in prices.items()}
print(discounted)
# Applies 10% discount
# Output: {'apple': 90.0, 'banana': 45.0, 'orange': 72.0}
