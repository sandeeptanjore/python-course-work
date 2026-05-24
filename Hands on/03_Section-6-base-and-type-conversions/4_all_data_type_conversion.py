f = 16.59
b = True
s1=125
s2= '0b1010'
s3='0xA'

print('Starting with int type conversions....')
x = int(f)
print(x, type(x))

print(int(b))

print(int(s1))

y= int(s2,2)
print(y,type(y))

#print(int(3+4j)) # not possible; throws an error

print('End of int type conversions....')

print('Starting with float type conversions....')

print(float(125))
print(float(True))
print(float('12.75'))
print('End of float type conversions....')

print('Start of bool type conversions....')

print(bool(5))
print(bool('anything'))
print(bool('TRUE'))
print(bool(1))
print(bool('FAlse'))
print(bool(False))
print(bool(0))

print(bool(-12))

print('End of bool type conversions....')
print('........')
print('Start of string type conversions')
print(str(10))
print(str(-12))
print(str(-1.2E-3))
print(str(False))
print(str(3+4j))


