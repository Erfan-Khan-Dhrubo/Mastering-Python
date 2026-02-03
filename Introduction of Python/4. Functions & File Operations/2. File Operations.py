# ==========================================
# 1️⃣ Opening Files (Basic Syntax)
# ==========================================

# Open file in read mode ('r')
# file = open('example.txt', 'r')

# Open file in write mode ('w')
# file = open('example.txt', 'w')

# Open file in append mode ('a')
# file = open('example.txt', 'a')

# Always close file when done
# file.close()


# ==========================================
# 2️⃣ Writing to a File ('w' mode)
# ==========================================

file = open('example.txt', 'w')
file.write("Hello Python\n")
file.write("File handling is important.\n")
file.close()

# 'w' mode creates file if it doesn't exist
# It also OVERWRITES existing content


# ==========================================
# 3️⃣ Appending to a File ('a' mode)
# ==========================================

file = open('example.txt', 'a')
file.write("This line is appended.\n")
file.close()

# 'a' mode adds content at the end
# It does NOT remove previous content


# ==========================================
# 4️⃣ Reading from a File ('r' mode)
# ==========================================

file = open('example.txt', 'r')

content = file.read()
print(content)
# read() reads entire file as one string

file.close()


# ==========================================
# 5️⃣ readline()
# ==========================================

file = open('example.txt', 'r')

first_line = file.readline()
print(first_line)
# Reads only one line at a time

file.close()


# ==========================================
# 6️⃣ readlines()
# ==========================================

file = open('example.txt', 'r')

lines = file.readlines()
print(lines)
# Returns list of lines

file.close()


# ==========================================
# 7️⃣ Using Context Manager (BEST PRACTICE)
# ==========================================

# Automatically closes file after block execution
with open('example.txt', 'r') as file:
    data = file.read()
    print(data)

# No need to call file.close()


# ==========================================
# 8️⃣ Writing Using Context Manager
# ==========================================

with open('example2.txt', 'w') as file:
    file.write("Using context manager.\n")
    file.write("This is safer and cleaner.\n")


# ==========================================
# 9️⃣ writelines()
# ==========================================

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open('example3.txt', 'w') as file:
    file.writelines(lines)

# writelines() writes list of strings
# It does NOT add newline automatically
