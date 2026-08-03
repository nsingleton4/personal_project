class Arcane_spells:
    def __init__(self):
        self.spells_by_level = {
            1: ["Magic Missle", "Shield", "Burning Hands"],
            3: ["Find Familiar", "Fireball"]
        }

    def spells_on_lvl_up(self, level):
        """Return the list of spells available at this specific level"""
        return self.spells_by_level.get(level, [])