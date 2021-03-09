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

class Utility(commands.Cog):
  def __init__(self, client):
    self.client = client

   #status
  @commands.command()
  async def status(self, ctx):
    embed=discord.Embed(title="FrogBot Status", url="https://stats.uptimerobot.com/qLRpwtOg1X/", description="Password Is frogbot", color=0x00f900)
    await ctx.send(embed=embed)

def setup(client):
   client.add_cog(Utility(client))
