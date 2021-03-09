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

class Fun(commands.Cog):
  def __init__(self, client):
    self.client = client

  #tired
  @commands.command()
  async def tired(self, ctx):
    embed=discord.Embed(title="me to, but bots arent allowed to sleep, :sad: the last time I selpt was March 5 2015", color=0x00f900)
    await ctx.send(smbed=embed)


def setup(client):
   client.add_cog(Fun(client))
