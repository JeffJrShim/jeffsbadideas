from .configkiller import ConfigKiller


def setup(bot):
    bot.add_cog(ConfigKiller(bot))