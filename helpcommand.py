import asyncio
import discord
from discord.ext import commands


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


def setup(bot) :
    bot.add_cog(commandcog(bot))