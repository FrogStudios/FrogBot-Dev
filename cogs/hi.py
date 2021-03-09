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
  
  #hi
  @commands.command()
  async def hi(self, ctx):
    embed=discord.Embed(title="Hello", color=0x00f900)
    await ctx.send(embed=embed)


def setup(client):
   client.add_cog(Fun(client))
