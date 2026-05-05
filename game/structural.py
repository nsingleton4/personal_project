import time
import os

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def ital(text):
    return f"\x1B[3m{text}\x1B[23m"
def bold(text):
    return f"\x1B[1m{text}\x1B[22m"

miss_dict = {
    1: "You swing wide!",
    2: "The enemy dodges!",
    3: "Your attack misses!",
    4: "Your attack was parried!",
    5: "Your blow glances off harmlessly!"
}

hit_dict = {
    1: "Your strike lands cleanly!",
    2: "A solid hit connects!",
    3: "You slash through your enemy!",
    4: "Your weapon hits with force!",
    5: "A direct blow lands on target!"
}
