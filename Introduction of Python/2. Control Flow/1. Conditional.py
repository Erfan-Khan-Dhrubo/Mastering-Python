# Example: Checking a student's marks and assigning grades

marks = 85
attendance = 90  # percentage

# ------------------------------
# if statement
# ------------------------------
if marks >= 90:
    print("Grade: A")
    # Only executes if marks >= 90
    # Output here will not happen because marks = 85

# ------------------------------
# elif statement (multiple conditions)
# ------------------------------
elif marks >= 75:
    print("Grade: B")
    # Executes if previous 'if' was False and marks >= 75
    # Output: Grade: B

elif marks >= 60:
    print("Grade: C")
    # Output will not happen because marks = 85

# ------------------------------
# else statement (default case)
# ------------------------------
else:
    print("Grade: F")
    # Executes if none of the above conditions are True
    # Output will not happen because marks = 85

# ------------------------------
# Nested if statement
# ------------------------------
if marks >= 75:
    print("Passed with good marks")
    # Output: Passed with good marks

    if attendance >= 80:
        print("Eligible for certificate")
        # Nested if inside another if
        # Output: Eligible for certificate
    else:
        print("Not eligible for certificate")
else:
    print("Failed")
