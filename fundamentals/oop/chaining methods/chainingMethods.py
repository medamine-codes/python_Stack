class User:
    def init(self,name,lastname,email,age):
        self.first_name =name
        self.last_name =lastname
        self.email=email
        self.age = age
        self.rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print("first name",self.first_name)
        print("last name",self.last_name)
        print(" email",self.email)
        print("age",self.age)
        print("rewards member",self.rewards_member)
        print("gold card points",self.gold_card_points)
        return self
    def enroll(self):
        self.rewards_member=True
        self.gold_card_points=200
        return self
    def spend_points(self, amount):
        self.gold_card_points= self.gold_card_points - amount
        return self

ret3iy=User("ret3iy","yayaya","test@gmail.com",40)
youcef=User("youcef","yiyiyi","test2@gmm.tn",36)
ret3iy.display_info().enroll().display_info().spend_points(50).display_info().enroll().spend_points(80)