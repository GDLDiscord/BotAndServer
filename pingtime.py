import discord
from discord.ext import commands
import time


class PingTime:
    """Displays the Bot's Ping Time in M/S"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def pingtime(self,ctx):
        """Ping Time"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        await self.bot.say("Ping Time: {}ms".format(round((t2-t1)*1000)))
            
                

def setup(bot):
    bot.add_cog(PingTime(bot))
