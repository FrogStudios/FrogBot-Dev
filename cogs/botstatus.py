import discord
import os
import requests
import json
import random
from replit import db
import asyncio
import logging
from discord.ext import commands
import random

class Owner(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(hidden=True)
  @commands.is_owner()
  async def botstatus(self, ctx, mode, *, namestatus):
    if mode == "dnd":
      activity = discord.Activity(name=namestatus, type=discord.ActivityType.playing)
      await self.client.change_presence(status=discord.Status.dnd, activity=activity)
    if mode == "online":
      activity = discord.Activity(name=namestatus, type=discord.ActivityType.playing)
      await self.client.change_presence(status=discord.Status.online, activity=activity)
    if mode == "idle":
      activity = discord.Activity(name=namestatus, type=discord.ActivityType.playing)
      await self.client.change_presence(status=discord.Status.idle, activity=activity)

def setup(client):
   client.add_cog(Owner(client))
