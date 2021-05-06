import discord
from discord.ext import commands
import random

print("Starting bot ...\n")
intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)
token = 'ODM4OTMyODQ2MTE3OTEyNjA2.YJCTGQ.Vaj7Z1OixlGP9So4anYKNtY6n2s'
member_list = []


# Displays on terminal when the bot is up.
@client.event
async def on_ready():
    global monke_state
    monke_state = False
    print('Bot is ready!')
    for guilda in client.guilds:
        for member in guilda.members:
            if not member.bot:
                member_list.append(member.name)


# Welcome message to new members
@client.event
async def on_member_join(member):
    print(f'Seja bem-viado, {member}\n todo mundo aqui é um lixo e ninguém vai te julgar.')
    await client.message(f'Seja bem-viado, {member}\n todo mundo aqui é um lixo e ninguém vai te julgar.')


# Says on discord chat the info of the Author when typed $minfo
@client.command()
async def minfo(ctx):
    user = ctx.message.author
    await ctx.send(f'''Author name: {user.name}
                   Author ID: {user.id}
                   Author Discord Id: {ctx.message.author}
                   Author Status: {user.status}
                   Author Role: {user.top_role}
                   Author Joined At: {user.joined_at}
                    ''')


# Says on discord chat the current ping between the bot and the Discord.
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# Says on discord chat a random response to a question, based on the list below
# The command is $8ball {question}
@client.command(aliases=['8ball', '.8ball'])
async def _8ball(ctx, *, question):
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


# Clear the x amount of messages in the requested chat.
# The command is $clear {amount}
@client.command()
async def clear(ctx, amount=5):
    print(f'{ctx.author} cleaned {amount} messages.')
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{ctx.author} cleaned {amount} messages.')


# Kicks the specified player (ADM ONLY)
# The command is $kick {member} // Member is the id of the kicked person (guy#1234)
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if member not in member_list:
        await ctx.send(f'O corno {member} foi kickado por {reason}.\nbye bye bitch bye bye')


@client.command()
async def get_members(ctx):
    for guilda in client.guilds:
        for member in guilda.members:
            if not member.bot:
                member_list.append(member.name)
                await ctx.send(f'Membro - @{member.name}')


@client.command()
async def mention_info(ctx, *, mention):
    await ctx.send(mention)


@client.event
async def on_message(message):
    print(f'{"-"*25}\nAuthor: {message.author}\nMessage: {message.content}\n{"-"*25}')
    await client.process_commands(message)

client.run(token)
pass
