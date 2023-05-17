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
    def enroll(self):
        self.rewards_member=True
        self.gold_card_points=200
    def spend_points(self, amount) :
        self.gold_card_points= self.gold_card_points - amount

retii=User("retii","yayaya","tes@gmail.com",50)
youcef=User("youcef","yiyiyi","test2@gmail.tn",36)
retii.display_info()
retii.enroll()
retii.display_info()
retii.spend_points(50)
retii.display_info()
youcef.enroll()
youcef.spend_points(80)