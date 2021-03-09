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

  #kick
  @commands.command(hidden=True)
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked User')




def setup(client):
   client.add_cog(Admin(client))
