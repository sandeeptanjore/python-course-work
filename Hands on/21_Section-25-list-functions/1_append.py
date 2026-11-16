#Adding elements:
#append 

l1=[1,2,3,4,5]

l1.append(6) #[1, 2, 3, 4, 5, 6]
print(l1)

# results in an error as it can take only 1 element
# TypeError: list.append() takes exactly one argument (2 given)
# l1.append(6,7) 
# print(l1)

l1.append('Sandeep') # [1, 2, 3, 4, 5, 6, 'Sandeep']
print(l1)

l1.append('[999,1000]')
print(l1) # [1, 2, 3, 4, 5, 6, 'Sandeep', '[999,1000]']


# we can use slicing operation too to insert elements at the end 

l1[8:8] = ['Anirudh']
print(l1)

#appending in between the list using slicing
#[1, 2, 3, 'Vaishu', 5, 6, 'Sandeep', '[999,1000]', 'Anirudh'] ==> I used l1[3:4] = ['Vaishu]. It removed integer/number 4 all together
l1[3:3] = ['Vaishu'] # [1, 2, 3, 'Vaishu', 4, 5, 6, 'Sandeep', '[999,1000]', 'Anirudh']
print(l1)