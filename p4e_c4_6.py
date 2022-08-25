def computepay(h, r):
    if h<=40:
        gross_pay=h*r
    else:
        gross_pay=40*r+(h-40)*r*1.5
    return gross_pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h=float(hrs)
r=float(rate)
p = computepay(h, r)
print("Pay", p)
input('Press Enter to Quit')
