import random
from att.player.player_global import *
from att.__main__ import *

def roll(d20=False, d12=False, d10=False, d6=False,d4=False):
    if d20:
        return random.randint(1,20)
    elif d12:
        return random.randint(1,12)
    elif d10:
        return random.randint(1,10)
    elif d6:
        return random.randint(1,6)
    elif d4:
        return random.randint(1,4)
    else:
        return None

e_names = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Elijah", "Sophia", "James"]

def display_sheet(var):
    print(p.name)
    print("\n -- Statistics -- \n")
    print(f"Strength: {p.str}, \nDexterity: {p.dex}, \nConstitution: {p.con}")
    print("\n --Inventory -- \n")
    print(f"Weapons: {p.weapon}, \nGear: {p.armor}, \nAccessories: {p.accessories}")
    return intro(p)

