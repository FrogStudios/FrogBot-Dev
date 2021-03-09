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

class Utility(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def joinroom(self, ctx, rn, rp):
    channel = discord.utils.get(ctx.guild.channels, name=rn)
    if rp == db[f'V{channel.id}']:
      await ctx.author.move_to(channel)
      await ctx.message.delete()


  @commands.command()
  async def lockroom(self, ctx, rp):
    db[f'V{ctx.author.voice.channel.id}'] = rp
    embed=discord.Embed(title="You Have Locked A VC Channel", color=0x00f900)
    embed.set_author(name="Voice Channel Pin", icon_url="https://cdn.discordapp.com/attachments/810707023032483860/818892969347645450/Untitled_design.png")
    embed.add_field(name="Pin", value=rp, inline=True)
    embed.add_field(name="Channel", value=ctx.author.voice.channel.name, inline=True)
    embed.add_field(name="Server", value=ctx.message.guild.name, inline=True)
    embed.add_field(name="Invite Others", value="Do >roominvite To Invite Others", inline=True)
    await ctx.author.send(embed=embed)
    await ctx.message.delete()


  @commands.command()
  async def unlockroom(self, ctx):
    channel = ctx.author.voice.channel.id
    del db[f'V{channel}']

  @commands.command()
  async def roominvite(self, ctx, member: discord.Member):
    embed=discord.Embed(title="Invite", description="You Have Been Invited To A Locked VC Channel", color=0x00f900)
    embed.set_author(name="Voice Channel Pin", icon_url="https://cdn.discordapp.com/attachments/810707023032483860/818892969347645450/Untitled_design.png")
    embed.add_field(name="Inviter", value=ctx.author, inline=True)
    embed.add_field(name="Pin", value=db[f'V{ctx.author.voice.channel.id}'], inline=True)
    embed.add_field(name="Server", value=ctx.message.guild.name, inline=True)
    embed.add_field(name="How To Join", value=f"To Join This VC Do >joinroom {ctx.author.voice.channel.name} {db[f'V{ctx.author.voice.channel.id}']} In {ctx.message.guild.name}", inline=False)
    await member.send(embed=embed)

    

  @commands.command()
  async def deldata(self, ctx):
    for i in db: 
        del db[i]
        print(f'deleted {i}')


  



def setup(client):
   client.add_cog(Utility(client))
