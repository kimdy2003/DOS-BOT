import asyncio
import discord
from discord.ext import commands
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os 

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'heroic-venture-270306-6b725eb305d4.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1FxYkmYVxMRHXk1VrBgVk0PBrKlzKVFsQZHw4fDdSbis/edit#gid=0'
doc = gc.open_by_url(spreadsheet_url)

client = commands.Bot(command_prefix = '>')
token = os.environ["TOKEN"]

@client.event
async def on_ready () :
    print ("Bot is working")
    print (client.user.id)

@client.event
async def on_guild_join(guild) :
    doc.add_worksheet(str(guild.id), rows = '5', cols = '10')

@client.command(aliaes = ['핑'])
async def ping (ctx) :
    latency = round(client.latency, 4)
    embed = discord.Embed(colour = discord.Colour.blue(), description = '{}ms'.format(latency))
    embed.set_author (name = 'Pong!')
    embed.set_thumbnail(url = 'https://cdn2.iconfinder.com/data/icons/sport-8/70/ping_pong-512.png')
    embed.set_footer (text = datetime.datetime.today())
    await ctx.channel.send (embed = embed)

startup_extensions = ['Internet','helpcommand', 'userinfo']
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

client.run(token)

