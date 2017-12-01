import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import os



class Yomamma:

    """Yomamma insult cog created by Vulcan"""
    def __init__(self, bot):
        self.bot = bot
        self.insults = fileIO("data/yomamma/yomammas.json","load")

    @commands.command(pass_context=True, no_pm=True)
    async def yomamma(self, ctx, user : discord.Member=None):
        """Insult the user"""

        msg = ' '
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = "I dont have a mom... I'm a bot :robot: "
                await self.bot.say(user.mention + msg)
            else:
                await self.bot.say(user.mention + msg + randchoice(self.insults))
        else:
            await self.bot.say(ctx.message.author.mention + msg + randchoice(self.insults))


def check_folders():
    folders = ("data", "data/yomamma/")
    for folder in folders:
        if not os.path.exists(folder):
            print("Creating " + folder + " folder...")
            os.makedirs(folder)


def check_files():
    """Moves the file from cogs to the data directory. Important -> Also changes the name to yomammas.json"""
    insults = {"You're mom ugly as hell damn. Probably why most of your friends are online right?"}

    if not os.path.isfile("data/yomamma/yomammas.json"):
        if os.path.isfile("cogs/put_in_cogs_folder.json"):
            print("moving default insults.json...")
            os.rename("cogs/put_in_cogs_folder.json", "data/yomamma/yomammas.json")
        else:
            print("creating default yomammas.json...")
            fileIO("data/yomamma/yomammas.json", "save", insults)


def setup(bot):
    check_folders()
    check_files()
    n = Yomamma(bot)
    bot.add_cog(n)
