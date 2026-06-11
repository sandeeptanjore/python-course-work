print('1: Program to count digits of a Number')
number = int(input('Enter a number: '))
original_number= number
i = 0

print(number)

while number>0:
    number= number//10
    i+=1

print('The number', original_number, "has", i, "digits")


