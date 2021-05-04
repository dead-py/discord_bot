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
    if message.content.startswith(pf_insult):
            await message.channel.send(message.content.lstrip(pf_insult) + " CORNO COACH QUÂNTICO ELEITOR DO BOLSONARO FUDIDO")

    if message.content.startswith('/members'):
        member_list = message.guild.members
        print("Server Name - ", message.guild.name)
        print("Server Owner -", message.guild.owner)
        print("Members Count - ", message.guild.member_count)

        for member in member_list:
            await message.channel.send(member)

    if message.content.startswith('/bot_info'):
        await message.channel.send("This is Astolfo bot, type /help for more info.")
        await message.channel.send("help feature actually not working lmao")

    if message.content.startswith('MOAN help'):
        await message.channel.send("Don't insist, it does not work...")


client.run(token)
