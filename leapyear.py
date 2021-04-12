leapyear = input("enter year to check weather it is leap year or not\n")
int_leapyear = int(leapyear)
if int_leapyear % 4 == 0 and int_leapyear % 100 != 0:
    print(f"{int_leapyear} is a leapyear")
elif int_leapyear % 100 == 0:
    print(f"{int_leapyear} is not a leapyear")
elif int_leapyear % 400 == 0:
    print(f"{int_leapyear} is a leapyear")
else:
    print(f"{int_leapyear} is not a leapyear")
    
