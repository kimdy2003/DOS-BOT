import asyncio
import discord
from discord.ext import commands

class functions(commands.Cog) :

    def __init__(self, bot) :
        self.bot = bot
    
    @commands.command()
    async def userinfo (self, ctx, *args) :
        if len(args) > 0 :
            name = args[0]
            if len(args) > 1 :
                for i in range(1, len(args)) :
                     name += ' ' + args[i]
            for member in ctx.author.guild.members :
                if member.display_name == name :
                    embed = discord.Embed(colour = discord.Colour.blue())
                    embed.set_author (name = member.name)
                    embed.set_thumbnail (url = member.avatar_url)
                    embed.add_field (name = '# Name', value = member.name, inline = True)
                    embed.add_field (name = '# Display name', value = member.display_name, inline = True)
                    embed.add_field (name = '# Id', value = str(member.id), inline = True)
                    embed.add_field (name = '# Join date', value = str(member.joined_at)[:-7], inline = True)
                    embed.add_field (name = '# Create date', value = str(member.created_at)[:-7], inline = True)
                    embed.add_field (name = '# Status', value = member.status, inline = True)
                    embed.set_footer(text = 'DOS.')
                    await ctx.channel.send(embed = embed)
        else :
            await ctx.channel.send ('Type user\'s displayed name')

    @commands.command()
    async def findnow(self, ctx) :
        actlst = dict()
        info = str()
        for member in ctx.author.guild.members :
            if member.bot == False :
                act = member.activity
                if type(act) != type(None) :
                    if act.name not in actlst :
                        actlst[act.name] = 1
                    else :
                        temp = actlst[act.name]
                        actlst.update({act.name : temp+1})
        actvi = list(actlst.items())
        for i in range(len(actvi)) :
            info += '\n {0} : __**{1}**__ playing'.format(actvi[i][0], actvi[i][1])
        embed = discord.Embed(colour = discord.Colour.blue(), description = info)
        embed.set_author (name = '현재 상태 목록', icon_url = 'https://cdn3.iconfinder.com/data/icons/text/100/list-512.png')
        embed.set_footer (text = self.bot.user.name, icon_url = self.bot.user.avatar_url)  
        await ctx.channel.send(embed = embed)
            
def setup(bot):
    bot.add_cog(functions(bot))