#startswith

s1= 'Rossum@gmail.com'
print(s1.startswith('Rossum'));

print(s1.startswith('gmail', 7))

#endswith
print(s1.endswith('.com'))
print(s1.endswith('.au'))

#startswith
s2='Python is very easy'
print(s2.startswith('python'))#false
print(s2.startswith('Python'))#true

print(s2.startswith('is', 7))#true

#endswith
print(s2.endswith('easy'))#true
s3='abcs@gmail.com'
print(s3.endswith('gmail.com'))#true

#removeprefix
s4=s2.removeprefix('Py')
print(s4)#thon is very easy

s5=s2.removeprefix('Java')
print(s5) #gives the same string if the search criteria is not met

#remove suffix
s6 ='Python Programming'
s7=s6.removesuffix('ing')
print(s7)

#partition
var1 = 'Python is easy'
var2 = var1.partition('is')
print(var2)

var3= var1.partition('-')
print(var3)

var4= 'Python-is-easy'
var5= var4.partition('-')
print(var5)

#rpartition
var6= var4.rpartition('s')
print(var6)# 'Python-is-ea', 's', 'y'