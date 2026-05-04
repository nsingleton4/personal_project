from tabnanny import check

from game.items.clothes import rough_leathers
from game.items.conventional_weapons import basic_spear
from game.enemies.bandit import enemy_1
from game.dice import roll_dice
from game.player.player import display_sheet


def scene_1(p1, p2=None):
    print(f"Hi, {p1["name"]}")
    print("\n\nYou walk out the front door and see a bandit trying to rob you")
    print("What do you do?")
    print("1. Attack")
    print("2. Run")
    action = input("Choose your action: ")
    if action.lower() == "1":
        player_turn_tutorial_fight(p1, enemy_1)


def attack_roll(player, weapons):
    return roll_dice(d20=True) + weapons["attack_bonus"] + player["statistics"]["dexterity"]


def damage_roll(weapons):
    return roll_dice(d6=True) + weapons["damage_bonus"]


def player_turn_tutorial_fight(player, enemy):
    while player["statistics"]["hp"] > 0 and enemy_1["statistics"]["hp"] > 0:
        print(f"\nYour HP: {player["statistics"]['hp']} | Bandit HP: {enemy_1["statistics"]['hp']}")
        print("1. Attack")
        print("2. Defend")

        choice = input("Choose your action: ")

        if choice == "1":
            weapon = player["inventory"]["weapons"]["spear"]
            defense = enemy_1["inventory"]["clothes"]["defense"]

            attack = attack_roll(player, weapon)
            print(f"\nYou rolled {attack} to hit!")

            if attack > defense:
                damage = damage_roll(weapon)
                enemy_1["statistics"]["hp"] -= damage
                print(f"Hit! You deal {damage} damage!")
            else:
                print("Miss!")

        elif choice == "2":
            player["inventory"]["clothes"]["shirt"]["defense"] += 5
            print(f"Your defense increased to {player["inventory"]["clothes"]["shirt"]["defense"]}!")

        if enemy_1["statistics"]["hp"] > 0:
            print("\nThe bandit attacks!")
            enemy_1_attack = roll_dice(d20=True)
            print(f"The bandit rolled a {enemy_1_attack} to attack!")
            player_defense = player["inventory"]["clothes"]["shirt"]["defense"]

            if enemy_1_attack > player_defense:
                enemy_1_dmg = roll_dice(d6=True) - 2
                player["statistics"]["hp"] -= enemy_1_dmg
                print(f"You take {enemy_1_dmg} damage!")
            else:
                print("The bandit misses!")

    if player["statistics"]["hp"] <= 0:
        print("You lost!")
    else:
        print("You defeated the bandit!")

    display_sheet(player)

