from discord.ext import commands
import random

class Flip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx, max: int = 100):
        if max is None:
            max = 100
        random_int = random.randint(1,max)

        #check for doubles
        num_str = str(random_int)

        if len(num_str) <= 1 or len(set(num_str)) != 1:
            await ctx.send(f"you rolled {random_int}")
        else:
            await ctx.send(f"BOOM! you rolled :sparkles: {random_int} :sparkles: ")

async def setup(bot):
    await bot.add_cog(Flip(bot))