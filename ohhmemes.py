import discord
from discord.ext import commands
import random

client = discord.Client()

class OHHMemes:
    """Display a random meme from the "Our Humber Home" server """

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ohhmeme(self):

        memes = [
            "**OHH Meme #1:** ",
    ]
        choice = random.choice(memes)
        await self.bot.say(choice)
def setup(bot):
    bot.add_cog(OHHMemes(bot))
