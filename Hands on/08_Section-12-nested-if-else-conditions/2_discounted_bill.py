print('A program that calculates discount amount against a bill')
amount_spent = float(input("Enter the amount spent: "))
total_amount=0
# discount=float(0)

if (amount_spent <1000):
    total_amount= amount_spent-amount_spent*0.1
elif (amount_spent>1000 and amount_spent<5000):
    total_amount = amount_spent - amount_spent*0.15
elif (amount_spent>5000 and amount_spent<10000):
    total_amount = amount_spent - amount_spent*0.20
else:
    total_amount= amount_spent-amount_spent*0.25

print('Amount spent: ', amount_spent)
#print('Discount given: ', total_amount)
print('Final bill ', total_amount)