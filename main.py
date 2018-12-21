from discord.ext import commands
import asyncio

TOKEN = 'BOT-TOKEN' #Here is the bot token

client = commands.Bot(command_prefix=".")

@client.command(pass_context=True)
async def mario(ctx):
    msg = 'MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    await client.send_message(ctx.message.channel, msg)
    author = ctx.message.author
    chan = author.voice_channel
    voice = await client.join_voice_channel(chan)
    while True:
        player = voice.create_ffmpeg_player("mario.mp3")
        player.volume = 100/100
        player.start()
        await asyncio.sleep(60+34)

@client.command(pass_context=True)
async def mario2(ctx):
    msg = 'MAMAMAMAMAMAMAMAMAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    await client.send_message(ctx.message.channel, msg)
    author = ctx.message.author
    chan = author.voice_channel
    voice = await client.join_voice_channel(chan)
    while True:
        player = voice.create_ffmpeg_player("mario2.mp3")
        player.volume = 100/100
        player.start()
        await asyncio.sleep(60+34)

@client.command(pass_context=True)
async def mario3(ctx):
    msg = 'MAAAAAAAAAA'
    await client.send_message(ctx.message.channel, msg)
    author = ctx.message.author
    chan = author.voice_channel
    voice = await client.join_voice_channel(chan)
    while True:
        player = voice.create_ffmpeg_player("mario3.mp3")
        player.volume = 100/100
        player.start()
        await asyncio.sleep(60+34)

@client.command(pass_context=True)
async def padoru(ctx):
    msg = "PAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADORUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
    await client.send_message(ctx.message.channel, msg)
    author = ctx.message.author
    chan = author.voice_channel
    voice = await client.join_voice_channel(chan)
    while True:
        player = voice.create_ffmpeg_player("padorupadoru.mp3")
        player.volume = 100/100
        player.start()
        await asyncio.sleep(60+34)



@client.command(pass_context = True)
async def leav(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)
