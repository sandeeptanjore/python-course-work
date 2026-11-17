# Permutations: all possible arrangements 

#formuala = nPr = n!/(n-r)!
# so if say you have a list that has 4 elements but
# you only want permutations of 2 elements then how will you go?
# apply the formula = 2P2 = 2!/(4-2)! = 12

# Cominations: all possible selections or combinations

# formula = nCr = n!/(n-r)!r!
# 4C2 = 4!/(4-2)! 2! = 6
import itertools as it

lst= ['A','B','C','D']

perms= it.permutations(lst,r=2)
print(perms)
perm_list= list(perms)
#print('Permutations:', perm_list)

print('Permutations: ')
print('=============')
for t in perm_list:
    print(t)