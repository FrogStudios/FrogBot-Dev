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

  #ban
  @commands.has_permissions(ban_members=True)
  @commands.command(hidden=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned User')

def setup(client):
   client.add_cog(Admin(client))
