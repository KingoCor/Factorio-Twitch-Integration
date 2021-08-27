from configparser import ConfigParser
from sys import exit
from time import time
import factorio_rcon

config = ConfigParser()
config.read("config.cfg")

BOOT_TIME = time()
OWNER = config.get("Twitch", "channel")

client = factorio_rcon.RCONClient(config.get("Rcon", "host"), config.getint("Rcon", "port"), config.get("Rcon", "password"))

def help(bot, prefix, cmds):
    commands = filter(lambda cmd: cmd.only_owner==False, sorted(cmds, key=lambda cmd: cmd.callables[0]))
    bot.send_message(f"Registered commands (incl. aliases): "
                    + ", ".join([f"{prefix}{'/!'.join(cmd.callables)} {cmd.description}" for cmd in commands]))

def give_random_item(bot, user, *args):
    client.send_command("/gri")
    bot.send_message(f"@{user['name']} give random item")

def dress_up(bot, user, *args):
    client.send_command("/dup")
    bot.send_message(f"@{user['name']} dress up you")

def summon_biters(bot, user, *args):
    client.send_command("/sb")
    bot.send_message(f"@{user['name']} summon biters around")

def random_tp(bot, user ,*args):
	client.send_command("/rtp")
	bot.send_message(f"@{user['name']} teleport you")

def shutdown(bot, user, *args):
    if user["name"].lower() == OWNER:
        bot.send_message("Shutting down.")
        bot.disconnect()
        exit(0)
    else:
        bot.send_message("You can't do that.")
