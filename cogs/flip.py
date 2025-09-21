from discord.ext import commands
import random

class Flip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx):
        random_int = random.randint(1,10)

        if random_int % 2 == 0:
            await ctx.send("Heads da yo")
        else: 
            await ctx.send("Tails da yo")
            

async def setup(bot):
    await bot.add_cog(Flip(bot))