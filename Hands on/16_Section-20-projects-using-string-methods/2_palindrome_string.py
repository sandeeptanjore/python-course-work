print('*****************************')
print('A program to check if the given string is a palindrome and if not convert it to a palindrome....')
s1 = input('Enter a string \n')
#s1= 'Race car'


# incase there are spaces in the string remove them
s2= s1.replace(' ',"")

# printing the string  post reversing
#print(s2)
rev = s2[::-1]
print('Reverse of a string:', rev)

# checking if the strings are equal and if so, its a Palindrome
if s2.casefold() == rev.casefold():
    print('A straight forward case of a Palindrome')
    print('Yes, the string ',s1,'is a palindrome')
# if it's not a palindrome then converting it into a Palindrome    
else:
    print('Converting it into a palindrome....') 
    palindrome = s2.casefold() + rev.casefold()
    print('After converting the string:', palindrome , 'is a palindrome')