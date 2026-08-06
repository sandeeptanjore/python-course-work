#isdigit()
s1='7235'
print(s1.isdigit()) #True

print('23453'.isdigit()) #True
print('33434.33'.isdigit()) #False

#isdecimal()
print(s1.isdecimal()) #False
print('47.8291'.isdecimal()) #false because Strictly checks for Unicode digits 0–9.

#isnumeric()
print(s1.isnumeric()) # true
print('4/2'.isnumeric()) # false

#isascii()
print('Sandeep'.isascii()) #true

#isalnum()
print('As12'.isalnum()) #true
print('4/2'.isalnum()) #false