from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = "5689646"
API_HASH = "895de5ae804308803c19814afabb0de7"
BOT_TOKEN = "5205589679:AAHVdkVgja1qN_UIw4KkjG9sWUHHm6TDMD0"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
