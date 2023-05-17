from human import Human

print(Human)


class Knight(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 120
        self.strength += 10
        self.mana -= 3
        self.defense += 5

    def heal(self):
        self.health = self.mana