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
            "**OHH Meme #1:** https://cdn.discordapp.com/attachments/240902066602508288/352387684808917002/Danymoreofthem.PNG",
            "**OHH Meme #2:** https://cdn.discordapp.com/attachments/240902066602508288/352387687854112778/deaglebelike.PNG",
            "**OHH Meme #3:** https://cdn.discordapp.com/attachments/240902066602508288/352387692639682560/download.jpg",
            "**OHH Meme #4:** https://cdn.discordapp.com/attachments/240902066602508288/352387703016390656/fearK.jpg",
            "**OHH Meme #5:** https://cdn.discordapp.com/attachments/240902066602508288/352387710062821376/Kanymoreofthem.PNG",
            "**OHH Meme #6:** https://cdn.discordapp.com/attachments/240902066602508288/352387718036324353/kistyping.PNG",
            "**OHH Meme #7:** https://cdn.discordapp.com/attachments/240902066602508288/352387724168134666/Kohakuisalwayswatching.PNG",
            "**OHH Meme #8:** https://cdn.discordapp.com/attachments/240902066602508288/352387730161795072/oakybelike.PNG",
            "**OHH Meme #9:** https://cdn.discordapp.com/attachments/240902066602508288/352387733894987790/peanutalwayscomesback.jpg",
            "**OHH Meme #10:** https://cdn.discordapp.com/attachments/240902066602508288/352387744183615498/peanutbelike.PNG",
            "**OHH Meme #11:** https://cdn.discordapp.com/attachments/240902066602508288/352387753310158849/smeaglemydeagle.PNG",
            "**OHH Meme #12:** https://cdn.discordapp.com/attachments/240902066602508288/352387760289611787/vcomesonline.PNG",
            "**OHH Meme #13:** https://cdn.discordapp.com/attachments/240902066602508288/352387766006448129/whentheservsdead.PNG"
    ]
        choice = random.choice(memes)
        await self.bot.say(choice)
def setup(bot):
    bot.add_cog(OHHMemes(bot))
