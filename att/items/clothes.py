class Armor:
    def __init__(self, name=None, defense=None):
        self.name = name
        self.defense = defense

class Tunic(Armor):
    def __init__(self, name=None, defense=None):
        super().__init__(name, defense)
        self.name = "Rough Tunic"
        self.defense = 10

class SteelPlate(Armor):
    def __init__(self, name=None, defense=None):
        super().__init__(name, defense)
        self.name = "Steel Plate"
        self.defense = 15

class DragonPlate(Armor):
    def __init__(self, name=None, defense=None):
        super().__init__(name, defense)
        self.name = "Pristine Dragon Plate"
        self.defense = 20