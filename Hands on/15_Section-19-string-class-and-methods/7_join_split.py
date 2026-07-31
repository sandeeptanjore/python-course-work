#repalce:
S1= 'a-b-c-d-e'
print(S1)
S2= S1.replace('-','**')
print(S2)

S3=S1.replace('-','#', 2)
print(S3)

S4= S1.replace('k','m')
print(S4)

S5_email = 'abcd@gmail.com'
S6_email = S5_email.replace('gmail', 'yahoo')
print(S6_email)

#join = 

S5= 'xyz'
S6= 'abc'
S7= S5.join(S6)
print(S7)

SA='/'
S8= 'ABC'
SB= SA.join(S8)
print(SB)

print('********SPLIT CONCEPTS BELOW************')
name='John Jani Janardhan'
print(name)
new_name= name.split()
print(new_name)

new_Name= name.split('h')
print(new_Name)

NAME = 'John,Smith,Ajay'
split_name = NAME.split(',')
print(split_name)

space_name = 'John-Smith-Ajay-Khan-james'
hyfen= space_name.split('-')
print(hyfen)

print(space_name.split('-',2))