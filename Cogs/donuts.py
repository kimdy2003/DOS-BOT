import discord
from discord.ext import commands
import asyncio
import datetime
import time
import math


class donut(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def eval (self, ctx, *args) :
        args = " ".join(args)
        try :
            result = eval(args)
            embed = discord.Embed(colour = discord.Colour.green(), title = f"```{result}```")
            embed.set_author(name = 'OUTPUT', icon_url = 'https://img.icons8.com/ios-filled/2x/output.png')
            await ctx.channel.send(embed=embed)
        except : 
            await ctx.channel.send("Command raised an exception!")

def setup(bot) :
    bot.add_cog(donut(bot))
    
    