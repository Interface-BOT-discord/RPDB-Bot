import disnake
from disnake.ext import commands

helper = disnake.ApplicationCommandInteraction


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='help', description='Получить информацию о боте')
    async def help(self,
                   ctx: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title='Сводка о боте',
                              description='Interface & EraserColor : RPDB \n'
                                          'Бот, который помогает в организации проектов по SCP: RP.')
        embed.add_field(name='Discord', value='https://discord.com/invite/32p2BWqgJn')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
