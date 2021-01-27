import asyncio
import discord
import random
import platform
from itertools import cycle
from discord import Embed
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from disputils import BotEmbedPaginator 
from keep_alive import keep_alive
#BotConfirmation, BotMultipleChoice 
#hmmmm why? it worked for me

#YES IT WORKED!!
# I IMPLEMENTED IT!


intents = discord.Intents.all()
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = '*', intents = intents)
bot.remove_command('help')
status = cycle(['with Technic Bot Developers', '*help'])

@bot.event
async def on_ready():
  change_status.start()
  print('bot is online')
  print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))
  
@bot.command()
async def help(ctx):
  embed=discord.Embed(title="HELP COMMAND", description="Here are the list of Commands", color=discord.Colour.gold())
  embed.set_author(name="Technic Bot", url="https://discord.com/oauth2/authorize?client_id=769879892049133568&permissions=8&scope=bot")
  embed.set_thumbnail(url="https://c.tenor.com/HsQkCVGaPPMAAAAM/lizzie-mcguire-help.gif")
  embed.add_field(name="Fun Commands", value="***meme** (Gives you a random meme)  \n***hack** (Hacks The Member You Mention, not really )", inline=True)
  embed.add_field(name="Moderator Commands", value="***kick** (Kicks The Member You Mention) \n***ban** (Bans The Member You Mention)  \n***warn** (Warns The Member You Mention)  \n***unban** (Unbans The Member You Mention)  \n***clear** (Clears The Messages Of Amount You Gave", inline=True)
  embed.add_field(name="Normal Commands", value="***ping** (Sends Ping of The Bot) \n***say** (Prints The Message You Send) \n***poll** (Polls Your Message")
  embed.set_footer(text="Made by OM_GaminG#8785, Aashish#4160, JustAnSucide69#5386 & uwu#2059 ")
  await ctx.send(embed=embed)


# normal	
@bot.command()
async def say(ctx,*,content):
  await ctx.send(content)
	
@bot.command()
async def ping(ctx):
  await ctx.send(f"{round(bot.latency * 1000)} ms")
  
  
@bot.command()
async def poll(ctx,*,content:str = None):
  embed = discord.Embed(title='**POLL**',description=f'{content}')
  if content == None:
    await ctx.send("Pls provide description")
  else:
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    

    
    
keep_alive()