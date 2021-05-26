import random
import game_data
import art


def random_choice():
    return random.choice(game_data.data)

#returns printable format of a data
def printing_data(user):
    user_name=user['name']
    user_country=user['country']
    user_decsri=user['description']
    return f'{user_name}, {user_decsri} from {user_country}'

def comparision(guess_option,A_followers,B_followers):
    if A_followers>B_followers:
        return 'A' if guess_option=='a' else 'C'
    elif B_followers>A_followers:
        return 'B' if guess_option=='b' else 'D'
    else:
        print('choose valid ')

print(art.logo)
score=0
user_a=random_choice()
user_b=random_choice()
while True:
    print(f"Compare A:{printing_data(user_a)}")
    print(art.vs)
    print(f"Compare B:{printing_data(user_b)}")
    guess=input('which one has higher followers: A or B\n').lower()
    follow_a=user_a['follower_count']
    follow_b=user_b['follower_count']

    a_or_b=comparision(guess_option=guess,A_followers=follow_a,B_followers=follow_b)
    if a_or_b=='A':
        score+=1
        print('you won with score',score)
        user_b=random_choice()
    elif a_or_b=='B':
        score+=1
        user_a=random_choice()
        print('you won .your score is',score)
    else:
        break

