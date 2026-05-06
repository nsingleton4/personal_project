import random
import time
from game.enemies.bandit import enemy
from game.player.player import display_sheet
from game.tutorial.scene_2 import scene_2
from game.structural import slow_print, ital, miss_dict, hit_dict, roll_dice
from game.player.transformations.earth import rock_monster


def transform_player(player, new_dict):
    transformed = player.copy()
    for key1 in player:
        if key1 in new_dict and type(new_dict[key1]) is dict:
            for key2 in player[key1]:
                if key2 in new_dict[key1]:
                    transformed[key1][key2] = new_dict[key1][key2]
        elif key1 in new_dict and type(new_dict[key1]) is str:
            transformed[key1] = new_dict[key1]

    return player, transformed

def attack_roll(player, weapons):
    return roll_dice(d20=True) + weapons["attack_bonus"] + (player["statistics"]["dexterity"]/2)

def damage_roll(weapons):
    return roll_dice(d6=True) + weapons["damage_bonus"]

def tutorial_fight(player, enemy, choice):
    while player["statistics"]["hp"] > 0 and enemy["statistics"]["hp"] > 0:
        slow_print(f"\nYour HP: {player["statistics"]['hp']} | Bandit HP: {enemy["statistics"]['hp']}")
        print("1. Attack")
        print("2. Check Character Sheet")

        choice = input("Choose your action: ")
        turn_taken = False

        weapon = player["inventory"]["weapons"]["spear"]
        e_def = enemy["inventory"]["clothes"]["defense"]
        if choice == "1":
            print(ital("\nYou ready and thrust your spear."))
            turn_taken = True
            attack = int(attack_roll(player, weapon))
            print(f"\nYou rolled {attack} to hit!")

            if attack > e_def:
                damage = damage_roll(weapon)
                enemy["statistics"]["hp"] -= damage
                slow_print(hit_dict[random.randint(1,5)])
                slow_print(f"You deal {damage} damage!")
            else:
                slow_print(miss_dict[random.randint(1,5)])

        elif choice == "2":
            display_sheet(player)
        else:
            print("Choose between the options")
            continue

        enemy_attack = roll_dice(d20=True)
        if turn_taken and enemy["statistics"]["hp"] > 0:
            slow_print("\nThe bandit flails around to hit you!")

            slow_print(f"The bandit rolled a {enemy_attack} to attack!")
            player_defense = player["inventory"]["clothes"]["shirt"]["defense"]

            if enemy_attack > player_defense:
                enemy_dmg = roll_dice(d4=True)
                player["statistics"]["hp"] -= enemy_dmg
                slow_print(f"You take {enemy_dmg} damage!")
            else:
                slow_print("The bandit misses!")

    if player["statistics"]["hp"] <= 0:
        slow_print("You lost!")
    else:
        slow_print("You defeated the bandit!")
        time.sleep(2)

        scene_2(player)

def new_guy_fight():
    pass

def escape(player):
    print("""\nYou hear the bandit laughing as you run saying \x1B[3mI'm gonna get all your stuff!\x1B[0m""")


def scene_1(p1, p2=None):
    time.sleep(2)
    slow_print("\n\nYou walk out the front door and see a bandit trying to rob you!")
    slow_print("What do you do?")
    print("1. Attack")
    print("2. Run")
    print("3. Display Character Sheet")
    print("4. Transform")
    action = input("Choose your action: ")
    if action.lower() == "1":
        tutorial_fight(p1, enemy)
    elif action.lower() == "2":
        escape(p1)
    elif action.lower() == "3":
        display_sheet(p1)
        return scene_1(p1)
    elif action.lower() == "4":
        new_guy_fight(p1)
    else:
        print("You must make another selection.")
        return scene_1(p1)
