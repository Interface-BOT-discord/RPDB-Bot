import disnake
from disnake.ext import commands

from data import *

helper = disnake.ApplicationCommandInteraction


class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='logChannel', description='указать канал для логов')
    async def set_log_channel(self, ctx: helper, channel: disnake.TextChannel):
        if ctx.permissions.administrator or ctx.author.guild_permissions.administrator:
            await ctx.send('database table not found.', delete_after=7)
        else:
            await ctx.send('Недостаточно прав!', delete_after=7)


def setup(bot):
    bot.add_cog(Settings(bot))
