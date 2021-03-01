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
    async def music(self, ctx, *args,author: discord.User=None):
        await ctx.message.delete()
        if ctx.author.voice and ctx.author.voice.channel:
            channel= ctx.author.voice.channel.id
            message=''
            for arg in args:
                message = message + " " + arg
            song=('"{}"'.format(message))
            os.system('start /wait cmd /k python zeenode/cogs/play.py {} {}'.format(channel,song))
        else:
            await ctx.send("You are not connected to a voice channel")
            return

def setup(bot):
    bot.add_cog(music(bot))
