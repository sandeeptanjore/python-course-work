l1=[1,2,3,4,5,6]

del l1[4]
print(l1) # [1, 2, 3, 4, 6]

del l1[1:4]
print(l1) #[1, 6]

# deletes the list itself i.e. the variable itself is deleted
del l1 
print(l1) #NameError: name 'l1' is not defined