# bot.py
# Vidar Petersson, created 2019-10-31

import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} is connected and ready!")

client.run(token)