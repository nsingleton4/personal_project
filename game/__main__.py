from game.dice import roll_dice
from game.player.player import empty_player_dict, display_sheet
from game.items.conventional_weapons import basic_spear
from game.items.clothes import basic_tunic
from game.tutorial.scene1 import scene_1
from game.structural import slow_print

def roll_stat(stat_name):
    while True:
        stat_roll = 8 + roll_dice(d10=True)
        choice = input(f"Your {stat_name} is {stat_roll} (1: Accept or 2: Reroll) ").lower().strip()

        if choice == "1":
            return stat_roll
        elif choice == "2":
            continue
        else:
            print('Please type "Accept" or "Reroll"')

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

    print(input("\nPress Enter to cont."))

    slow_print("You put on your tunic and grab your spear as you head out the door.\n")

    slow_print("\x1B[3m* Your tunic and spear have been added to your inventory *\x1B[23m")
    player["inventory"]["weapons"] = {"spear":basic_spear}
    player["inventory"]["clothes"] = {"shirt":basic_tunic}

    print(input("\nPress Enter to view your character sheet."))

    display_sheet(player)
    return player

def start():
    while True:
        begin = input("\nBegin adventure? (Yes or No) >>>  ")
        if begin.lower() == "yes":
            player = character_creation()
            scene_1(player)
            break
        elif begin.lower() in {'quit', 'no'}:
            break
        else:
            print("\n \"{}\" is not a valid entry. Begin adventure? (yes or no) >>>  ".format(begin))

if __name__ == "__main__":
    start()