import random

def roll(d100=False, d20=False, d10=False,d6=False, d4=False):
    if d100:
        return random.randint(1,100),
    elif d20:
        return random.randint(1,20),
    elif d10:
        return random.randint(1, 10),
    elif d6:
        return random.randint(1, 6),
    elif d4:
        return random.randint(1, 4),
    else:
        print("Choose either d100, d20, d10, d6, or d4.")
        return

