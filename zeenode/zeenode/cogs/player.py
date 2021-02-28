import discord
import asyncio
import sys
import psutil
import os
client = discord.Client(status=discord.Status.offline)

voice_id=(sys.argv[1])
filename=(input("path to the song"))

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
            await asyncio.sleep(0.5)
        await vc.disconnect(force=True)
client.run("",bot=False)"""token of your alt acc"""
