'''
-Project Objective
-Write a Python program to accept a credit card number
- and mask the first 12 digits of the credit card number and display only the last 4 digits
'''
print('')
print('A program to accept credit card number from a user and display only the last 4 digits....')

credit_card_number = input('Enter a credit card number: ')
masking_credit_card_number = credit_card_number[0:12]
masked_credit_card_number = credit_card_number[12:17]

mask = 'X'
#masking_credit_card_number = (mask * 12)
masking_credit_card_number = (mask * 4 + ' '+ mask*4 + ' '+ mask*4+' ')

print('The credit card number entered is: ' , masking_credit_card_number + masked_credit_card_number)


