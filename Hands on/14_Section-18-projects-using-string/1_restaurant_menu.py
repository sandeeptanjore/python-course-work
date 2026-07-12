'''
-Project Objective
-Write a Python program to print a restaurant menu of four items and their prices
- Each line displays the item name, followed by dashes, then the price
- The total length of each printed line is constant (eg: 20 characters)
'''
print("A program to print a restaurant menu of four items and it's prices....")

# for i in range(1,5):
#     item=input("Enter an item: ")
#     price= int(input("Enter it's price: "))
#     price = str(price)
#     separator='*' 
#     separator_count=20
#     separator_print = separator_count - len(item) - len(price)
#     print(item + '*' * separator_print+ price)

# Keying in values

item_1 =  input('Enter the first item: ')
price_1 = int(input("Enter it's price: "))

item_2 =  input('Enter the second item: ')
price_2 =  int(input("Enter it's price: "))

item_3 =  input('Enter the third item of your choice: ')
price_3 =  int(input("Enter it's price: "))

item_4 =  input('Enter the fourth item of your choice: ')
price_4 =  int(input("Enter it's price: "))

# Converting the prices to string

price_1 = str(price_1)
price_2 = str(price_2)
price_3 = str(price_3)
price_4 = str(price_4)

# Printing the dashes
pattern = '-'
pattern_fixed_length=20

dash_1 = pattern_fixed_length- len(price_1)-len(item_1)
dash_2 = pattern_fixed_length- len(price_2)-len(item_2)
dash_3 = pattern_fixed_length-len(price_3)-len(item_3)
dash_4 = pattern_fixed_length-len(price_4)-len(item_4)

# Now printing the menu
print('\n =====Restaurant Menu========')
print(item_1 + pattern*dash_1 + price_1)
print(item_2 + pattern*dash_2 + price_2)
print(item_3 + pattern*dash_3 + price_3)
print(item_4 + pattern*dash_4 + price_4)
