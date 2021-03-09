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

class Admin(commands.Cog):
  def __init__(self, client):
    self.client = client

  #clear
  @commands.command(hidden=True)
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, ammount=1):
    await ctx.channel.purge(limit=ammount)

def setup(client):
   client.add_cog(Admin(client))
