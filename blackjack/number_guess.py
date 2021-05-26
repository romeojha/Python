import random
random_number=random.choice(range(200))
choice=input("easy or hard?")
condition=True
attempt=10 if choice=='easy' else 7

def printing(val='low'):
        print(f"you guessed {val}:{guess_number}")
        print(f"attempt left {attempt}")
def guessing():
    if guess_number<random_number:
        printing(val='low')
        return True
    elif guess_number>random_number:
        printing(val='high')
        return True
    if guess_number==random_number:
        print(f"your guess is right:{guess_number}")
        return False

           
while condition and attempt>0 :
    attempt-=1
    guess_number=int(input("guess number between 1 and 200\n"))
    if 0<guess_number<201:
        condition=guessing()
    else:
        print("not")
        break