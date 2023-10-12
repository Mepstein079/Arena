import random


print("Welcome to the Arena!!")
print("----------------------")


player_class = int(input("To pick your class enter 1, 2, or 3\n"
                    "1: Figher, 2: wizard, 3: Juggernaut: "))


def fighter():
    hp = 18
    hp_increase = 2
    base_attack = (3, 6)
    big_attack = (5, 8)
    return hp, hp_increase, base_attack, big_attack


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
    return hp, hp_increase, base_attack


if player_class == 1:
    hp, hp_increase, attack1, attack2 = fighter()

elif player_class == 2:
    hp, hp_increase, attack1, attack2, attack3 = wizard()

elif player_class == 3:
    hp, hp_increase, attack1 = juggernaut()

else:
    print("Not an option")
con = None
level = 0

while level < 10:
    monster_hp = 35

    while (hp > 0) and (monster_hp > 0):
        if player_class == 1:
            action = input("Type A1 or A2 to attack or D to dodge: ")
            if action == "A1":
                player_damage = random.randint(attack1)
            elif action == "A2":
                player_damage = random.randint(attack2)


        elif player_class == 2:
            action = input("Type A1, A2, or A3 to attack or D to dodge: ")
            if action == "A1":
                player_damage = random.randint(attack1)
            elif action == "A2":
                player_damage = random.randint(attack2)
            elif action == "A3":
                player_damage = random.randint(attack3)

        elif player_class == 3:
            action = input("Type A1 to attack or D to dodge: ")
            if action == "A1":
                player_damage = random.randint(attack1)

        chance = random.random()
        monster_damage = random.randint(2, 3)
        health_gain = random.randint(2, 5)
        mosnter_dmg_taken = 0
        player_dmg_taken = 0

        if action == "A1":
            if chance <=0.40:
                print(f"HIT! You dealt {player_damage} damage.")
                monster_hp -= player_damage
                mosnter_dmg_taken += player_damage
            elif chance < 0.85:
                print("Miss!")
            elif chance < 0.95:
                print(f"The Monster countered, dealing {monster_damage} damage")
                hp -= monster_damage
                player_dmg_taken += monster_damage
            else:
                print(f"CRITICAL HIT!! You dealt {player_damage * 2} damage.")
                monster_hp -= (player_damage * 2)
                mosnter_dmg_taken += (player_damage * 2)

        elif action == "A2":
            if chance <=0.35:
                print(f"HIT! You dealt {player_damage} damage.")
                monster_hp -= player_damage
                mosnter_dmg_taken += player_damage
            elif chance < 0.80:
                print("Miss!")
            elif chance < 0.95:
                print(f"The Monster countered, dealing {monster_damage} damage")
                hp -= monster_damage
                player_dmg_taken += monster_damage
            else:
                print(f"CRITICAL HIT!! You dealt {player_damage * 2} damage.")
                monster_hp -= (player_damage * 2)
                mosnter_dmg_taken += (player_damage * 2)

        elif action == "A3":
            if chance <=0.30:
                print(f"HIT! You dealt {player_damage} damage.")
                monster_hp -= player_damage
                mosnter_dmg_taken += player_damage
            elif chance < 0.85:
                print("Miss!")
            elif chance < 0.975:
                print(f"The Monster countered, dealing {monster_damage} damage")
                hp -= monster_damage
                player_dmg_taken += monster_damage
            else:
                print(f"CRITICAL HIT!! You dealt {player_damage * 2} damage.")
                monster_hp -= (player_damage * 2)
                mosnter_dmg_taken += (player_damage * 2)

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


    if hp < 0:
        print('You lose!')

    elif monster_hp < 0:
        print ("Congrats you win!")
        hp += player_dmg_taken + hp_increas
        monster_hp += mosnter_dmg_taken + 10

    con = input("Enter 'C' to continue, anything else to quit: ")
    
    if con == 'C':
        level += 1
