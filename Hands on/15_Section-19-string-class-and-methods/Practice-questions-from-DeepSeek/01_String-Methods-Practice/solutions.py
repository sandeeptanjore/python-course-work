# 1. using find() and index() methods solve the questions below

s = "Python Programming is fun"

# A: Find the position of "Prog" using find()

print('### 1. find() and index() Methods')

s_position = s.find('Prog')
print('The position of Prog is at: ',s_position)

# B: Find the position of "fun" using index()
s_index = s.index('fun')
print('The position of fun is at: ', s_index)

#C: What happens if you use find() for a substring that doesn’t exist? Write code to show it.
#Answer: it returns a negative 1 i.e. -1 and is demonstrated below:
s_find = s.find('Sandeep')
print('The position of Sandeep is at: ', s_find)

#D: What happens if you use `index()` for a substring that doesn't exist? Write code to show it.
#Answer: it returns an error: ValueError: substring not found
# s_idx = s.index('sandeep')  # commenting this because of valueError 
# print('The position of Sandeep is at: ', s_idx) # commenting this because of valueError 

print('')

print('### 2. String Alignment and Padding')

s1 = "Python"

#E: Left-align `s` in a field of width 15 characters, padding with `*`
s2 = s1.ljust(15,'*')
print(s2)

#F: Right-align `s` in a field of width 15 characters, padding with `*`
s_right_align = s1.rjust(15,'*')
print(s_right_align)

#G: Center-align `s` in a field of width 15 characters, padding with `*`.
s_center_align= s1.center(15,'*')
print(s_center_align)

print('')
print('### 3. Joining and Splitting')

#H: Join the list into a single string separated by `-`.
words = ['apple', 'banana', 'cherry']
string = '-'
words_join = string.join(words)
print(words_join)

#I: Join the list into a single string separated by `, `.
separator = ','
words_separator = separator.join(words)
print(words_separator)

#J:  Split the string at `, ` to get back the list.
long_string = "apple, banana, cherry"
split_string = long_string.split(', ')
print(split_string)

print('')
print('*************')
print('### 4. Final combined questions (K, L, M)')

combined = "Hello, World! Welcome to Python."

#K: Find the position of "World"
combined_position = combined.find('World')
print('The position of the word World is at: ', combined_position)

#L: Split the string at the comma (`,`). What do you get?
combined_split = combined.split(',')
print(combined_split)

#M: Left-align the word `"Python"` in a field of width 10 with `*` padding.
extract_python = combined[25:31]
combined_align = extract_python.ljust(10,'*')
print(extract_python)
print(combined_align)