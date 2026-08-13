from att.structural import *

class Player:
    def __init__(self, name="", weapon=None, armor=None, accessories=None, health=None, level=None, str=None, dex=None, con=None):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.accessories = accessories
        self.health = health
        self.level = level
        self.str = str
        self.dex = dex
        self.con = con

def make_player_1(var):
    s_stat_roll = 10 + roll(d6=True)
    d_stat_roll = 10 + roll(d6=True)
    c_stat_roll = 10 + roll(d6=True)

    choice = input(f"Your Strength score is {s_stat_roll}. \nYour Dexterity score is {d_stat_roll}. "
                   f"\nYour Constitution is {c_stat_roll}. \n\nAccept (1) or Reroll (2)? >> ")

    if choice == "1":
        p.str = s_stat_roll
        p.dex = d_stat_roll
        p.con = c_stat_roll
        return s_stat_roll, d_stat_roll, c_stat_roll, display_sheet(p)
    elif choice == "2":
        return make_player_1(var)
    else:
        print("Make a correct choice")
        return choice

def display_sheet(var):
    print(p.name)
    print("\n -- Statistics -- \n")
    print(f"Strength: {p.str}, \nDexterity: {p.dex}, \nConstitution: {p.con}")
    print("\n --Inventory -- \n")
    print(f"Weapons: {p.weapon}, \nGear: {p.armor}, \nAccessories: {p.accessories}")
    return

n1 = input("What is your name? >>> ")
print(f"Hello {n1}!")
p = Player(name=n1)
make_player_1(p)