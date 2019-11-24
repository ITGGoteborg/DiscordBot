#bot.py
#First created 2019-10-31

import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f"{client.user} is connected to the following guild(s):\n"
        f"{guild.name} (id: {guild.id})"
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel_send(
        f"Hej {member.name}, välkommen till NTI Johannebergs Programmeringsklubb!"
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    programming_jokes = [
        "How many programmers does it take to screw in a light bulb? \n\nNone. It's a hardware problem.",
        "A programmer puts two glasses on his bedside table before going to sleep. A full one, in case he gets thirsty, and an empty one, in case he doesn’t.",
        "Java and C were telling jokes. It was C's turn, so he writes something on the wall, points to it and says \"Do you get the reference?\" But Java didn't.",
        "There are 10 kinds of people in this world: Those who understand binary, those who don't, and those who weren't expecting a base 3 joke.",
        "A programmer is heading out to the grocery store, so his wife tells him \"get a gallon of milk, and if they have eggs, get a dozen.\" He returns with 13 gallons of milk.",
        "What's the best thing thing about UDP jokes? \nI don't care if you get them",
        "What's the best part about TCP jokes? \nI get to keep telling them until you get them.",
        "Your mama's so FAT she can't save files bigger than 4GB.",
        "In order to understand recursion you must first understand recursion."
    ]

    if message.content == "joke":
        response = random.choice(programming_jokes)
        await message.channel.send("Did someone say joke? \n" + response)
    elif message.content == "raise-exception":
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open("err.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise

client.run(TOKEN)