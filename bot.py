#bot.py
#First created 2019-10-31

import os
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

client.run(TOKEN)