import discord
from discord.ext import commands

class own(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.Activity(type=discord.ActivityType.competing, name="Development!"))
        print('lol why are we here')

def setup(bot):
    bot.add_cog(own(bot))