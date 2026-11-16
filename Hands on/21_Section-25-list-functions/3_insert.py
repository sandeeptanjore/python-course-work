l1=[1,2,3,4]
l1.insert(0,500)
print(l1)
print(len(l1))

l1.insert(100,'Python')
print(l1)

#[500, 1, 2, 3, 'Sandeep', 4, 'Python']
l1.insert(len(l1)-2,'Sandeep')
print(l1)