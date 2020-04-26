import asyncio
import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='>')

@client.event
async def on_ready() :
    print("Bot is working")
    print(f"{client.user.id}")
    

for cogname in [file[:-3] for file in os.listdir("./cogs/") if file.endswith(".py")] :
    try :
        client.load_extension(f"Cogs.{cogname}")
        print(f"성공적으로 {cogname}이 로드되었음.")
    except Exception :
        print(f"{cogname} 로드를 실패하였음.")

client.run(os.environ["BOT_TOKEN"])
