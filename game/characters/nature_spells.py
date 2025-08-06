class NatureSpells:
    def __init__(self):
        self.spells_by_level = {
            1: ["Entangle", "Speak to Animals and Plants", "Cure Light Wounds", "Create or Destroy Water"],
            3: ["Call Lightning", "Summon Friend", "Cure Wounds", "Mold Earth"]
        }

        self.lvl_1_ns_desc = {
        'Entangle': "Vines and plants grow from the earth. Restrain a targets movement for 1 turn upon a failed save.",
        'Speak to Animals and Plants': "Gain the ability to communicate with creatures that are normally unable to speak.",
        'Cure Light Wounds': "Gain back 15% of lost hit points.",
        'Create or Destroy Water': "Create or destroy a 3 meter cube of water."
        }



if input(nature_spells.spells_by_level, ns_spell_name):
    return lvl_1_ns_desc

    def spells_on_lvl_up(self, level):
        """Return the list of spells available at this specific level"""
        return self.spells_by_level.get(level, [])


    def ns_desc(self, spell_name):
        return self.lvl_1_ns_desc.get(spell_name)