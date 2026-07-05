print('A program to print Factors of a Number')

factor_number= int(input("Enter a number"))
result =0

for i in range(1,factor_number+1):
    if (factor_number%i==0):
        # result = i
        print(i)

# print('Factors of ', factor_number, 'are:', result)