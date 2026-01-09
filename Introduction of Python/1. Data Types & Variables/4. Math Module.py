# Import the math module
import math

# ------------------------------
# math.sqrt()
# ------------------------------
num = 16
print(math.sqrt(num))
# Square root of 16 → Output: 4.0

# ------------------------------
# math.ceil()
# ------------------------------
val = 7.3
print(math.ceil(val))
# Rounds UP to nearest integer → Output: 8

# ------------------------------
# math.floor()
# ------------------------------
print(math.floor(val))
# Rounds DOWN to nearest integer → Output: 7

# ------------------------------
# math.pow()
# ------------------------------
print(math.pow(2, 3))
# 2 raised to the power 3 → Output: 8.0

# ------------------------------
# math.factorial()
# ------------------------------
print(math.factorial(5))
# Factorial of 5 → 5*4*3*2*1 → Output: 120

# ------------------------------
# math.pi and math.e
# ------------------------------
print(math.pi)
# Value of π → Output: 3.141592653589793
print(math.e)
# Value of Euler's number e → Output: 2.718281828459045

# ------------------------------
# math.sin(), math.cos(), math.tan()
# ------------------------------
angle = math.pi / 4  # 45 degrees in radians
print(math.sin(angle))
# sin(45°) → Output: 0.7071067811865475
print(math.cos(angle))
# cos(45°) → Output: 0.7071067811865476
print(math.tan(angle))
# tan(45°) → Output: 0.9999999999999999 (~1)

# ------------------------------
# math.log()
# ------------------------------
print(math.log(10))
# Natural logarithm (base e) → Output: 2.302585092994046
print(math.log10(100))
# Log base 10 → Output: 2.0

# ------------------------------
# math.radians() and math.degrees()
# ------------------------------
print(math.radians(180))
# Converts 180° to radians → Output: 3.141592653589793
print(math.degrees(math.pi))
# Converts π radians to degrees → Output: 180.0

# ------------------------------
# math.fabs()
# ------------------------------
print(math.fabs(-7.5))
# Absolute value → Output: 7.5

# ------------------------------
# math.isqrt()
# ------------------------------
print(math.isqrt(17))
# Integer square root → Output: 4
