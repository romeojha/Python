total = input("enter your total bill\n")
consumers = input("total number of friends to pay bill\n")
tips = input("how much tip do you wanna give?\n")
vat = input("is there an extra VAT(yes/no)\n")
if vat == "yes" or "YES" or "Yes":
    vatamt = (13/100)*int(total)
else:
    vatamt = int(total)
to_pay = (int(total)+float(tips)+float(vatamt))/int(consumers)
pay_per_person = f'total amount to pay per person is {to_pay:.2f}'
print(pay_per_person)
