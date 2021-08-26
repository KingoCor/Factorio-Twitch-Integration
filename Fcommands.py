from datetime import timedelta
from sys import exit
from time import time
import factorio_rcon

BOOT_TIME = time()
OWNER = "your twitch nickname"

client = factorio_rcon.RCONClient("0.0.0.0", 25575, "123")

def help(bot, prefix, cmds):
	bot.send_message(f"Registered commands: "
		+ ", ".join([f"{prefix}{cmd.callables[0]}" for cmd in sorted(cmds, key=lambda cmd: cmd.callables[0])]))

	bot.send_message(f"Registered commands (incl. aliases): "
		+ ", ".join([f"{prefix}{'/'.join(cmd.callables)}" for cmd in sorted(cmds, key=lambda cmd: cmd.callables[0])]))


def give_random_item(bot, user ,*args):
	client.send_command("/gri")
	bot.send_message(f"@{user['name']} give random item")

def dress_up(bot, user ,*args):
	client.send_command("/dup")
	bot.send_message(f"@{user['name']} dress up you")

def summon_biters(bot, user ,*args):
	client.send_command("/sb")
	bot.send_message(f"@{user['name']} summon biters around")


def shutdown(bot, user, *args):
	if user["name"].lower() == OWNER:
		bot.send_message("Shutting down.")
		bot.disconnect()
		exit(0)

	else:
		bot.send_message("You can't do that.")