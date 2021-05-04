import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$')
token = 'ODM4OTMyODQ2MTE3OTEyNjA2.YJCTGQ.Vaj7Z1OixlGP9So4anYKNtY6n2s'

@client.event
async def on_ready():
        print('-'*35)
        print("Bot ready!")
        print("Server info:")
        print("Logged in as {0.user}".format(client))
        print("ID -", client.user.id)
        for guild in client.guilds:
            print('Server - {}'.format(guild.name))
            print("Number of Members - {}" .format(guild.member_count))

@client.event
async def on_member_join(member):
    print(f'Seja bem-viado, {member}\n todo mundo aqui é um lixo e ninguém vai te julgar.')
    await client.message(f'Seja bem-viado, {member}\n todo mundo aqui é um lixo e ninguém vai te julgar.')


@client.event
async def on_member_remove(member):
    print(f'Ban hammer nessa desgraça chamada {member}')

@bot.command()
async def ping(ctx, arg):
    print(ctx, arg)
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@commands.command()
async def test(ctx, arg):
    print(2)

@bot.command(aliases=['8ball', '.8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run(token)
