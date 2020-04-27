import discord
from discord.ext import commands
import asyncio
import datetime


class donut(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear (self, ctx, *args) :
        await ctx.channel.purge(limit=None)

    @commands.command()
    async def date (self, ctx) :
        await ctx.channel.send(f"{datetime.datetime.today()}")
    
    @commands.command()
    async def userid(self, ctx, *name) :
        if bool(name) == False :
            await ctx.channel.send(f"Your id is {ctx.author.id}")
        else :
            name = list(name)
            name = " ".join(name)
            for member in ctx.author.guild.members :
                if member.display_name == name :
                    await ctx.channel.send(f"{member.name}'s id is {member.id}")

    @commands.command()
    async def chanid(self, ctx, *name) :
        try :
            name = list(name)
            name = " ".join(name)
            for channel in ctx.author.guild.channels :
                if channel.name == name :
                    await ctx.channel.send(f"{name} ID : {channel.id}")
        except :
            await ctx.channel.send(":: Command Error")

def setup(bot) :
    bot.add_cog(donut(bot))
    
    