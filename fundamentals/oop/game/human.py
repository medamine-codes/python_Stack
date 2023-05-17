class Human:
    def __init__(self):
        self.name = "Your name"
        self.health = 100
        self.strength = 10
        self.agility = 10
        self.mana = 10
        self.defense = 5

    def attack(self, target):
        print("[Attack] " + self.name + " is attacking " + target.name)
        target.defend(self.strength)  # !abstraction

    def defend(self, damage):
        damage -= self.defense
        self.health -= damage
        print("[Defend] " + self.name + "takes " +
            str(damage) + " DMG and now has " + str(self.health))

    def display(self):
        print(self.name, self.health,)

