import random
from game.enemies.bandit import enemy
from game.dice import roll_dice
from game.player.player import display_sheet
from game.supplemental.combat import miss_dict, hit_dict
from game.tutorial.scene_2 import scene_2

def scene_1(p1, p2=None):
    print("\n\nYou walk out the front door and see a bandit trying to rob you")
    print("What do you do?")
    print("1. Attack")
    print("2. Run")
    print("3. Display Character Sheet")
    action = input("Choose your action: ")
    if action.lower() == "1":
        tutorial_fight(p1, enemy)
    elif action.lower() == "2":
        escape(p1)
    elif action.lower() == "3":
        display_sheet(p1)
        return scene_1(p1)
    else:
        print("You must make another selection.")
        return scene_1(p1)

def attack_roll(player, weapons):
    return roll_dice(d20=True) + weapons["attack_bonus"] + (player["statistics"]["dexterity"]/2)

def damage_roll(weapons):
    return roll_dice(d6=True) + weapons["damage_bonus"]

def tutorial_fight(player, enemy):
    while player["statistics"]["hp"] > 0 and enemy["statistics"]["hp"] > 0:
        print(f"\nYour HP: {player["statistics"]['hp']} | Bandit HP: {enemy["statistics"]['hp']}")
        print("1. Attack")
        print("2. Check Character Sheet")

        choice = input("Choose your action: ")

        if choice == "1":
            print("\nYou ready and thrust your spear.")
            turn_taken = True
            weapon = player["inventory"]["weapons"]["spear"]
            defense = enemy["inventory"]["clothes"]["defense"]

            attack = int(attack_roll(player, weapon))
            print(f"\nYou rolled {attack} to hit!")

            if attack > defense:
                damage = damage_roll(weapon)
                enemy["statistics"]["hp"] -= damage
                print(hit_dict[random.randint(1,5)])
                print(f"You deal {damage} damage!")
            else:
                print(miss_dict[random.randint(1,5)])

        elif choice == "2":
            turn_taken = False
            display_sheet(player)

        if turn_taken and enemy["statistics"]["hp"] > 0:
            print("\nThe bandit flails around to hit you!")
            enemy_attack = roll_dice(d20=True)
            print(f"The bandit rolled a {enemy_attack} to attack!")
            player_defense = player["inventory"]["clothes"]["shirt"]["defense"]

            if enemy_attack > player_defense:
                enemy_dmg = roll_dice(d4=True)
                player["statistics"]["hp"] -= enemy_dmg
                print(f"You take {enemy_dmg} damage!")
            else:
                print("The bandit misses!")

    if player["statistics"]["hp"] <= 0:
        print("You lost!")
    else:
        print("You defeated the bandit!")

        scene_2(player)

def escape(player):
    print("""\nYou hear the bandit laughing as you run saying \x1B[3mI'm gonna get all your stuff!\x1B[0m""")
