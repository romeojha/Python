# from typing import Counter, KeysView
# import main

# # water=main.capacity['water']
# # coffee_beans=main.capacity['coffee']
# # milk=main.capacity['milk']
# empty_ingre = main.empty
# required_ingre = main.capacity
# espresso_ingre = main.MENU['espresso']['ingredients']
# latte_ingre = main.MENU['latte']['ingredients']
# cappuccino_ingre = main.MENU['cappuccino']['ingredients']
# print('cappuccino,latte,mocha')
# insert_money = float(input("how many one dollar bill to insert?\n"))
# condition = True


# def requirements(required_ingre, coffee_ingre):
#     temp1 = Counter(required_ingre)
#     temp2 = Counter(coffee_ingre)
#     return temp1-temp2

#     ###deproved version of same code####
#     # req={key: required_ingre[key]-coffee_ingre.get(key,0)
#     # for key in required_ingre.keys()}
#     # print(req)


# def money_check(coffee_):
#     return insert_money - main.MENU[coffee_]['cost']


# def ingre_compare(required_ingre, coffee_ingre):
#     for key in required_ingre:
#         if required_ingre[key] >= coffee_ingre[key]:
#             return True
#     return False


# def reduce(remaining):
#     if remaining >= 0 and ingre_compare(required_ingre, coffee_ingre):
#         print(f"take your coffee and your change of", remaining)
#         return remaining
#     else:
#         print("insufficient materials", required_ingre)
#         return False


# while condition:
#     coffee = input("which coffe you want:(cappuccino,latte,mocha)?\n")
#     if coffee == "off":
#         condition = False
#     elif coffee == 'report':
#         print(required_ingre)
#     elif coffee == 'cappuccino':
#         change = money_check(coffee_='cappuccino')
#         required_ingre = requirements(required_ingre, cappuccino_ingre)
#         condition = reduce(remaining=change)
#     elif coffee == 'latte':
#         change = money_check(coffee_='latte')
#         required_ingre = requirements(required_ingre, latte_ingre)
#         condition = reduce(remaining=change)
#     elif coffee == 'espresso':
#         change = money_check(coffee_='espresso')
#         required_ingre = requirements(required_ingre, espresso_ingre)
#         condition = reduce(remaining=change)
#     else:
#         print('pressed wrong')
from main import MENU, empty, capacity
from typing import Counter


def is_enough_resources(req_coffee, req_ingredent):
    for item in req_coffee:
        if req_ingredent[item] < req_coffee[item]:
            print(f"sorry,not enough {item}")
            return False
    return True


def coin_process():
    '''process given coin and return total money as float'''
    print('insert money')
    money = float(input('how many rupees: '))*1
    # money += float(input('how many quarters'))*.25
    print(f"you inserted total sum of {money}")
    return money


def drink_report():
    """returns dict of coffee machine capacity to hold items"""
    req = capacity
    return req


def can_do_transaction(inserted_money, required_money):
    global payment
    if inserted_money >= required_money:
        change = inserted_money-required_money
        print(f'transaction success. here is your change {change}')
        payment = change
        return True
    else:
        print(f"transaction failed. here is your refunded {inserted_money}")
        return False


def make_coffee(drink_name, req_ingredent, cof_ingredent):
    global required_ingredent
    par1 = Counter(req_ingredent)
    par2 = Counter(cof_ingredent)
    par1 -= par2
    required_ingredent = par1
    print(f'here is your {drink_name} coffee')


condition = True
required_ingredent = drink_report()

while condition:
    drink = input('which drink would you like(cappuccino/latte/espresso):  ')
    if drink == 'off':
        condition = False
    elif drink == 'report':
        print(required_ingredent)
    else:
        coffee = MENU[drink]
        if is_enough_resources(req_coffee=coffee['ingredients'], req_ingredent=required_ingredent):
            payment = coin_process()
            if can_do_transaction(inserted_money=payment, required_money=coffee['cost']):
                make_coffee(drink_name=drink, req_ingredent=required_ingredent,
                            cof_ingredent=coffee['ingredients'])
