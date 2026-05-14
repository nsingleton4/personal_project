from game.enemies.bandit import bandit
from game.player.player import display_sheet
from game.tutorial.scene_2 import scene_2
from game.structural import *
from game.environment import *

def attack_roll(player, weapons):
    return roll_dice(d20=True) + weapons["attack_bonus"] + (player["statistics"]["dexterity"]/2)

def damage_roll(weapons):
    return roll_dice(d6=True) + weapons["damage_bonus"]


def tutorial_fight(player, bandit):
    while player["statistics"]["hp"] > 0 and bandit["statistics"]["hp"] > 0:
        slow_print(f"\nYour HP: {player["statistics"]['hp']} | Bandit HP: {bandit["statistics"]['hp']}")
        print("1. Attack")
        print("2. Check Character Sheet")

        choice = input("Choose your action: ")
        turn_taken = False

        weapon = player["inventory"]["weapons"]["spear"]
        e_def = bandit["inventory"]["clothes"]["defense"]
        if choice == "1":
            print(ital("\nYou ready and thrust your spear."))
            turn_taken = True
            p_attk = int(attack_roll(player, weapon))
            print(f"\nYou rolled {p_attk} to hit!")

            if p_attk > e_def:
                damage = damage_roll(weapon)
                bandit["statistics"]["hp"] -= damage
                slow_print(hit_dict[random.randint(1,5)])
                slow_print(f"You deal {damage} damage!")
            else:
                slow_print(miss_dict[random.randint(1,5)])

        elif choice == "2":
            display_sheet(player)
        else:
            print("Choose between the options")
            continue

        bandit_attack = roll_dice(d20=True)
        if turn_taken and bandit["statistics"]["hp"] > 0:
            slow_print("\nThe bandit flails around to hit you!")

            slow_print(f"The bandit rolled a {bandit_attack} to attack!")
            player_defense = player["inventory"]["clothes"]["shirt"]["defense"]

            if bandit_attack > player_defense:
                bandit_dmg = roll_dice(d4=True)
                player["statistics"]["hp"] -= bandit_dmg
                slow_print(f"You take {bandit_dmg} damage!")
            else:
                slow_print("The bandit misses!")

    if player["statistics"]["hp"] <= 0:
        slow_print("You lost!")
    else:
        slow_print("You defeated the bandit!")
        time.sleep(2)

        scene_2(player)


def escape(player):
    print("""\nYou hear the bandit laughing as you run saying "I'm gonna get all your stuff!" """)


def scene_1(player, app):
    time.sleep(2)
    slow_print("\n\nYou walk out the front door and see a bandit trying to rob you!")
    slow_print("What do you do?")
    print("1. Attack")
    print("2. Run")
    print("3. Display Character Sheet")
    action = input("Choose your action: ")
    if action == "1":
        old_pos = player["position"][:]
        player["position"] = [4,3]
        app.update_position(old_pos, player)
        return tutorial_fight(player, bandit),
    elif action == "2":
        return escape(player)
    elif action == "3":
        display_sheet(player)
        return scene_1(player)
    else:
        print("You must make another selection.")
        return scene_1(p1)



# def transform_player(player, new_dict):
#     transformed = player.copy()
#     for key, value in new_dict.items():
#         if isinstance(value,dict) and key in transformed:
#             #recuse in nested dicts
#             transformed[key] = transform_player(transformed[key], value)[1]
#         else:
#             transformed[key] = value
#     return player, transformed
