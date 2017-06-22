import discord
from discord.ext import commands

class AdvancedBotHelp:
    """A small help guide to GDL Bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self):
        """Invite GDL Bot to you're server with this link"""

        
        await self.bot.say("**Invite GDL Bot with this link!** - https://discordapp.com/oauth2/authorize?client_id=289855165056679937&scope=bot&permissions=469765175")

    @commands.command()
    async def server(self):
        """Official GDL Discord Link"""

        
        await self.bot.say("**Join the Official GDL Discord server with this link - https://discord.gg/GJ2N2en**")

    @commands.command()
    async def support(self):
        """Official GDL Bot Support"""

        
        await self.bot.say("**Need help with GDL Bot? Ask in our support channel! - https://discord.gg/7uFKtE7**")

def setup(bot):
    bot.add_cog(AdvancedBotHelp(bot))
