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
ydl_opts = {}
full_cmd_arguments = sys.argv
song=full_cmd_arguments[2]
channel=full_cmd_arguments[1]
played = []
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
            'outtmpl': 'zeenode/cogs/Music/{}.webm'.format(song),
            'default-search':'ytsearch',
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
