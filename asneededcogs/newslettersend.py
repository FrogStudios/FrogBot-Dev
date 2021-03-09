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

  @commands.command(hidden=True)
  @commands.is_owner()
  async def newsletter(self, ctx):
    embed=discord.Embed(title="FrogBot Weekly Newsletter", color=0x00f900)
    embed.set_author(name="FrogOnMyPuppyDog", icon_url="https://cdn.discordapp.com/avatars/761001447030259742/65a310d00455da2e81358624027f503a.png")
    embed.add_field(name="New Features:", value="ㅤ", inline=False)
    embed.add_field(name="Warn Command:", value="This command Used in the following context: [>warn(User To Warn Mention) (Reason Of Warn)] will warn a user. Currently warnings are not tracked however in the future that will be tracked", inline=False)
    embed.add_field(name="Rewrite:", value="Frog Bot Is Undergoing Massive Changes that will allow us to add commands without restarting frogbot. In the coming week I will be moving every command into a cog so that they can be added and removed without a restart", inline=False)
    embed.add_field(name="On The Horizon:", value="Discord Has Added / Commands For Bots, However Discord.py currently doesn’t support / Commands here is a statement from the devs of d.py about / commands", inline=False)
    embed.add_field(name="ㅤ", value="“Slash commands are a new way to make commands right within discord, discord.py will probably not support them as they are lacking features and requires a major rewrite to handle.  ”", inline=False)
    embed.set_footer(text="Thanks For Reading This Newsletter And Supporting Frogbot. If You Have Any  Questions Please Contact FrogOnMyPuppyDog")
    await ctx.send(embed=embed)

def setup(client):
   client.add_cog(Fun(client))
