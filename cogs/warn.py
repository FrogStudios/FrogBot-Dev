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

  #warn
  @commands.command(hidden=True)
  @commands.has_permissions(kick_members=True)
  async def warn(self, ctx, member: discord.Member, *, reason=None):
    embed=discord.Embed(title="Warning", description="You Have Been Warned", color=0x00f900)
    embed.set_author(name=ctx.author)
    embed.add_field(name="Server:", value=f'{ctx.message.guild.name}', inline=True)
    embed.add_field(name="Reason:", value=reason, inline=True)
    await member.send(embed=embed)
    await ctx.send(f'Warned User')

def setup(client):
   client.add_cog(Admin(client))
