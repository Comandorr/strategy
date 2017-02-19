#main
# Прочитай ссылку про PEP8, реально
import os
class City:
	def __init__(self, name, lvl, exp, units):
		self.name = name
		self.lvl = lvl
		self.exp = exp
		self.units = units
gold = 0
turns = 1
cities_l = []
cities_l.append(City("Capital", 1, 0, 0))

def commander():
	command = input("INPUT ")
	if command == "exit": ()
	elif command == "city": cities()
	elif command[:11] == "create city": create_city(command[12:])
	elif command[:11] == "create unit": create_unit(command[12:])
	elif command == "turn": turn()
	else: commander()

def cities():
	os.system("clear")
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
	(cities_l[int(input("CITY "))-1]).units += int(n) # Зачем скобки?
	cities()

def turn():
	gold += 100
	turns += 1
	# Почему не for city in cities_l?
	# Уменьшает кол-во кода
	for i in range(len(cities_l)):
		city = cities_l[i]
		city.exp += 30
		if city.exp >= city.lvl*150:
			city.exp -= city.lvl*150
			city.lvl += 1
	cities()

cities()