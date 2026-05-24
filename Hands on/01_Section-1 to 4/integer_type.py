import sys


x=101
y= 123456789012345678

print(x)
print(id(x))
print(y)

x= 205
print(x)
# a separate memory location is created 
# instead of the above that it created in the beginning
print(id(x)) 

print(sys.getsizeof(x));
print(sys.getsizeof(y));

