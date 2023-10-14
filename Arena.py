"""To-do list:
look into switch cases to make the actions cleaner (in python called match)
"""

"""Future Goals:
Get this onto some type of application
Change it from text-based to 2d graphics
"""

import random
import classes

print("Welcome to the Arena!!")
print("----------------------")

# determines which class the player is
player_class = int(input("To pick your class enter 1, 2\n"
                         "1: Fighter\n2: Wizard\n"))
while player_class not in (1, 2):
    print("Not an option. Try Again")
    player_class = int(input())


# game loop function, to make the while loop look cleaner
def game_loop(result, player_hp, enemy_hp, dmg_taken1, dmg_taken2, hp_increase, enemy_increase, mana, mana_used, level):
    con = input("Enter 'C' to continue, anything else to quit: ")
    con = con.capitalize()
    if con != "C":
        print("Play again soon :)")
        level = 11
        return player_hp, enemy_hp, mana, level
    if result == "failure":
        player_hp += dmg_taken1
        enemy_hp += dmg_taken2
        mana += mana_used
    elif result == "success":
        player_hp += dmg_taken1 + hp_increase
        enemy_hp = dmg_taken2 + enemy_increase
        mana += mana_used
        level += 1
    return player_hp, enemy_hp, mana, level


# based on the class choses, the variables are made global
if player_class == 1:
    hp, mana, hp_increase, action1, action2, action3, cost, class_prompt = classes.fighter()

elif player_class == 2:
    hp, mana, hp_increase, action1, action2, action3, cost, class_prompt = classes.wizard()



# variables to be used in while loop
enemy_class = random.randint(0,1)

if enemy_class == 0:
    enemy_hp, enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique = classes.juggernaut()
    enemy_class_name = "Juggernaut"
if enemy_class == 1:
    enemy_hp, enemy_hp_increase, enemy_base_attack, enemy_big_attack, unique = classes.witch()
    enemy_class_name = "Witch"

con = None
level = 1
max_enemy_hp = enemy_hp
temp_hp = 0
turn = 1
enemy_dmg_taken = 0
player_dmg_taken = 0
mana_used = 0
max_hp = hp
print(f"You are on level {level}")

while level < 11:

