l1=[1,2,3,4]

l1.extend([5,6,7])
print(l1)

# it print it as: [1, 2, 3, 4, 5, 6, 7, 'P', 'y', 't', 'h', 'o', 'n']
# this is because it is iterable
l1.extend('Python')
print(l1)

# it print it as: [1, 2, 3, 4, 5, 6, 7, 'P', 'y', 't', 'h', 'o', 'n',100,101,102,103,104]
l1.extend(range(100,105))
print(l1)