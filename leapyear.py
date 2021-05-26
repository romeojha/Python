# leapyear = input("enter year to check weather it is leap year or not\n")
# int_leapyear = int(leapyear)
# if int_leapyear % 4 == 0 and int_leapyear % 100 != 0:
#     print(f"{int_leapyear} is a leapyear")
# elif int_leapyear % 100 == 0:
#     print(f"{int_leapyear} is not a leapyear")
# elif int_leapyear % 400 == 0:
#     print(f"{int_leapyear} is a leapyear")
# else:
#     print(f"{int_leapyear} is not a leapyear")

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leapyear(year):
    """check leapyear and returns true or false"""
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False

def days_in_month(year,month):
    """if leapyear, returns month 2nd as 29"""
    if not 1<=month<=12:
        return 'not a month'
    if month==2 and is_leapyear(year):
        return 29
    else:
        return month_days[month-1]       
    
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


