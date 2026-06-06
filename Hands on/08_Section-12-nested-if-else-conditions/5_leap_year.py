print('A program to check if the year entered is a leap year or not')
year_entered = int(input('Enter the year to be checked: '))

if (year_entered%100==0):
   if (year_entered%400==0):
      print(year_entered, ' is a leap year')
   else:
      print(year_entered, ' is a not leap year')
elif (year_entered%4==0):
   print(year_entered, ' is a leap year')
else:
   print(year_entered, ' is a not leap year')   