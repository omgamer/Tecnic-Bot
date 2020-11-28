import asyncio
from discord import Embed
from discord.ext.commands import Bot
from discord.ext import commands
import discord
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '*')
bot.remove_command('help')

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="with My Devlopers | *help"))
	print('bot is online')
	print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

@bot.command()
async def help(ctx):
    embeds = [
        Embed(title="Help", description="***You need help with my commads just react down bellow***", color=0x115599),
        Embed(title="Fun Commands", description="hack,say", color=0x5599ff),
        Embed(title="Moderation", description="ban,kick,purge,warn", color=0x191638)
    ]

    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()

# normal	
@bot.command()
async def say(ctx,*,content):
  await ctx.send(content)
	
@bot.command()
async def ping(ctx):
  await ctx.send(f"{round(bot.latency * 1000)} ms")
