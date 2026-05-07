import random

def roll():
    roll_1 = random.randint(1,2)
    if roll_1 == 1:
        print("Heads")
    else:
        print("Tails")

roll()