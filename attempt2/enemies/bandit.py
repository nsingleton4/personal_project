from attempt2.items.weapons import worn_longsword
from attempt2.items.clothes import rough_leathers
from structural import roll_dice

bandit = {
    "name": "Bandit",
    "statistics": {
        "hp": 10,
        "dexterity": 5,
        "wisdom": 5,
        "charisma": 5
    },
    "inventory": {
        "weapon": worn_longsword,
        "clothes": rough_leathers
    },
    "position": [0,0],
    "initiative": 1 + roll_dice(d6=True)
}


class Bandit:
    def __init__(self, name, weapon, gear):
        self.name = name
        self.weapon = weapon
        self.gear = gear
    def equipment(self, inventory):
        inventory = roll_dice(d20=True)
        print(f"A bandit wearing a {self.gear} and wielding a {self.weapon} approaches you!")