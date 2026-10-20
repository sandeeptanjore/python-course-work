#List creation examples

L1 = [1, 2, 3, 4, 5]
L2= list((3,5,7,9))
L3= list(('abcde'))
L4=[]

print(L1)
print(L2)
print(L3)
print(L4)
L5= [6,5,4,5,6,7,7]
print(L5)
print(L5[2])
print(L5[-7])
print(L5[0])

print('Traversing...')
for x in L5:
    print(x)


 #Hetrogenous
 # Example of a heterogeneous list
L6 = [1, "two", 3.0, [4, 5], True,5+6j]
print('Traversing heterogeneous list...')
print(L6)

# Mutating
# Original value of L6 variable = [1, "two", 3.0, [4, 5], True,5+6j]
L6[1] = "TWO"
L6[0]= 9999
print('After mutation:')
print(L6)
for x in L6:
    print(x)

#Adding a new element
L6.append("new element")
print('After adding a new element:')
print(L6)
for x in L6:
    print(x)

#Removing an element
L6.remove('new element')
print('After removing the element:')
print(L6)
for x in L6:
    print(x)


    # What is a list = an ordered collection of Hetrogenouselements in Python. 
    # It can have indices 
    # and allows duplicate elements. Lists are mutable, meaning their elements can be changed after creation.