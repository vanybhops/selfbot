import asyncio
from discord.ext import commands
import discord
import asyncio
import sys
import psutil
import os
from threading import Thread
import os
import sys
import time
import ctypes
import random
import requests
import subprocess
import youtube_dl

class music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def p(self, ctx, *args,author: discord.User=None):
        def play():
            ydl_opts = {}
            played = []
            try:
                os.remove("zeenode/cogs/Music/none.wav")
            except:
                pass

            if not os.path.isdir('zeenode/cogs/Music/'):
                os.mkdir('zeenode/cogs/Music/')
            while True:
                selectedsong = song
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info('ytsearch:'+selectedsong, download=False)
                    video_title = info_dict.get('title', None)
                if os.path.isfile('zeenode/cogs/Music/{}.wav'.format(video_title)):
                    pass
                else:
                    ydl_opts = {
                        'outtmpl': 'zeenode/cogs/Music/none.webm',
                        'default-search':'ytsearch',
                        'quite': 'true',
                        'postprocessor_args': ['-loglevel', 'panic'],
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'wav',
                        'preferredquality': '192',
                        }],
                    }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download(['ytsearch:{}'+selectedsong])
                p = subprocess.Popen(['python ','zeenode/cogs/player.py ','{}'.format(channel),'zeenode/cogs/Music/{}.wav'.format(song),str(os.getpid())])
                while p.poll() is None:
                    ctypes.windll.kernel32.SetConsoleTitleW("Playing: {}".format(video_title))
                    time.sleep(3)
                played.append(selectedsong)
                if len(played) == len(selectedsong):
                    break
        await ctx.message.delete()
        if ctx.author.voice and ctx.author.voice.channel:
            channel= ctx.author.voice.channel.id
            message=''
            for arg in args:
                message = message + " " + arg
            song=('"{}"'.format(message))
            Thread(target=play).start()
        else:
            await ctx.send("You are not connected to a voice channel")
            return

def setup(bot):
    bot.add_cog(music(bot))
