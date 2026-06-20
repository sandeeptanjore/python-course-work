print('A program to print maximum number of given numbers...')
number_of_elements = int(input('How many numbers do you want to enter? '))
print('This program prints maximum of a number from given' , number_of_elements, 'numbers')
print('Enter those', number_of_elements, 'numbers') # this is prompt and its values will be stored in x
maximum_number = float('-inf')
counter=0 # reads number of elements entered
minimum_number = float('inf')

while counter < number_of_elements:
    counter = counter+1
    current_number_entered  = int(input('')) # this was declared as x by Bari
    if current_number_entered > maximum_number:
        maximum_number = current_number_entered

    if current_number_entered < minimum_number:
        minimum_number = current_number_entered

print('Maximum number is: ', maximum_number)
print('Minimum number is: ', minimum_number)


