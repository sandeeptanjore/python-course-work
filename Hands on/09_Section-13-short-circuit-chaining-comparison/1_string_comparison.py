# Strings are compared Lexicographically (like in a dictionary) in Python. 
# The first character is compared, if they are the same, 
# the second character is compared and so on until a difference is 
# found or the end of the string is reached.   
# example: apple <ball <cat<dog<python
# also : Upper case letters come before lower case letters in lexicographical order.

apply = "apply"
apple = "apple"

print(apply == apple) # output: False
print(apply<apple) # output: False
print(apply>apple) # output: True

cat = "cat"
catch = "catch"
print(cat == catch) # output: False
print(cat > catch) # output: False because the first three characters are the same,
print (catch <cat) # output: False as it is greater and not smaller than cat
print (catch > cat) # output: True because the first three characters are the same, 
#                     but the fourth character 'c' in catch is 
#                     greater than the end of string in cat.

