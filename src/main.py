import discord
from discord.ext import commands
from modules.utils import get_token, get_prefix
import os
import logging


intents = discord.Intents().all()

bot = commands.Bot(command_prefix=get_prefix(), intents=intents)

for filename in os.listdir('./src/entertaiment'):
    if filename.endswith('.py'):
        print(f'Carregando entertaiment {filename}')
        bot.load_extension(f'entertaiment.{filename[:-3]}')
for filename in os.listdir('./src/events'):
    if filename.endswith('.py'):
        print(f'Carregando event {filename}')
        bot.load_extension(f'events.{filename[:-3]}')
for filename in os.listdir('./src/cogs'):
    if filename.endswith('.py'):
        print(f'Carregando cogs {filename}')
        bot.load_extension(f'cogs.{filename[:-3]}')
        
bot.run(get_token()) 