import discord

class Giveaway:
    """General Dev Bot Commands"""

    def __init__(self, bot):
        self.bot = bot
        
        @commands.command(pass_context=True)
        async def giveaway(self,em):
    	"""Enter The Gift Card Giveaway!"""
            em = discord.Embed(description='YOU HAVE BEEN ENTERED INTO THE GIFTCARD GIVEAWAY!', colour=0xFF0000)
   	        em.set_author(name='GIVEAWAY BOT', url='discord.me/gdl')
   	        em.set_thumbnail(url='http://isahotel.com.au/wp-content/uploads/2016/02/Gift_Card.jpg')

def setup(bot):
    bot.add_cog(Giveaway(bot))
