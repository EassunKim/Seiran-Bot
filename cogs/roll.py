from discord.ext import commands
import random

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, max: int = 100):
        random_int = random.randint(1,max)

        #check for doubles
        num_str = str(random_int)

        if len(num_str) <= 1 or len(set(num_str)) != 1:
            await ctx.send(f"you rolled {random_int}")
        else:
            await ctx.send(f"BOOM! you rolled :sparkles: {random_int} :sparkles: ")

    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("use it right :3 !roll [max value]")

async def setup(bot):
    await bot.add_cog(Roll(bot))