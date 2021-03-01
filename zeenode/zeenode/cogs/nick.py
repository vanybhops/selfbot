import os, sys, ast, json, time, random, base64, requests, shutil, uuid, threading
from itertools import cycle
import urllib.request
import discord
from discord.ext import commands as zeenode
from ..config import auth
import subprocess
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
headers, proxies = setup_request(token)
request = requests.Session()
n = []
for x in name.rstrip():
    n.append(x)
cyclename = cycle(n)
newnick = ''
while name!=stop:
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
