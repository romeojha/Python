# row1 = ['a', 'b', 'c', 'd', 'e']
# row2 = ['f', 'g', 'h', 'i', 'j']
# row3 = ['k', 'l', 'm', 'n', 'o']
# row4 = ['p', 'q', 'r', 's', 't']
# row5 = ['u', 'v', 'w', 'x', 'y']
# merged_row = [row1, row2, row3, row4, row5]
# print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
# position = int(input('enter the row,column position\n'))
# position2 = int(input('enter column postion\n'))
# print('\n', merged_row[position-1][position2-1])


# print('# from angela')
# row1 = ['a', 'b', 'c', 'd', 'e']
# row2 = ['f', 'g', 'h', 'i', 'j']
# row3 = ['k', 'l', 'm', 'n', 'o']
# row4 = ['p', 'q', 'r', 's', 't']
# row5 = ['u', 'v', 'w', 'x', 'y']
# merged_row = [row1, row2, row3, row4, row5]
# print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")
# position = input("enter row and column\n")
# vertical = int(position[0])
# horizontal = int(position[1])
# merged_row[vertical-1][horizontal-1] = 'FUCK'
# print(merged_row[vertical-1][horizontal-1])
# print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")


import random
rock = 'rock'
scissor = 'scissor'
paper = 'paper'
list = ['', rock, paper, scissor]
which = int(input("1 for rock/2 for paper/3 for scissor\n"))
random_number = random.randint(1, 3)
if 4 > which > 0:
    print("you choose:")
    print(list[which])
    print(f"computer choose")
    print(list[random_number])
    compare = [which, random_number]
    if compare[0] == compare[1]:
        print("its a draw")
    elif compare[0] == 1 and compare[1] == 3:
        print("you win")
    elif compare[0] == 3 and compare[1] == 1:
        print("you lose")
    elif 3 > compare[0] > compare[1] > 0:
        print("you win")
    elif 3 > compare[0] < compare[1] > 0:
        print("you lose")
    else:
        print("invalid")
else:
    print("wrong order")
