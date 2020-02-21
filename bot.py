#bot.py
#First created 2019-10-31

import os
import random

import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv
import time
import schedule

#Initializes required tokens from .env-file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix = ".") #Initialize client class

logging.basicConfig(level=logging.INFO) #Initialize logging and status printout


def meetingInfo():
    channel = discord.utils.get(client.get_all_channels(), name="bot-commands")
    channel.send(f"Beep-Boop: Möte som vanligt i sal 318 kl. 15:00 idag. Fika finns som vanligt. \n{discord.Guild.default_role}")
def yeet():
    print("Test1230")

schedule.every().tuesday.at("18:00").do(meetingInfo)
schedule.every().minute.do(yeet)
""" while True: 
    schedule.run_pending() 
    time.sleep(1) 
 """
#Prints BOTs status and connected guild at start
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds)
    print(
        "------------------------------------------------------\n"
        f"{client.user} is connected to the following guild(s):\n"
        f"{guild.name} (id: {guild.id})"
        "\n------------------------------------------------------"
    )

#When new member joins, sends them a direct-message on Dicord
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel_send(f"Hej {member.name}, välkommen till NTI Johannebergs Programmeringsklubb!")

#When member leaves, print to console
#@client.event
#async def on_member_remove(member):
#    print(f"{member} has left the server.")
#    await member.create_dm()
#    await member.dm_channel_send(f"Hej {member.name}, tråkigt att du lämnar oss")

def plus(content):
    # find index of plus
    pos = content.find("+")
    if pos != -1: # if characters isnt found, find() returns -1
        content = "".join(c for c in content if c.isdigit()) # remove all non ints from content
        left_of = content[0:pos]
        right_of = content[pos:len(content)]
        print(left_of + right_of)
        return int(left_of) + int(right_of)

#Commands and responses for client
@client.command(name="ping", help="Returns latency of Bot.")
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(help="Repeats your message n times")
async def repeat(ctx, times: int, content='repeating...'):
    #Repeats a message multiple times.
    for i in range(times):
        await ctx.send(f":clap:{content}:clap:")

""" @client.command(name="meetingInfo")
async def meetingInfo(ctx):
    channel = discord.utils.get(client.get_all_channels(), name="bot-commands")
    await channel.send(f"Beep-Boop: Möte som vanligt i sal 318 kl. 15:00 idag. Fika finns som vanligt. \n{ctx.guild.default_role}") """

@client.command(aliases = ["8ball"], help="The Magic 8 Ball has all the answers to life's questions.")
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.event
async def on_message(message):
    #Checks if BOT sent the message to prevent infinite feedback-loop
    if message.author == client.user:
        return

    programming_jokes = [
        "How many programmers does it take to screw in a light bulb? \n\nNone. It's a hardware problem.",
        "A programmer puts two glasses on his bedside table before going to sleep. A full one, in case he gets thirsty, and an empty one, in case he doesn’t.",
        "Java and C were telling jokes. It was C's turn, so he writes something on the wall, points to it and says \"Do you get the reference?\" \nBut Java didn't.",
        "There are 10 kinds of people in this world: Those who understand binary, those who don't, and those who weren't expecting a base 3 joke.",
        "A programmer is heading out to the grocery store, so his wife tells him \"get a gallon of milk, and if they have eggs, get a dozen.\" He returns with 13 gallons of milk.",
        "What's the best thing thing about UDP jokes? \n\nI don't care if you get them",
        "What's the best part about TCP jokes? \n\nI get to keep telling them until you get them.",
        "Your mama's so FAT she can't save files bigger than 4GB.",
        "In order to understand recursion you must first understand recursion."
    ]

    #Checks the message contains and responds accordingly
    for msg in ["i am", "im", "i'm", "jag är"]: #Dadjoke 
        if msg in message.content.lower():
            response = message.content.lower().split()
            msg_out = response[response.index(msg.split()[-1]) +1]
            await message.channel.send(f"Hej {msg_out}, jag är {client.user}")
    if message.content == "joke":
        response = random.choice(programming_jokes)
        await message.channel.send("Did someone say joke? \n" + response)
    elif message.content == "dm":
        await message.author.send("Test123")
    elif message.content == "Hello":
        await message.channel.send(f"Hello dear {message.author.nick} at {message.guild}, I see you joined {message.author.joined_at}.")
    elif "+" in message.content:
        await message.channel.send(plus(message.content))
    
    await client.process_commands(message) #Enables commands

@commands.guild_only()
@client.command(name="clear")
async def clear(ctx, amount=1):
    role = discord.utils.get(ctx.guild.roles, name="styrelseledamöter")
    if role in ctx.author.roles:
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send(f"{ctx.author} doesn't have permission")



#Advanced logging
#logger = logging.getLogger("discord")
#logger.setLevel(logging.DEBUG)
#handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)

client.run(TOKEN) #Actually starts and runs the BOT