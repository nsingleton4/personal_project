from game.dice import roll_dice
from game.player.player import empty_player_dict, display_sheet
from game.items.conventional_weapons import basic_spear
from game.items.clothes import basic_tunic
from game.tutorial.scene1 import scene_1

def character_creation():
    player = empty_player_dict.copy()
    name = input("\nWhat is your name?\n Enter name >>> ")
    player["name"] = name
    print(f'\nHello {player["name"]}')

    # making the stats random until I can figure out how to allow the player to choose their stats later
    baseline = 5
    dex = baseline + roll_dice(d10=True)
    wis = baseline + roll_dice(d10=True)
    cha = baseline + roll_dice(d10=True)

    player["statistics"]["dexterity"] = dex
    print(f'Your Dexterity in human form is {player["statistics"]["dexterity"]}')
    player["statistics"]["wisdom"] = wis
    print(f'Your Wisdom is {player["statistics"]["wisdom"]}')
    player["statistics"]["charisma"] = cha
    print(f'Your Charisma is {player["statistics"]["charisma"]}')

    print(input("\nPress Enter to cont."))

    print("You put on your tunic and grab your spear as you head out the door.\n")

    print("\x1B[3m* Your tunic and spear have been added to your inventory *\x1B[23m")
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