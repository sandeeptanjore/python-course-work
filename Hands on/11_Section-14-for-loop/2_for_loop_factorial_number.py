# demo of a factorial number and sum of n natural numbers

# Sum of first n natural numbers => 1,2,3,4,5 and so on

sum_of_n_natural_numbers = int(input('Enter the number of natural numbers to sum: '))
# print(sum_of_n_natural_numbers)
sum = 0

for i in range(1,sum_of_n_natural_numbers+1):
    sum = sum+i
print('Sum for first',sum_of_n_natural_numbers, 'natural numbers is: ', sum)


# factorial of a number

# n! = n * (n-1) * (n-2) *  2*1
# n! = 1*2*3 .... * (n-1) *n
# 5! =  1*2*3*4*5 = 120

factorial_number =int(input('Enter a number to find its factorial: '))
#print(factorial_number)
fact = 1 

for k in range(1,factorial_number+1):
    fact = fact *k
print('Factorial of', factorial_number, 'is: ', fact)    