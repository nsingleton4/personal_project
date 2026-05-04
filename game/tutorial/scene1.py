from tabnanny import check

from game.items.clothes import rough_leathers
from game.items.conventional_weapons import basic_spear
from game.enemies.bandit import bandit
from game.dice import roll_dice

def scene_1(p1, p2=None):
    print(f"Hi, {p1["name"]}")
    print("\n\nYou walk out the front door and see a bandit trying to rob you")
    action = input("What do you do? (attack or run) >>> ")
    if action.lower() == "attack":
        p1 = player_turn_tutorial_fight(p1, bandit)
    return p1


def attack_roll(player, weapons):
    return roll_dice(d20=True) + weapons["attack_bonus"] + player["statistics"]["dexterity"]


def damage_roll(weapons):
    return roll_dice(d6=True) + weapons["damage_bonus"]


def player_turn_tutorial_fight(player, bandit):
    while player["statistics"]["hp"] > 0 and bandit["statistics"]["hp"] > 0:
        print(f"\nYour HP: {player["statistics"]['hp']} | Bandit HP: {bandit["statistics"]['hp']}")
        print("1. Attack")
        print("2. Defend")

        choice = input("Choose your action: ")

        if choice == "1":
            weapon = player["inventory"]["weapons"]["spear"]
            defense = bandit["inventory"]["clothes"]["defense"]

            attack = attack_roll(player, weapon)
            print(f"You rolled {attack} to hit!")

            if attack > defense:
                damage = damage_roll(weapon)
                bandit["statistics"]["hp"] -= damage
                print(f"Hit! You deal {damage} damage!")
            else:
                print("Miss!")

        elif choice == "2":
            print("You defend!")

        if bandit["statistics"]["hp"] > 0:
            print("\nThe bandit attacks!")
            player["statistics"]["hp"] -= 2  # placeholder damage
            print("You take 2 damage!")

    if player["statistics"]["hp"] <= 0:
        print("You lost!")
    else:
        print("You defeated the bandit!")

    return player

