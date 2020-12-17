import discord
import math
import asyncio
import aiohttp
import json
from discord.ext import commands
from random import randint
import traceback
import sqlite3
import sys
with open("./config.json", "r") as configjsonFile:
    configData = json.load(configjsonFile)
    token = configData["token"]
    prefix = configData["prefix"]

client = discord.Client()

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")


initial_extensions = ['cogs.voice']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Ошибка с {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print('Авторизован бот:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=prefix+"help"))


bot.run(token)
