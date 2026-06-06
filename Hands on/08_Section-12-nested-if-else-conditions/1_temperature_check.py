print("A program to that accepts temperature and displays the state")
temp = float(input("Enter temperature "))

if temp==25:
    print('Normal temperature')
else:
    if temp < 25:
         print('Cold temperature')
    else:
        print('Hot temperature')

# another way of doing
if temp==25:
    print('Normal temperature')
elif temp <25:
    print('Cold temperature')
else:
    print('Hot temperature')


