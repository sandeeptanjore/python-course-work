# A program to remove all duplicates from a given list

print('A program to remove all duplicates from a given or predefined list')

list_one = [3,5,7,9,3,6,5,2,3,7]
unique_list = []

for num in list_one:
    print(num)
    if num not in unique_list:
        unique_list.append(num)
        #unique_list.sort()

print('****')
print(unique_list)


# for num in list_one:
#     print("num =", num)
#     print("list_one[num] =", list_one[num])
#     break

# for num in list_one:
#     print(list_one[num])