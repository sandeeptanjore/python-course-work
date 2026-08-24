print('A simple program to reset a password using CUI....')

reset_password = input('Enter the new password you want to set...\n')
#reset_password = 'Admin123'
print(reset_password)
confirm_password = input('Enter the same password to confirm...\n')
print(confirm_password)
#print(reset_password)

if reset_password == confirm_password:
    print('Password changed...')
else:
    if reset_password.casefold()!=confirm_password.casefold():
        print('Please check cases and try again...')
    else:
        print('Password do not match...')


   