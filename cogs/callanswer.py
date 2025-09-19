from discord.ext import commands

class callanswer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if message.content.lower() == "hi":
            await message.reply(":3")

        
async def setup (bot):
    await bot.add_cog(callanswer(bot))