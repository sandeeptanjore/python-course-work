# A few practice questions on String slicing by DeepSeek

s = "Python Programming"

# Question 1:
# Extract the first character using positive indexing.

print(s[0])

# Question 2:
# Extract the last character using negative indexing.

print(s[-1])

# Question 3:
# Extract "Prog" using positive indexing.
print(s[7:11:1])

# Question 4:
# Extract "ming" using negative indexing.

print(s[-4:])

# Question 5:
# Extract "Python" using positive indexing (start and end)

print(s[0:6])

# Question 6:
# Extract "Prog" using negative indexing (start and end both negative).

print(s[-11:-7])

# Question 7:
# Extract every second character starting from position 0 to the end using positive indexing.

print(s[0: :2])

# Question 8:
# Extract the string in reverse using negative step.

print(s[: :-1])

# Question 9:
# Extract "nohtyP" (reverse of "Python") using negative step.

print(s[-13::-1])

# Question 10:
# Extract characters from position -12 to -6 with a step of 2.

print(s[-12:-5:-2]) # output: empty string
