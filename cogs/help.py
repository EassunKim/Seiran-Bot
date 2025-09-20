from discord.ext import commands

#imports


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send("For commands and bot info go to https://eassunkim.github.io/Seiran-Bot/")

async def setup(bot):
    await bot.add_cog(help(bot))