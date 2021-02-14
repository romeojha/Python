cheese_price = 50
small = 200
medium = 275
large = 350
size = input(
    f"what size pizza do you want? S M L of Rs{small,medium,large} \n")
cheese = input(f"do you want extra cheese of Rs{cheese_price}?Y/N\n")
pepper = input("do you want some pepper Rs'50-100'? Y/N\n")
# small size pizza
if size == "s":
    if cheese == "y" and pepper == "y":
        pizza_price = small+cheese_price+50
        print("you choose small pizza with cheese and pepper of", pizza_price)
    elif cheese == "y":
        pizza_price = small+cheese_price
        print("you choose small pizza with cheese of", pizza_price)
    elif pepper == "y":
        pizza_price = small+50
        print("you choose small pizza with pepper of", pizza_price)
    else:
        pizza_price = small
        print("you choose small pizza of ", pizza_price)
        # medium pizza price
elif size == "m":
    if cheese == "y" and pepper == "y":
        pizza_price = medium+cheese_price
        print("you choose medium pizza with cheese and pepper of", pizza_price)
    elif cheese == "y":
        pizza_price = medium+cheese_price
        print("you choose medium pizza with cheese of", pizza_price)
    elif pepper == "y":
        pizza_price = medium+75
        print("you choose medium pizza with pepper of", pizza_price)
    else:
        pizza_price = medium
        print("you choose medium pizza of ", pizza_price)
        # large pizza price
elif size == "l":
    if cheese == "y" and pepper == "y":
        pizza_price = large+cheese_price+100
        print("you choose large pizza with cheese and pepper of", pizza_price)
    elif cheese == "y":
        pizza_price = large+cheese_price
        print("you choose large pizza with cheese of", pizza_price)
    elif pepper == "y":
        pizza_price = large+100
        print("you choose large pizza with pepper of", pizza_price)
    else:
        pizza_price = large
        print("you choose large pizza of ", pizza_price)
else:
    print("please enter small letters(s,m,l)")
total = pizza_price
consumers = input("total number of friends to pay bill.\n")
tips = input("how much tip do you wanna give?\n")
vat = input("is there an extra VAT?(yes/no)\n")
if vat == "yes":
    vatamt = (13/100)*int(total)
else:
    vatamt = 0
to_pay = (int(total)+float(tips)+float(vatamt))/int(consumers)
pay_per_person = f'total amount to pay per person is {to_pay:.2f}'
print(pay_per_person)
