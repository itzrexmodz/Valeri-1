from modules._config import OWNER_ID, TOKEN, bot
from modules._helpers import load_modules

bot.start(bot_token=TOKEN)
if not OWNER_ID == 1833850637:
    exit(69)  # huehue

load_modules()

bot.run_until_disconnected()
