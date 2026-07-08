print('A program to generate Prime Numbers for a given number....')

n= int(input('Enter the number you wish to print Prime Number for: '))

# for n in range(1,101):
for n in range(1,n+1):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1

    if count ==2:
     print(n)        
