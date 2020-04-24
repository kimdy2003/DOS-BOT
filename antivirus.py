import discord
import asyncio
from discord.ext import commands
import requests

key = 'e5e0b291436ee536d101920c9e7986a22b4b41901169ee5e7330525bd4e8a110'

class filechecks(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message) :
        contents = message.content.split()
        for url in contents :
            if url[0:4] == 'http' :
                scaned = linkscan(url)
                checked = linkcheck(scaned['resource'])
                embed = discord.Embed(colour = discord.Colour.blue(), description = checked['url'][8:-2])
                if int(checked['positives']) <= 5 :
                    embed.set_author(name = '이 사이트는 안전합니다!', icon_url = 'https://cdn3.iconfinder.com/data/icons/navigation-elements-1/512/letter-v-key-keyboard-2-512.png')
                elif int(checked['positives']) > 5 :
                    embed.set_author(name = '사이트 접근에 주의가 필요합니다.', icon_url = 'https://iconsetc.com/icons-watermarks/flat-circle-white-on-orange/alphanum/alphanum_lowercase-letter-v/alphanum_lowercase-letter-v_flat-circle-white-on-orange_512x512.png')
                embed.add_field (name = '# checked', value = '총 {0}개의 백신 중 {1}개의 백신에서 문제점을 발견했습니다.'.format(checked['total'], checked['positives']))
                await message.channel.send (embed = embed)
def setup(bot) :
    bot.add_cog(filechecks(bot))


def linkcheck(link) :
        url = 'https://www.virustotal.com/vtapi/v2/url/report'
        params = {'apikey': key, 'resource': link}
        response = requests.post(url, data=params)
        return response.json()

def linkscan(link) :
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': key, 'url':link}
    response = requests.post(url, data=params)
    return response.json()