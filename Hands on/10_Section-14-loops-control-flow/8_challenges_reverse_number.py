print('A program to reverse of a given number')
rev=0
remainder=0
number = int(input('Enter a number that you wish to reverse '))
original_number=number

while number>0:
    remainder = number%10
    rev = rev*10 +remainder
    number= number//10

print('Reverse of', original_number, 'is:',rev)