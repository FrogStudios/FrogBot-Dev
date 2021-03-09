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

  #tp
  @commands.command()
  async def tp(self, ctx):
    embed=discord.Embed(title="do you want toilet or paper", color=0x00f900)
    embed.add_field(name=">toilet", value="Toilet", inline=True)
    embed.add_field(name=">paper", value="Paper", inline=True)
    embed.add_field(name=">both", value="Both", inline=True)
    await ctx.send(embed=embed)

  #paper
  @commands.command(hidden=True)
  async def paper(self, ctx):
    embed=discord.Embed(title=":newspaper: Ouch paper cut", color=0x00f900)
    await ctx.send(embed=embed) 

  #toilet
  @commands.command(hidden=True)
  async def toilet(self, ctx):
    embed=discord.Embed(title=":toilet: have fun pooping", color=0x00f900)
    await ctx.send(embed=embed)

  #both
  @commands.command(hidden=True)
  async def both(self, ctx):
    embed=discord.Embed(title=":roll_of_paper: :roll_of_paper:  :roll_of_paper:  :roll_of_paper: = $$$$$$$$$", color=0x00f900)
    await ctx.send(embed=embed)




def setup(client):
   client.add_cog(Fun(client))
