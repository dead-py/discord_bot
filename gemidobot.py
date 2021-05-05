#!/bin/python3
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)
token = 'ODM4OTMyODQ2MTE3OTEyNjA2.YJCTGQ.Vaj7Z1OixlGP9So4anYKNtY6n2s'
member_list = []

@client.event
async def on_ready():
    print('-'*35)
    print("Server info")
    print("Logged in as {0.user}".format(client))
    print("ID -", client.user.id)
    print("\n")
#    for guilda in client.guilds:
#        for member in guilda.members:
#            print(f'Membro - {member.name}')
#            print(f'ID - {member.id}')
#            print(f'Is bot? - {member.bot}')
#            print('\n')
#            if not member.bot:
#                member_list.append(member.name)

#    print(member_list)
@client.command()
async def get_members(ctx):
    for guilda in client.guilds:
        for member in guilda.members:
            print(f'Membro - {member.name}')
            print(f'ID - {member.id}')
            print(f'Is bot? - {member.bot}')
            print('\n')
            if not member.bot:
                member_list.append(member.name)

    print(member_list)
client.run(token)
