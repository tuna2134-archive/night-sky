from discord.ext import commands
from .modules import setup as setup_sys


def setup(bot: commands.Bot):
    return setup_sys
