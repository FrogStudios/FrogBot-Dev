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

  @commands.command(aliases=['8ball', '8 ball'])
  async def eightball(self, ctx, *, question=None): 
    responses = [ ':green_circle: It is certain.',
                  ':green_circle: It is decidedly so.',
                  ':green_circle: Without a doubt.',
                  ':green_circle: Yes – definitely.',
                  ':green_circle: You may rely on it.',
                  ':green_circle: As I see it, yes.',
                  ':green_circle: Most likely.',
                  ':green_circle: Outlook good.',
                  ':green_circle: Yes.',
                  ':green_circle: Signs point to yes.',
                  ':yellow_circle: Reply hazy, try again.',
                  ':yellow_circle: Ask again later.',
                  ':yellow_circle: Better not tell you now.',
                  ':yellow_circle: Cannot predict now.',
                  ':yellow_circle: Concentrate and ask again.',
                  ':red_circle: Dont count on it.',
                  ':red_circle: My reply is no.',
                  ':red_circle: My sources say no.',
                  ':red_circle: Outlook not so good.',
                  ':red_circle: Very doubtful.']  
    embed=discord.Embed(title="Magic 8 Ball", color=0x00f900)
    embed.add_field(name="Question: ", value=f"{question}", inline=True)
    embed.add_field(name="Answer: ", value=f"{random.choice(responses)}", inline=True)
    await ctx.send(embed=embed)



def setup(client):
   client.add_cog(Fun(client))
