data = "data"
Data = "Data"
print(data == Data) # output: False because of case sensitivity
print(data > Data) # output : True because uppercase letters come before lowercase letters in lexicographical order.
print (data < Data) # output: False because uppercase letters come before lowercase letters in lexicographical order.
print (Data < data) # output: True because uppercase letters come before lowercase letters in lexicographical order.
print (Data > data) # output: False because uppercase letters come before lowercase letters in lexicographical order.
# in other words think of Data as 2 and data as 3, so 2 is less than 3 and 3 is greater than 2.
