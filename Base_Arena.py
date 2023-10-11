import random


start = input("Enter 'S' to being: ")
level = 0
hp = 10
damage_taken = 0
monster_hp = 20
monster_damage_taken = 0


while level < 10 and start  == 'S':


    while (hp > 0) and (monster_hp > 0):
        action = input("Type A to attack or D to Dodge: ")
        chance = random.random()
        player_damage = random.randint(1, 4)
        monster_damage = random.randint(2, 3)
        health_gain = random.randint(1, 3)

        if action == "A":
            if chance < 0.45:
                print("Hit")
                print(f"You dealt {player_damage} damage")
                monster_hp -= player_damage
                monster_damage_taken += player_damage
            elif chance < 0.85:
                print("Miss")
            elif chance < 0.95:
                print(f"The monster countered your attack, dealing {monster_damage} damage!")
                hp -= monster_damage
                damage_taken += monster_damage
            else:
                print("CRIT!!!")
                print(f"You dealt {player_damage * 2} damage")
                monster_hp -= (player_damage * 2)
                monster_damage_taken += (player_damage * 2)

        elif action == "D":
            if chance < 0.45:
                print("Success")
                print(f"You healed {health_gain} hp")
                hp += health_gain
                damage_taken -= health_gain
            elif chance < 0.95:
                print("Failed")
                print(f"You took {monster_damage} damage")
                hp -= monster_damage
                damage_taken += monster_damage
            else:
                print("CRIT!!!")
                print(f"You took {monster_damage * 2} damage")
                hp -= (monster_damage * 2)
                damage_taken += (monster_damage * 2)
        else:
            print("Wrong input, you LOSE!")
            hp -= hp
        print("Your health:", hp)


    if hp <= 0:
        print('You lose!')

    elif monster_hp <= 0:
        print ("Congrats you win!")
        hp += damage_taken + 4
        monster_hp += monster_damage_taken + 10
        level += 1
        print("Your new HP:", hp)

    start = input("Press 'S' to continue: ")