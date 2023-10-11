import random


print("Welcome to the Arena!!")
print("----------------------")


start = input("To start type 'S': ")
xp = 0

while start == 'S':
    hp = 10
    monster_hp = 20

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
            elif chance < 0.85:
                print("Miss")
            elif chance < 0.95:
                print(f"The monster countered your attack, dealing {monster_damage} damage!")
                hp -= monster_damage
            else:
                print("CRIT!!!")
                print(f"You dealt {player_damage * 2} damage")
                monster_hp -= (player_damage * 2)

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
        print("Monster's HP:", monster_hp)


    if hp == 0:
        print('You lose!')

    elif monster_hp == 0:
        print ("Congrats you win!")
        xp += 10
        print(f"You gain 10 xp, with a new total of {xp}")
    
    
    start = input("Type 'Q' to quit or 'S' to play again: ")





""" def fighter():
    hp = 15
    base_attack = random.randint(1,4)
    big_attack = random.randint(3, 6)
    if xp >= 50:
        base_attack += 2
        big_attack += 2
        hp += 3

"""
