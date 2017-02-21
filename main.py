#main
# Прочитай ссылку про PEP8, реально
import os

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
	command = input("INPUT ")
	if command == "exit": ()
	elif command == 'create unit': create_unit_v2()
	elif command == 'create city':
		if len(command.split(' ')) == 3: create_city(command.split(' ')[2])
		else:
			print('INVALID COMMAND')	
			commander()
	elif command == "turn": turn()
	elif command == 'help': help()
	else:
		print('INVALID COMMAND')
		commander()

def cities():
    os.system("clear")
    for city in cities_l:
        city.units = 0
        for unit in units_l:
            if city.name == unit.city:
                city.units +=1

    """
    Этот цикл можно заменить на:
    for number, value in enumerate(cities_l):
        ...
    Про enumerate() прочитай в доках
    """
    for i in range(len(cities_l)):
        city = cities_l[i]
        print("{n}.  CITY {name} | LVL {lvl} | EXP {exp} OF {exp1} | HP {hp} OF {hp1} | UNITS {units}".format(n=i+1,
                                                                                           name = city.name,
                                                                                           lvl=city.lvl,
                                                                                           exp=city.exp,
                                                                                           exp1=city.lvl*150,
                                                                                           hp = city.hp,
                                                                                           hp1 = 300+(city.lvl-1)*100,
                                                                                           units = city.units))
        print("----------------------------------------------------------------------------")
    print("GOLD {gold} | TURN {turn}".format(gold = gold, turn = turns))
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

def create_unit(n):
    global gold
    if gold < units_l[0].cost*n:
        print('NOT ENOUGH GOLD ({cost} NEED)'.format(cost = 30*n))
        commander()
    else:
        for i in range(n):
            if gold >= units_l[0].cost:
                units_l.append(Unit('Soldier','Capital', 30, True))
                gold -= units_l[0].cost
            else: break
    cities()

def turn():
    global gold
    gold += 100
    global turns
    turns += 1
    for city in cities_l:
        city.exp += 30
        if city.exp >= city.lvl*150:
            city.exp -= city.lvl*150
            city.lvl += 1
    cities()

def help():
	os.system('clear')
	print('HELP')
	print('create city "name"')
	print('create unit + nomer & kolichestvo')
	print('turn')
	input('exit')
	cities()

def create_unit_v2():
	global gold
	print('1.  SOLDIER | HP {hp} | ATTACK {atk} | COST {cost}'.format(hp = units_l[0].hp,
															atk = units_l[0].attack,
															cost = units_l[0].cost))
	print('2.  BADASS SOLDIER | HP {hp} | ATTACK {atk} | COST {cost}'.format(hp = units_l[1].hp,
															atk = units_l[1].attack,
															cost = units_l[1].cost))
	print('3.  REALLY BADASS SOLDIER | HP {hp} | ATTACK {atk} | COST {cost}'.format(hp = units_l[2].hp,
															atk = units_l[2].attack,
															cost = units_l[2].cost))
	command = input()
	u = int(command.split(' ')[0])-1   #unit type
	if len(command.split(' ')) == 2:		   #number
		n = int(command.split(' ')[1])
	elif len(command.split(' ')) == 1: n = 1
	if gold < units_l[u].cost*n:
		input('NOT ENOUGH GOLD ({cost} NEED)'.format(cost = units_l[u].cost*n))
		cities()
	else:
		for i in range(n):
				if gold >= units_l[u].cost:
					units_l.append(Unit(units_l[u].name, 'Capital', units_l[u].cost, units_l[u].hp, units_l[u].attack, True))
					gold -= units_l[u].cost
				else: break
	cities()
help()