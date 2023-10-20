"""Both Player and Enemy classes to be imported."""
from collections import namedtuple

# possible classes the user could play
def fighter():
    hp = 18
    mana = 4
    hp_increase = 2
    base_attack = (3, 6)
    base_attack_double = base_attack * 2
    heal = (3, 5)
    cost = 1
    class_prompt = ("Enter a1, a2, or a3 to do the following:\n"
                   "a1: Attack\na2: Double Attack\na3: Regain HP\n")
    return hp, mana, hp_increase, base_attack, base_attack_double, heal, cost, class_prompt


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
    hp_increase = 10
    base_attack = (2, 3)
    big_attack = (3, 4)
    heal = (8, 12)
    return hp, hp_increase, base_attack, big_attack, heal

def witch():
    hp = 15
    hp_increase = 5
    base_attack = (4, 6)
    big_attack = (6, 8)
    heal = (5, 8)
    return hp, hp_increase, base_attack, big_attack, heal
