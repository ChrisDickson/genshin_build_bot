import discord
import os
from dotenv import load_dotenv
from genshin_funcs import get_build, get_set

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):

    switcher = {
        "!build": get_build,
        "!artifact": get_set,
    }

    if message.author == client.user:
        return
    
    choice = message.content.split(" ")[0]
    args = message.content.split(" ")[1:]
    item = switcher[choice]
    if callable(item):
        resp = item(*args)
        for r in resp:
            await message.channel.send(r)
    else:
        await message.channel.send(f"Invalid option - valid options are: {switcher.keys()}")


client.run(DISCORD_TOKEN)