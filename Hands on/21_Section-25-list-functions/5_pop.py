l1=[12,10,13,14,15]
print(l1)
l1.pop() # by default the last element is deleted if no index is specified
print(l1)

names = ["Alice", "Bob", "Charlie", "Diana"]
#the name Charlie is deleted
names.pop(2)
print(names) # ['Alice', 'Bob', 'Diana']

# gives an error:
# IndexError: pop from empty list
empty_list=[]
empty_list.pop()
print(empty_list)