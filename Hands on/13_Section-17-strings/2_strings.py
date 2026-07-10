#Creating a variable and assigning a value to it
s1='Sandeep'

#Now accessing each character
print(s1[0]) # S
print(s1[1]) # a
print(s1[-5]) # n
print(s1[4]) #e
print(s1[-1]) # p
print('')

#Now finding out the length of the string
print('The length of the string is:',len(s1))

#Now let us traverse a string

print('Now let us traverse a string')
print('Method 1')
for x in s1:
    print(x)

print('Method 2')
for i in range(len(s1)):
   # print(i, s1[i])
    print(s1[i])