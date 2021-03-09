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

  #commands
  @commands.command(hidden=True)
  @commands.is_owner()
  async def botrestart(self, ctx):
    embed=discord.Embed(title="FrogOnMyPuppyDog Wanted Me To Let You Know That He Is Restarting Me Right N", color=0x00f900)
    await ctx.send(embed=embed)

def setup(client):
   client.add_cog(Owner(client))
