print('A program to print maximum and minimum number from given set of numbers...')

number_of_elements = int(input('How many numbers do you want to enter? '))

print('This program prints maximum and minimum from given',
      number_of_elements, 'numbers')

print('Enter those', number_of_elements, 'numbers')

maximum_number = 0
minimum_number = 0
counter = 0

while counter < number_of_elements:

    current_number_entered = int(input(''))

    # First number entered becomes the starting point
    if counter == 0:
        maximum_number = current_number_entered
        minimum_number = current_number_entered

    else:
        if current_number_entered > maximum_number:
            maximum_number = current_number_entered

        if current_number_entered < minimum_number:
            minimum_number = current_number_entered

    counter = counter + 1


print('Maximum number is:', maximum_number)
print('Minimum number is:', minimum_number)