import asyncio
import discord
from discord.ext import commands
import datetime

class commandcog (commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot
    
    @commands.command()
    async def helpcommands (self, ctx) :
        helps = discord.Embed(colour = discord.Colour.gold())
        helps.set_author(name = 'Commands', icon_url = self.bot.user.avatar_url)
        helps.add_field (
            name = 'Dos command'
            , value = '```>info >userinfo```'
            ,inline = True
        )

        await ctx.channel.send (embed = helps)

    @commands.command()
    async def info (self,ctx) :
        infos = discord.Embed(
            colour = discord.Colour.blurple()
            ,description = 'Version : Debugging\n{0}개의 서버에서 사용중'.format(len(self.bot.guilds))
            )
        infos.set_author (name = 'DOS', icon_url = self.bot.user.avatar_url)
        await ctx.channel.send (embed = infos)

    @commands.command(aliaes = ['핑'])
    async def ping (self, ctx) :
        latency = round(self.bot.latency, 4)
        embed = discord.Embed(colour = discord.Colour.blue(), description = f"{latency}ms")
        embed.set_author (name = 'Pong!')
        embed.set_thumbnail(url = 'https://cdn2.iconfinder.com/data/icons/sport-8/70/ping_pong-512.png')
        embed.set_footer (text = datetime.datetime.today())
        await ctx.channel.send (embed = embed)

def setup(bot) :
    bot.add_cog(commandcog(bot))