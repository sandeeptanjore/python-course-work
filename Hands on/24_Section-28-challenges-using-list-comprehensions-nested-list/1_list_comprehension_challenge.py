#Challenge: Split Odd and Even numbers using List Comprehension

nums = [4,8,3,5,10,7,2,9,13,6]

even_numbers= [num for num in nums if num%2==0] # [4, 8, 10, 2, 6]
even_numbers.sort()
print(f'Even numbers are: {even_numbers}')

odd_numbers = [num for num in nums if num%2!=0] # [3, 5, 7, 9, 13]
print(f'Odd numbers are: {odd_numbers}')