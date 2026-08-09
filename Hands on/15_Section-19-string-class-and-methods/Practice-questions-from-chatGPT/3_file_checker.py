# ============================================================
# Question 3 - Python File Checker
# ============================================================
# Task:
# Ask the user to enter a filename.
# Check whether the filename ends with ".py".
# Print "Python file" or "Not a Python file".
#
# Use: endswith(), if/else
# ============================================================

# Write your solution below:

print('A program to check if the file is a Python file or not')
file_name= input('Enter a file name \n')
#print(file_name)
if file_name.endswith('.py'):
    print(f'The file name {file_name} is a Python file')
else:
    print(f'The file name {file_name} is not a Python file')

