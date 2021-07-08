#creating a new class
class User:
    def __init__(self,user_id,username) -> None:
        self.id=user_id
        self.name=username
        self.followers=0
        self.following=0
    def follow(self,person):
        person.followers+=1
        self.following+=1

user1=User('01','rome')
user2=User('02','dxta')

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)