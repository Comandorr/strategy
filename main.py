#main
# Прочитай ссылку про PEP8, реально
import os
class City:
	def __init__(self, name, lvl, exp, units):
		self.name = name
		self.lvl = lvl
		self.exp = exp
		self.units = units

class Unit:
	def __init__(self, name, city, cost, active):
		self.name = name
		self.city = city
		self.cost = cost
		self.active = True

gold = 100
turns = 1
cities_l = []
cities_l.append(City("Capital", 1, 0, 0))
units_l = []
units_l.append(Unit('Soldier', 'Capital', 30, True))

def commander():
	command = input("INPUT ")
	if command == "exit": ()
	elif command.split(' ')[0] == 'create':
		if command.split(' ')[1] == 'unit': create_unit (int(command.split(' ')[2]))
		elif command.split(' ')[1] == 'city': create_city(command.split(' ')[2])
	elif command == "turn": turn()
	else: cities()

def cities():
	os.system("clear")
	for city in cities_l:
		city.units = 0
		for unit in units_l:
			if city.name == unit.city:
				city.units +=1

	for i in range(len(cities_l)):
		city = cities_l[i]
		print("{n}.  CITY {name} | LVL {lvl} | EXP {exp} OF {exp1} | UNITS {units}".format(n = i+1, name = city.name, lvl = city.lvl, exp = city.exp, exp1 = city.lvl*150, units = city.units))
		print("----------------------------------------------------------------------------")
	print("GOLD {gold} | TURN {turn}".format(gold = gold, turn = turns))
	commander()

def create_city(name):
	cities_l.append(City(name, 1, 0, 0))	
	cities()

def create_unit(n):
	global gold
	if gold < units_l[0].cost*n:
		print('NOT ENOUGH GOLD')
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

cities()