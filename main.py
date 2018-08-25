import os
from collections import namedtuple
import random

import colored
from colored import stylize
import readchar

# TODO: handle Ctrl + C

HeroTypeInfo = namedtuple('HeroTypeInfo', ['hp', 'str', 'dodge', 'description'])

adventurer_type_infos = {
	'f': HeroTypeInfo(hp=30, str=12, dodge=4, description='brave fighter'),
	'n': HeroTypeInfo(hp=30, str=12, dodge=4, description='stealthy ninja'),
	't': HeroTypeInfo(hp=30, str=12, dodge=4, description='sneaky thief'),
}

os.system("cls||clear")

print("--------------------------------------")
print("! ! ! " +
	stylize("Welcome", colored.fg("light_yellow")) +
	" to " +
	stylize("Cave", colored.fg("light_red")) +
	" " +
	stylize("Adventures", colored.fg("light_cyan")) +
	" ! ! !")
print("--------------------------------------")

print()
player_name = input("What is thy name, adventurer? ")
print("Are you a " +
	stylize("F", colored.fg("light_magenta")) +
	"ighter, " +
	stylize("N", colored.fg("light_magenta")) +
	"inja, or " +
	stylize("T", colored.fg("light_magenta")) +
	"hief? ", end='', flush=True)

adventurer_type_id = None
while adventurer_type_id not in adventurer_type_infos:
	adventurer_type_id = readchar.readchar().decode('utf-8').lower()

adventurer_type = adventurer_type_infos[adventurer_type_id]
player_hp = adventurer_type.hp

print("\n")
print("Welcome, " + adventurer_type.description + " " + player_name + "!")
print("Press any key to continue.")

readchar.readchar()

os.system("cls||clear")
print()

enemy_hp = 8
enemy_str = 6
block_chance = 3

print("You are in a room with an IMP!!")

while enemy_hp > 0 and player_hp > 0:
	enemy_mood = random.randint(1, 10)
	print("He looks like he's getting ready to " + ("block" if enemy_mood <= block_chance else "attack") + "!")
	print("Attack, Block, or Run? ")
	readchar.readchar()
	break

print("DONE. EVERYTHING AFTER THIS IS NOT OUR PROGRAM.")
