#list of cards in deck
#user bid,computer bid
#given 2 random number to you. both seen. dealer one card is shown. one hidden.
#if sum of list <21 . hit or stand. if hit and >21 lose; if hit and <21 . wanna hit again?
#if stand then compare both list. greater than but small than 21 wins.
#need to add bid to the game

import random

def random_generator():
    deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    # deck_len=len(deck)-1
    # rand=[]
    # int=random.randint(0,deck_len)
    rand=random.choice(deck)             #improved over 10-12
    return rand
random_generator()


udeck=[random_generator(),random_generator()]
cdeck=[random_generator()]
usum=sum(udeck)
print("your deck" ,udeck)
print("dealer deck" ,cdeck)
cdeck+=[random_generator()]
if sum(cdeck)<17:
    cdeck+=[random_generator()]
csum=sum(cdeck)
h_or_s=input('"hit" or "stand?"\n').lower()

# ubid=input('how much you wanna bid')

def dealer_won(usum):
    print(f"dealer won,dealer deck and is{cdeck},{csum}")
    print(f'you deck and sum is {udeck},{usum}')
def you_won(newsum):
    print(f"you won.you deck and sum is,{udeck} {newsum}")
    print(f"dealer deck and is,{cdeck} {csum}")
def draw(usum):
    print(f"draw. your deck:{udeck},{usum}\n dealer deck {cdeck},{csum}")


if h_or_s== 'hit':
    udeck+=[random_generator()]
    newsum=sum(udeck)
    if newsum>21 and 11 in udeck:
        udeck.remove(11)
        udeck.insert(0,1)
    if newsum>21 or csum>newsum:
        dealer_won(newsum)
    elif newsum<22 and newsum>csum:
        you_won(newsum)
    elif newsum==csum:
        draw(newsum)
    else:
        print('code fucks',newsum,csum)

elif h_or_s == 'stand':
    if usum>csum:
        you_won(usum)
    elif usum==csum:
        draw(usum)
    elif usum==21 and len(udeck)==2:
        print("blackjack",udeck,usum)
    elif usum<csum and csum<22:
        dealer_won(usum)
            


                   

