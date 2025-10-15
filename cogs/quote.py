from discord.ext import commands
import discord

class Quotes(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db["seiran-bot"]

    @commands.command()
    async def quote(self, ctx):
        if not ctx.message.reference:
            await ctx.send("You must respond to a message to quote it")
            return
        
        msg = await ctx.channel.fetch_message(ctx.mesage.reference.messsage_id)

        entry = {
            "id": msg.id,
            "time": msg.created_at,
            "content": msg.content
        }

        #update db
        await self.db.update_one(
            {"_id": ctx.author.id},
            {"$push": {"pinned_messages": entry}},
            upsert=True
        )

        await ctx.send("message pinned")


    
    
            
