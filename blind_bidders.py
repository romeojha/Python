import os
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\,
                         `'-------'`
                       .-------------.
                      /_______________\,
''')

#variables
clear = lambda: os.system('clear')
##1improve loop=True
input_dict={}
init=0

#loop
while True:
    #input,dictionary
    who_bid=input("who wants to bid\n")
    to_bid=int(input("how much can you bid\n$"))
    input_dict[who_bid]=to_bid
    remaining=input("are there any remaining bidders left? 'yes' or 'no'\n").lower()

    if remaining=='no':
        break #1improved    
        ##1improve loop=False
    elif remaining=='yes':
        clear()

#funciton
def highest_bidder(dictionary,amount):
    for key in dictionary:
        value=dictionary[key]
        if value>amount:
            new_key=key
            amount=value
    print(f"the greatest bid is of {amount} dollars by {new_key}")

highest_bidder(dictionary=input_dict,amount=init)
