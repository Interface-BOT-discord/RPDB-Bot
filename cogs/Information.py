import disnake
from disnake.ext import commands

helper = disnake.ApplicationCommandInteraction


class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='echo', description='Echo command')
    async def echo(self, ctx: helper, *, message: str, channel: disnake.TextChannel = None):
        print(f'"{message}" from {ctx.author}')
        if channel is None:
            await ctx.send('Sent!', ephemeral=True)
            await ctx.channel.send(message)
        else:
            await ctx.send('Sent!', ephemeral=True)
            await channel.send(message)


def setup(bot):
    bot.add_cog(Entertainment(bot))
