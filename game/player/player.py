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
        "weapons": {
            "staff": None
        },
        "clothes": {
            "shirt": None
        },
    },
}


# # for the game, start with an empty dictionary
# player = dict()
# # player = {} -> this makes a dict but python doesn't like it
# # player["inventory"] = ... this resets the entire inventory
#
# player["inventory"] = {"weapons": {"dagger": "dagger of souls"}} # starting the dictionary, creates the dagger within the weapon class in the inventory
# player["inventory"]["weapons"]["swords"] = "sword of death" # this adds a sword cat in weapons and adds a sword in that cat
#
# print(player["inventory"]["weapons"]["dagger"]) # accesses what daggers are in the dict
#
# player["inventory"]["clothes"] = "shirt" # adds shirt into clothes key
# player["inventory"]["pouch"] = None # this adds a pouch key with nothing in it
# print(player["inventory"]["clothes"]) # accesses clothes key
# print(player["inventory"]["weapons"]["dagger"]) # accesses dagger key
# print(player["inventory"].keys()) # shows all keys within inventory
#

# print(p1["statistics"]["wisdom"])
# print(p1["name"])