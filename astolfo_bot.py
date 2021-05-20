import discord, random, urllib.parse, urllib.request, re
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio
from bot_token import token


print("Starting bot ...\n")
intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')
guild = discord.guild
member_list = []


# Displays on terminal when the bot is up.
@bot.event
async def on_ready():
    print(' BUJÃO IS READY! '.center(50, '-'))

    channel = bot.get_channel(838973221285134378)
    await channel.send(f'Bujão is ready!')
    #await channel.send(GIF_PATH)
    for guilda in bot.guilds:
        for discord.Member in guilda.members:
            if not discord.Member.bot:
                member_list.append(discord.Member)
    print(member_list)

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
    try:
        await ctx.channel.purge(limit=amount+1)
        print(f'{ctx.author} cleaned {amount} messages.\n')
        await ctx.send(f'{ctx.author} cleaned {amount} messages.')

    except:
        await ctx.send(f' \nOpsie!\nNão tenho permissão para excluir mensagens neste canal!')
    print(" CLEAR END ".center(50, '-'), '\n')


# Kicks the specified player (ADM ONLY)
# The command is $kick {member} // Member is the id of the kicked person (guy#1234)
@bot.command(pass_context = True)
async def kick(ctx, member : discord.User, *, reason='corno'):
    print(" KICK START ".center(50, '-'))

    if member in member_list:
        print(f'{member} is on the list.')
        await ctx.guild.kick(member, reason)
        await ctx.send(f'O corno {member} foi kickado pelo motivo:\n - {reason} -')

    else:
        print(f'{member} Not on server')
        await ctx.send(f'O membro {member} não está no servidor!\nTem certeza que informou o id correto?')

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


# Makes the bot join voice channel.
@bot.command()
async def join(ctx):
    print(" JOIN START ".center(50, '-'), '\n')

    if not ctx.message.author.voice:
        await ctx.send(f'The requester {ctx.message.author.name} is not connected to a voice channel.')
        return
    else:
        channel = ctx.author.voice.channel

    try:
        await channel.connect()
        #voice = get(bot.voice_clients, guild=ctx.guild)
        #play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/GÁS_PATH/"))
        print(f'Bot Connected to {channel} channel.')

    except discord.ClientException:
        print('Bot already connected to voice channel.')
        await ctx.send('Bot already connected to voice channel.')

    print(" JOIN END ".center(50, '-'), '\n')


# Make the bot leave from the voice channel.
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

# Plays audio from specific youtube url.
@bot.command()
async def play(ctx, url):
    print(" PLAY START ".center(50, '-'), '\n')

    voice = get(bot.voice_clients, guild=ctx.guild)
    YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.add_default_info_extractors()
            info = ydl.extract_info(url, download=False)

        URL = info['formats'][0]['url']
        try:
            voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS, executable="C:/ffmpeg/bin/ffmpeg.exe"))
            voice.is_playing()

        except discord.AttributeError:
            await ctx.send("The bot is not connected to a voice channel.\nYou must add it with $join")
    else:
        await ctx.send("Already playing song")
        return

    print(" PLAY END ".center(50, '-'), '\n')


# Pauses the currently music, if there's any.
@bot.command()
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()

    else:
        await ctx.send('The bot is not playing anything at the moment.')

# Resumes the paused youtube audio, if there's any.
@bot.command()
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client

    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send('The bot is not playing anything at the moment.\n Use $play command.')


# Stops the youtube audio, if there's any.
@bot.command()
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client

    if voice_client.is_playing():
        await voice_client.stop()

    else:
        await ctx.send('The bot is not playing anything.\nUse the $play command to play something.')


# Search for the arguments passed on youtube and plays the audio.
@bot.command()
async def search(ctx, *, search):
    query_string = urllib.parse.urlencode({'search_query': search})
    html_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                html_content.read().decode())
    try:
        await play(ctx, 'https://www.youtube.com/watch?v=' + search_results[0])
        await ctx.send(f'Playing: https://www.youtube.com/watch?v={search_results[0]}')

    except:
        await ctx.send('Somenthing happened with the Discord API.\nTry again another time.')

#This must be fixed
@bot.command()
async def help(ctx):
     await ctx.send('''

                 - Bot commands -
                 <Bugs are expected, please tell me if you discover anything.>

                 $help: Display the currently working bot commands. or not
                 $ping: Returns a Pong! with the time in ms that the API communicate with the code.
                 $_8ball <question>: This command returns a message with a response for your question. Based on a list of answers.
                 $clear <amount>: Erases the previous <amount> messages, or return a message when the bot or the author have no permission to do that.
                 $kick <member> <reason>: Kicks the specified <member> and displays the <reason>. (The reason is optional.)
                 $get_members: Returns all the members names.
                 $member_info: Returns some info of the <member>.
                 $join: Forces the bot to enter in voice chat. (The caller MUST be on a voice chat, or the bot will not join.)
                 $leave: Forces the bot to leave any voice chat that he joined.
                 $play <youtube link>: Tells the bot to play the AUDIO of the specified youtube video or stream.
                 $pause: Forces the bot to pause ANY currently playing audio.
                 $Resume: Resume the previous paused audio.
                 $stop: Forces the bot to STOP any currently playing audio.
                 $search <my father>: Searches for <my father> on youtube and play the audio from the FIRST video found.

                 <i will probably cry to death if you discover any bug>

                   ''')
# should have a gui implementation here...
def bot_gui():
    print('You should do the gui thing!')
    pass


bot.run(token())
