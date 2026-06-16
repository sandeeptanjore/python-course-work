print('A program to check if the given number is a Palindrome or not')
number = int(input('Enter a number: '))
original_number = number
rev=0
remainder=0

while number>0:
    remainder = number%10
    rev = rev*10 +remainder
    number= number//10

if original_number == rev:
    print('The given number', original_number,' is a Palindrome')
else:
     print('The given number', original_number,' is not a Palindrome')
