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
client = discord.Client(status=discord.Status.offline)
full_cmd_arguments = sys.argv
voice_id=full_cmd_arguments[1]
filename=("{}").format(full_cmd_arguments[2])
print (filename)
print(voice_id)
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
            if sys.platform.startswith('linux'):
                proc = psutil.Process(int(parentprocess))
                if proc.status() == psutil.STATUS_ZOMBIE:
                    await client.logout()
                    sys.exit()
            if not psutil.pid_exists(int(parentprocess)):  # Parent is dead, Kill self :cry:
                await client.logout()
                sys.exit()
            await asyncio.sleep(1)
        await vc.disconnect(force=True)
client.run("",bot=False)
