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

    @commands.slash_command(name='echo', description='Отправляет сообщение в канал')
    async def echo(self, ctx: disnake.ApplicationCommandInteraction,
                   msg: str,
                   channel: disnake.TextChannel = None):
        if ctx.author.guild_permissions.manage_messages:
            if msg is None or msg == ' ':
                await ctx.send('Нельзя отправить пустое сообщение!', ephemeral=True)
                return
            if channel is None:
                await ctx.send('Отправляю!', ephemeral=True)
                channel = ctx.channel
                await channel.send(msg)
            else:
                await ctx.send('Отправляю!', ephemeral=True)
                await channel.send()
        else:
            await ctx.send('Недостаточно прав', ephemeral=True)


def setup(bot):
    bot.add_cog(Information(bot))
