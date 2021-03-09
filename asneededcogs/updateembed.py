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
  async def updateembedsend(self, ctx):
    embed=discord.Embed(title="V2 Change Log:", color=0x00f900)
    embed.set_author(name="FrogOnMyPuppyDog", icon_url="https://cdn.discordapp.com/avatars/761001447030259742/65a310d00455da2e81358624027f503a.png")
    embed.add_field(name="Mayjor Rewrite", value="Frogbot was rewritten to have all commands in seprate files. so that commands can be added without a restart", inline=False)
    embed.set_footer(text="Thanks For Supporting Frogbot. If You Have Any  Questions Please Contact FrogOnMyPuppyDog")
    await ctx.send(embed=embed)
  

def setup(client):
   client.add_cog(Owner(client))
