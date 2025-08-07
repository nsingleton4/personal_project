from characters.nature_spells import NatureSpells

class Druid:
    def __init__(self, name="Character", age=25, level = 1, experience = 0):
        self.name = name
        self.age = age
        self.level = level
        self.experience = experience
        self.attributes = {
            "Wisdom": 10,
            "Resolve": 10
        }
        self.health = self.attributes["Resolve"] * 10
        self.casts_per_day = self.level * int(self.attributes["Wisdom"] / 2)
        self.spells = []
        self.nature_spells = NatureSpells()

        # dictionary
        self.skills = {
            "Druidism": 1,
            "Herbalism": 1,
            "Animal Empathy": 1
        }

        # dictionary
        self.inventory = {
            "Alchemy Pouch": 1,
            "Cloak": 1,
            "Staff": 1
        }

    def get_spells(self):
        #try avoids having the wrong key
        try:
            self.spells.extend(self.nature_spells.spells_by_level[self.level])
        except KeyError:
            return
        #sets can only have 1 item, eliminates duplicates
        self.spells = list(set(self.spells))
        return self.spells

    def gain_experience(self, amount):
        self.experience += amount
        self.check_level_up()

    def check_level_up(self):
        while self.experience >= (10 * self.level):
            self.experience -= 10 * self.level
            self.level += 1
            self.health += 10
            print(f"You have leveled up! You are now level {self.level}.")
            self.spells = self.get_spells()

    def display_sheet(self):
        print(f"\n=== Character Sheet: {self.name} ===")
        print(f"\nAge: {self.age}")
        print(f"\nLevel: {self.level}")
        print(f"\nHealth: {self.health}")
        print(f"\nExperience: {self.experience}\n")
        print("\n-- Skills --")
        for skill, level in self.skills.items():
            print(f"{skill}: {level}")
        print("\n-- Spells --")
        for spell in self.get_spells():
            print(f"{spell}")
        print("Casts per day -", self.casts_per_day)
        print("\n-- Inventory --")
        for inventory in self.inventory:
            print(f'{inventory}: {self.inventory[inventory]}')