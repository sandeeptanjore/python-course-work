'''
-Project Objective
-Write a Python program to print a URL and parse it as follows:
- Protocol : https
- Domain : kaggle
- page : /datasets
- 
'''

print('A program to accept the URL, print the URL and parse it...')
url = input('Enter a URL of your choice \n')
print('The URL entered is:', url)

# protocol = url[0:5]
# domain = url[12:18]
# page = url[22:]

colon_position = url.find(':')
protocol = url[0:colon_position]

first_dot_position = url.find('.')
second_dot_position = url.find('.com')
domain = url[first_dot_position+1:second_dot_position]


forward_slash_position = url.find('/', second_dot_position)
page = url[forward_slash_position:]


print('Protocol is:',protocol)
# print('first dot', first_dot_position)
# print('second dot', second_dot_position)
# print('forward_slash_position', forward_slash_position)
print('Domain is:',domain)
print('Page is:', page)

