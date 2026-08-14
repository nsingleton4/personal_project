from att.structural import *
from att.test.intro_v2 import *

class Player:
    def __init__(self, name="", weapon=None, armor=None, accessories=None, health=None, level=None, str=None, dex=None, con=None):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.accessories = accessories
        self.health = health
        self.level = level
        self.str = str
        self.dex = dex
        self.con = con
