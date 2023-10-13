"""To-do list:
put all the classes in a diff file to import here as a module
look into making enemy classes
    fix juggernaut to fit an enemy class
    make a witch (idea is making it hard to hit her and she does big dmg (low chance tt hit for balance))
look into switch cases to make the actions cleaner
"""

"""Future Goals:
Get this onto some type of website/browser so it can be played without needing access to this file
Change it from text-based to 2d graphics
"""

import random


print("Welcome to the Arena!!")
print("----------------------")

# determines which class the player is
player_class = int(input("To pick your class enter 1, 2\n"
                         "1: Fighter\n2: Wizard\n"))
while player_class not in (1, 2):
    print("Not an option. Try Again")
    player_class = int(input())

"""opponent_class = int(input("To pick your class enter 1, 2\n"
                           "1: Juggernaut\n2: Witch\n"))
while opponent_class not in (1, 2):
    print("Not an option. Try Again")
    opponent_class = int(input())
"""
# game loop function, to make the while loop look cleaner
def game_loop(result, player_hp, monster_hp, dmg_taken1, dmg_taken2, hp_increase, mana, mana_used, level):
    con = input("Enter 'C' to continue, anything else to quit: ")
    con = con.capitalize()
    if con != "C":
        print("Play again soon :)")
        level = 11
        player_hp = 0
        monster_hp = 0
        mana = 0
        return player_hp, monster_hp, mana, level
    if result == "failure":
        player_hp += dmg_taken1
        monster_hp += monster_dmg_taken
        mana += mana_used
        level = level
    elif result == "success":
        player_hp += dmg_taken1 + hp_increase
        monster_hp = dmg_taken2 + 10
        mana += mana_used
        level += 1
    return player_hp, monster_hp, mana, level


# possible classes the user could play
def fighter():
    hp = 18
    mana = 4
    hp_increase = 2
    base_attack = (3, 6)
    base_attack_double = base_attack * 2
    temp_hp = (3, 5)
    cost = 1
    class_prompt = ("Enter a1, a2, or a3 to do the following:\n"
                   "a1: Attack\na2: Double Attack\na3: Gain temporary HP\n")
    return hp, mana, hp_increase, base_attack, base_attack_double, temp_hp, cost, class_prompt


def wizard():
    hp = 11
    hp_increase = 1
    mana = 3
    base_attack = (6, 9)
    big_attack = (10, 14)
    recharge = (1, 3)
    cost = 1
    class_prompt = ("Enter a1, a2, or a3 to do the following:\n"
                   "a1: Firebolt\na2: Fireball\na3: Regain Mana\n")
    return hp, mana, hp_increase, base_attack, big_attack, recharge, cost, class_prompt

# Possiblle enemies the user could face
def juggernaut():
    hp = 30
    mana = 6
    hp_increase = 3
    base_attack = (2, 3)
    big_attack = (3, 4)
    heal = (4, 5)
    cost = 2
    class_prompt = ("Enter a1, a2, or a3 to do the following:\n"
                   "a1: Punch\na2: Uppercut\na3: Heal\n")
    return hp, mana, hp_increase, base_attack, big_attack, heal, cost, class_prompt




# based on the class choses, the variables are made global
while player_class not in (1, 2):
    print("Not an option")
    player_class = int(input("To pick your class enter 1, 2\n"
                             "1: Figher\n2: Wizard\n3: Juggernaut\n"))
if player_class == 1:
    hp, mana, hp_increase, action1, action2, action3, cost, class_prompt = fighter()

elif player_class == 2:
    hp, mana, hp_increase, action1, action2, action3, cost, class_prompt = wizard()


con = None
level = 1
print(f"You are on level {level}")
monster_hp = 35
max_monster_hp = monster_hp
temp_hp = 0
turn = 1
monster_dmg_taken = 0
player_dmg_taken = 0
mana_used = 0
max_hp = hp
#   makes sure it only runs while both entities are alive
while (hp > 0) and (monster_hp > 0):
    print("---------------")
#   lists of variables to be used throughout the game
    action = input(class_prompt)
    chance = random.random()
    monster_damage = random.randint(2, 3)
    health_gain = random.randint(2, 5)
    print("---------------")

#   makes sure the user makes the right option
    while action not in ("a1", "a2", "a3"):
        print("Wrong input, try again")
        action = input(class_prompt)
#   outcomes based on the action selected, with different results depending on class selected
    if action == "a1":
        player_damage = random.randint(action1[0], action1[1])
        if chance <= 0.55:
            print(f"HIT! You dealt {player_damage} damage.")
            monster_hp -= player_damage
            monster_dmg_taken += player_damage
        elif chance < 0.85:
            print("Miss!")
        elif chance < 0.95:
            print(f"The Monster countered, dealing {monster_damage} damage")
            monster_damage -= temp_hp
            hp -= monster_damage
            player_dmg_taken += monster_damage
        else:
            print(f"CRITICAL HIT!! You dealt {player_damage * 2} damage.")
            monster_hp -= (player_damage * 2)
            monster_dmg_taken += (player_damage * 2)

    elif action == "a2":
        if mana > 0:
            player_damage = random.randint(action2[0], action2[1])
            mana -= cost
            mana_used += cost
            if chance <= 0.50:
                print(f"HIT! You dealt {player_damage} damage.")
                monster_hp -= player_damage
                monster_dmg_taken += player_damage
            elif chance < 0.85:
                print("Miss!")
            elif chance < 0.95:
                print(f"The Monster countered, dealing {monster_damage} damage")
                monster_damage -= temp_hp
                hp -= monster_damage
                player_dmg_taken += monster_damage
            else:
                print(f"CRITICAL HIT!! You dealt {player_damage * 2} damage.")
                monster_hp -= (player_damage * 2)
                monster_dmg_taken += (player_damage * 2)
        else:
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

# gives the user its current hp, mana, and what turn it is of this level
    print(f"Your health: {hp}/{max_hp}")
    print(f"Your mana: {mana}")
    print(f"Monster's health: {monster_hp}/{max_monster_hp}")
    print(f"End of turn {turn}")
    turn += 1

    if hp <= 0:
        print("---------------")
        print('You lose!')
        hp, monster_hp, mana, level = game_loop("success", hp, monster_hp, player_dmg_taken, monster_dmg_taken,
                                                hp_increase, mana, mana_used, level)
        turn = 0


    elif monster_hp <= 0:
        print("---------------")
        print("Congrats you win!")
        hp, monster_hp, mana, level = game_loop("success", hp, monster_hp, player_dmg_taken, monster_dmg_taken,
                                                hp_increase, mana, mana_used, level)
        if level <= 10:
            print(f"Entering Level {level}")
        max_hp = hp
        max_monster_hp = monster_hp
        turn = 0
