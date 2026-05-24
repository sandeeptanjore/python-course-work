name = 'Alexa'

#This wont convert or work as the name should be an integer i.e. something like:
# "123" or "34343". Pure string like the above won't work and will result in an error:
# ValueError: invalid literal for int() with base 10: 'Alexa'
#print(int(name))

f = 16.59
b = True
s1 = '123'
s2= '0b1010'
s3 = 'OxA'

x = int(f) # I am passing the int function to the variable x and storing it in x
print(x , type(x)) # output: 16 <class 'int'>

print(int(b) , type(int(b))) # output: 1 <class 'int'>

print(int(s1) , type(int(s1))) # output: 123 <class 'int'>
x= int(s2,2)
print(x, type(x)) # output: 1010 <class 'int'>
