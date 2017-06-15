import discord
from discord.ext import commands


class PingTime:
    """Displays the Bot's Ping Time in M/S"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pingtime(self):

         
            
                pongmsg = await self.bot.say("**Pong!**")
                await self.bot.edit_message(pongmsg, new_content="**Pong! Pinging...**")
            
                def timedelta_milliseconds(td):
                    return td.days*86400000 + td.seconds*1000 + td.microseconds/1000

                await self.bot.edit_bot(pongmsg, new_content="**Pong! Took:  {}ms**".format(str(int(timedelta_milliseconds(pongmsg.timestamp-message.timestamp)))))

def setup(bot):
    bot.add_cog(PingTime(bot))

