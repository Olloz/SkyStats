import json
import aiohttp
from discord.ext import commands
import discord

class skyblock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def playercount(self, ctx):

        json_data = open('private.json')
        hypixeldata = json.load(json_data)

        url = f'https://api.hypixel.net/gameCounts?key={hypixeldata["hypixelKey"]}'

        async with aiohttp.request("GET", url) as response:
            if response.status == 200:
                data = await response.json()
                skyblock = data["games"]["SKYBLOCK"]["players"]
                hub = data["games"]["SKYBLOCK"]["modes"]["hub"]

                embed = discord.Embed(title='Player Counts', color=0x00fffb)
                embed.set_thumbnail(url="https://imgur.com/IWINFPK.png")
                embed.set_footer(text='SkyStats by: Olloz#0001')
                embed.add_field(name='**SkyBlock PLayer Counts**:',
                                value=(f'\n**Total Online**: {skyblock:,}'
                                       f'\n**SkyBlock Hub**: {hub:,}'))

                await ctx.send(embed=embed)
                json_data.close()
                return


def setup(bot):
    bot.add_cog(skyblock(bot))