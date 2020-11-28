import discord
from discord.ext import commands
import random
import asyncio
from boto import bot

@bot.command()
async def meme(ctx):
  
  images = ['Meme 1.jpeg','Meme 2.jpeg','Meme 3.jpeg']
  
  random_image = random.choice(images)
  
  await ctx.send(file=discord.File(random_image))
