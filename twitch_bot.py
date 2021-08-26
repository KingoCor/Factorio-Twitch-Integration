from irc.bot import SingleServerIRCBot
from configparser import ConfigParser
from requests import get
import cmds

config = ConfigParser()
config.read("config.cfg")

USERNAME = config.get("Twitch", "username")
CHANNEL = config.get("Twitch", "channel")
CLIENT_ID  = config.get("Twitch", "client_id")
TOKEN = config.get("Twitch", "token")

class Bot(SingleServerIRCBot):
    def __init__(self):
        self.HOST = "irc.chat.twitch.tv"
        self.PORT = 6667
        self.USERNAME = USERNAME.lower()
        self.CHANNEL = f"#{CHANNEL}"

        self.CLIENT_ID = CLIENT_ID
        self.TOKEN = TOKEN

        url = f"https://api.twitch.tv/kraken/users?login={self.USERNAME}"
        headers = {"Client-ID": self.CLIENT_ID,
                   "Accept": "application/vnd.twitchtv.v5+json"}
        response = get(url, headers=headers).json()

        super().__init__(
            [(self.HOST, self.PORT, f"oauth:{self.TOKEN}")], self.USERNAME, self.USERNAME)

    def on_welcome(self, cxn, event):
        for req in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")

        cxn.join(self.CHANNEL)
        self.send_message("Now online.")

    def on_pubmsg(self, cxn, event):
        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        user = {"name": tags["display-name"], "id": tags["user-id"]}
        message = event.arguments[0]

        if user["name"] != USERNAME:
            cmds.process(bot, user, message)

    def send_message(self, message):
        self.connection.privmsg(self.CHANNEL, message)

if __name__ == "__main__":
    bot = Bot()
    bot.start()
