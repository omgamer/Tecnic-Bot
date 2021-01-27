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
    
@bot.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member = None, *, reason = "No reason provided"):
    if member == None:
      await ctx.send(ctx.author.mention + ", mention member who to kick")
    await member.kick(reason=reason)
    await ctx.send(f' ✅ Kicked  {member.name}')


@bot.command(aliases=['w'])
@commands.has_permissions(kick_members = True)
async def warn(ctx, member : discord.Member = None , *, reason = "No reason provided"):
    if member == None:
       await ctx.send(ctx.author.mention + ", mention member who to warn")
    await ctx.send(member.name + " have been warned. Reason : "+ reason)
    await member.send("You have been warned. Reason : "+ reason)
    
@bot.command(aliases = ['purge'])
@commands.has_permissions(administrator = True)
async def clear(ctx, amount = 5):
  await ctx.channel.purge(limit=amount+1)
  await ctx.send(f'{amount} messages deleted', delete_after=5)



@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, member: str = "", reason: str = "You have been unbanned. Time is over. Please behave"):
        if member == "":
            await ctx.send("Please specify username as text")
            return

        bans = await ctx.guild.bans()
        for b in bans:
            if b.user.name == member:
                await ctx.guild.unban(b.user, reason=reason)
                await ctx.send("User was unbanned")
                return
        await ctx.send("User was not found in ban list.")







      #wait now u can chat
      #
      #Animepdf: Yes
      #
      #OM: okay
      #
      #OM: Why are we doing this? lol
      #
      #Animepdf: idk why not
      #
      #OM: but its kinda fun
      #
      #Animepdf: ye mb
      #
      #OM: lol
      #
      #Animepdf: I go play games ;)
      #
      #OM: Which game?
      #
      #Animepdf: Factorio with my friend
      #
      #OM: okay good ggs but tysm for all of thid = )
      #
      #Animepdf: np
      #
      #OM: dont delete this lol idk why but dont
      #
      #OM: btw do u have vps? can u host my bot? im on mobile so yeah u know
      #
      #Animepdf: yes, when bot will be fully working and completed
      #
      #OM: okay 