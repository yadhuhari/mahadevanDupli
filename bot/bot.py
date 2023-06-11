from pyrogram import Client, enums, __version__

from . import API_HASH, API_ID, LOGGER, BOT_TOKEN 

from bot.plugins.webcode import bot_run
from os import environ
from aiohttp import web as webserver

PORT_CODE = environ.get("PORT", "8080")

class Bot(Client):
    def __init__(self):
        super().__init__(
            "bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={
                "root": "bot/plugins"
            },
            workers=200,
            bot_token=BOT_TOKEN,
            sleep_threshold=10
        )
