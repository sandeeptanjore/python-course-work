print('A program to check if the given number is a Prime number or not.....')

prime_number = int(input('Enter a number'))
count=0

for i in range(1,prime_number+1):
     if(prime_number%i==0):
            count= count+1

if count==2:
    print('Given number: ', prime_number,'is a prime number')
else:
    print('Given number: ', prime_number,'is NOT a prime number')
