import discord
from discord.ext import commands
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
from aiohttp import ClientSession
import time
import os
import random
import asyncio
from boto import bot

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.User = None,*, reason = "No reason provided"):
    if member == None:
      await ctx.send(ctx.author.mention + ", mention member who to ban")
    await member.ban(reason=reason)
    await ctx.send(f':white_check_mark:  Banned {member.name}') 
    
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member = None, *, reason = "No reason provided"):
    if member == None:
      await ctx.send(ctx.author.mention + ", mention member who to kick")
    await member.kick(reason=reason)
    await ctx.send(f' ✅ Kicked {member.mention}') 
    
@bot.command(aliases=['w'])
@commands.has_permissions(kick_members = True)
async def warn(ctx, member : discord.Member = None , *, reason = "No reason provided"):
    if member == None:
       await ctx.send(ctx.author.mention + ", mention member who to warn")
    await ctx.send(member.mention + " have been warned. Reason : "+ reason)
    await member.send("You have been warned. Reason : "+ reason)
    
@bot.command(aliases = ['clear'])
@commands.has_permissions(administrator = True)
async def __clear(ctx, amount = 5):
  await ctx.channel.purge(limit=amount+1)
  await ctx.send(f'{amount} messages deleted')
