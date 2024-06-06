import disnake
from disnake.ext import commands

helper = disnake.ApplicationCommandInteraction


class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='help', description='Получить информацию о боте')
    async def help(self, ctx: helper):
        embed = disnake.Embed(title='Сводка о боте',
                              description='Interface & EraserColor : RPDB \n'
                                          'Бот, который помогает в организации проектов по SCP: RP.')
        # TODO: Сделать список команд и их описания
        await ctx.send('Отправил инфу тебе в личные сообщения!)')
        await ctx.author.send(embed=embed)


def setup(bot):
    bot.add_cog(Entertainment(bot))
