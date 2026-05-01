# player is a dictionary rather than a class
# all transformations, stats, and abilities will be dictionaries as well

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

def display_sheet(player):
    print(f"\nName: {player['name']}")
    print() # blank line
    print(' -- Statistics -- ')
    for stat, value in player["statistics"].items():
        print(f"{stat.capitalize()}: {value}")
    print()
    print(' -- Inventory -- ')
    for category, items in player["inventory"].items():
        print(f"{category.capitalize()}: {items}")



# # for the game, start with an empty dictionary
# player = dict()
# # player = {} -> this makes a dict but python doesn't like it
# # player["inventory"] = ... this resets the entire inventory
#
# player["inventory"] = {"items": {"dagger": "dagger of souls"}} # starting the dictionary, creates the dagger within the weapon class in the inventory
# player["inventory"]["items"]["swords"] = "sword of death" # this adds a sword cat in items and adds a sword in that cat
#
# print(player["inventory"]["items"]["dagger"]) # accesses what daggers are in the dict
#
# player["inventory"]["clothes"] = "shirt" # adds shirt into clothes key
# player["inventory"]["pouch"] = None # this adds a pouch key with nothing in it
# print(player["inventory"]["clothes"]) # accesses clothes key
# print(player["inventory"]["items"]["dagger"]) # accesses dagger key
# print(player["inventory"].keys()) # shows all keys within inventory
#

# print(p1["statistics"]["wisdom"])
# print(p1["name"])