# DISCORD MEMBER DISCONNECT TOOL
# **Instructions are available in the README.md file**

import discord
import time

intents = discord.Intents.default()
intents.reactions = True
intents.members = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    while True:
        server = client.get_guild() # Put server's ID between the brackets
        member = server.get_member() # Put member's ID between the brackets
        await member.edit(voice_channel = None)
        time.sleep(1.1)
        
client.run("") # Put your bot token between the quotation marks