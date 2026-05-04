from tabnanny import check

from game.items.clothes import rough_leathers
from game.items.conventional_weapons import basic_spear
from game.enemies.bandit import bandit
from game.dice import roll_dice

# def start_intro():
#     current_node = attack["front_door"]
#
#     while True:
#         print(current_node["text"])
#
#         for i, choice in enumerate(current_node["choice"]):
#             print(f"{i + 1}: {choice['text']}")  # fixed quotes
#
#         user_input = int(input("Choose an option: ")) - 1
#         selected_choice = current_node["choice"][user_input]
#
#         if selected_choice.get("action") == "Attack the bandit!":
#             player_turn_tutorial_fight(player, bandit)
#             break

def scene_1(p1, p2=None):
    print(f"Hi, {p1["name"]}")
    print("You walk out the front door and see a bandit trying to rob you")
    action = input("What do you do? (attack or run)")
    if action.lower() == "attack":
        player_turn_tutorial_fight(p1, bandit)


attack = {
    "front_door": {
        "text": "\nYou walk out the front door and see a bandit trying to rob you",
        "choice": [
            {"text": "attack", "action": "player_turn_tutorial_fight"},
        ]
    }
}

def attack_roll(player, weapon):
    roll = weapon["attack_dice"]
    return roll + weapon["stat_bonus"] + player["statistics"]["dexterity"]


def damage_roll(weapon):
    return roll_dice(d6=True) + weapon["stat_bonus"]


def player_turn_tutorial_fight(player, bandit):
    while player["statistics"]["hp"] > 0 and bandit["statistics"]["hp"] > 0:
        print(f"\nYour HP: {player["statistics"]['hp']} | Bandit HP: {bandit["statistics"]['hp']}")
        print("1. Attack")
        print("2. Defend")

        choice = input("Choose your action: ")

        if choice == "1":
            weapon = player["inventory"]["weapons"]["basic_spear"]
            defense = bandit["inventory"]["clothes"]["rough_leathers"]["defense"]

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

        if bandit["hp"] > 0:
            print("\nThe bandit attacks!")
            player["statistics"]["hp"] -= 2  # placeholder damage
            print("You take 2 damage!")

    # result
    if player["statistics"]["hp"] <= 0:
        print("You lost!")
    else:
        print("You defeated the bandit!")

fight_success = {
    "defeated_bandit": {
        "text": """\nYou see the body of the bandit laying on the ground in front of you. 
        Just then, your friend Placeholder Name comes running up to you.""",
        "choice": [
            {"text": "Howdy how are ya?", "action": "say_hello"},
        ]
    }
}

say_hello = {
    "friend_talk": {

    }
}
