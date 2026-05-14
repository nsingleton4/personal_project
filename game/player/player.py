from game.structural import *
from game.items.weapons import *
from game.items.clothes import *


empty_player_dict = {
    "name": None,
    "statistics": {
        "dexterity": None,
        "wisdom": None,
        "charisma": None,
        "hp": 10
    },
    "inventory": {
        "weapons": None,
        "clothes": None
    },
    "position": None,
    "initiative": 1 + roll_dice(d6=True)
}

def roll_stat(stat_name):
    while True:
        stat_roll = 8 + roll_dice(d10=True)
        choice = input(f"Your {stat_name} is {stat_roll} (1: Accept or 2: Reroll) ").lower().strip()

        if choice == "1":
            return stat_roll
        elif choice == "2":
            continue
        else:
            print('Please type 1 (Accept) or 2 (Reroll)')

def character_creation():
    player = empty_player_dict.copy()
    name = input("\nWhat is your name?\n Enter name >>> ")
    player["name"] = name
    print(f'\nHello {player["name"]}')

    dex = roll_stat("Dexterity")
    wis = roll_stat("Wisdom")
    cha = roll_stat("Charisma")

    player["statistics"]["dexterity"] = dex
    slow_print(f'\nYour Dexterity is {player["statistics"]["dexterity"]}')
    player["statistics"]["wisdom"] = wis
    slow_print(f'Your Wisdom is {player["statistics"]["wisdom"]}')
    player["statistics"]["charisma"] = cha
    slow_print(f'Your Charisma is {player["statistics"]["charisma"]}')
    time.sleep(1.5)

    print(input("\nPress Enter to cont."))

    slow_print("You put on your tunic and grab your spear as you head out the door.\n")

    slow_print(ital("* Your tunic and spear have been added to your inventory *"))
    player["inventory"]["weapons"] = {"spear":basic_spear}
    player["inventory"]["clothes"] = {"shirt":basic_tunic}
    time.sleep(1.5)

    print(input("\nPress Enter to view your character sheet."))
    time.sleep(1)

    display_sheet(player)
    return player

def display_sheet(player):
    print(f"\nName: {player['name']}")
    print('\n -- Statistics -- ')
    for stat, value in player["statistics"].items():
        print(f"{stat.lower()}: {value}")
    print('\n -- Inventory -- ')
    for category, items in player["inventory"].items():
        print(f"{category.lower()}: {items}")



# # for the game, start with an empty dictionary
# player = dict()
# # player = {} -> this makes a dict but python doesn't like it
# # player["inventory"] = ... this resets the entire inventory
#
# player["inventory"] = {"items": {"dagger": "dagger of souls"}} # starting the dictionary, creates the dagger within the weapon class in the inventory
# player["inventory"]["items"]["swords"] = "sword of death" # this adds a sword cat in items and adds a sword in that cat
#
# print(player["inventory"]["items"]["dagger"]) # accesses what daggers are in the dict
#
# player["inventory"]["clothes"] = "shirt" # adds shirt into clothes key
# player["inventory"]["pouch"] = None # this adds a pouch key with nothing in it
# print(player["inventory"]["clothes"]) # accesses clothes key
# print(player["inventory"]["items"]["dagger"]) # accesses dagger key
# print(player["inventory"].keys()) # shows all keys within inventory
#

# print(p1["statistics"]["wisdom"])
# print(p1["name"])