play = input(
    "this is the adventure destiny game.\nEnter 'play' or 'exit' to do the same\n")
print(''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       __ _ __`~^~`~^^~`~^~`~^^~`~^~`~^^~____    ,~~`~~_`~^~`~^^~`~^~`~^^~`~^~`~^^~
   ,'`  /      \~-~^~^~`~^~` ____________/    \,-`        /`~^~`~^^~`~^~`~^^~`~^~`~^^~
 ,'     |       \~~boat\/~~~ \/Beach                     /`~^~`~^^~`~^~`~^^~`~^~`~^^~
(destiny|        \^~^~`~^~`/                            /v`~^~`~^^~`~^~`~^^~`~^~`~^^~
 \   _ _|        /~~^~^^~/                       \/Newcastle`~^~`~^^~`~^~`~^^~
  (_/   |__ _ __/ ~^~^~`| \/brokenHill  # # # #       /`~^~`~^^~`~^~`~^^~`~^~`~^^~
`~^~`~^^~`~^~`~^^~ `~^~`|              #    #       /`~^~`~^^~`~^~`~^^~`~^~`~^^~
`~~`~^~`~^^~~^~`~^~`~^^.|              #   #       / `~^~`~^^~`~^~`~^^~`~^~`~^^~
`~^~`~^^~`~^~`~^^~`~^~,' \_____        #  #    \/start`~^~`~^^~`~^~`~^^~`~^~`~^^~
 `~^~`~^^`~^~`~^^~`~^~`~^^~`~^~'\_,~~~, # #      /`~^~`~^^~`~^~`~^^~`~^~`~^^~
  ~~-~^~^~`~^~`~^^~^~-^~^~^~-~`~^~``~  \_#      /`~^~`~^^~`~^~`~^^~`~^~`~^^~
 ~^~ ~~-^`~^~`~^^~~^~-^~^~^~-~^~^`~^~`~^^\_|   /`~^~`~^^~`~^~`~^^~`~^~`~^^~
  ~^~`~~-~^~^~`~^^~^~-^~^~^~-~^~^`~^~`~^^~`\../ ~^^~`~^~`~^^~''')


if play == 'play':
    print("Rules/process\n 1.you must avoid hash and look map to find the way out\n 2.you only have one half of map to guide you\n 3.you will get real world rewards if you reach your destiny\n 4.each travel takes one day")
    male_female = input("enter :'male'\n")
    if male_female == 'male':
        print('''
                            ___/""\     
                               oo##
                              `-6 #
                               ,'`.
                              // `\\
                             ||o   \\
                              \-+--//
                              :_|_(/
                            ..--:: :..
                            |..|   |..| ''')
        r_or_left = input(
            "you are at the start point facing the hash(###)(look given map for reference).\nyou have handful of foods to survive on this journey\n\n Take 'left' or 'right'?")
        if r_or_left == 'right':
            print("you reached New castle after a day of travel.")
            print('''
                                                                              
                                                                              
                                 ____                                         
                              .-"    `-.      ,                               
                            .'          '.   /j\                              
                           /              \,/:/#\                /\           
                          ;              ,//' '/#\              //#\          
                          |             /' :   '/#\            /  /#\         
                          :         ,  /' /'    '/#\__..--""""/    /#\__      
                           \       /'\'-._:__    '/#\        ;      /#, """---
                            `-.   / ;#\']" ; """--./#J       ':____...!       
                               `-/   /#\  J  [;[;[;Y]         |      ;        
""""""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |        
             ""--.. _.--""     /      ,/#\'-..____.;_,   |    |   '  |        
                   "-.        :_....___,/#} "####" | '_.-",   | #['  |        
                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        
                      ,   `-.   |        :     _   .;'    /;\ |   #" |        
                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        
                     .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
          .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      
        i__..'%] _:_   ;##J         \      :"#...._!   '  "  "|__  |    `--.._
         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._    
     ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;  
   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  
    |""": |   /   \|   .----+  ;      /#\  :___..--"";                  ,'MM; 
   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; 
  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM  
  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
  |          :     |______                        ___!_ "#""#""#"""#"""#"""|  
__|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
  "\-.      :      |#                                  :                   |  
    /#'.    |      /##,                                !                   |  
   .',/'\   |       #:#,                                ;       .==.       |  
  /"\'#"\',.|       ##;#,                               !     ,'||||',     |  
        /;/`:       ######,          ____             _ :     M||||||M     |  
       ###          /;"\.__"-._   """                   |===..M!!!!!!M_____|  
                           `--..`--.._____             _!_                    
                                          `--...____,="_.'`-.____        
''')
            enter = input(
                "you found more foods,bag and a rope in Newcastle.\ndo you want to keep it?(y/n)\n")
            if enter == 'y':
                print("your have bag full of food and you have rope with you.")
                r_or_left = input("do you want to go 'left' or 'right'?")
                if r_or_left == 'left':
                    print("you travelled for one day to reach the beach")
                    print('''
        ... ....                     .. ...           
  .. ...... .                           ........__    
...                                      ......|__|   
                                             /|. .    
            ,d888b,                          / |\     
           J8888888L                        /^^|^\    
           888888888                     __/___|__\_  
`~^~`~^^~^~-^~^~^~-~^~`~^~`~^^~^~-^~`~~`L\-`--------'-
      - -__--__--__--__ -       `~^~`~^^~^~-^~^~^~-~^~   
       - __--__--__-- _       
        _ -__--__--_ -              |:     ::.        
          - _--__- _                |/       ::.      
           _ --__ -                 /'         :`--.__
      .--.  _ -_ -                 /'   ._ .     ``   
    _/____\_               _,-'   __/. .... .  .      _              
      |OO|
      |()|
 .----\""/----.
 |     \/     |
 | |    .   | |
 | |    .   | |____/__
 \ \    .   (_____/_=
  \ \       \,
   \/\=[]===)
   (""\     |
   |   |_/  |
   |   |    |
   
''')

                    print("you reached the beach,there is a boat in middle of river(but the sea is vast)\na trader on the beach\n a sign directing to broken hill(unknown land with no proof of survival).\n 1.do you want to 'swim' to get the boat?\n 2.do you want to 'trade' your leftover foods with trader for new boat?\n 3.do you want to go to 'brokenhill' to collect foods?")
                    s_t_b = input("enter 'swim' or 'trade' or 'brokenhill'\n")
                    if s_t_b == 'trade':
                        print(
                            "you traded your leftover food with trader\n now you are in your journey to unknown island.")
                        print('''
                   ~;
                  ,/|\,
                ,/' |\ \,
              ,/'   | |  \,
            ,/'     | |   |
          ,/'       |/    |
        ,/__________|-------,
       ___..........''-----/
       \                  /
   ~~-~^~~^~^^~`~^~`~^^~^~-^~^~^~-^~`~^~`~^^~^~-^~^~^~-^~`~^~`~^^~^~-^~^~^~-
''')
                        enter = input(
                            "you reached this new bizzare island after one day.\n no food, no animals but something strange about this place\n do you want to continue?(y/n)\n")
                        print('''


                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::.\\
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-'
   "  / |  :' :/""\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\.___./'-.
    / :/|\ :\_:\   \#//\            /  |  
    |:/ | ""--':\   (#//)              '
    \/  \ :|  \ :\  (#//)
         \:\   '.':. \#//\\
          ':|    "--'(#///)
                     (#///)
                     (#///)            /""\     
                      \#///\           #oo#
                      (##///)          \__/
                      (##///)          ,'`.
                      (##///)         // `\\
                      (##///)        ||o   \\
                       \##///\        \-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__'''
                              ''''   __;: :            "-._
          __..--""                  `---/ ;                '._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     """--...  ___"""""-----......._______......----"""     --"""
                   """"       ---.....   ___....----

''')

                        if enter == 'y':
                            print(
                                "you are hungry.after walking for one day,you found three path  and three boards\nstraight says'4days' left says'3days' right says'5days'.they all meant your survival days from begining")
                            threeway = input(
                                "do you want to go 'straight' or ' right' or 'left' ?")
                            if threeway == 'straight':
                                print("you found the treasure named 'DESTINY' \n")
                                print('''

                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
            ./   _/ \_     <_o#\__/#o_>     _/ \_   \.
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|========================|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{  DESTINY  }=====|o|===|
              | __/ \__     ...........    __/ \__ |
              |====================================|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`

                            ''')
                                treasure = input(
                                    "do you want to open DESTINY?(y/n)\n")
                                if treasure == 'y':
                                    print('''
                    /"""\
                    |\./|
                    |   |
                    |   |
                    |>~<|
                    |   |
                 /'\|   |/'\..
             /~\|   |   |   | \
            |   =[@]=   |   |  \
            |   |   |   |   |   \
            | ~   ~   ~   ~ |`   )
            |                   /
             \                 /
              \               /
               \    _____    /
                |--//''`\--|
                | (( +==)) |
                |--\_|_//--|
                              ''')
                                    print("you create your own DESTINY")
                            else:
                                print(
                                    "you missed the hint throughout the game. you can try again")
                        else:
                            print("you quit at final stage")
                    elif s_t_b == 'swim':
                        print(
                            "you went to swimming to get the nearest boat and killed by sea animals")
                    elif s_t_b == 'brokenhill':
                        print(
                            'it took one day to reach broken hill.\nnothing in broken hill. your only option is to return')
                        print('you die with starvation')
                    else:
                        print("you pressed wrong")
                else:
                    print(
                        "you are out of map. you will die starving and cannot enter the game")
            elif enter == 'n':
                R_or_L = input("do you want to go 'left' or 'right'?")
                if R_or_L == 'right':
                    print("you are out of map. you will die starving")
                else:
                    print(
                        "you choose right path but you are starving and cannot survive this game.\nyou will die soon")
        else:
            print("you died. Hash kiled you ")
    else:
        print("you quit, you cannot try again or try again if you like")
else:
    print("you quit, you cannot try again or try again if you like")
