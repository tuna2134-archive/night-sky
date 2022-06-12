from discord.ext import commands
from .modules import Module


def setup(bot: commands.Bot):
    bot.add_command(Module)
