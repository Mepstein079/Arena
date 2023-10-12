"""To-do list:
Fix action choices in the while loop
Re-organize so most code is not in an if statement
prompt the user inside the class functions
rearange probabilities so user is rewarded for not only attack
add mana/energy system to wizard and possibly other classes
"""

import random


print("Welcome to the Arena!!")
print("----------------------")


player_class = int(input("To pick your class enter 1, 2, or 3\n"
                    "1: Figher, 2: Wizard, 3: Juggernaut: "))


def fighter():
    hp = 18
    hp_increase = 2
    base_attack = (3, 6)
    big_attack = (5, 8)
    base_attack_double = base_attack * 2
    return hp, hp_increase, base_attack, big_attack, base_attack_double


def wizard():
    hp = 11
    hp_increase = 1
    base_attack = (6, 9)
    big_attack = (8, 11)
    even_bigger_attack = (10, 14)
    return hp, hp_increase, base_attack, big_attack, even_bigger_attack


def juggernaut():
    hp = 30
    hp_increase = 3
    base_attack = (2, 3)
    big_attack = (3,4)
    heal = (4,5)
    return hp, hp_increase, base_attack, big_attack, heal


if player_class == 1:
    hp, hp_increase, action1, action2, action3, user_choice = fighter()

elif player_class == 2:
    hp, hp_increase, action1, action2, action3, user_choice = wizard()

elif player_class == 3:
    hp, hp_increase, action1, action2, action3, user_choice = juggernaut()

else:
    print("Not an option")
con = None
level = 0

while level < 10:
    monster_hp = 35

    while (hp > 0) and (monster_hp > 0):
        action = user_choice

        chance = random.random()
        monster_damage = random.randint(2, 3)
        health_gain = random.randint(2, 5)
        monster_dmg_taken = 0
        player_dmg_taken = 0

        if action == "A1":
            if chance <=0.40:
                print(f"HIT! You dealt {player_damage} damage.")
                monster_hp -= player_damage
                monster_dmg_taken += player_damage
            elif chance < 0.85:
                print("Miss!")
            elif chance < 0.95:
                print(f"The Monster countered, dealing {monster_damage} damage")
                hp -= monster_damage
                player_dmg_taken += monster_damage
            else:
                print(f"CRITICAL HIT!! You dealt {player_damage * 2} damage.")
                monster_hp -= (player_damage * 2)
                monster_dmg_taken += (player_damage * 2)

        elif action == "A2":
            if chance <=0.35:
                print(f"HIT! You dealt {player_damage} damage.")
                monster_hp -= player_damage
                monster_dmg_taken += player_damage
            elif chance < 0.80:
                print("Miss!")
            elif chance < 0.95:
                print(f"The Monster countered, dealing {monster_damage} damage")
                hp -= monster_damage
                player_dmg_taken += monster_damage
            else:
                print(f"CRITICAL HIT!! You dealt {player_damage * 2} damage.")
                monster_hp -= (player_damage * 2)
                monster_dmg_taken += (player_damage * 2)

        elif action == "A3":
            if chance <=0.30:
                print(f"HIT! You dealt {player_damage} damage.")
                monster_hp -= player_damage
                monster_dmg_taken += player_damage
            elif chance < 0.85:
                print("Miss!")
            elif chance < 0.975:
                print(f"The Monster countered, dealing {monster_damage} damage")
                hp -= monster_damage
                player_dmg_taken += monster_damage
            else:
                print(f"CRITICAL HIT!! You dealt {player_damage * 2} damage.")
                monster_hp -= (player_damage * 2)
                monster_dmg_taken += (player_damage * 2)

        elif action == "D":
            if chance < 0.45:
                print("Success")
                print(f"You healed {health_gain} hp")
                hp += health_gain
            elif chance < 0.95:
                print("Failed")
                print(f"You took {monster_damage} damage")
                hp -= random.randint(2, 3)
            else:
                print("CRIT!!!")
                print(f"You took {monster_damage * 2} damage")
                hp -= (monster_damage * 2)
        else:
            print("Wrong input, you LOSE!")
            hp -= hp
        print("Your health:", hp)

    if hp < 0:
        print('You lose!')

    elif monster_hp < 0:
        print ("Congrats you win!")
        hp += player_dmg_taken + hp_increase
        monster_hp += monster_dmg_taken + 10

    con = input("Enter 'C' to continue, anything else to quit: ")
    
    if con == 'C':
        level += 1
