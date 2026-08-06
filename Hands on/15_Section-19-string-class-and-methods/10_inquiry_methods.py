#isalpha()

s1= 'Hello Sandeep! Good Morning'
print(s1.isalpha()) #false

s2 ='Hello'
print(s2.isalpha()) #true

#islower()
print(s2.islower()) #false

#isupper()
print(s2.isupper()) #false

#istitle()
print(s2.istitle()) #true

#isspace() => \n\v\r\f and ' '
print(s2.isspace()) #false
print(s1.isspace()) #false

s3= 'Hello Sandeep! Good Morning    '
print(s3.isspace()) #false

s4 = ' '
print(s4.isspace()) #true

s5=''
print(len(s5)) #0 => empty string is not true
print(s5.isspace())#false

#isprintable() => \n\v\r\f\b\a es1

#isidentifier()
