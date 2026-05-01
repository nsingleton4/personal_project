from pprint import pprint as print

player = {
    "name": None,
    "statistics": {
        "dexterity": None,
        "wisdom": None,
        "charisma": None
    },
    "inventory": {
        "weapons": None,
        "clothes": None
    },
}

def display_player(player):
    print(f"Name: {player['name']}")

    print("\n -- Statistics --")
    for stat, value in player["statistics"].items():
        print(f"{stat.capitalize()}: {value}")

    print("\n -- Inventory --:")
    for category, items in player["inventory"].items():
        print(f"{category.capitalize()}: {items}")

display_player(player)
