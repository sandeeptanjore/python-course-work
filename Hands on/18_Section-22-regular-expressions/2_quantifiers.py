import re as regex

full_match = regex.fullmatch('(ab)?','ab')
print(full_match)

full_match = regex.fullmatch('(ab)?','ab').group()
print(full_match)

full_match_1= regex.fullmatch('(ab)?', '')
print(full_match_1)

full_match_1= regex.fullmatch('(ab)?', '').group()
print(full_match_1)

find_all = regex.findall('[abc]+', '123 abc 786 987 bbbccc@cbcabc charminar a.s.rao nagar')
print(find_all)


