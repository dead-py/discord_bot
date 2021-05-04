#!/bin/python3
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)
token = 'ODM4OTMyODQ2MTE3OTEyNjA2.YJCTGQ.Vaj7Z1OixlGP9So4anYKNtY6n2s'
pf_insult = "/insult"

@client.event
async def on_ready():
    print('-'*35)
    print("Server info")
    print("Logged in as {0.user}".format(client))
    print("ID -", client.user.id)
    print("Guilds -")
    for guild in client.guilds:
        print("     ", guild)


@client.event
async def on_message(message):
    if message.content.startswith('$members'):
        member_list = message.guild.members.names
        print(member_list)
        return member_list


client.run(token)
