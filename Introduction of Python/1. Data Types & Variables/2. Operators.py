# ==============================
# 1️⃣ ARITHMETIC OPERATORS
# ==============================

a = 10
b = 3

print(a + b)    # Adds a and b → 10 + 3 → Output: 13
print(a - b)    # Subtracts b from a → 10 - 3 → Output: 7
print(a * b)    # Multiplies a and b → 10 * 3 → Output: 30
print(a / b)    # Divides a by b (float) → 10 / 3 → Output: 3.3333333333333335
print(a // b)   # Floor division → 10 // 3 → Output: 3
print(a % b)    # Remainder → 10 % 3 → Output: 1
print(a ** b)   # Power → 10 ** 3 → Output: 1000


# ==============================
# 2️⃣ ASSIGNMENT OPERATORS
# ==============================

x = 5           # Assign 5 to x → x = 5
x += 2          # Add 2 to x → x = 7
x -= 1          # Subtract 1 → x = 6
x *= 2          # Multiply by 2 → x = 12
x /= 2          # Divide by 2 → x = 6.0

print(x)        # Prints final value of x → Output: 6.0


# ==============================
# 3️⃣ COMPARISON OPERATORS
# ==============================

p = 10
q = 20

print(p == q)   # Checks equality → 10 == 20 → Output: False
print(p != q)   # Checks not equal → 10 != 20 → Output: True
print(p > q)    # Greater than → 10 > 20 → Output: False
print(p < q)    # Less than → 10 < 20 → Output: True
print(p >= q)   # Greater or equal → 10 >= 20 → Output: False
print(p <= q)   # Less or equal → 10 <= 20 → Output: True


# ==============================
# 4️⃣ LOGICAL OPERATORS
# ==============================

is_adult = True
has_id = False

print(is_adult and has_id)  # AND → both must be True → Output: False
print(is_adult or has_id)   # OR → any one True → Output: True
print(not is_adult)         # NOT → reverse True → Output: False


# ==============================
# 5️⃣ IDENTITY OPERATORS
# ==============================

m = 10
n = 10

print(m is n)        # is → True if both point to same memory
print(m is not n)    # is not → True if different objects


# ==============================
# 6️⃣ MEMBERSHIP OPERATORS
# ==============================

languages = ["Python", "JavaScript", "C++"]

print("Python" in languages)      # Checks existence → Output: True
print("Java" not in languages)    # Checks non-existence → Output: True


# ==============================
# 7️⃣ BITWISE OPERATORS
# ==============================

c = 5   # Binary: 0101
d = 3   # Binary: 0011

print(c & d)   # AND → 0101 & 0011 = 0001 → Output: 1
print(c | d)   # OR → 0101 | 0011 = 0111 → Output: 7
print(c ^ d)   # XOR → different bits → Output: 6
print(~c)      # NOT → invert bits → Output: -6
print(c << 1)  # Left shift → 0101 << 1 = 1010 → Output: 10
print(c >> 1)  # Right shift → 0101 >> 1 = 0010 → Output: 2
