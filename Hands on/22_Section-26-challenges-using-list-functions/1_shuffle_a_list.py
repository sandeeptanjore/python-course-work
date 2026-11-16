# random module and importing it
import random as rd # library to generate a random number
random_number= rd.random()
print(random_number) # gives any floating number between 0 and 1
print(random_number*10) # gives any number between 1 and 10

# prints integer random number only
print(rd.randint(1,100)) # 70 random number between 1 and 100
print(rd.randint(1,100)) # 18 random number between 1 and 100

# prints random range number
print(rd.randrange(1,10,2)) # prints odd numbers between 1 and 10
print(rd.randrange(2,101,2)) # prints even number between 1 and 100

#different set of random numbers each time you run
print('')
print('Different set of random numbers:')
for i in range(5):
    print(rd.randint(1,100))

#same set of random numbers each time you run using a function called seed
print('')
print('Same set of random numbers:')    
rd.seed(10) # seed means starting point
for i in range(5):
    print(rd.randint(1,100))

print('')
print('a choice of numbers:')  
l= ['a','b','d',10,12,1.5,2.7,True]      
print(rd.choices(l,k=2)) # ['a', 10]

# Shuffling set of numbers and characters
print('')
print('Shuffling numbers and characters....')
l1=[1,2,3,4,100,200,333,'Sandeep','Soni']
rd.shuffle(l1)
print(l1) #[3, 'Soni', 333, 4, 1, 2, 200, 100, 'Sandeep']

