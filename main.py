# main
# Прочитай ссылку про PEP8, реально
import os, sys


class City:
    def __init__(self, name, lvl, exp, hp, units):
        self.name = name
        self.lvl = lvl
        self.exp = exp
        self.units = units
        self.hp = hp


class Unit:
    def __init__(self, name, city, cost, hp, attack, active):
        self.name = name
        self.city = city
        self.cost = cost
        self.active = True
        self.hp = hp
        self.attack = attack


gold = 100
turns = 1
cities_l = [City("Capital", 1, 0, 300, 0)]
units_l = [Unit('Soldier', '', 30, 30, 30, True),
           Unit('Badass Soldier', '', 50, 65, 65, True),
           Unit('REALLY BADASS SOLDIER', '', 75, 90, 90, True)]


def commander():
    command = input("INPUT > ")
    if command == "exit":
        exit(1)
    elif 'create unit' in command:
        create_unit()
    elif 'create city' in command:
        if len(command.split()) == 3:
            create_city()
        else:
            print('INVALID COMMAND')
            commander()
    elif command == "turn":
        turn()
    elif command == 'help':
        help_command()
    else:
        print('INVALID COMMAND')
        commander()


def cities():
    os.system("cls")
    for city in cities_l:
        city.units = 0
        for unit in units_l:
            if city.name == unit.city:
                city.units += 1
    for i, city in enumerate(cities_l):
        print("{0}.  CITY {1} | LVL {2} | EXP {3} OF {4} "
              "| HP {5} OF {6} | UNITS {7}"
              .format(i + 1, city.name,
                      city.lvl, city.exp,
                      city.lvl * 150, city.hp,
                      (city.lvl - 1) * 100 + 300,
                      city.units)
              , "\n", "-" * 76)
    print("GOLD {0} | TURN {1}".format(gold, turns))
    commander()


def create_city():
    global gold
    if gold >= 300:
        name = input('Enter city name\nINPUT > ')
        cities_l.append(City(name, 1, 0, 300, 0))
        gold -= 300
    else:
        print('NOT ENOUGH GOLD (300 NEED)')
        commander()
    cities()


def turn():
    global gold
    gold += 100
    global turns
    turns += 1
    for city in cities_l:
        city.exp += 30
        if city.exp >= city.lvl * 150:
            city.exp -= city.lvl * 150
            city.lvl += 1
    cities()


def help_command():
    print('\nHELP'
          '\n[create city] - create new city (cost 300)'
          '\n[create unit] - create units in current city'
          '\n[turn] - next turn'
          '\n[help] - help menu'
          '\n[exit] - quit the game\n')
    input('Press ENTER to continue...\n')
    cities()


def create_unit():
    global gold
    print('1.  SOLDIER | HP {0} | ATTACK {1} | COST {2}'
          .format(units_l[0].hp,
                  units_l[0].attack,
                  units_l[0].cost))
    print('2.  BADASS SOLDIER | HP {0} | ATTACK {1} | COST {2}'
          .format(units_l[1].hp,
                  units_l[1].attack,
                  units_l[1].cost))
    print('3.  REALLY BADASS SOLDIER | HP {0} | ATTACK {1} | COST {2}'
          .format(units_l[2].hp,
                  units_l[2].attack,
                  units_l[2].cost))
    print('Enter [UNIT_NUMBER] [NUMBER_OF_UNITS] or [cancel]')
    command = input()
    if command == "cancel":
        print("Cancelled...\n")
        cities()
        commander()
    unit_type = int(command.split()[0]) - 1  # unit type
    n = 1
    if len(command.split()) == 2:  # number:
        n = int(command.split(' ')[1])
    elif len(command.split(' ')) > 2:
        print('INVALID COMMAND')
        create_unit()

    if gold < units_l[unit_type].cost * n:
        print('NOT ENOUGH GOLD ({cost} NEED)\n...\n'
              .format(cost=units_l[unit_type].cost * n))
    else:
        for i in range(n):
            units_l.append(
                Unit(units_l[unit_type].name, 'Capital',
                     units_l[unit_type].cost, units_l[unit_type].hp,
                     units_l[unit_type].attack, True))
            gold -= units_l[unit_type].cost
        print("{0} x {1} Сreated!".format(units_l[unit_type].name, n))

    cities()


cities()
