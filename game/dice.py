import random

def roll_dice(d20=False, d10=False, d6=False, d4=True, number = 1):
    if d20:
        return random.randint(1,20)
    elif d10:
        return random.randint(1,10)
    elif d6:
        return random.randint(1,6)
    elif d4:
        return random.randint(1,4)
    else:
        print("No dice chosen")


if __name__ == "__main__":
    print(roll_dice(d20 = True))
