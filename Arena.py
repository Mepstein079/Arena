"""To-do list:
Change it from text-based to 2d graphics
---------------------
Future Goals:
learn flask
throw it on pythonanywhere
Get this onto some type of application
"""
from collections import namedtuple
import random
import classes


# prepares the game with each class's stats
def preamble_player():
    player_class = picking_user_class()
    user_class = namedtuple("name", ["max_hp", "mana", "hp_increase",
                            "action1", "action2", "action3", "cost", "class_prompt"])
    # based on the class choses, the variables are made global
    if player_class == "1":
        max_hp, mana, hp_increase, action1, action2, action3, cost, class_prompt = classes.fighter()
        user = user_class(max_hp, mana, hp_increase, action1, action2, action3, cost, class_prompt)

    elif player_class == "2":
        max_hp, mana, hp_increase, action1, action2, action3, cost, class_prompt = classes.wizard()
        user = user_class(max_hp, mana, hp_increase, action1, action2, action3, cost, class_prompt)
    return player_class, user


def preamble_enemy():
    enemy_class = picking_enemy_class()
    opponent_class = namedtuple(
        "name", ["name", "max_hp", "hp_increase", "action1", "action2", "unique"])
    if enemy_class == 0:
        max_enemy_hp, enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique = classes.juggernaut()
        opponent = opponent_class("Juggernaut", max_enemy_hp, enemy_hp_increase,
                                  enemy_base_attack, enemy_big_attack, unique)
    elif enemy_class == 1:
        max_enemy_hp, enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique = classes.witch()
        opponent = opponent_class("Witch", max_enemy_hp, enemy_hp_increase,
                                  enemy_base_attack, enemy_big_attack, unique)
    return opponent


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


# runs to pick the players class and what the opponent they will face
def picking_user_class():
    # determines which class the player is
    player_class = input("To pick your class enter 1, 2\n"
                         "1: Fighter\n2: Wizard\n")
    while player_class not in ("1", "2"):
        print("Not an option. Try Again")
        player_class = input()

    return player_class


def picking_enemy_class():
    enemy_class = random.randint(0, 1)
    return enemy_class


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
            print(f"You regained {unique} health.")
            hp += unique
        elif player_class == "2":
            print(f"You regained {unique} mana.")
            mana += unique
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
def game_loop(player, enemy, level, result=None):
    if result == "success":
        level += 1
    player_hp = player.max_hp + (player.hp_increase * level)
    enemy_hp = enemy.max_hp + (enemy.hp_increase * level)
    mana = player.mana
    return player_hp, enemy_hp, mana, level


# runs the game
def run_game():
    print("Welcome to the Arena!!")
    print("----------------------")
    player_class, player = preamble_player()
    enemy = preamble_enemy()
    con = "C"
    level = 0
    max_enemy_hp = enemy.max_hp
    enemy_hp = max_enemy_hp
    max_hp = player.max_hp
    hp = max_hp
    mana = player.mana
    print(f"You are on level {level + 1}")
    print(f"You are facing the {enemy.name}")


# the con == C is to make sure the program ends without an error
    while level < 10 and con == "C":
        turn = 1

    # players turn if they have > 0 hp
        while (hp > 0) and (enemy_hp > 0):
            print("---------------")
            action, to_hit, to_hit2, action_chance, counter_dmg = game_actions(player.class_prompt)
            hp, enemy_hp, mana = players_action(
                player_class, player, enemy, action, to_hit, counter_dmg, hp, enemy_hp, mana)
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
                max_hp, max_enemy_hp, mana, level = game_loop(player, enemy, level)
                hp = max_hp
                enemy_hp = max_enemy_hp

    # If the user wins then the program goes to the next level
        if enemy_hp <= 0:
            print("---------------")
            print("Congrats you win!")
            con = input("Enter 'C' to continue, anything else to quit: ")
            con = con.capitalize()
            if con == "C":
                enemy = preamble_enemy()
                max_hp, max_enemy_hp, mana, level = game_loop(player, enemy, level, "success")
                hp = max_hp
                enemy_hp = max_enemy_hp
                print("---------------")
                print(f"Entering Level {level + 1}")
                print(f"You are now facing the {enemy.name}")

    if level < 10:
        print("Thanks for playing :)")
    if level >= 10:
        print("Congratulations!!! You beat the Arena.")
        print("Thanks for playing :)")


# executes
run_game()
