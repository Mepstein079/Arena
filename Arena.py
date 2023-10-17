"""To-do list:
Add a way to switch between enemies in each level
look into switch cases to make the actions cleaner (in python called match)
Make namedtuples to clean up the amount of variables returned/called
"""

"""Future Goals:
Get this onto some type of application
Change it from text-based to 2d graphics
"""


import random
import classes


# prepares the game with each class's stats
def preamble():
    player_class, enemy_class = picking_classes()
    # based on the class choses, the variables are made global
    if player_class == "1":
        max_hp, mana, hp_increase, action1, action2, action3, cost, class_prompt = classes.fighter()

    elif player_class == "2":
        max_hp, mana, hp_increase, action1, action2, action3, cost, class_prompt = classes.wizard()

    if enemy_class == 0:
            max_enemy_hp, enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique = classes.juggernaut()
            enemy_name = "Juggernaut"
    elif enemy_class == 1:
            max_enemy_hp, enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique = classes.witch()
            enemy_name = "Witch"
    return (player_class, max_hp, mana, hp_increase, action1, action2, action3, cost, class_prompt, max_enemy_hp,
            enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique, enemy_name)


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
def players_action(player_class, action, to_hit, counter_dmg, action1, action2, action3, enemy_name, hp, enemy_hp, mana, cost):
    if action == "a1":
        dmg = random.randint(action1[0], action1[1])
    elif action == "a2":
        dmg = random.randint(action2[0], action2[1])
        if mana <= 0:
            print("Not enough mana, wasted turn")
            if to_hit < 0.40:
                print(f"The monster took the opportunity to attack dealing {counter_dmg}")
                hp -= counter_dmg
            return hp, enemy_hp, mana 
        mana -= cost
    elif action == "a3":
        unique = random.randint(action3[0], action3[1])
    if action in ("a1", "a2"):
        if to_hit < 55:
            print(f"HIT! You dealt {dmg} damage.")
            enemy_hp -= dmg
        elif to_hit < 60:
            print(f"CRITICAL HIT!! You dealt {dmg * 2} damage.")
            enemy_hp -= (dmg * 2)
        elif to_hit < 90:
            print("Miss!")
        else:
            print(f"The {enemy_name} countered, dealing {counter_dmg} damage")
            hp -= counter_dmg
    elif action == "a3":
        if player_class == 1:
            hp += random.randint(action3[0], action3[1])
        elif player_class == 2:
            mana += random.randint(action3[0], action3[1])
    return hp, enemy_hp, mana


# runs the enemies turn
def enemies_action(enemy_name, to_hit, action_chance, action1, action2, action3, hp):
    if action_chance < 50:
        action_outcome = random.randint(action1[0], action1[1])
    elif action_chance < 85:
        action_outcome = random.randint(action2[0], action2[1])
    else:
        action_outcome = random.randint(action3[0], action3[1])
    if to_hit < 45:
        print(f"The {enemy_name} attacked you, dealing {action_outcome} damage.")
        hp -= action_outcome
    elif to_hit < 50:
        print(f"The {enemy_name} crit while attacking you, dealing {action_outcome * 2} damage.")
        hp -= (action_outcome * 2)
    else:
        print(f"The {enemy_name} missed their attack")
    return hp


# game loop function, to make the while loop look cleaner
def game_loop(result, max_hp, enemy_max_hp, hp_increase, enemy_increase, mana, mana_used, level):
    if result == "failure":
        player_hp = max_hp
        enemy_hp = enemy_max_hp
        mana += mana_used
    elif result == "success":
        player_hp = max_hp + hp_increase
        enemy_hp = enemy_max_hp + enemy_increase
        mana += mana_used
        level += 1
    return player_hp, enemy_hp, mana, level


# runs the game
def run_game():
    print("Welcome to the Arena!!")
    print("----------------------")
    (player_class, max_hp, max_mana, hp_increase, action1, action2, action3, cost, class_prompt, max_enemy_hp,
    enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique, enemy_name) = preamble()
    con = "C"
    level = 1
    print(f"You are on level {level}")


# the con == C is to make sure the program ends without an error
    while level < 11 and con == "C":
        mana_used = 0
        turn = 1
        enemy_hp = max_enemy_hp
        hp = max_hp
        mana = max_mana


    # players turn if they have > 0 hp
        while (hp > 0) and (enemy_hp > 0):
            print("---------------")
            action, to_hit, to_hit2, action_chance, counter_dmg = game_actions(class_prompt)
            hp, enemy_hp, mana = players_action(player_class, action, to_hit, counter_dmg, action1, action2, action3, enemy_name, hp, enemy_hp, mana, cost)
            if enemy_hp > 0 and hp > 0:
                hp = enemies_action(enemy_name, to_hit2, action_chance, enemy_base_attack, enemy_big_attack, unique, hp)

            # gives the user its current hp, mana, and what turn it is of this level
            print(f"Your health: {hp}/{max_hp}")
            print(f"Your mana: {mana}/{max_mana}")
            print(f"{enemy_name}'s health: {enemy_hp}/{max_enemy_hp}")
            print(f"End of turn {turn}")
            turn += 1

    # If the user loses then it restarts the level
        if hp <= 0:
            print("---------------")
            print('You lose!')
            con = input("Enter 'C' to continue, anything else to quit: ")
            con = con.capitalize()
            if con == "C":
                max_hp, max_enemy_hp, mana, level = game_loop("failure", max_hp, max_enemy_hp,
                                                              hp_increase, enemy_hp_increase, mana, mana_used, level)
                hp = max_hp
                enemy_hp = max_enemy_hp

    # If the user wins then the program goes to the next level
        if enemy_hp <= 0:
            print("---------------")
            print("Congrats you win!")
            con = input("Enter 'C' to continue, anything else to quit: ")
            con = con.capitalize()
            if con == "C":
                max_hp, max_enemy_hp, mana, level = game_loop("success", max_hp, max_enemy_hp,
                                                              hp_increase, enemy_hp_increase, mana, mana_used, level)
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