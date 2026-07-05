print('A program to demonstrate the Fibonacci Series...')

# declare three initial variables:
n = int(input('Enter a number'))

first_number =0
second_number=1
third_number=0

for i in range(0, n):
    #get third_number by adding first_number and second_number
    third_number = first_number+ second_number
    # then assign the value of second number to first number 
    first_number= second_number
    # then assign the value of third number to second number
    second_number = third_number

# finally print the first number and that will be your result
print(first_number)