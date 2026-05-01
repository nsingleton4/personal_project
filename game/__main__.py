from game.dice import roll_dice
from game.player.player import player

p1 = player.copy()

name = input("What is your name\n Enter name >>> ")
p1["name"] = name
print(f'Hello {p1["name"]}')

# making the stats random until I can figure out how to allow the player to choose their stats later
dex = sum([roll_dice(d10 = True),
            roll_dice(d10 = True),
            roll_dice(d6 = True)])
wis = sum([roll_dice(d10 = True),
            roll_dice(d10 = True),
            roll_dice(d6 = True)])
cha = sum([roll_dice(d10 = True),
            roll_dice(d10 = True),
            roll_dice(d6 = True)])

p1["statistics"]["dexterity"] = dex
print(f'Your Dexterity in human form is {p1["statistics"]["dexterity"]}')
p1["statistics"]["wisdom"] = wis
print(f'Your Wisdom is {p1["statistics"]["wisdom"]}')
p1["statistics"]["charisma"] = cha
print(f'Your Charisma is {p1["statistics"]["charisma"]}')

print(p1)