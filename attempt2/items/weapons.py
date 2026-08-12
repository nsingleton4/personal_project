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

class Spear:
    def __init__(self, dmg_dice=None, level=None, abilities=None):
        self.dmg_dice = dmg_dice
        self.level = level
        self.abilities = abilities

    def attack(self):
