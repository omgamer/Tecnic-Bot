import discord
from discord.ext.commands import command
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
from discord import Embed
from aiohttp import ClientSession
import time
from discord.ext.commands.cooldowns import BucketType
import os
import random

bot = Bot(command_prefix = '*')
bot.remove_command('help')

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="with My Devlopers | *help"))
	print('bot is online')

@bot.event
async def on_command_errors(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Invaild Command used.')

# normal	
@bot.command()
async def say(ctx,*,content):
	await ctx.send(content)
	
@bot.command()
async def ping(ctx):
	await ctx.send(bot.latency)

# Fun
@bot.command()
async def hack(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return

    passwords=['imnothackedlmao','sendnoodles63','ilovenoodles','icantcode','christianmicraft','server','icantspell','hackedlmao','WOWTONIGHT','69'] 
    fakeips=['154.2345.24.743','255.255. 255.0','356.653.56','101.12.8.6053','255.255. 255.0']

    embed=discord.Embed(title=f"**Hacking: {member}** 0%", color=0x2f3136)
    m = await ctx.send(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 19%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 34%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 55%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 67%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 84%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 99%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(1)
    embed=discord.Embed(title=f"**Hacking: {member}** 100%", color=0x2f3136)
    await m.edit(embed=embed)
    time.sleep(3)
    embed=discord.Embed(title=f"{member} info ", description=f"*Email `{member}@hacked.com` Password `{random.choice(passwords)}`  IP `{random.choice(fakeips)}`*", color=0x2f3136)
    embed.set_footer(text="this is a joke plses dont worry.")
    await m.edit(embed=embed)
    time.sleep(1)	

# Mod 	
@bot.command()
@has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f':white_check_mark:  Banned {member.mention}') 
    
@bot.command()
@has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f' ✅ Kicked {member.mention}') 
    
@bot.command(aliases=['w'])
@has_permissions(kick_members = True)
async def warn(ctx, member : discord.Member, *, reason = "No reason provided"):
    await ctx.send(member.mention + " have been warned. Reason : "+ reason)
    await member.send("You have been warned. Reason : "+ reason)
    
@bot.command(aliases = ['clear'])
@has_permissions(administrator = True)
async def __clear(ctx, amount = 5):
  await ctx.channel.purge(limit=amount+1)

#Help
@bot.command()
async def help(ctx):
    embeds = [
        Embed(title="Help", description="***You need help with my commads just react down bellow***", color=0x115599),
        Embed(title="Fun Commands", description="hack,say", color=0x5599ff),
        Embed(title="Moderation", description="ban,kick,purge,warn", color=0x191638)
    ]

    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()
    
    
bot.run('NzY5ODc5ODkyMDQ5MTMzNTY4.X5VchQ.__YKEuclK3m-fwzO7eWMrUP94OM')
        
        
