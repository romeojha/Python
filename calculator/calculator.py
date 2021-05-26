
number=float(input('input number\n'))
def calc(number):
    operator=input('which operator you want to use.\n + \n - \n / \n * \n')
    number2=float(input('input number\n'))
    if operator=="+":
        sum=number+number2
        return sum 
    elif operator=="-":
        sum=number-number2
        return sum 
    elif operator=="*":
        sum=number*number2
        return sum 
    elif operator=="/":
        sum=number/number2
        return sum

while True:
    result=calc(number)
    print(f'{result}')
    cont=input('continue with same calculation?"y" or "n" \n').lower()
    if cont=='y':
        number=result
    elif cont=='n':
        break


# condition=True 
# while condition:
#     func_operator=input('which operator you want to use.\n + \n - \n / \n * \n')
#     func_number2=float(input('input number\n'))

