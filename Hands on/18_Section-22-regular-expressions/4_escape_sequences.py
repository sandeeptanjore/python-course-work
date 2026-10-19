import re as regex

# Example of escape sequences in regular expressions

date = "31/12/1970"
# Using escape sequences to match the date format
pattern = r"\d{2}/\d{2}/\d{4}"
match = regex.match(pattern, date)
print(match)