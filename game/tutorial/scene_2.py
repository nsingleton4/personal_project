from game.player.player import display_sheet

def scene_2(player):
    print("\nYou see the bandit laying on the ground in front of you. Reeling from the combat, your friend rushes over.")
    print('Placeholder name says "Are you hurt? Here, let me help."')
    if player["statistics"]["hp"] < 10:
        print('\n*Placeholder name rubs a balm on your wounds and heals them.* They look at you and say "What happened?"')
        player["hp"] = 10
        print(f"Placeholder name has healed you back up to {player["hp"]} hit points!")
    else:
        print("""Placeholder name looks you over and says I don't see any damage. What happened?""")

    print("\nWhat do you say?")
    print("1. This man tried to steal my things and I had to defend myself.")
    print("2. He messed with the wrong guy. *kick his corpse*")
    print("3. Begin looting his corpse and say * I don't know but I'm about to find out *")
    choice = input("Choose your action: ")

    if choice == "1":
        print('\nPlaceholder name gives you a grim look and says "I am glad you are okay."')
    elif choice == "2":
        print('\nPlaceholder name looks in shock and says "What the fuck is wrong with you?"')
    elif choice == "3":
        print("\nScavenging through the body earns you a small note.")
        print("\x1B[3m* Bandit note has been added to your inventory *\x1B[23m")
        player["inventory"]["items"] = {"items": "Bandit's note"}

        display_sheet(player)
