import discord
from discord.ext import commands
from discord.utils import get
import random
import youtube_dl

print("Starting bot ...\n")
intents = discord.Intents.all()
#client = commands.Bot(command_prefix='$', intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)
token = 'ODM4OTMyODQ2MTE3OTEyNjA2.YJCTGQ.Vaj7Z1OixlGP9So4anYKNtY6n2s'
guild = discord.guild
member_list = []


# Displays on terminal when the bot is up.
@bot.event
async def on_ready():
    print(' BOT IS READY! '.center(50, '-'))
    channel = bot.get_channel(838973221285134378)
    await channel.send(f'BOT IS READY CARALHO!!!')
    for guilda in bot.guilds:
        for member in guilda.members:
            if not member.bot:
                member_list.append(member.name)
                print(member.name)


# Welcome message to new members
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(838941962513678358)
    print(" ON_MEMBER_JOIN START ".center(50, '-'))
    print(f'Seja bem-viado,  <@!{member.id}>\n Todo mundo aqui é um lixo e ninguém vai te julgar.')
    await channel.send(f'Seja bem-viado,  <@!{member.id}>\n Todo mundo aqui é um lixo e ninguém vai te julgar.')
    print(" ON_MEMBER_JOIN END ".center(50, '-'), '\n')


# Says on discord chat the info of the Author when typed $minfo
@bot.command()
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
@bot.command()
async def ping(ctx):
    print(" PING START ".center(50, '-'))
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms\n')
    print(" PING END ".center(50, '-'), '\n')


# Says on discord chat a random response to a question, based on the list below
# The command is $8ball {question}
@bot.command(aliases=['8ball', '.8ball'])
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
    await ctx.send(f'''.
    Pergunta: {question}
    Resposta: {random.choice(responses)}''')
    print(" 8BALL END ".center(50, '-'))


# Clear the x amount of messages in the requested chat.
# The command is $clear {amount}
@bot.command()
async def clear(ctx, amount=5):
    print(" CLEAR START ".center(50, '-'))
    print(f'{ctx.author} cleaned {amount} messages.\n')
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'{ctx.author} cleaned {amount} messages.')
    print(" CLEAR END ".center(50, '-'), '\n')


# Kicks the specified player (ADM ONLY)
# The command is $kick {member} // Member is the id of the kicked person (guy#1234)
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    print(" KICK START ".center(50, '-'))
    if member not in member_list:
        await ctx.send(f'O corno {member} foi kickado pelo motivo:\n - {reason} -')
        await kick

    print(" KICK END ".center(50, '-'), '\n')


@bot.command()
async def get_members(ctx):
    print(" GET_MEMBERS START ".center(50, '-'))
    for guilda in bot.guilds:
        for member in guilda.members:
            if not member.bot:
                member_list.append(member)
                await ctx.send(f'Membro - {member.name}')
    print(" GET_MEMBERS END ".center(50, '-'), '\n')


# On message event, logs all the messages on the server
@bot.event
async def on_message(message):
    print(" ON_MESSAGE START ".center(50, '-'))
    if message.author == bot.user:
        print(f'bot_message - {message.content}\n')
        return

    else:
        print(f'Author: {message.author}\nMessage: {message.content}\n')
        await bot.process_commands(message)
    print(" ON_MESSAGE END ".center(50, '-'), '\n')


# Show the specified member info
@bot.command()
async def member_info(ctx, * ,user):
    print(" MEMBER_INFO START ".center(50, '-'))
    user = user[3:21]
    for guilda in bot.guilds:
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


youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'deafault_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title - data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:

            #takes first item from a playlist
            data = data['entries'][0]

        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename


@bot.command()
async def join(ctx):
    print(" JOIN START ".center(50, '-'), '\n')
    if not ctx.message.author.voice:
        await ctx.send(f'{ctx.message.author.name} is not connected to a voice channel.')
        return
    else:
        channel = ctx.author.voice.channel


    await channel.connect()
    print(f'Bot Connected to {channel} channel.')
    print(" JOIN END ".center(50, '-'), '\n')


@bot.command()
async def leave(ctx):
    print(" LEAVE START ".center(50, '-'), '\n')

    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    print(voice_client)

    if voice_client.is_connected():
        print(f' Connected to voice channel.')
        await voice_client.disconnect()

    else:
        await ctx.send('The bot is not connected to a voice channel.')

    print(" LEAVE END ".center(50, '-'), '\n')

@bot.command()
async def play(ctx, url):
    try:
        print('trying')
        server = ctx.message.guilda
        voice_channel = server.voice_client

        async with ctx.typing():
            print('playing')
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send(f'** Now Playing: **\n{filename}')

    except:
        await ctx.send("The bot is not connected to a voice channel.")

bot.run(token)
