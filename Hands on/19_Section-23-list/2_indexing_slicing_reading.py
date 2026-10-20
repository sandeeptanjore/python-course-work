#Index and Slicing can be used for both reading and writing

#Indexing for reading purposes:
l1=[3,6,9,12,15,18,21]
print('These are examples of Indexing....')
print(l1[4])
l2 = l1[-3]
print(l2)


#Slicing
print('These are examples of Slicing.....')
l1[ : ]
print(l1)

print(l1[2:])

print(l1[2:5])
print(l1[-5:-2])

#3 Parts of Slicing
print(l1[ : :1])
print(l1[ : :3]) # every third element starting from first element though
print(l1[4: :-1])