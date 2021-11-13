# Discord member disconnect tool

Has it ever occurred to you that you had to gradually disconnect someone from a discord server because you didn’t want a certain person in the voice channel but that person was constantly joining back into the voice channel? 

Well, then you are in the right place as it can also be done automatically! If you want to have your own discord bot that will **disconnect people from a discord voice channel for you indefinitely**, follow the instructions below!

*If you don't have any development knowledge, it is recommended to join the Discord support server to get help.*

### ⚡ Configuration
Open the main file located in ```main.py```.
```py
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
```

### 📑 Installation
To use the project correctly you will need some tools.

[Python](https://www.python.org/downloads/) to run the code.

After installing python you'll need to install [Discord.py](https://github.com/Rapptz/discord.py). You can do so by opening your preffered command line and running the ```pip install discord``` command.

Without forgetting of course the code editor.


