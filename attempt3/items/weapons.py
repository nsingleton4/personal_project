from attempt3.enemies import enemy1_global
from structural import roll_dice

class One_Handed:
    def __init__(self, damage, reach):
        self.damage = damage
        self.reach = reach

    def damage_roll(self):
        damage = roll_dice(d10=True)
        modifier = enemy1_global.strength
        return damage + modifier

class Sword(One_Handed):
    def __init__(self, damage, reach):
        One_Handed.__init__(self, damage, reach)