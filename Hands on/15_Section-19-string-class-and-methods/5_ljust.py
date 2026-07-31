s= 'Hello'

x = s.ljust(100,'$') # fills with $ on left side 
print(x)

x = s.rjust(10,'$') # fills with $ on right side
print(x)

x = s.center(10,'#') # fills with # at either ends
print(x)

x= s.zfill(10) # zero filling = fills 0 on lhs
print(x)

z = s.zfill(7)
print(z)