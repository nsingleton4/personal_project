from game.dice import roll_dice
from game.player.player import player
from game.items.conventional_weapons import basic_spear
from game.items.clothes import basic_tunic

p1 = player.copy()

name = input("\nWhat is your name\n Enter name >>> ")
p1["name"] = name
print(f'\nHello {p1["name"]}')

# making the stats random until I can figure out how to allow the player to choose their stats later
baseline = 10
dex = baseline + roll_dice(d10 = True) + roll_dice(d10 = True)
wis = baseline + roll_dice(d10 = True) + roll_dice(d10 = True)
cha = baseline + roll_dice(d10 = True) + roll_dice(d10 = True)

p1["statistics"]["dexterity"] = dex
print(f'Your Dexterity in human form is {p1["statistics"]["dexterity"]}')
p1["statistics"]["wisdom"] = wis
print(f'Your Wisdom is {p1["statistics"]["wisdom"]}')
p1["statistics"]["charisma"] = cha
print(f'Your Charisma is {p1["statistics"]["charisma"]}')

print(input("\nPress Enter to cont."))

print("""As you wake, your worn tunic slides over your chest, rough with years of abuse and sweat.
As you approach the door, you grab the spear given to you after the first time you mastered a form.\n""")

print("\x1B[3m* Your tunic and spear have been added to your inventory *\x1B[23m\n")
p1["inventory"]["weapons"] = basic_spear
p1["inventory"]["clothes"] = basic_tunic

print(p1["inventory"])


