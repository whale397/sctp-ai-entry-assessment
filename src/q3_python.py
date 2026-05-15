# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

def formatName(firstName, lastName):
    # Capitalize the first and last name
    first = firstName.capitalize()
    last = lastName.capitalize()
    return last + ", " + first


# Task 2:
# Write a function called formatInitials(firstName, lastName) that returns the
# initials of the person as a string in uppercase.
# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

def formatInitials(firstName, lastName):
    # Convert the first and last name to uppercase
    first = firstName.upper()
    last = lastName.upper()
    # Extract the first letter of the first and last name and add a period after each
    return first[0] + "." + last[0] + "."

# Task 3:
# Call both functions with the following inputs and print each result:
#   formatName("Alice", "Tan")  → Expected: "Tan, Alice"
#   formatName("bob", "lim")    → Expected: "Lim, Bob"
#   formatInitials("Alice","Tan") → Expected: "A.T."
#   formatInitials("bob","lim")   → Expected: "B.L."

print(formatName("Alice", "Tan"))
print(formatName("bob", "lim"))
print(formatInitials("Alice","Tan"))
print(formatInitials("bob","lim"))