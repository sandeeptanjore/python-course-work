
# Question 1:
# Write a program that asks the user to enter a sentence.
# Print:
# Total number of characters
# First character
# Last character

sentence = input('Enter a sentence...\n')
#print(f"{sentence}")
# username= input("Enter your name: ")
# print(f"Hello, {username}")

total_number_of_characters= len(sentence)
first_character = sentence[0]
last_character = sentence[-1]
print("The sentence entered :",sentence, "consists of following details....")
#print("consists of following details....")
print("=====================================================================")
print("Total number of characters:",total_number_of_characters)
print("First character:", first_character)
print("Last character:",last_character)