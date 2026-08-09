# ============================================================
# Question 5 - Split and Join
# ============================================================
# Task:
# Ask the user to enter a sentence.
# Split the sentence into words.
# Join the words using a hyphen (-).
# Print the result.
#
# Use: split(), join()
# ============================================================

# Write your solution below:

sentence = input("Enter a sentence of your choice\n")
hyphen = '-'
#splitting the sentence into words
words = sentence.split()
print(words)
#joining the words back into a sentence
print(hyphen.join(words))
