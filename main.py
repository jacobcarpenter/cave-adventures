import os
import colored
from colored import stylize
import readchar

adventurer_descriptions = {
	'f': 'brave fighter',
	'n': 'stealthy ninja',
	't': 'sneaky thief'
}

os.system("cls||clear")

print()

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
adventurer = input("What is thy name, adventurer? ")
print("Are you a " +
	stylize("F", colored.fg("light_magenta")) +
	"ighter, " +
	stylize("N", colored.fg("light_magenta")) +
	"inja, or " +
	stylize("T", colored.fg("light_magenta")) +
	"hief? ", end='', flush=True)

while True:
	adventurer_type = readchar.readchar().decode('utf-8').lower()
	if adventurer_type in adventurer_descriptions :
		break


print("\n")
print("Welcome, " + adventurer_descriptions[adventurer_type] + " " + adventurer + "!")
print("Press any key to continue.")

readchar.readchar()

os.system("cls||clear")

print("DONE. EVERYTHING AFTER THIS IS NOT OUR PROGRAM.")
