from redbot.core import commands, Config
import random
import asyncio
import discord


class RussianRoulette(commands.Cog):
    """russian roulette tbh"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=723841)
        default_guild = {
            chances = "6"
        }
        self.config.register_guild(**default_guild)

    @commands.command()
    async def russianroulette(self, ctx):
        """try your luck"""
        russianroulettegenerator=random.randint(1,chances)
        embed = discord.Embed(
            description="You pulled the trigger and...", color=await ctx.embed_color()
            )
        msg = await ctx.send(embed=embed)
        if russianroulettegenerator == 3:
            embed2 = discord.Embed(
                description=f"You pulled the trigger and...\n\nBANG! You're dead!",
                color=await ctx.embed_color(),
            )
            await msg.edit(embed=embed2)
        else: 
            embed3 = discord.Embed(
                description=f"You pulled the trigger and...\n\nBANG! You're safe!",
                color=await ctx.embed_color(),
            )
            await msg.edit(embed=embed3)
    
    @commands.mod()
    @commands.group()
    async def russianrouletteset(self, ctx):
        """Set defaults for the russian roulette"""
        pass
    
    @commands.mod()
    @russianrouletteset.command()
    async def setdefault(self, ctx, new_value: int = 6):
        """Sets the chamber value for the Russian Roulette."""
        if new_value < 6:
            return await ctx.send("The new value cannot be less than 6! Sorry D:")
        else:
            await self.config.guild(ctx.guild).new_value.set(new_value)
            await ctx.send("The new value has been set.")
        
