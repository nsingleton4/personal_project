from att.structural import *

class TwoHanded:
    def __init__(self, name=None, atk_roll=None, dmg_roll=None, level=None, abilities=None):
        self.name = name
        self.atk_roll = roll(d20=True)
        self.dmg_roll = dmg_roll
        self.level = level
        self.abilities = abilities

class Spear(TwoHanded):
    def __init__(self, name=None, atk_roll=None, dmg_roll=None, level=None, abilities=None):
        super().__init__(name, atk_roll, dmg_roll, level, abilities)
        self.dmg_roll = (roll(d8=True) * 2)

class Greatsword(TwoHanded):
    def __init__(self, name=None, atk_roll=None, dmg_roll=None, level=None, abilities=None):
        super().__init__(name, atk_roll, dmg_roll, level, abilities)
        self.dmg_roll = roll(d12=True)

class OneHanded:
    def __init__(self, name=None, atk_roll=None, dmg_roll=None, level=None, abilities=None):
        self.name = name
        self.atk_roll = roll(d20=True)
        self.dmg_roll = dmg_roll
        self.level = level
        self.abilities = abilities

class LongSword(OneHanded):
    def __init__(self, name=None, atk_roll=None, dmg_roll=None, level=None, abilities=None):
        super().__init__(name, atk_roll, dmg_roll, level, abilities)
        self.dmg_roll = ((roll(d4=True) * 2) + 2)

class ShortSword(OneHanded):
    def __init__(self, name=None, atk_roll=None, dmg_roll=None, level=None, abilities=None):
        super().__init__(name, atk_roll, dmg_roll, level, abilities)
        self.dmg_roll = roll(d8=True)

# spear_basic = Spear()
# spear_basic.name = "Trusty Spear"
# print(spear_basic.name, spear_basic.atk_roll)
#
# big_sword = Greatsword()
# print(big_sword.atk_roll)
