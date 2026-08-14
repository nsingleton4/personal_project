from att.__main__ import *
from att.enemies.enemy_global import *
from att.player.player_global import *

def testing(p):
    e1 = Bandit()
    while p.health > 0 and e1.health > 0:
        print("You see a man walking up to you")
        swing = input("Press 1 to try and dodge the attack.")

        if swing == "1":
            print("You trust your spear")
            if e1.weapon.atk_roll > p.armor.defense
                e1_dmg = e1.weapon.dmg_roll
                p.health -= e1_dmg
                print(f'You were hit for {e1_dmg} damage')
            else:
                print("The fucker missed!")
        else:
            print("choose the correct response")
            continue

        if p.health <= 0:
            print("You lost")
        else:
            print("You defeated the bandit")