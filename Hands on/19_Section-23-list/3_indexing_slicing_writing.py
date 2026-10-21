#Indexing for writing purposes:
l1=[1,2,3,4,5]
print(l1)

#modifying l1[3] from 3 to 10
l1[3] = 10
print(l1)

l1[3] = [10,11]
print(l1)

#slicing: l1[start:stop] = [any number of elements]
#slicing: l1[start:stop:step] = [exact number of elements] should be mentioned


#slicing: l1[start:stop] = [any number of elements]
l2_slicing = [11,12,13,15,14,16]
l2_slicing[0:0]=[10]
# print(l2_slicing[0:0]=[10])
print(l2_slicing) #[10, 11, 12, 13, 15, 14, 16]

l2_slicing[3:3] = [100] # so element 13 at index 3 will be pushed on the right 
                        # or to next location  and replaced with 100
print(l2_slicing) #[10, 11, 12, 100, 13, 15, 14, 16]

#now trying to insert a number at the end
l2_slicing[8:] = [999]
print(l2_slicing) # [10, 11, 12, 100, 13, 15, 14, 16, 999]

l2_slicing[9:9] = [10001]
print(l2_slicing) # [10, 11, 12, 100, 13, 15, 14, 16, 999, 10001]

l2_slicing[3:3] = [222,333,444] 
print(l2_slicing) 
# output will be: 
# [10, 11, 12, 222,333,444,100, 13, 15, 14, 16, 999, 10001]


print(' ')
#slicing: l1[start:stop:step] = [exact number of elements] should be mentioned
print('Now slicing: l3[start:stop:step]')
l3_slicing = [1,2,3,4,5]
l3_slicing[::2]= [100,200,300]
#output will be [100,2,200,4,300]
print(l3_slicing)
l3_slicing[ : : -1]=[10,11,12,13,14]
print(l3_slicing) # [14, 13, 12, 11, 10]

l3_slicing[3: 0: -1] = [999,888,777]
print(l3_slicing) #[14, 777, 888, 999, 10]