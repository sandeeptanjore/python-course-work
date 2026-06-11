n = 436987
print('A program to print the digits of a number in reverse order')
print('..in other words it is: Give me ALL digits from last to first until nothing is left')

while n >0:
    remainder = n%10
    print('The remainder of the number',n,'is: ',remainder)
    n=n//10
    print('The number after discarding the last digit is', n)
    print(' ')