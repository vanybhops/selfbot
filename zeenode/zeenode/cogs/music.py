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
    async def music(self, ctx,message,author: discord.User=None):
        await ctx.message.delete()
        try:
            if ctx.author.voice and ctx.author.voice.channel:
                channel= ctx.author.voice.channel.id
                song=message
                os.system('start /wait cmd /k python zeenode/cogs/play.py {} {}'.format(channel,song))
                os.system('start /wait cmd /k python C:/213/launch.py')
                exit()
            else:
                await ctx.send("You are not connected to a voice channel")
                return
        except:
            print("jebem ti boga mrtvog sto neces")
            pass

def setup(bot):
    bot.add_cog(music(bot))
