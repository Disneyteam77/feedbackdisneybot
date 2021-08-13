import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class feedback(Client):
    
    def __init__(self):
        super().__init__(
            session_name="CHANNELFORWARD",
            bot_token = Config.BOT_TOKEN,
            api_id = Config.API_ID,
            api_hash = Config.API_HASH,
            plugins = dict(
                root="plugins"
            )
        )

if __name__ == "__main__" :
    feedback().run()i
