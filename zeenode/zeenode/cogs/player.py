import os
import sys
import time
import ctypes
import random
import requests
import subprocess
import youtube_dl
import discord
import asyncio
import psutil
client = discord.Client(status=discord.Status.offline)
full_cmd_arguments = sys.argv
voice_id=full_cmd_arguments[1]
filename=("C:/213/zeenode/cogs/Music/none.wav")
if not os.path.isdir('zeenode/cogs/Music/'):
    os.mkdir('zeenode/cogs/Music/')
@client.event
async def on_ready():
    await asyncio.sleep(1)
    voice_channel = client.get_channel(int(voice_id))
    while not client.is_closed():
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(filename))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1
        while vc.is_playing():
            await asyncio.sleep(1)
    exit()
    os.remove("zeenode/cogs/Music/none.wav")
client.run("",bot=False)
