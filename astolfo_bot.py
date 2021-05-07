import discord
from discord.ext import commands
from discord.utils import get
import random

print("Starting bot ...\n")
intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)
token = 'ODM4OTMyODQ2MTE3OTEyNjA2.YJCTGQ.Vaj7Z1OixlGP9So4anYKNtY6n2s'
guild = discord.guild
member_list = []


# Displays on terminal when the bot is up.
@client.event
async def on_ready():
    print(' BOT IS READY! '.center(50, '-'))
    channel = client.get_channel(838973221285134378)
    await channel.send(f'BOT IS READY CARALHO!!!')
    for guilda in client.guilds:
        for member in guilda.members:
            if not member.bot:
                member_list.append(member.name)


# Welcome message to new members
@client.event
async def on_member_join(member):
    channel = client.get_channel(839978515427491891)
    print(" ON_MEMBER_JOIN START ".center(50, '-'))
    print(f'Seja bem-viado,  <@!{member.id}>\n Todo mundo aqui é um lixo e ninguém vai te julgar.')
    await channel.send(f'Seja bem-viado,  <@!{member.id}>\n Todo mundo aqui é um lixo e ninguém vai te julgar.')
    print(" ON_MEMBER_JOIN END ".center(50, '-'), '\n')


# Says on discord chat the info of the Author when typed $minfo
@client.command()
async def my_info(ctx):
    print(" MY_NFO START ".center(50, '-'))
    user = ctx.message.author
    await ctx.send(f'''\n
Author name: {user.name}
Author ID: {user.id}
Author Discord Id: {ctx.message.author}
Author Status: {user.status}
Author Role: {user.top_role}
Author Joined At: {user.joined_at}
                    ''')
    print(" MY_NFO END ".center(50, '-'), '\n')


# Says on discord chat the current ping between the bot and the Discord.
@client.command()
async def ping(ctx):
    print(" PING START ".center(50, '-'))
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    print(" PING END ".center(50, '-'), '\n')


# Says on discord chat a random response to a question, based on the list below
# The command is $8ball {question}
@client.command(aliases=['8ball', '.8ball'])
async def _8ball(ctx, *, question):
    print(" 8BALL START ".center(50, '-'))
    responses = ["Com certeza.",
                "Foi decidido que sim.",
                "Sem dúvida",
                "Sim - Definitivamente",
                "Você pode contar com isso.",
                "Ao meu ver, sim.",
                "Provavelmente sim.",
                "Há uma boa perspectiva.",
                "Sim.",
                "Os sinais apontam que sim.",
                "Sua pergunta foi tão bosta que o bot travou.",
                "Pergunte novamente depois.",
                "Melhor não te contar agora.",
                "Não consigo prever agora.",
                "Se concentre e pergunte novamente.",
                "Não conte com isso.",
                "Minha resposta é não.",
                "Minhas fontes dizem que não.",
                "A perspectiva não é muito boa.",
                "Aposto que não."]
    await ctx.send(f'''Pergunta: {question}
                   Resposta: {random.choice(responses)}''')
    print(" 8BALL END ".center(50, '-'))


# Clear the x amount of messages in the requested chat.
# The command is $clear {amount}
@client.command()
async def clear(ctx, amount=5):
    print(" CLEAR START ".center(50, '-'))
    print(f'{ctx.author} cleaned {amount} messages.')
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{ctx.author} cleaned {amount} messages.')
    print(" CLEAR END ".center(50, '-'), '\n')


# Kicks the specified player (ADM ONLY)
# The command is $kick {member} // Member is the id of the kicked person (guy#1234)
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    print(" KICK START ".center(50, '-'))
    if member not in member_list:
        await ctx.send(f'O corno {member} foi kickado pelo motivo:\n - {reason} -\n')
        await kick

    print(" KICK END ".center(50, '-'), '\n')


@client.command()
async def get_members(ctx):
    print(" GET_MEMBERS START ".center(50, '-'))
    for guilda in client.guilds:
        for member in guilda.members:
            if not member.bot:
                member_list.append(member)
                await ctx.send(f'Membro - {member.name}')
    print(" GET_MEMBERS END ".center(50, '-'), '\n')


@client.command()
async def mention_info(ctx, *, mention):
    print(" MENTION_INFO START ".center(50, '-'))
    await ctx.send(mention)
    print(" MENTION_INFO END ".center(50, '-'), '\n')


@client.event
async def on_message(message):
    print(" ON_MESSAGE START ".center(50, '-'))
    if message.author == client.user:
        print(f'bot_message - {message.content}')
        return

    else:
        print(f'Author: {message.author}\nMessage: {message.content}')
        await client.process_commands(message)
    print(" ON_MESSAGE END ".center(50, '-'), '\n')


@client.command()
async def member_info(ctx, * ,user):
    print(" MEMBER_INFO START ".center(50, '-'))
    user = user[3:21]
    for guilda in client.guilds:
        for member in guilda.members:
            if not member.bot and int(user) == int(member.id):
                await ctx.send(f'''
-
Member name: {member.name}
Member ID: {member.id}
Member Status: {member.status}
Member Role: {str(member.top_role).lstrip('@')}
Member Joined At: {member.joined_at}
-
                                ''')
    print(" MEMBER_INFO END ".center(50, '-'), '\n')


client.run(token)
