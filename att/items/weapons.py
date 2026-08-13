from att.structural import roll
basic_spear = {
    "name": "Trusty Spear",
    "attack_dice": "d20",
    "damage_dice": "d6",
    "attack_bonus": 2,
    "damage_bonus": 1,
    "scaling": "dexterity"
}

worn_longsword = {
    "name": "Worn Longsword",
    "attack_dice": "d20",
    "damage_dice": "d6",
    "attack_bonus": 0,
    "damage_bonus": 0,
    "scaling": "dexterity"
}

class TwoHanded:
    def __init__(self, name = "", atk_dice=None, dmg_dice=None, level=None, abilities=None):
        self.name = name
        self.atk_dice = atk_dice
        self.dmg_dice = dmg_dice
        self.level = level
        self.abilities = abilities

class Spear(TwoHanded):
    def __init__(self):
        super().__init__()

class Greatsword(TwoHanded):
    def __init__(self):
        super().__init__()

spear_basic = Spear()

print(spear_basic.name)