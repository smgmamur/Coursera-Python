hrs = input('Enter Hours:')
rate = input('Enter Rate:')
f_hrs = float(hrs)
f_rate = float(rate)
gross_pay = 0
if f_hrs<=40.0:
    gross_pay = f_hrs*f_rate
else:
    gross_pay = 40*f_rate+1.5*(f_hrs-40)*f_rate
print(gross_pay)
input('Press Enter to Quit')
