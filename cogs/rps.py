from discord.ext import commands

#imports
import discord


class MyView(discord.ui.View):
    def __init__(self, author:discord.Member, tagged:discord.Member):
        super().__init__(timeout=120)
        self.allowed_users={author.id, tagged.id}
        self.choices = {}
        self.author=author
        self.tagged=tagged

    async def interaction_check(self, interaction: discord.Interaction):
        if interaction.user.id not in self.allowed_users:
            await interaction.response.send_message(
                "You were not challenged."
            )
            return False
        return True
    
    async def winner(self):
        choice1 = self.choices[self.author.id]
        choice2 = self.choices[self.tagged.id]
        
        if choice1 == choice2:
            return "Draw!"
        elif choice1 == "Rock":
            if choice2 == "Paper":
                return f"{self.tagged} papers {self.author} GG!"
            else: 
                return f"{self.author} rocks {self.tagged} GG!"
        elif choice1 == "Paper":
            if choice2 == "Scisssors":
                return f"{self.tagged} scissors {self.author} GG!"
            else: 
                return f"{self.author} papers {self.tagged} GG!"
        elif choice1 == "Scissors":
            if choice2 == "Rock":
                return f"{self.tagged} rocks {self.author} GG!"
            else: 
                return f"{self.author} scissors {self.tagged} GG!"
    
    async def ret_choice(self, interaction:discord.Interaction, choice: str):
        self.choices[interaction.user.id] = choice
        await interaction.response.send_message(
            f"You chose {choice}", ephemeral= True
        )

        # #disable buttons after choice is made
        # for child in self.children:
        #     child.disabled = True

        # await interaction.message.edit(view=self)

        #once both have chosen
        if set(self.choices.keys()) == self.allowed_users:
            for child in self.children:
                child.disabled = True
            message = await self.winner()
            await interaction.message.edit(content=message, view = self)

    
    @discord.ui.button(label="Rock", style=discord.ButtonStyle.primary)
    async def rock(self, interaction: discord.Interaction, button: discord.ui.button):
        await self.ret_choice(interaction, "Rock")

    @discord.ui.button(label="Paper", style=discord.ButtonStyle.primary)
    async def paper(self, interaction: discord.Interaction, button: discord.ui.button):
        await self.ret_choice(interaction, "Paper")

    @discord.ui.button(label="Scissors", style=discord.ButtonStyle.primary)
    async def scissors(self, interaction: discord.Interaction, button: discord.ui.button):
        await self.ret_choice(interaction, "Scissors")




class rps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx, member:discord.Member):
        view=MyView(ctx.author, member)
        await ctx.send(
            f"{ctx.author.mention} challenges {member.mention}",
            view=view
        )

    @rps.error
    async def rps_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("use it right :3 !rps @<user>")

async def setup(bot):
    await bot.add_cog(rps(bot))