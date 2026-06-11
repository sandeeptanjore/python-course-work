print ('2: Sum of the digits of a given number')
number = int(input('Enter a number: '))
original_number= number
i = 0
sum=0
remainder=0

while number>0:
    remainder= number%10
    sum+=remainder
    number= number//10

print('Sum of a given number is: ', sum)