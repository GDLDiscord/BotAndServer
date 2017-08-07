import discord
from discord.ext import commands
import random

client = discord.Client()

class Chickerino:
    """Display a random chickerino meme"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def chicken(self):

        memes = [
            "**Chickerino meme #1** http://i.imgur.com/Qvf8sRI.png",
            "**Chickerino meme #2** http://i.imgur.com/4ImQV1Z.png",
            "**Chickerino meme #3** http://i.imgur.com/RUOsT5j.png",
            "**Chickerino meme #4** http://i.imgur.com/arIDux5.png",
            "**Chickerino meme #5** http://i.imgur.com/P75c85h.png",
            "**Chickerino meme #6** http://i.imgur.com/waWhOLO.png",
            "**Chickerino meme #7** http://i.imgur.com/RHV5X2H.png",
            "**Chickerino meme #8** http://i.imgur.com/2Qv0E5O.png",
            "**Chickerino meme #9** http://i.imgur.com/QV9a4rj.png",
            "**Chickerino meme #11** http://i.imgur.com/QV9a4rj.png",
            "**Chickerino meme #12** http://i.imgur.com/eIqwfro.png",
            "**Chickerino meme #13** http://i.imgur.com/wTSUdfB.png",
            "**Chickerino meme #14** http://i.imgur.com/kGPUWt0.png",
            "**Chickerino meme #15** http://i.imgur.com/MsStVjv.png",
            "**Chickerino meme #16** http://i.imgur.com/jvfu5uS.png",
            "**Chickerino meme #17** http://i.imgur.com/vDBqr42.png",
            "**Chickerino meme #18** http://i.imgur.com/YxrHb8S.png",
            "**Chickerino meme #19** http://i.imgur.com/AisqxU3.png",
            "**Chickerino meme #20** http://i.imgur.com/u1YAUmq.png",
            "**Chickerino meme #21** https://cdn.discordapp.com/attachments/320554920375877634/330019493139054607/unknown.png",
            "**Chickerino meme #22** http://i.imgur.com/sratP8K.png"
    ]
        choice = random.choice(memes)
        await self.bot.say(choice)
def setup(bot):
    bot.add_cog(Chickerino(bot))



