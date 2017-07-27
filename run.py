import discord
from discord.ext.commands import Bot
import logging
import sys
import os
import config
import asyncio
import random

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
description = '''Python'''
bot = Bot(command_prefix=config.PREFIX) # Sets the client and sets the prefix

bot.run(config.TOKEN)
