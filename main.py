
print('welcome to the tip calculator')
bill= input('what was the total bill? $')
tip= input('what porcentage tip would you want to give? 10, 12 or 15? ')
number_people = input('How many people to split the bill? ')

#code👇
bill_float = float(bill)
tip_int = int(tip)
payers = int (number_people)

porcentage = tip_int / 100
total_bill = bill_float + bill_float * porcentage
pay_each= total_bill / payers 
payment_per_person = round(pay_each,2)
payment_per_person = "{:.2f}".format(pay_each) #this is a format option to add the zero in the decimal if it is not there.
print(f"Each person should pay ${payment_per_person}")