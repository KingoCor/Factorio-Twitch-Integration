from time import time

import Fcommands

PREFIX = "!"

class Cmd(object):
    def __init__(self, callables, func, cooldown=0, only_owner=False):
        self.callables = callables
        self.func = func
        self.cooldown = cooldown
        self.next_use = time()
        self.only_owner = only_owner

cmds = [
    Cmd(["gri", "всп"], Fcommands.give_random_item),
    Cmd(["sb", "ыи"],   Fcommands.summon_biters),
    Cmd(["dup", "вгз"], Fcommands.dress_up),
    Cmd(["off", "щаа"], Fcommands.shutdown, only_owner=True)
]


def process(bot, user, message):
    if message.startswith(PREFIX):
        cmd = message.split(" ")[0][len(PREFIX):]
        args = message.split(" ")[1:]
        perform(bot, user, cmd, *args)


def perform(bot, user, call, *args):
    if call in ("help", "commands", "cmds"):
        Fcommands.help(bot, PREFIX, cmds)

    else:
        for cmd in cmds:
            if call in cmd.callables:
                if time() > cmd.next_use:
                    cmd.func(bot, user, *args)
                    cmd.next_use = time() + cmd.cooldown

                else:
                    bot.send_message(f"Cooldown still in effect. Try again in {cmd.next_use-time():,.0f} seconds.")

                return

        bot.send_message(f"{user['name']}, \"{call}\" isn't a registered command.")
