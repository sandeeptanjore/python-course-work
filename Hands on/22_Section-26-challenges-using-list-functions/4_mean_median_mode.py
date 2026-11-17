#Mean and Average = are equal to same
# Median = Middle element of a sorted list
# Mode = element appearing most in a list

import statistics as st

lst = [6,8,4,9,3,10,8,11,5,7,8,4,2]
mean = st.mean(lst)
print(f'Mean is: {mean:.2f}')

median = st.median(lst)
print(f'Median is: {median}')

mode = st.mode(lst)
print(f'Mode is: {mode}')

