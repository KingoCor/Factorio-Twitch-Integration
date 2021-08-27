from irc.bot import SingleServerIRCBot
from configparser import ConfigParser
from requests import get
import logging
import sys
import cmds

config = ConfigParser()
config.read("config.cfg")

USERNAME = config.get("Twitch", "username")
CHANNEL = config.get("Twitch", "channel")
CLIENT_ID  = config.get("Twitch", "client_id")
TOKEN = config.get("Twitch", "token")

log_enabled = config.getboolean("System", "debug", fallback=False)

def _get_logger(log_enabled=False):
    logger_name = 'Twitch bot'
    logger_ = logging.getLogger(logger_name)
    if not log_enabled:
        logging_handler = logging.NullHandler()
        return logger_
    logger_level = logging.DEBUG
    log_line_format = '%(asctime)s | %(name)s - %(levelname)s : %(message)s'
    log_line_date_format = '%Y-%m-%dT%H:%M:%SZ'

    logger_.setLevel(logger_level)
    logging_handler = logging.StreamHandler(stream=sys.stdout)
    logging_handler.setLevel(logger_level)
    logging_formatter = logging.Formatter(log_line_format, datefmt=log_line_date_format)
    logging_handler.setFormatter(logging_formatter)
    logger_.addHandler(logging_handler)
    return logger_

logger = _get_logger(log_enabled)

class Bot(SingleServerIRCBot):
    def __init__(self):
        logger.debug('Bot.__init__ on channel %s', CHANNEL)
        self.HOST = "irc.chat.twitch.tv"
        self.PORT = 6667
        self.USERNAME = USERNAME.lower()
        self.CHANNEL = f"#{CHANNEL}"

        self.CLIENT_ID = CLIENT_ID
        self.TOKEN = TOKEN

        super().__init__([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")], self.USERNAME, self.USERNAME)

    def on_welcome(self, cxn, event):
        logger.debug('Bot.on_welcome')
        for req in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")

        cxn.join(self.CHANNEL)
        self.send_message("Now online.")

    def on_pubmsg(self, cxn, event):
        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        user = {"name": tags["display-name"], "id": tags["user-id"]}
        message = event.arguments[0]
        logger.debug('Bot.on_pubmsg User %s, message %s', user, message)

        if user["name"] != USERNAME:
            cmds.process(bot, user, message)

    def send_message(self, message):
        logger.debug('Bot.send_message')
        self.connection.privmsg(self.CHANNEL, message)

if __name__ == "__main__":
    if log_enabled:
        logger.warning("Debug mode is enabled")

    bot = Bot()
    bot.start()
    logger.debug('Bot started')
