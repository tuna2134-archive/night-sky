from .shell import ShellCog
from discord.ext import commands


async def setup(bot: commands.Bot):
    await bot.add_cog(ShellCog(bot))
