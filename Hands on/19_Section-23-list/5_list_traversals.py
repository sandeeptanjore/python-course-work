# Various list traversal methods:
# 1. for loop
# 2. for loop using range()
# 3. while loop

l1 = [5,6,7,8,9]

# for loop
for x in l1:
    print(x)

# for loop using range
print('Using for loop using range...')
for i in range (len(l1)):
    print(i, l1[i])

# using while loop
print('Using while loop...')    
j=0
while(j< len(l1)):
    print(l1[j])
    j= j+1


