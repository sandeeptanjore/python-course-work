
# String indexing
s1 ='Hello World'

print(s1[0]) # Output: H
print(s1[-7]) # Output: o

print(s1[1:7]) #Output: ello W
print(s1[3:7]) # Extracts alphabets from 3rd to 6th position/indices; Output: l,o, ,w

print(s1[2:]) #Extracts the entire string from position 2 (till the end); Output: llo World



print(s1[:7]) #Extracts the string from position 0 till 6th index; Output: llo World 

print(s1[6:]) #Extracts the string from position 6 till the end of the string; Output: World

print(s1[-5:]) #Extracts the string from -5 position till the end of the string; Output: World


print(s1[-8:-4]) #Extracts the string from position - 8 to -5 in forward direction; Output: lo W

print(s1[0:11:1]) #Extracts the string from position 0 to 11 of S1 variable with a step of 1; Output: Hello World

print(s1[0:11:2]) #Extracts the string from position 0 to 11 of S1 variable with a step of 2; Output: HloWrd

print(s1[ : : ]) #Extracts the entire string 

s2= print(s1[ : :-1 ]) #Extracts the entire string in reverse order. Output: dlroW olleH

s3= print(s1[-3: :-1]) #Extracts the string from backwards direction again with starting point as -3 Output: roW olleH

s3 = print(s1[-2:-9:-1]) #Output: lroW ol