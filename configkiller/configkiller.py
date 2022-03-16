from redbot.core import commands
import random
import asyncio
import discord


class ConfigKiller(commands.Cog):
    """config killer tbh"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=88888)
        default_global = {
            "foobar": True,
            "foo": {
                "bar": True,
                "baz": False
            }
        }
        default_guild = {
            "blah": [],
            "baz": 1234567890
        }
        self.config.register_global(**default_global)
        self.config.register_guild(**default_guild)

    @commands.command()
    @checks.admin_or_permissions(manage_guild=True)
    async def setbaz(self, ctx, new_value):
        await self.config.guild(ctx.guild).baz.set(new_value)
        await ctx.send("Value of baz has been changed!")

    @commands.command()
    @checks.is_owner()
    async def setfoobar(self, ctx, new_value):
        await self.config.foobar.set(new_value)
        await ctx.send("k")

    @commands.command()
    async def checkbaz(self, ctx):
        baz_val = await self.config.guild(ctx.guild).baz()
        await ctx.send("The value of baz is {}".format("True" if baz_val else "False"))
