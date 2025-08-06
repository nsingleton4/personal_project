from game.characters.player_druid import Druid

druid = Druid()
druid.gain_experience(30)

print(druid.spells)

#set is immutable
myset = ("ss", "poo")

my_mutable_dict = {myset: "poop"}

#dictionarys are mutable and dynamic, can be used to add to inventory and update skills
druid.inventory["Helmet"] = 2
print(druid.inventory)

print(my_mutable_dict[("ss", "poo")])

# for loop
# check every number in a list

# Data Types

# int = 50
# float = 60.5
# string = "Hello World"
# list = ["geeks", "for", "geeks"]
# set = ("geeks", "for", "geeks")