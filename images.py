from discord.ext import commands


class images:
    def __init__(self, bot):
        self.bot = bot
        self.base = 'data/images/images/'

    @commands.command(pass_context=True)
    async def jesus(self, context):
        await self.bot.send_file(context.message.channel, '{}jesuschrist.jpg'.format(self.base))

    @commands.command(pass_context=True)
    async def gaben(self, context):
        await self.bot.send_file(context.message.channel, '{}gaben.jpg'.format(self.base))

def setup(bot):
    n = images(bot)
    bot.add_cog(n)
