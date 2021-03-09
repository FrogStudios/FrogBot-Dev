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

  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    if after.author == self.client.user:
      return

    logch = db[f'L{before.guild.id}']
    logc = discord.utils.get(before.guild.channels, id=logch)
    embed=discord.Embed(title="Message Edited", color=0x00f900)
    embed.set_author(name="Logging", icon_url="https://cdn1.iconfinder.com/data/icons/jetflat-multimedia-vol-2/90/004_090_log_script_file_document_sheet_page_text-512.png")
    embed.add_field(name="Before", value=before.content, inline=True)
    embed.add_field(name="After", value=after.content, inline=True)
    embed.add_field(name="ㅤ", value="ㅤ", inline=True)
    embed.add_field(name="User", value=before.author, inline=True)
    embed.add_field(name="Channel", value=before.channel.name, inline=True)
    embed.add_field(name="ㅤ", value="ㅤ", inline=True)
    await logc.send(embed=embed)

  
    

    


def setup(client):
   client.add_cog(Fun(client))
