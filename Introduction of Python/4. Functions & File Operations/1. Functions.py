# ==========================================
# 1️⃣ Defining Functions with def
# ==========================================

def greet():
    print("Hello, Welcome to Python!")


greet()
# Calls the function
# Output: Hello, Welcome to Python!


# ==========================================
# 2️⃣ Parameters
# ==========================================

# 🔹 Positional Parameters
def add(a, b):
    print(a + b)


add(5, 3)
# 5 goes to a, 3 goes to b
# Output: 8


# 🔹 Keyword Arguments
add(a=10, b=20)
# Order does not matter when using keywords
# Output: 30


# 🔹 Default Parameters
def introduce(name, country="Bangladesh"):
    print("Name:", name)
    print("Country:", country)


introduce("Frank")
# Uses default country
# Output:
# Name: Frank
# Country: Bangladesh

introduce("Alice", "USA")
# Overrides default value
# Output:
# Name: Alice
# Country: USA


# ==========================================
# 3️⃣ Return Values
# ==========================================

def multiply(x, y):
    return x * y


result = multiply(4, 5)
print(result)
# Returns value instead of printing directly
# Output: 20


# ==========================================
# 4️⃣ Variable Scope (Local vs Global)
# ==========================================

# Global variable
x = 10


def show_value():
    # Local variable
    y = 5
    print("Inside function:")
    print("x =", x)  # Can access global variable
    print("y =", y)  # Local variable


show_value()

print("Outside function:")
print("x =", x)
# print(y) ❌ Error: y is local to function

# Output:
# Inside function:
# x = 10
# y = 5
# Outside function:
# x = 10


# 🔹 Modifying global variable

count = 0


def increase():
    global count
    count += 1


increase()
print(count)
# Output: 1


# ==========================================
# 5️⃣ Multiple Return Values
# ==========================================

def calculate(a, b):
    sum_value = a + b
    product = a * b
    return sum_value, product   # Returning multiple values


result = calculate(3, 4)

print(result)
# Output: (7, 12)
# Returns a tuple


# Unpacking multiple return values
total, multiply_result = calculate(5, 6)

print(total)
# Output: 11

print(multiply_result)
# Output: 30
