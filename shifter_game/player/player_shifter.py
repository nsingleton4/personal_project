from tkinter.font import names

class Shifter:
    def __init__(self, name = "Character", age = 21, level = 1, experience = 1):
        self.name = name
        self.age = age
        self.level = level
        self.experience = experience

        #dictionaries
        self.transformations = {
            "Earth Elemental": self.level,
            "Fire Elemental": self.level,
            "Water Elemental": self.level,
            "Air Elemental": self.level
        }
        self.skills = {
            "Stealth": 1,
            "Athleticism": 1,
            "Personality": 1,
            "Herbalism": 1,
        }
        self.inventory = {
            "Alchemy Pouch": 1,
            "Cloak": 1,
            "Staff": 1
        }

    def check_level_up(self):
        while self.experience >= (10 * self.level):
            self.experience -= 10 * self.level
            self.level += 1
            self.health += 10
            print(f"You have leveled up! You are now level {self.level}.")

    def gain_experience(self, amount):
        self.experience += amount
        self.check_level_up()

    def display_sheet(self):
        print(f"\n=== Character Sheet: {self.name} ===")
        print(f"\nAge: {self.age}")
        print(f"\nLevel: {self.level}")
        print(f"\nHealth: {self.health}")
        print(f"\nExperience: {self.experience}\n")
        print("\n-- Skills --")
        for skill, level in self.skills.items():
            print(f"{skill}: {level}")
        print("\n-- Inventory --")
        for inventory in self.inventory:
            print(f'{inventory}: {self.inventory[inventory]}')
        print(f"\n-- Transformations --")
        for transformations in self.transformations:
            print(f'{transformations}: {self.transformations[transformations]}')
        print("\n-- Transformations Remaining Today --")
        for transformation in self.transformations:
            print(f'{self.level}')
