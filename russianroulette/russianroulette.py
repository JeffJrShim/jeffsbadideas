from redbot.core import commands
import random

class RussianRoulette(commands.Cog):
    """russian roulette tbh"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def russianroulette(self, ctx):
        """try your luck"""
        await ctx.send("testing if this works")