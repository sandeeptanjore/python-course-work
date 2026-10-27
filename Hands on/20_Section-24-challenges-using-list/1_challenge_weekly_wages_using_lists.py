print("A program to calculate a person's weekly wages...")

# Accept daily working hours
hours = input("Enter hours worked each day, separated by spaces: ")

hourly_wage_rate = 12

# Convert input into a list of strings
hours = hours.split()

# Convert the strings into floating-point numbers using list comprehension
week_hours = [float(x) for x in hours]
print(week_hours)

# Calculate total weekly hours
total_hours = sum(week_hours)

# Calculate regular wages and overtime
if total_hours > 40:
    regular_hours = 40
    over_time = total_hours - 40

    regular_amount = regular_hours * hourly_wage_rate
    over_time_amount = over_time * hourly_wage_rate * 1.5

else:
    regular_hours = total_hours
    over_time = 0

    regular_amount = regular_hours * hourly_wage_rate
    over_time_amount = 0

# Calculate total wages
total_wages_to_be_paid = regular_amount + over_time_amount

# Display results
print("Your regular working hours were:", regular_hours)
print("Your overtime hours were:", over_time)
print("Your total working hours were:", total_hours)
print("Your regular amount was: $", regular_amount)
print("Your overtime amount was: $", over_time_amount)
print("Your final salary to be paid is: $", total_wages_to_be_paid)