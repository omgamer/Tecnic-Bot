import discord
from discord.ext import commands
import asyncio
from boto import bot


@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    embed=discord.Embed(title='Error',description='Invalid Command Used. Do ***help**')
    await ctx.send(embed=embed, delete_after=5)
    
    
    