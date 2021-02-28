import asyncio
from discord.ext import commands
import discord
import asyncio
import sys
import psutil
import os
from threading import Thread
class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def music(self, ctx, author: discord.User = None):
        await ctx.message.delete()
        if ctx.author.voice and ctx.author.voice.channel:
            channel= ctx.author.voice.channel.id
            os.system('start /wait cmd /k python zeenode/cogs/player.py {}'.format(channel))

        else:
            await ctx.send("You are not connected to a voice channel")
            return
def setup(bot):
    bot.add_cog(music(bot))
