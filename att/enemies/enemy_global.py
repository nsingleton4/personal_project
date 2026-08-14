from att.items.weapons import *
from att.items.clothes import *
from att.structural import *

class Enemy:
    def __init__(self, name="", weapon=None, armor=None, health=None, level=None, str=None, dex=None, con=None):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.health = health
        self.level = level
        self.str = str
        self.dex = dex
        self.con = con

str_calc = 10 + roll(d6=True)
dex_calc = 10 + roll(d6=True)
con_calc = 10 + roll(d6=True)

class Bandit(Enemy):
    def __init__(self, name=None, weapon=None, armor=None, health=None, level=None, str=None, dex=None, con=None):
        super().__init__(name, weapon, armor, health, level, str, dex, con)
        greatsword = Greatsword()
        self.weapon = greatsword

# e1 = Bandit()
# print(e1.weapon.atk_roll)
# assigns e1 to the bandit class and calls the attack roll characteristic from
# the weapon class greatsword to give a numeric value of the randomized roll

# e2 = Bandit()
# print(e2.weapon.atk_roll)


# ### this is how I can make it so I can easily update the classes and make multiple enemies with changing inventories
# e1 = Enemy("Nathan",
#            basic_spear,
#            basic_tunic,
#            10,
#            1,
#            str_calc,
#            dex_calc,
#            con_calc)
# print(e1.weapon)
# #
# # print(f"Your name is {e1.name} wielding a {e1.weapon} and wearing a {e1.armor}."
# #       f"\nYou feel healthy (hp: {e1.health}) and feel rather inexperienced (lvl: {e1.level}).")
#
# # this is how to change certain characteristics of a part of a class to update it as you go
# e1.weapon = "sword"
# print(e1.weapon)
