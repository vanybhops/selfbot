import os, sys, ast, json, time, random, base64, requests, shutil, uuid, threading
from itertools import cycle
import urllib.request
import discord
from discord.ext import commands as zeenode
from ..config import auth
from threading import Thread
class mass(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot


    @zeenode.command()
    async def massreact(self, ctx, emote):
        await ctx.message.delete()
        messages = await ctx.message.channel.history(limit=100).flatten()
        for message in messages:
            await message.add_reaction(emote)


    @zeenode.command()
    async def spam(self, ctx, amount:int=None, *, message: str=None):
        await ctx.message.delete()
        for each in range (0, amount):
            await ctx.send(f"{message}")
    @zeenode.command()
    async def nick(self,ctx,message: str=None):
        server=ctx.message.guild.id
        await ctx.message.delete()
        name= message
        def request_new_proxy():
            proxy_origin = select_random_proxy()
            if proxy_auth == 1:
                proxies = {
                    'http': f'{proxy_type}://{proxy_user}:{proxy_pass}@{proxy_origin}',
                    'https': f'{proxy_type}://{proxy_user}:{proxy_pass}@{proxy_origin}'
                }
            else:
                proxies = {
                    'http': f'{proxy_type}://{proxy_origin}',
                    'https': f'{proxy_type}://{proxy_origin}'
                }
            return proxies
        global token
        token=auth
        def setup_request(token):
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
            }
            use_proxies=0
            if use_proxies == 1:
                proxy_origin = select_random_proxy()
                if proxy_auth == 1:
                    proxies = {
                        'http': f'{proxy_type}://{proxy_user}:{proxy_pass}@{proxy_origin}',
                        'https': f'{proxy_type}://{proxy_user}:{proxy_pass}@{proxy_origin}'
                    }
                else:
                    proxies = {
                        'http': f'{proxy_type}://{proxy_origin}',
                        'https': f'{proxy_type}://{proxy_origin}'
                    }
            else:
                proxies = {
                    "http": None,
                    "https": None,
                }
            return headers, proxies
        def newthread():
            headers, proxies = setup_request(token)
            request = requests.Session()
            n = []
            for x in name.rstrip():
                n.append(x)
            cyclename = cycle(n)
            global newnick
            newnick = ''
            while name!="stop":
                if len(newnick) == len(name.rstrip()):
                    newnick = ''
                newnick += next(cyclename)
                payload = {'nick': newnick}
                while True:
                    try:
                        src = request.patch(f'https://canary.discordapp.com/api/v6/guilds/{server}/members/@me/nick', headers=headers, json=payload, proxies=proxies, timeout=10)
                    except Exception:
                        if use_proxies == 1:
                            proxies = request_new_proxy()
                        else:
                            break
                    else:
                        break
                time.sleep(1)
        Thread(target = newthread).start()
    Thread(target = nick).start()



def setup(bot):
    bot.add_cog(mass(bot))
