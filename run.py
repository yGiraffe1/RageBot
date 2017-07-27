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
bot.remove_command("help")

@bot.command(pass_context=True)
async def help(ctx):
    """Help"""
    em = discord.Embed(color=author.colour)
    em.add_field(name='COMMANDS', value=("\n"
                                         "**Commands**\n"
                                         ""))
@bot.command()
async def warn(user="", reason=""):
    """Warn Someone"""
    if user == "":
      await bot.say(":x: Error 101 : No user Mentioned!")
    if reason == "":
      await bot.say(":x: Error 101 : No Reason Entered!")
    try:
      em = discord.Embed(color=author.colour)
      em.add_field(name=':warning: Warning', value=("\n"
                                          "You have been warned!"))
      em.add_field(name='Reason', value=(reason))
      await bot.say(embed=em)
    except:
        await bot.say(":x: Error 404 : No Embed Permissions!")
bot.run(config.TOKEN)
