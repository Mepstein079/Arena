"""To-do list:
Make namedtuples to clean up the amount of variables returned/called
Add a way to switch between enemies in each level
look into switch cases to make the actions cleaner (in python called match)
"""

"""Future Goals:
Change it from text-based to 2d graphics
learn flask
throw it on pythonanywhere
Get this onto some type of application
"""


import random
import classes
from collections import namedtuple

# prepares the game with each class's stats
def preamble():
    player_class, enemy_class = picking_classes()
    user_class = namedtuple("name", ["max_hp", "mana", "hp_increase", "action1", "action2", "action3", "cost", "class_prompt"])
    opponent_class = namedtuple("name", ["name", "max_hp", "hp_increase", "action1", "action2", "unique"])
    # based on the class choses, the variables are made global
    if player_class == "1":
        max_hp, mana, hp_increase, action1, action2, action3, cost, class_prompt = classes.fighter()
        user = user_class(max_hp, mana, hp_increase, action1, action2, action3, cost, class_prompt)

    elif player_class == "2":
        max_hp, mana, hp_increase, action1, action2, action3, cost, class_prompt = classes.wizard()
        user = user_class(max_hp, mana, hp_increase, action1, action2, action3, cost, class_prompt)

    if enemy_class == 0:
        max_enemy_hp, enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique = classes.juggernaut()
        opponent = opponent_class("Juggernaut", max_enemy_hp, enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique)
    elif enemy_class == 1:
        max_enemy_hp, enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique = classes.witch()
        opponent = opponent_class("Witch", max_enemy_hp, enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique)
    return player_class, user, opponent


# the actions for the game
def game_actions(class_prompt):
    action = input(class_prompt)
    while action not in ("a1", "a2", "a3"):
            print("Wrong input, try again")
            action = input(class_prompt)
    to_hit = random.randrange(0, 100)
    to_hit2 = random.randrange(0, 100)
    action_chance = random.randrange(0, 100)
    counter_dmg = random.randint(2, 3)
    print("---------------")
    return action, to_hit, to_hit2, action_chance, counter_dmg


# runs to pick the players class and what the oponenent they will face
def picking_classes():
    # determines which class the player is
    player_class = input("To pick your class enter 1, 2\n"
                        "1: Fighter\n2: Wizard\n")
    while player_class not in ("1", "2"):
        print("Not an option. Try Again")
        player_class = input()

    enemy_class = random.randint(0,1)

    return player_class, enemy_class


# runs the player's turn
def players_action(player_class, player, enemy, action, to_hit, counter_dmg, hp, enemy_hp, mana):
    if action == "a1":
        dmg = random.randint(player.action1[0], player.action1[1])
    elif action == "a2":
        dmg = random.randint(player.action2[0], player.action2[1])
        if mana <= 0:
            print("Not enough mana, wasted turn")
            if to_hit < 0.40:
                print(f"The monster took the opportunity to attack dealing {counter_dmg}")
                hp -= counter_dmg
            return hp, enemy_hp, mana 
        mana -= player.cost
    elif action == "a3":
        unique = random.randint(player.action3[0], player.action3[1])
    if action in ("a1", "a2"):
        if to_hit < 55:
            print(f"HIT! You dealt {dmg} damage.")
            enemy_hp -= dmg
        elif to_hit < 60:
            dmg = dmg * 2
            print(f"CRITICAL HIT!! You dealt {dmg} damage.")
            enemy_hp -= (dmg)
        elif to_hit < 90:
            print("Miss!")
        else:
            print(f"The {enemy.name} countered, dealing {counter_dmg} damage")
            hp -= counter_dmg
    elif action == "a3":
        if player_class == "1":
            hp += random.randint(player.action3[0], player.action3[1])
        elif player_class == "2":
            mana += random.randint(player.action3[0], player.action3[1])
    return hp, enemy_hp, mana


# runs the enemies turn
def enemies_action(to_hit, action_chance, enemy, hp, enemy_hp):
    if action_chance < 50:
        action_outcome = random.randint(enemy.action1[0], enemy.action1[1])
    elif action_chance < 85:
        action_outcome = random.randint(enemy.action2[0], enemy.action2[1])
    else:
        action_outcome = random.randint(enemy.unique[0], enemy.unique[1])
        print(f"The {enemy.name} healed for {action_outcome} damage.")
        enemy_hp += action_outcome
        return hp, enemy_hp

    if to_hit < 45:
        print(f"The {enemy.name} attacked you, dealing {action_outcome} damage.")
        hp -= action_outcome
    elif to_hit < 50:
        print(f"The {enemy.name} crit while attacking you, dealing {action_outcome * 2} damage.")
        hp -= (action_outcome * 2)
    else:
        print(f"The {enemy.name} missed their attack")
    return hp, enemy_hp


# game loop function, to make the while loop look cleaner
def game_loop(result, player_max, hp_increase, enemy_max, enemy_increase, mana, level):
    if result == "failure":
        player_hp = player_max
        enemy_hp = enemy_max
        mana = mana
    elif result == "success":
        player_hp = player_max + hp_increase
        enemy_hp = enemy_max + enemy_increase
        mana = mana
        level += 1
    return player_hp, enemy_hp, mana, level


# runs the game
def run_game():
    print("Welcome to the Arena!!")
    print("----------------------")
    player_class, player, enemy = preamble()
    con = "C"
    level = 1
    print(f"You are on level {level}")
    max_enemy_hp = enemy.max_hp
    enemy_hp = max_enemy_hp
    max_hp = player.max_hp
    hp = max_hp
    mana = player.mana


# the con == C is to make sure the program ends without an error
    while level < 11 and con == "C":
        turn = 1

    # players turn if they have > 0 hp
        while (hp > 0) and (enemy_hp > 0):
            print("---------------")
            action, to_hit, to_hit2, action_chance, counter_dmg = game_actions(player.class_prompt)
            hp, enemy_hp, mana = players_action(player_class, player, enemy, action, to_hit, counter_dmg, hp, enemy_hp, mana)
            if enemy_hp > 0 and hp > 0:
                hp, enemy_hp = enemies_action(to_hit2, action_chance, enemy, hp, enemy_hp)
            # gives the user its current hp, mana, and what turn it is of this level
            print(f"Your health: {hp}/{max_hp}")
            print(f"Your mana: {mana}/{player.mana}")
            print(f"{enemy.name}'s health: {enemy_hp}/{max_enemy_hp}")
            print(f"End of turn {turn}")
            turn += 1

    # If the user loses then it restarts the level
        if hp <= 0:
            print("---------------")
            print('You lose!')
            con = input("Enter 'C' to continue, anything else to quit: ")
            con = con.capitalize()
            if con == "C":
                max_hp, max_enemy_hp, mana, level = game_loop("failure", max_hp, player.hp_increase, max_enemy_hp, enemy.hp_increase, player.mana, level)
                hp = max_hp
                enemy_hp = max_enemy_hp

    # If the user wins then the program goes to the next level
        if enemy_hp <= 0:
            print("---------------")
            print("Congrats you win!")
            con = input("Enter 'C' to continue, anything else to quit: ")
            con = con.capitalize()
            if con == "C":
                max_hp, max_enemy_hp, mana, level = game_loop("success", max_hp, player.hp_increase, max_enemy_hp, enemy.hp_increase, player.mana, level)
                hp = max_hp
                enemy_hp = max_enemy_hp
                print(f"Entering Level {level}")
                print("---------------")


    if level < 10:
        print("Thanks for playing :)")
    if level > 10:
        print("Congratulations!!! You beat the Arena.")
        print("Thanks for playing :)")


# executes
run_game()