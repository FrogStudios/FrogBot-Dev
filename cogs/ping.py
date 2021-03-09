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

  #ping
  @commands.command()
  async def Utility(self, ctx):
    embed=discord.Embed(title="Ping", description=f"pong! {round(self.client.latency*1000)}ms", color=0x00f900)
    await ctx.send(embed=embed) 

def setup(client):
   client.add_cog(Utility(client))