# players turn if they have > 0 hp
    while (hp > 0) and (enemy_hp > 0):
        print("---------------")
    #   lists of variables to be used throughout the game
        action = input(class_prompt)
        to_hit = random.randrange(0, 100)
        action_chance = random.randrange(0, 100)
        counter_dmg = random.randint(2, 3)
        print("---------------")

    #   makes sure the user makes the right option
        while action not in ("a1", "a2", "a3"):
            print("Wrong input, try again")
            action = input(class_prompt)
    #   outcomes based on the action selected, with different results depending on class selected
        if action == "a1":
            player_damage = random.randint(action1[0], action1[1])
            if to_hit < 55:
                print(f"HIT! You dealt {player_damage} damage.")
                enemy_hp -= player_damage
                enemy_dmg_taken += player_damage
            elif to_hit < 60:
                print(f"CRITICAL HIT!! You dealt {player_damage * 2} damage.")
                enemy_hp -= (player_damage * 2)
                enemy_dmg_taken += (player_damage * 2)
            elif to_hit < 90:
                print("Miss!")
            else:
                print(f"The {enemy_class_name} countered, dealing {counter_dmg} damage")
                counter_dmg -= temp_hp
                temp_hp = 0
                if counter_dmg > 0:
                    hp -= counter_dmg
                    player_dmg_taken += counter_dmg
                else:
                    temp_hp -= counter_dmg

        elif action == "a2":
            if mana > 0:
                player_damage = random.randint(action2[0], action2[1])
                mana -= cost
                mana_used += cost
                if to_hit < 50:
                    print(f"HIT! You dealt {player_damage} damage.")
                    enemy_hp -= player_damage
                    enemy_dmg_taken += player_damage
                elif to_hit < 55:
                    print(f"CRITICAL HIT!! You dealt {player_damage * 2} damage.")
                    enemy_hp -= (player_damage * 2)
                    enemy_dmg_taken += (player_damage * 2)
                elif to_hit < 95:
                    print("Miss!")
                else:
                    print(f"The {enemy_class_name} countered, dealing {counter_dmg} damage")
                    counter_dmg -= temp_hp
                    temp_hp = 0
                    if counter_dmg > 0:
                        hp -= counter_dmg
                        player_dmg_taken += counter_dmg
                    else:
                        temp_hp -= counter_dmg
            else:
                print("Not enough mana, wasted turn")
                if to_hit > 60:
                    print(f"The monster took the opportunity to attack dealing {counter_dmg}")
                    player_dmg_taken += counter_dmg
                    hp -= counter_dmg
            

        elif action == "a3":
            unique_ability = random.randint(action3[0], action3[1])
            if player_class == 1:
                temp_hp = unique_ability
            elif player_class == 2:
                mana += unique_ability
                mana_used -= unique_ability

        if enemy_hp > 0:
            if action_chance < 33:
                enemy_damage = random.randint(enemy_base_attack[0], enemy_base_attack[1])
                if to_hit < 45:
                    print(f"The {enemy_class_name} attacked you, dealing {enemy_damage} damage.")
                    enemy_damage -= temp_hp
                    temp_hp = 0
                    if enemy_damage > 0:
                        hp -= enemy_damage
                        player_dmg_taken += enemy_damage
                    else:
                        temp_hp -= enemy_damage
                elif to_hit < 50:
                    print(f"The {enemy_class_name} crit while attacking you, dealing {enemy_damage} damage.")
                    enemy_damage *= 2
                    enemy_damage -= temp_hp
                    temp_hp = 0
                    if enemy_damage > 0:
                        hp -= enemy_damage
                        player_dmg_taken += enemy_damage
                    else:
                        temp_hp -= enemy_damage
                else:
                    print(f"The {enemy_class_name} missed their attack")
            elif action_chance < 66:
                enemy_damage = random.randint(enemy_big_attack[0], enemy_big_attack[1])
                if to_hit < 45:
                    print(f"The {enemy_class_name} attacked you, dealing {enemy_damage} damage.")
                    enemy_damage -= temp_hp
                    temp_hp = 0
                    if enemy_damage > 0:
                        hp -= enemy_damage
                        player_dmg_taken += enemy_damage
                    else:
                        temp_hp -= enemy_damage
                elif to_hit < 50:
                    enemy_damage *= 2
                    print(f"The {enemy_class_name} crit while attacking you, dealing {enemy_damage} damage.")
                    enemy_damage -= temp_hp
                    temp_hp = 0
                    if enemy_damage > 0:
                        hp -= enemy_damage
                        player_dmg_taken += enemy_damage
                    else:
                        temp_hp -= enemy_damage
                else:
                    print(f"The {enemy_class_name} missed their attack")
            else:
                heal = random.randint(unique[0], unique[1])
                print(f"{enemy_class_name} healed for {heal} hp")
                enemy_hp += heal
                if enemy_hp > max_enemy_hp:
                    enemy_hp = max_enemy_hp


    # gives the user its current hp, mana, and what turn it is of this level
        print(f"Your health: {hp}/{max_hp}")
        if player_class == 1:
            print(f"Temp HP: {temp_hp}")
        print(f"Your mana: {mana}")
        print(f"{enemy_class_name}'s health: {enemy_hp}/{max_enemy_hp}")
        print(f"End of turn {turn}")
        turn += 1

        if hp <= 0:
            print("---------------")
            print('You lose!')
            hp, enemy_hp, mana, level = game_loop("success", hp, enemy_hp, player_dmg_taken, enemy_dmg_taken,
                                                    hp_increase, enemy_hp_increase, mana, mana_used, level)
            turn = 0
            
        if enemy_hp <= 0:
            print("---------------")
            print("Congrats you win!")
            hp, enemy_hp, mana, level = game_loop("success", hp, enemy_hp, player_dmg_taken, enemy_dmg_taken,
                                                  hp_increase, enemy_hp_increase, mana, mana_used, level)
            if level <= 10:
                print(f"Entering Level {level}")
            max_hp = hp
            max_enemy_hp = enemy_hp
            turn = 0
