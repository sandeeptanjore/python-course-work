# ============================================================
# Question 7 - Check Numeric Input
# ============================================================
# Task:
# Ask the user to enter a value.
# Check whether the entered value contains only digits.
# Print "Numeric value" if it does.
# Otherwise, print "Not a numeric value".
#
# Use: isdigit(), if/else
# ============================================================

# Write your solution below:

input_value = input('Enter a value of your choice \n')
print(input_value)
if input_value.isdigit():
    print(f'The value entered {input_value} is a numeric value')
else:
    print(f'The value entered {input_value} is non numeric value')