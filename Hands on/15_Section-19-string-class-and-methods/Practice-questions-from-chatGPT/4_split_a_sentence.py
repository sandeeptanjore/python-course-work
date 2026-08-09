# ============================================================
# Question 4 - Split a Sentence
# ============================================================
# Task:
# Ask the user to enter a sentence.
# Split the sentence into individual words.
# Print the resulting words.
#
# Use: split()
# ============================================================


# Write your solution below:

print('A program to split a sentence into words')
sentence_entered = input('Enter a sentence to be split \n')
words= sentence_entered.split()
print(f'Entered sentence was: {sentence_entered} and its resulting words are: {words}')