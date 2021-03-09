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

  #joke
  @commands.command()
  async def joke(self, ctx):
    jokes = ['1. There’s a fine line between a numerator and a denominator.',
              '2. Two windmills are standing on a wind farm. One asks, ‘What’s your favorite kind of music?\nThe other replies, ‘I’m a big metal fan.',                
              '3. Did you hear about the first restaurant to open on the moon?\nIt had great food, but no atmosphere.',
              '4. What did one ocean say to the other ocean?\nNothing, it just waved.',
              '5. Do you want to hear a construction joke?\nSorry, I’m still working on it.',
              '6. Did you hear about the fire at the circus?\nIt was in tents!',
              '7. Why do ducks have feathers?\nTo cover their butt quacks!',
              '8. What’s the difference between a hippo and a zippo?\nOne is really heavy and the other’s a little lighter.',
              '9. What does a nosey pepper do?\nIt gets jalapeño business.',
              '10. Why should you never trust stairs?\nThey’re always up to something.',
              '11. When does a joke become a ‘dad’ joke?\nWhen it becomes apparent.',
              '12. Why did the bullet end up losing his job?\nHe got fired.',
              '13. What kind of shorts do clouds wear?\nThunderpants',
              '14. I entered ten puns in a contest to see which would win.\nNo pun in ten did.',
              '15. How do you measure a snake?\nIn inches—they don’t have feet.',
              '16. Where does a waitress with only one leg work?\nIHOP.',
              '17. What does a house wear?\nAddress!',
              '18. Why are toilets always so good at poker?\nThey always get a flush',
              '19. Why is Peter Pan always flying?\nBecause he Neverlands.',
              '20. You heard the rumor going around about butter?\nNever mind, I shouldn’t spread it.']
    embed=discord.Embed(title="Jokes", description=f"{random.choice(jokes)}", color=0x00f900)
    await ctx.send(embed=embed)


def setup(client):
   client.add_cog(Fun(client))
