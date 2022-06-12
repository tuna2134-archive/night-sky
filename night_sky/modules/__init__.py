from .manager import Manager
from discord.ext import commands


async def setup(bot: commands.Bot):
    await bot.add_cog(Manager(bot))
