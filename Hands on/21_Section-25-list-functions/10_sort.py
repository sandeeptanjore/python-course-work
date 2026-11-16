l1_sort=[70,10,60,20,50,30,40]
l1_sort.sort() # default order or asc order of sorting
print(l1_sort) 

l1_sort.sort(reverse=True) # reverse order or desc order of sorting
print(l1_sort)

l2_string= ['coat','python','black', 'cat', 'Black']
l2_string.sort() # dictionary order sorting
print(l2_string) # ['Black', 'black', 'cat', 'coat', 'python']

l2_string.sort(key=len) #sorting based on the length of the string
print(l2_string) # ['cat', 'coat', 'Black', 'black', 'python']

# sorted based on ASCII values
l3_string = ['apple', 'Bat', 'cat','Dog']
l3_string.sort()
print(l3_string)  # ['Bat', 'Dog', 'apple', 'cat']

# sorted based on dictionary values
l3_string.sort(key=str.lower)
print(l3_string)  # ['apple', 'Bat', 'cat', 'Dog']

