# Question 2:
# Write a program that asks the user to enter a sentence.
# Ask the user to enter a word to search for.
# Print the starting position of the word.
# If the word does not exist, print "The word was not found."
# Use find() and if/else.
# Do not use loops.


print("A program that finds the starting position of a word....")
sentence= input("Enter a sentence \n")
#print(sentence)
word = input("Now enter a word to search for in the sentence \n")
#print(word)

starting_position = sentence.find(word)

if starting_position !=-1:
    print(f'The word {word} starts at index {starting_position}')
else:
    print(f"The word entered ({word}) is not part of your sentence")