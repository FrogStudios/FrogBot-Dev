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

  @commands.command()
  async def config(self, ctx, type, rw):
    if type == "logs":
      if rw == "write":
        db[f'L{ctx.message.guild.id}'] = ctx.message.channel.id
      if rw == "read":
        await ctx.send(f"Logging Channel Is {db[f'L{ctx.message.guild.id}']}")

def setup(client):
   client.add_cog(Admin(client))
