import math

print("Advent of Code 2015 - Day 21: RPG Simulator 20XX")
class Character:
    def __init__(self, hp, damage, defense):
        self.hp = hp
        self.damage = damage
        self.defense = defense
        self.gold_spent = 0
    
    def equip(self, weapon, armor, ring1, ring2):
        if weapon != None:
            self.damage += weapon.damage_added
            self.gold_spent += weapon.cost

        if armor != None:
            self.defense += armor.defense_added
            self.gold_spent += armor.cost

        if ring1 != None:
            self.damage += ring1.damage_added
            self.defense += ring1.defense_added
            self.gold_spent += ring1.cost
        
        if ring2 != None:
            self.damage += ring2.damage_added
            self.defense += ring2.defense_added
            self.gold_spent += ring2.cost

class Weapon:
    def __init__(self, cost, damage_added):
        self.cost = cost
        self.damage_added = damage_added
    
class Armor:
    def __init__(self, cost, defense_added):
        self.cost = cost
        self.defense_added = defense_added

class Ring:
    def __init__(self, cost, damage_added, defense_added):
        self.cost = cost
        self.damage_added = damage_added
        self.defense_added = defense_added

SHOP = '''
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
'''

WEAPONS = [
    Weapon(8, 4),
    Weapon(10, 5),
    Weapon(25, 6),
    Weapon(40, 7),
    Weapon(74, 8)   
]

ARMORS = [
    Armor(13, 1),
    Armor(31, 2),
    Armor(53, 3),
    Armor(75, 4),
    Armor(102, 5),
    None
]

RINGS = [
    Ring(25, 1, 0),
    Ring(50, 2, 0),
    Ring(100, 3, 0),
    Ring(20, 0, 1),
    Ring(40, 0, 2),
    Ring(80, 0, 3),
    None
]

with open('day21.txt') as f:
    boss_stats = [int(value) for _, value in 
        [line.split(': ') for line in f.read().splitlines()]]
    boss_hp, boss_damage, boss_defense = boss_stats

def fight(player1, player2):
    p1_damage = max(1, player1.damage - player2.defense)
    p2_damage = max(1, player2.damage - player1.defense)
    turns_to_defeat_p2 = math.ceil(player2.hp / p1_damage)
    turns_to_defeat_p1 = math.ceil(player1.hp / p2_damage)
    if turns_to_defeat_p2 <= turns_to_defeat_p1:
        return player1
    return player2

min_coins = 1000
max_coins = 0
enemy_boss = Character(boss_hp, boss_damage, boss_defense)

for weapon in WEAPONS:
    for armor in ARMORS:
        for ring1 in RINGS:
            for ring2 in RINGS:
                if (ring1 == ring2) and (ring1 != None):
                    continue
                player = Character(100, 0, 0)
                player.equip(weapon, armor, ring1, ring2)
                winner = fight(player, enemy_boss)
                if winner == player:
                    min_coins = min(min_coins, player.gold_spent)
                else:
                    max_coins = max(max_coins, player.gold_spent)

print(f'Part 1: {min_coins}') # 121 - part 1
print(f'Part 2: {max_coins}') # 201 - part 2
