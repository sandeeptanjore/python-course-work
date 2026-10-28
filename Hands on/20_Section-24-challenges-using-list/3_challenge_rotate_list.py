# A program to rotate a list

list_original= [1,2,3,4,5,6]
rotated_list =[]
rotate_number=0

print('A program to rotate a list of given number...')
rotate_number = int(input('Enter by how many places you wish to rotate\n'))
print(rotate_number)

#for num in list_original:
    #print(num)
rotated_list = list_original[rotate_number:]

rotated_list= rotated_list+(list_original[0:rotate_number])
print(rotated_list)
