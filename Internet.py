import asyncio
import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from twitch import TwitchClient
import r6sapi as api

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = '/users/user/desktop/heroic-venture-270306-6b725eb305d4.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1FxYkmYVxMRHXk1VrBgVk0PBrKlzKVFsQZHw4fDdSbis/edit#gid=0'
doc = gc.open_by_url(spreadsheet_url)

twitchclient = TwitchClient('7xxihwx46oev6r71efiyf5t96vnyii', 'sjnxmpv96rfdna85rt7x0wgodht8d8')


class twitch(commands.Cog) :
        
    def __init__(self, bot) :
        self.bot = bot

    @commands.command()  
    async def streamer(self, ctx, *args) :
        if len(args) > 0 :
            name = args[0]
            if len(args) > 1 :
                for i in range(1, len(args)) :
                    name += ' ' + args[i]
            channels = twitchclient.search.channels(name, limit=25, offset=0)
            ch = channels[0]
            info = discord.Embed(
                colour = discord.Colour.purple()
                ,description = ch.url
                )
            info.set_author (name = ch.display_name, icon_url = 'https://www.net-aware.org.uk/siteassets/images-and-icons/application-icons/app-icons-twitch.png?w=585&scale=down')
            info.add_field(name = '# Follower', value = ch.followers, inline = True)
            info.add_field(name = '# viewes', value = ch.views, inline = True)
            info.set_thumbnail (url = ch.logo)
            await ctx.channel.send (embed = info)


class r6class(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot

    @commands.command()
    async def r6s (self, ctx, name) :
        stat = r6sapi(name)
        await ctx.channel.send (str(stat['level']))
        
       
async def r6sapi(name) :
    r6auth = api.Auth('do_yung@naver.com', 'dy3011010')
    player = r6auth.get_player(name, api.Platforms.UPLAY) 
    return {
        'name' : player.name
        ,'icon' : player.icon_url
        ,'level' : player.level
    }

    

def setup(bot):
    bot.add_cog(twitch(bot))
    bot.add_cog(r6class(bot))