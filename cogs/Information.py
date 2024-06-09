import disnake
from disnake.ext import commands

helper = disnake.ApplicationCommandInteraction


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='help', description='Получить информацию о боте и проекте')
    async def help(self,
                   ctx: disnake.ApplicationCommandInteraction,
                   dm: str = commands.Param(name='в_личку', choices=['да', 'нет'])):
        embed = disnake.Embed(title='Сводка о боте',
                              description='Interface & EraserColor : RPDB \n'
                                          'Бот, который помогает в организации проектов по SCP: RP.')
        embed.add_field(name='Discord', value='https://discord.com/invite/32p2BWqgJn')
        embed.add_field(name='YouTube', value='https://www.youtube.com/@interface_NULL')
        if dm == 'нет':
            await ctx.send(embed=embed)
        else:
            await ctx.send('Отправил тебе в личку)', ephemeral=True)
            await ctx.author.send(embed=embed)
        # TODO: Create a commands list


def setup(bot):
    bot.add_cog(Information(bot))
