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

class AutoMod(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_message(self, message):
    if "testing" in message.content:
      embed=discord.Embed(title="Warning", description="You Have Been Warned", color=0x00f900)
      embed.set_author(name="AutoMod",  icon_url="https://image.flaticon.com/icons/png/512/421/421630.png")
      embed.add_field(name="Server:", value=f'{message.guild.name}', inline=True)
      embed.add_field(name="Reason:", value='Use Of Bad Words In Public Chat', inline=True)
      await message.author.send(embed=embed)
      await message.delete()
      embed=discord.Embed(description=f"{message.author} Has Been Warned", color=0x00f900)
      embed.set_author(name="AutoMod", icon_url="https://image.flaticon.com/icons/png/512/421/421630.png")
      embed.add_field(name="Reason", value="Use Of Bad Words In Public Chat", inline=False)
      await message.channel.send(embed=embed)

def setup(client):
   client.add_cog(AutoMod(client))
