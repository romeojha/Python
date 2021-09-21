# given_word=input("give a word as on which another player will guess.\n").lower()
# # guess_letter=input("guess the letter in the word given.\n")
# # random_words=["rome","haddi","kale","kajidon","romeo"]
# dash_value="_"
# # def dash():
# #     for i in range(0,len(given_word)):
# #         print(dash_value,end="")
# for i in range(len(given_word)):
#     d[i]=dash_value
#     print(d)
# # for letter in given_word:
#     display=dash_value
#     print(display)
    #     print('''
    #     ___________.._______
    # | .__________))______|
    # | | / /      
    # | |/ /       
    # | | /        
    # | |/         
    # | |          
    # | |          
    # | |         
    # | |        
    # | |        
    # | |        
    # | |        
    # | |          
    # | |            
        # ''')
import random
word_list=["suck","baboon","champion","rome"]
display=[]
random_value=random.randint(0,len(word_list)-1)
random_words=word_list[random_value]
print(f"the word is {random_words}") 


word_length=len(word_list[random_value])
for _ in range(word_length):
    display += "_"

condition=True  
while condition==True:
    print(display)
    user_guess=input("letter guess by second player\n").lower()
    for position in range(word_length):
        letter = random_words[position]
        if letter == user_guess:
            display[position]=letter

    if "_" not in display:
        condition=False
        print("you win")
    
    
print(display)

