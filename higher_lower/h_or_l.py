from game_data import data
import random
import art

def rand_int():
    '''returns random number from 0-49'''
    return random.choice(range(len(data)))

def celb(random_int, which):
    '''returns print statement and celibrity followers as statement,follow'''
    celb_name=data[random_int]['name']
    celb_follower=data[random_int]['follower_count']
    celb_discri=data[random_int]['description']
    celb_country=data[random_int]['country']
    return (f"{which}:{celb_name}, a {celb_discri} from {celb_country}"),celb_follower

def compare(follow1,follow2):
    '''compare followers which is passed and return true false'''
    return True if follow1>follow2 else False
    #also can be written as: return follow>follow2


statement1,follow1=celb(random_int=rand_int(),which= 'A')
statement2,follow2=celb(random_int=rand_int(),which= 'B')
score=0
print(art.logo)
while True:
    print(f'which one is higher? A or B ')
    print(statement1,follow1)
    print(art.vs)
    print(statement2,follow2)
    a_or_b=input('').upper()
    if a_or_b=='A' and compare(follow1,follow2):
        statement2,follow2=celb(random_int=rand_int(),which= 'B')
        score+=1
        print(f'you won. your score is:{score}')
    elif a_or_b=='B' and not compare(follow1,follow2):
        statement1,follow1=celb(random_int=rand_int(),which= 'A')
        score+=1
        print(f'you won. your score is:{score}')
    else:
        print(f'you lose.your final score is:{score}')
        break
