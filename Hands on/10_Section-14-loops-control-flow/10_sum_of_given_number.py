print('A program to print the sum of a given number')
number_entered = int(input('Enter the number to be summed....'))
counter = 0
sum=0

while counter<number_entered:
    counter= counter +1
    sum = sum + counter
print('The sum of first', number_entered,'numbers is: ', sum)