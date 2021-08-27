from time import time

import Fcommands

PREFIX = "!"

class Cmd(object):
    def __init__(self, callables, func, cooldown=0, only_owner=False, desciption=""):
        self.callables = callables
        self.func = func
        self.cooldown = cooldown
        self.next_use = time()
        self.only_owner = only_owner
        self.description = desciption

cmds = [
    Cmd(["gri"], Fcommands.give_random_item, desciption="Give random item" ),
    Cmd(["sb"], Fcommands.summon_biters, desciption="Summon biters"),
    Cmd(["dup"], Fcommands.dress_up, desciption="Dress up you"),
    Cmd(["rtp"], Fcommands.random_tp, cooldown=0, desciption="Teleport player to random point"),
    Cmd(["off", "в"], Fcommands.shutdown, only_owner=True),
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
