# ==========================================
# 1️⃣ Creating Sets
# ==========================================

# Basic set
numbers = {1, 2, 3, 4}

# Set automatically removes duplicates
duplicate_numbers = {1, 2, 2, 3, 4, 4}
print(duplicate_numbers)
# Output: {1, 2, 3, 4}

# Creating set using set() function
letters = set(["a", "b", "c", "a"])
print(letters)
# Output: {'a', 'b', 'c'}


# ==========================================
# 2️⃣ Basic Set Operations (Add / Remove)
# ==========================================

fruits = {"apple", "banana"}

# add()
fruits.add("orange")
print(fruits)
# Adds one element

# remove()
fruits.remove("banana")
print(fruits)
# Removes element (error if not found)

# discard()
fruits.discard("mango")
print(fruits)
# Removes element if exists (no error if not found)


# ==========================================
# 3️⃣ Set Operations
# ==========================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (all unique elements from both sets)
print(A | B)
# OR operator
# Output: {1, 2, 3, 4, 5, 6}

print(A.union(B))
# Same as above


# Intersection (common elements)
print(A & B)
# AND operator
# Output: {3, 4}

print(A.intersection(B))
# Same result


# Difference (elements in A but not in B)
print(A - B)
# Output: {1, 2}

print(B - A)
# Output: {5, 6}


# Symmetric Difference (elements in A or B but not both)
print(A ^ B)
# Output: {1, 2, 5, 6}


# ==========================================
# 4️⃣ Membership Checking
# ==========================================

print(3 in A)
# Checks if 3 exists in set A
# Output: True

print(10 in A)
# Output: False

print(5 not in A)
# Output: True


# ==========================================
# 5️⃣ Looping Through Set
# ==========================================

for item in A:
    print(item)
# Prints each element (order is not guaranteed)


# ==========================================
# 6️⃣ Set Comprehension (Bonus)
# ==========================================

squares = {x**2 for x in range(5)}
print(squares)
# Output: {0, 1, 4, 9, 16}
