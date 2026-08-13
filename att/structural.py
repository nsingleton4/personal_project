import random
def roll(d20=False, d12=False, d10=False, d6=False,d4=False):
    if d20:
        return random.randint(1,20)
    elif d12:
        return random.randint(1,12)
    elif d10:
        return random.randint(1,10)
    elif d6:
        return random.randint(1,6)
    elif d4:
        return random.randint(1,4)
    else:
        return None
