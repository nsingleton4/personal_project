from game.player.player import display_sheet
from game.structural import *
import time

def scene_2(player):
    slow_print("\nYou see the bandit laying on the ground in front of you. Reeling from the combat, your friend rushes over.")
    slow_print('Niki says "Are you hurt? Here, let me help."')
    time.sleep(1)
    if player["statistics"]["hp"] < 10:
        slow_print(ital('\n* Niki rubs a balm on your wounds and heals them.*'))
        slow_print('She looks at you and say "What happened?"')
        player["hp"] = 10
        slow_print(ital(f"Niki has healed you back up to {player["hp"]} hit points!"))
    else:
        print("""Niki looks you over and says "I don't see any damage. What happened?" """)

    slow_print("\nWhat do you say?")
    slow_print("1. This man tried to steal my things and I had to defend myself.")
    slow_print("2. He messed with the wrong guy. *kick his corpse*")
    slow_print("""3. Begin looting his corpse and say "I don't know but I'm about to find out" """)
    choice = input("Choose your action: ")
    time.sleep(1.5)

    if choice == "1":
        slow_print("""\nNiki gives you a grim look and says "I'm glad you're okay." """)
    elif choice == "2":
        slow_print('\nNiki looks in shock and says "What the fuck is wrong with you?"')
    elif choice == "3":
        slow_print(ital("\nScavenging through the body earns you a small note."))
        slow_print(ital("* Bandit note has been added to your inventory *"))
        player["inventory"]["items"] = {"items": "Bandit's note"}

        display_sheet(player)
