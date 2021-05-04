import discord
from discord.ext import commands
import random
#from gemidobot.py import on_message

client = commands.Bot(command_prefix='$')
token = 'ODM4OTMyODQ2MTE3OTEyNjA2.YJCTGQ.Vaj7Z1OixlGP9So4anYKNtY6n2s'
member_list = []

# Displays on terminal when the bot is up.
@client.event
async def on_ready():
    print('Bot is ready!')


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
                "Como eu vejo, sim.",
                "Provavelmente sim.",
                "Há uma boa perspectiva.",
                "Sim.",
                "Os sinais apontam que sim.",
                "Resposta incerta, tente novamente.",
                "Pergunte novamente depois.",
                "Melhor não te contar agora.",
                "Não consigo prever agora.",
                "Se concentre e pergunte novamente.",
                "Não conte com isso.",
                "Minha resposta é não.",
                "Minhas fontes dizem que não.",
                "Não tem uma perspectiva muito boa.",
                "Muito duvidoso."]
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




client.run(token)
