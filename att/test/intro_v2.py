from att.enemies.enemy_global import *
from att.structural import *

def start_intro(var):
    print('''You see a bandit approaching you.
    He says "Oi mate fuck off."
    How do you respond?''')
    choice = input('''1. Tell him to fuck off. 
    2. Ask him politely to leave you alone.
    3. Ready your weapon.
    >>>''')
    if choice == "1":
        print("The bandit stares at you before lunging.")
        return tutorial_fight(var)
    elif choice == "2":
        print("The bandit stares at you before lunging.")
        return tutorial_fight(var)
    else:
        print("The bandit stares at you before lunging.")
        return tutorial_fight(var)

def tutorial_fight(var):
    e1 = Bandit()
    e1.name = "Goon"
    e1.str = 8 + roll(d6=True)
    e1.dex = 8 + roll(d6=True)
    e1.con = 8 + roll(d6=True)
    print(e1.name, e1.str, e1.dex, e1.con)
    print(f"At least give me the satisfaction of your name before I kill you. I am {e1.name}")
