# Factorio Twitch Integration

## How to setup

#### 1. Generate client ID
For the bot, you may want to create a separate twitch account (alternatively you can just use your current twitch account).
Note: you will need Two-Factor Authentication (2FA) enabled for this step.

Go to https://dev.twitch.tv/ and login with this twitch account. Then click `Your Console`->`Register Your Application`.
Fill in the fields:

 * name: `FactorioChatBot`
 * OAuth Redirect URLs: `https://twitchapps.com/tokengen/`
 * Category: `Chat Bot`

Complete the reCAPTCHA and click `save` at the bottom.
Copy the Client ID and paste it into `config.cfg`.

#### 2. Changing Factorio RCON settings to host the server locally

If you are hosting the game locally, instead of a dedicated server then follow these instruction.
Otherwise if you already have a dedicated server, look up how to enable the RCON interface with a particular port and password.

1. On the main menu screen, hold Ctrl+Alt and then left click "Settings"
2. Now select the last item "The rest".
3. By `local-rcon-socket`, enter `0.0.0.0:25575`
4. By `local-rcon-password`, enter `my_password` (or any secret password, the same one as in settings.txt)
5. Then click confirm, and go back to the main menu.
6. Click Multiplayer -> Host a save game
7. Select the game you want to host.
8. Click Play

#### 3. Rename config.cfg.example to config.cfg adn fill
Section `[Twitch]`\
`channel = CHANNEL_NAME` The channel your bot will connect to\
`client_id = CLIENT_ID`  Your registered application's Client ID to allow API calls by the bot\
`token = TOKEN`  Your OAuth Token\
`username = USERNAME` The username of the chatbot\

Section `[Rcon]`\
`host=0.0.0.0` from `local-rcon-socket` before `:`\
`port=25575` from `local-rcon-socket` after `:`\
`password=my_password` from `local-rcon-password`\

Section `[System]`\
`debug=True or False` Enable or disable debug mode with log messages in console\

#### 4. Start the chatbot
Run `python twitch_bot.py`

## Big Thanks
@UnlucksMcGee
