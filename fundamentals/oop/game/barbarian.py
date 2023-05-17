from human import Human


class Barbarian(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health += 30
        self.strength += 20
        self.defense -= 5

    def rage(self, target):
        self.agility -= 1
        target.defend(self.strength*2)
        self.defend(self.strength)

        print("[Rage] " + self.name + "swings wildly")
        print("[Rage]" + self.name + " now has " + target.health + "HP")