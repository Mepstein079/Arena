"""To-do list:
Re-organize so most code is not in an if statement
rearange probabilities so user is rewarded for not only attack
reorganize user-interface
"""

import random


print("Welcome to the Arena!!")
print("----------------------")


player_class = int(input("To pick your class enter 1, 2, or 3\n"
                    "1: Figher\n2: Wizard\n3: Juggernaut\n"))


def fighter():
    hp = 18
    mana = 4
    hp_increase = 2
    base_attack = (3, 6)
    base_attack_double = base_attack * 2
    temp_hp = (3,5)
    cost = 1
    user_choice = ("Enter a1, a2, a3, or d to do the following:\n"
                   "a1: Attack\na2: Double Attack\na3: Gain temporary HP\nd:  Dodge\n")
    return hp, mana, hp_increase, base_attack, base_attack_double, temp_hp, cost, user_choice


def wizard():
    hp = 11
    hp_increase = 1
    mana = 3
    base_attack = (6, 9)
    big_attack = (10, 14)
    recharge = (1,3)
    cost = 1
    user_choice = ("Enter a1, a2, a3, or d to do the following:\n"
                   "a1: Firebolt\na2: Fireball\na3: Regain Mana HP\nd:  Dodge\n")
    return hp, mana, hp_increase, base_attack, big_attack, recharge, cost, user_choice


def juggernaut():
    hp = 30
    mana = 6
    hp_increase = 3
    base_attack = (2, 3)
    big_attack = (3,4)
    heal = (4,5)
    cost = 2
    user_choice = ("Enter a1, a2, a3, or d to do the following:\n"
                   "a1: Punch\na2: Uppercut\na3: Heal\nd:  Dodge\n")
    return hp, mana, hp_increase, base_attack, big_attack, heal, cost, user_choice


if player_class == 1:
    hp, mana, hp_increase, action1, action2, action3, cost, user_choice = fighter()

elif player_class == 2:
    hp, mana, hp_increase, action1, action2, action3, cost, user_choice = wizard()

elif player_class == 3:
    hp, mana, hp_increase, action1, action2, action3, cost, user_choice = juggernaut()

else:
    print("Not an option")
con = None
level = 0

while level < 10:
    print(f"You are on level {level + 1}")
    monster_hp = 35
    turn = 1

    while (hp > 0) and (monster_hp > 0):
        print("---------------")
        action = input(user_choice)
        chance = random.random()
        monster_damage = random.randint(2, 3)
        health_gain = random.randint(2, 5)
        monster_dmg_taken = 0
        player_dmg_taken = 0
        mana_used = 0
        print("---------------")

        while action not in ("a1", "a2", "a3", "d"):
            print("Wrong input, try again")
            action = input(user_choice)
        if action == "a1":
            player_damage = random.randint(action1[0], action1[1])
            if chance <=0.45:
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

        elif action == "a2" and mana > 0:
            player_damage = random.randint(action2[0], action2[1])
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
            mana -= cost
            mana_used += cost
        elif action == "a2" and mana <= 0:
            print("Not enough mana, wasted turn")
            if chance < 0.40:
                print(f"The monster took the opportunity to attack dealing {monster_damage}")
                player_dmg_taken += monster_damage
                hp -= monster_damage

        elif action == "a3":
            unique_ability = random.randint(action3[0], action3[1])
            if player_class == 1:
                temp_hp = unique_ability
            elif player_class == 2:
                mana += unique_ability
                mana_used -= unique_ability
            elif player_class == 3:
                hp += unique_ability

        elif action == "d":
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
        print(f"Your health: {hp}")
        print(f"Your mana: {mana}")
        print(f"End of turn {turn}")
        turn += 1


    if hp <= 0:
        print("---------------")
        print('You lose!')

    elif monster_hp <= 0:
        print("---------------")
        print ("Congrats you win!")


    con = input("Enter 'C' to continue, anything else to quit: ")
    con = con.capitalize()
    if con == "C":
        if hp <= 0:
            hp += player_dmg_taken
            mana += mana_used
            level = 0
        else:
             hp += player_dmg_taken + hp_increase
             monster_hp += monster_dmg_taken + 10
             mana += mana_used
             level += 1
    else:
        level = 11


print("Play again soon :)")
