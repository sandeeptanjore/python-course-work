import re as regex

output= regex.match("abc", "abcdef")
print('Sandeep, the match is: ',output)
output= regex.match("bcd", "abcdef")
print('Sandeep, the match is: ',output)

output= regex.fullmatch("python", "python")
print('Sandeep, the fullmatch is: ',output)

output= regex.fullmatch("python", "python").group()
print('Sandeep, the fullmatch is: ',output)

pattern_match = regex.search('very', 'Python is very easy').span()
print('Sandeep, the search is: ',pattern_match)

find_all = regex.findall('can', 'can you can a can as a canner in caNnes')
print('Sandeep, the findall is: ',find_all)