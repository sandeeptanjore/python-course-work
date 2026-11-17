import itertools as it

list_string = ['Sandeep', 'Soni', 'Vaishu','Madhavi']

perm = it.permutations(list_string,r=2)
perm_list= list(perm)
#print('Permutations:',perm_list)

print('Permutations: ')
print('=============')
for permutation in perm_list:
    print(permutation)
