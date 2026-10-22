#Operations:
# Concatenation ==> +
# Repetition ==> *
# Membership ==> in, not in
# List Comparison ==>  < <= > >= == !=

l1=[1,2,3]
l2= [8,9,10]
l3 = l1+l2
print(l3)

# l1+4 # error: not possible as list can only concatenate with list
l3=l1+[4]
print(l3)

l1.extend([4,5,6])
print(l1)

l2= l1*3
print(l2)

#Membership operation
l5 = [1,2,3,4,5,6,7]
print(2 in l5) # true
print(100 in l5) # false

l_colors = ['red','green','blue']
for x in l_colors:
    print(x)

print('orange' in l_colors)