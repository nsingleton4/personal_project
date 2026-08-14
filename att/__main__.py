from att.structural import roll
from att.player.player_global import *
from att.test.intro_v2 import *
from att.test.test_fight import *

def intro(var):
    choice = input(f"Are you ready to begin {p.name}? 1. Yes, 2. No >>> ")

    if choice == "1":
        testing(var)
    elif choice == "2":
        print("Are you sure pooki")
        return intro(var)
    else:
        print("Try again later")

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
        p.weapon = Spear()
        p.armor = Tunic()
        return s_stat_roll, d_stat_roll, c_stat_roll, display_sheet(p)
    elif choice == "2":
        return make_player_1(p)
    else:
        print("Make a correct choice")
        return choice

def display_sheet(var):
    print(p.name)
    print("\n -- Statistics -- \n")
    print(f"Strength: {p.str}, \nDexterity: {p.dex}, \nConstitution: {p.con}")
    print("\n --Inventory -- \n")
    print(f"Weapons: {p.weapon}, \nGear: {p.armor}, \nAccessories: {p.accessories}")
    return intro(p)


n1 = input("What is your name? >>> ")
print(f"Hello {n1}!")
p = Player(name=n1)
make_player_1(p)