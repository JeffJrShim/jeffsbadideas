from redbot.core import commands
import random
import asyncio
import discord


class RussianRoulette(commands.Cog):
    """russian roulette tbh"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def russianroulette(self, ctx):
        """try your luck"""
        responses_list = [
            "You're safe!",
            "You're safe!",
            "You're safe!",
            "You're safe!",
            "You're safe!",
            "BANG! You're dead now.",
        ]
        choice = random.choice(responses_list)
        embed = discord.Embed(
            description="You pulled the trigger and...", color=await ctx.embed_color()
        )
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(2)
        embed2 = discord.Embed(
            description=f"You pulled the trigger and...\n\n{choice}",
            color=await ctx.embed_color(),
        )
        await msg.edit(embed=embed2)
