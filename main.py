# main
# Прочитай ссылку про PEP8, реально
import os

FIRST = 1


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
cities_l = []
cities_l.append(City("Capital", 1, 0, 300, 0))
units_l = []
units_l.append(Unit('Soldier', '', 30, 30, 30, True))
units_l.append(Unit('Badass Soldier', '', 50, 65, 65, True))
units_l.append(Unit('REALLY BADASS SOLDIER', '', 75, 90, 90, True))


def commander():
    command = input("INPUT > ")
    if command == "exit":
        exit(1)
    elif 'create unit' in command:
        create_unit()
    elif 'create city' in command:
        if len(command.split(' ')) == 3:
            create_city(command.split(' ')[2])
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
    global FIRST
    if FIRST != 0:
        os.system("cls")
        FIRST = 0
    for city in cities_l:
        city.units = 0
        for unit in units_l:
            if city.name == unit.city:
                city.units += 1
    for i, city in enumerate(cities_l):
        print(("{0}.  CITY {1} | LVL"
               "{2} | EXP {3} OF {4} |"
               "HP {5} OF {6} | UNITS {7}").format(i + 1,
                                                   city.name,
                                                   city.lvl,
                                                   city.exp,
                                                   city.lvl * 150,
                                                   city.hp,
                                                   (city.lvl - 1) * 100 + 300,
                                                   city.units))
        print("----------------------------------------------------------------------------")
    print("GOLD {0} | TURN {1}".format(gold, turns))
    commander()


def create_city(name):
    global gold
    if gold >= 300:
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
    print('\nHELP')
    print('create city [CITY NAME] - create new city')
    print('create unit [UNIT NUMBER] [NUMBER OF UNITS] - create one or more units in city')
    print('turn - next turn')
    print('exit - quit the game\n')
    cities()


def create_unit():
    global gold
    print('1.  SOLDIER | HP {0} | ATTACK {1} | COST {2}'.format(units_l[0].hp,
                                                                units_l[0].attack,
                                                                units_l[0].cost))
    print('2.  BADASS SOLDIER | HP {0} | ATTACK {1} | COST {2}'.format(units_l[1].hp,
                                                                       units_l[1].attack,
                                                                       units_l[1].cost))
    print('3.  REALLY BADASS SOLDIER | HP {0} | ATTACK {1} | COST {2}'.format(units_l[2].hp,
                                                                              units_l[2].attack,
                                                                              units_l[2].cost))
    print('CREATE UNIT [UNIT NUMBER] [NUMBER OF UNITS]', end='')
    command = input()
    unit_type = int(command.split(' ')[0]) - 1  # unit type
    if len(command.split(' ')) == 2:  # number
        n = int(command.split(' ')[1])
    elif len(command.split(' ')) > 2:
        print('INVALID COMMAND')
        create_unit()
        return
    else:
        n = 1
    if gold < units_l[unit_type].cost * n:
        input('NOT ENOUGH GOLD ({cost} NEED)'.format(cost=units_l[unit_type].cost * n))
        cities()
    else:
        for i in range(n):
            if gold >= units_l[unit_type].cost:
                units_l.append(
                    Unit(units_l[unit_type].name, 'Capital',
                         units_l[unit_type].cost, units_l[unit_type].hp,
                         units_l[unit_type].attack, True))
                gold -= units_l[unit_type].cost
            else:
                break
    cities()


cities()
