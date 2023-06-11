#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import Client, __version__

from . import API_HASH, API_ID, LOGGER


class User(Client):
    def __init__(self):
        super().__init__(
            "userbot",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=20
        )
