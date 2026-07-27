#find method

s = 'Hello How are you'
print(s);

x=s.find('o') # finding the letter o
print(x)

how =  s.find('how') # finding the word 'how'
print(how); # returns -1 as it cannot find how

how = s.find('How') # finding the word 'How'
print(how);

x = s.find('o', 5)
print(x)

x = s.find('o', 5,8)
print(x)

x = s.find('o', 5,6)
print(x)
