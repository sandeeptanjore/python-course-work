# ============================================================
# Question 6 - Check Website Address
# ============================================================
# Task:
# Ask the user to enter a website address.
# Check whether it starts with "https://".
# Print "Secure website" if it does.
# Otherwise, print "Website does not use HTTPS".
#
# Use: startswith(), if/else
# ============================================================

# Write your solution below:

website_address = input('Enter a valid website address \n')

print('The website address is:',website_address)

if website_address.startswith('https://'):
    print('Secure website')
else:
    print('Website does not use HTTPS')