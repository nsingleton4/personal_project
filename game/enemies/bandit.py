from game.items.conventional_weapons import worn_longsword
from game.items.clothes import rough_leathers
from game.structural import roll_dice

enemy = {
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
    "initiative": 1 + roll_dice(d6=True)
}