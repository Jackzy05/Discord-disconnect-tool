# Discord member disconnect tool

Has it ever occurred to you that you had to gradually disconnect someone from a discord server because you didn’t want a certain person in the voice channel but that person was constantly joining back into the voice channel? 

Well, then you are in the right place as it can also be done automatically! If you want to have your own discord bot that will **disconnect people from a discord voice channel for you indefinitely**, follow the instructions below!

*If you don't have any development knowledge, it is recommended to join the [Discord support server](https://discord.gg/wU3P5PpEbd) to get help.*

### 📎 Useful links

These explain some stuff you'll need to use for the project to work properly!

- [Where can I find my discord User/Server/Message ID?](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)
- [What is a command line?](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line)
- [How to run Python code](https://www.knowledgehut.com/blog/programming/run-python-scripts#:~:text=The%20most%20basic%20and%20the,the%20keyboard%20and%20that's%20it.)

### ⚡ Configuration
Open the main file located in ```main.py``` and fill in all the needed ID's and your bot's token. Every place where you should fill in info is marked with #
```py
# DISCORD MEMBER DISCONNECT TOOL

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

And of course, you'll also need a code editor. Some are listed below:
- [VSCode](https://code.visualstudio.com/)
- [Sublime Text](https://www.sublimetext.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Atom](https://atom.io/)


