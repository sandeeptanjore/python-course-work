# Syntax: 
# l1=[exp for item in iterable]

l1= [x for x in range(1,5)]
print(l1)

l2=[x**2 for x in range(1,5)]
print(l2)

l3 =[]

for num in range(10,21):
    l3.append(num)

print(l3)

#Conversion into a list comprehension of the above l3 
l4=[num for num in range(20,31)]
print(l4)

# Exercise — Squares using List Comprehension
# Task: Create a list containing the squares of numbers from 1 to 6 (inclusive).

squared=[num*num for num in range(1,7)]
print(squared)