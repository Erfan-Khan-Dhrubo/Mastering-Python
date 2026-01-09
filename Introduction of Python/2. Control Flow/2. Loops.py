# ------------------------------
# FOR LOOP (iterate through a sequence)
# ------------------------------
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    # Iterates through each element in the list
    # Output:
    # apple
    # banana
    # cherry

# ------------------------------
# FOR LOOP with range()
# ------------------------------
for i in range(5):
    print(i)
    # range(5) → generates numbers 0,1,2,3,4
    # Output:
    # 0
    # 1
    # 2
    # 3
    # 4

for i in range(2, 7):
    print(i)
    # range(start, end) → numbers 2,3,4,5,6
    # Output:
    # 2
    # 3
    # 4
    # 5
    # 6

for i in range(1, 10, 2):
    print(i)
    # range(start, end, step) → numbers 1,3,5,7,9
    # Output:
    # 1
    # 3
    # 5
    # 7
    # 9

# ------------------------------
# WHILE LOOP (conditional iteration)
# ------------------------------
count = 0
while count < 5:
    print(count)
    count += 1
    # Loop continues until count < 5
    # Output:
    # 0
    # 1
    # 2
    # 3
    # 4

# ------------------------------
# LOOP CONTROL: break, continue, pass
# ------------------------------
for i in range(1, 6):
    if i == 3:
        continue
        # Skip the rest of this iteration
    elif i == 5:
        break
        # Exit the loop completely
    print(i)
    # Output:
    # 1
    # 2
    # 4

for i in range(3):
    pass
    # pass → does nothing, placeholder
print("Pass example finished")
# Output: Pass example finished
