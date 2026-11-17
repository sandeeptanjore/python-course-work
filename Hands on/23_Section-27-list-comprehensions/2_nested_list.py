#Nested list
l1=[1,2,3,4,5] # 5 elements
l2=[[1,2],3,4,5] # 4 elements with nested list

l3=[[1,2],[3,4],[5,6]]

l4=[[1,2,[3,4]],[5,6]]

print(l3)
print(l3[0])
print(l3[1])
print(l3[2])
print(l3[0][1])
print(l3[2][0])
print(l3[2][1])
print(l3[2])
print(l3[1])

print('')
print('Printing a Matrix list')
matrix_list=[[1,2,3], [3,5,7,9],[2,4,6,8],[4,3,2,1]]
print(matrix_list)
print(matrix_list[2]) # prints [2,4,6,8]
print(matrix_list[3][0],matrix_list[3][1]) # prints [4,3]