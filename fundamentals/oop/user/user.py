class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        def display_info(self):
            print(self.first_name)
            print(self.last_name)
            print(self.email)
            print(self.age)
            print(self.is_rewards_member)
            print(self.gold_card_points)
        def enroll(self):
            self.is_rewards_member = True
            self.gold_card_points = 200
        def spend_points(self, amount):
            self.gold_card_points -= amount

user1=User("ahmed","ouni","aaaa@gmail.com",21)
user2=User("youssef","mosbehi","yyyy@gmail.com",21)
user1.display_info()
user1.enroll()
user1.display_info()
user1.spend_points(50)
user1.display_info()
user2.enroll()
user2.spend_points(80)
user2.display_info()
