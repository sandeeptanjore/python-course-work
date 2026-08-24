print(' ')
print('**************************************')
print('A Python program to clean the data....')
print('**************************************')

input_string = 'These+notes#reveal9Newton seeking-out an(!underlying structure to/the\\pyramid:the' \
'unit of measurement?used>by its builders'
clean_string=''
print(input_string)

for x in input_string:
    if x.isalpha() or x.isspace():
        clean_string = clean_string +x
    else:
        clean_string = clean_string + ' '

print(clean_string)