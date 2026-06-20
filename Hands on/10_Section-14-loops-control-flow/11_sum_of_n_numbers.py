print('A program to print sum of given numbers...')
n = int(input('Enter a number'))
i=0
sum=0
print('Enter' , n, 'numbers')
while i<n:
    i= i+1
    x = int(input(''))
    sum+=x
print('The sum of', n, 'given numbers is: ',sum)