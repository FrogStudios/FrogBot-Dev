import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
import asyncio
import logging
from discord.ext import commands
import random
import time


client = commands.Bot(command_prefix='{')

@client.event
async def on_ready():
  print('bot online')
  activity = discord.Activity(name='{Help For Help', type=discord.ActivityType.playing)
  await client.change_presence(status=discord.Status.online, activity=activity)
  user = await client.fetch_user(761001447030259742)
  await user.send('Now Online')




@client.command(hidden=True)
async def loadcmd(ctx, path):
  client.load_extension(path)
  print('loaded')

@client.command(hidden=True)
async def unloadcmd(ctx, path):
  client.unload_extension(path)
  print('unloaded')


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
    print(f'{filename} Now loaded')





keep_alive()

client.run(os.getenv('TOKEN'))
