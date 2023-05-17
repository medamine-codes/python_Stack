from barbarian import Barbarian
from knight import Knight


barb = Barbarian("Olaf")
knight = Knight("Arthur")

#displaying infos
barb.display()
knight.display()

target = input('give me the target (K/B)')

if target == "K":
    while knight.health > 0:
        barb.attack(knight)
        if knight.health<=0:
            print("knight is dead")
else:
    while barb.health > 0:
        knight.attack(barb)
        if barb.health<=0:
            print("barb is dead")



