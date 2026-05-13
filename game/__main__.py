from game.player.player import *
from game.tutorial.scene1 import scene_1

def start():
    while True:
        begin = input("\nBegin adventure? (Yes or No) >>>  ")
        if begin.lower() == "yes":
            player = character_creation()
            scene_1(player)
            break
        elif begin.lower() in {'quit', 'no'}:
            break
        else:
            print("\n \"{}\" is not a valid entry. Begin adventure? (yes or no) >>>  ".format(begin))

if __name__ == "__main__":
    start()
