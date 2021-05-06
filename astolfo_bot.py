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
    print('Bot is ready!')
    for guilda in client.guilds:
        for member in guilda.members:
            if not member.bot:
                member_list.append(member.name)


# Welcome message to new members
@client.event
async def on_member_join(member):
    channel = client.get_channel(839978515427491891)
    print("on_member_join event start")
    print(f'Seja bem-viado,  <@!{member.id}>\n Todo mundo aqui é um lixo e ninguém vai te julgar.')
    await channel.send(f'Seja bem-viado,  <@!{member.id}>\n Todo mundo aqui é um lixo e ninguém vai te julgar.')
    print("on_member_join event end")


# Says on discord chat the info of the Author when typed $minfo
@client.command()
async def minfo(ctx):
    print("minfo command start")
    user = ctx.message.author
    await ctx.send(f'''Author name: {user.name}
                   Author ID: {user.id}
                   Author Discord Id: {ctx.message.author}
                   Author Status: {user.status}
                   Author Role: {user.top_role}
                   Author Joined At: {user.joined_at}
                    ''')
    print("minfo command end")

# Says on discord chat the current ping between the bot and the Discord.
@client.command()
async def ping(ctx):
    print("ping command start")
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    print("ping command end")


# Says on discord chat a random response to a question, based on the list below
# The command is $8ball {question}
@client.command(aliases=['8ball', '.8ball'])
async def _8ball(ctx, *, question):
    print("8ball command start")
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
    print("8ball command end")

# Clear the x amount of messages in the requested chat.
# The command is $clear {amount}
@client.command()
async def clear(ctx, amount=5):
    print("clear command start")
    print(f'{ctx.author} cleaned {amount} messages.')
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{ctx.author} cleaned {amount} messages.')
    print("clear command end")


# Kicks the specified player (ADM ONLY)
# The command is $kick {member} // Member is the id of the kicked person (guy#1234)
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    print("kick command start")
    if member not in member_list:
        await ctx.send(f'O corno {member} foi kickado pelo motivo: - {reason} - \nbye bye bitch bye bye')
    print("kick command end")


@client.command()
async def get_members(ctx):
    print("get_members command start")
    for guilda in client.guilds:
        for member in guilda.members:
            if not member.bot:
                member_list.append(member.name)
                await ctx.send(f'Membro - {member}')
    print("get_members command end")

@client.command()
async def mention_info(ctx, *, mention):
    print("mention_info command start")
    await ctx.send(mention)
    print(author.id)
    print("mention_info command end")

@client.event
async def on_message(message):
    print("on_message event start")
    print(f'{"-"*25}\nAuthor: {message.author}\nMessage: {message.content}\n{"-"*25}')
    await client.process_commands(message)


client.run(token)
