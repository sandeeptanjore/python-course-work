print('A program that takes a number and prints the day of the week')
day_number = int(input('Enter the day number: '))

if(day_number==0):
    print('It is a Monday')
elif (day_number==1):
    print('It is a Tuesday')
elif (day_number==2):
    print('It is a Wednesday')
elif (day_number==3):
    print('It is a Thursday')
elif (day_number==4):
    print('It is a Friday')
elif (day_number==5):
    print('It is a Saturday')
elif(day_number==6):
    print('It is a Sunday')
else:
    print('You have entered an invalid day number')