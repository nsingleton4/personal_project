from game.dice import roll_dice

basic_spear = {
    "name": "Trusty Spear",
    "attack": 2,
    "damage": roll_dice(d6 = True) + 1
}