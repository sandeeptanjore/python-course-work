print('A program to print a person\'s weekly wages...')

number_of_hours_worked = input("Enter number of hours worked each day for the week")
number_of_hours_worked = number_of_hours_worked.split()
total_hours = 0
over_time = 0

hourly_wage_rate = 12
regular_amount = 0
over_time_amount= 0
total_wages_to_be_paid =0

for hours_worked in number_of_hours_worked:
    total_hours = float(total_hours) + float(hours_worked)

if total_hours > 40:
    # Wages for the first 40 hours
    over_time = total_hours - 40

    print('Your regular working hours were:', 40, 'hours')
    print('Your overtime hours were:', over_time, 'hours')
    print ('Your total number of working hours was:',total_hours)
    regular_amount = (40 * 12)
    over_time_amount = (1.5 * 12) * (over_time)
    
    total_wages_to_be_paid = regular_amount + (over_time_amount)

    print('Your regular amount was:', regular_amount)
    print('Your overtime amount was:', over_time_amount)
    print('Your final salary to be paid is: ', total_wages_to_be_paid)
else:
    # What should happen if total_hours <= 40?
    print ('Your total number of working hours was:',total_hours)
    regular_amount=(total_hours * 12)
    total_wages_to_be_paid = regular_amount

    print('Your regular amount was:', regular_amount)
    print('Your final salary to be paid is: ', total_wages_to_be_paid)

        
