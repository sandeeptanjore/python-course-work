#strip methods:
#lstrip = removes leading spaces/unwanted characters from left side
#rstrip = removes trailing spaces/unwanted characters from right side
#strip = removes spaces/unwanted characters from either side

s= '  Sandeep'
print(s)
x= s.lstrip()
print(x)

a= '$$Hello'
b= a.lstrip('$')
print(b)

c = 'Guten Tag###'
print(c)
d = c.rstrip('#')
print(d)

A = '######Guten Abend###'
print(A)
B= A.strip('#')
print(B)

C = '#!Hello  $ *'
print(C)
D = C.strip('#! $*')
print(D)
