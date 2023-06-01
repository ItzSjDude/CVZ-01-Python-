from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

Api_id = ''
Api_hash = ''
bot_token = ''

bot = TelegramClient('BotzHub', Api_id, Api_hash).start(bot_token=bot_token) 
