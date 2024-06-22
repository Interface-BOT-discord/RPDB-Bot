import disnake
from disnake.ext import commands
from datetime import datetime

from handlers import add_modular as mod
from config import lists as devs
from database import del_, get_

helper = disnake.ApplicationCommandInteraction


class Morphs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='add', description='Добавляет морф в базу данных')
    async def add_morph(self, interaction: disnake.AppCmdInter):
        if interaction.author.guild_permissions == disnake.Permissions.manage_guild or interaction.author.id in devs.devs:
            await interaction.response.send_modal(modal=mod.MyModal())
        else:
            await interaction.send(embed=disnake.Embed(
                title='Ой',
                description='Я не нашел у вас необходимых прав :(',
                timestamp=datetime.now(),
                color=disnake.Color.red()
            ))

    @commands.slash_command(name='remove', description='Удаляет морф из базы данных')
    async def remove_morph(self, interaction: disnake.AppCmdInter,
                     id_: str = commands.Param(description='morph id')):
        if interaction.author.guild_permissions == disnake.Permissions.manage_guild or interaction.author.id in devs.devs:
            if del_(id_):
                await interaction.send(embed=disnake.Embed(
                    title='Ваш морф был удален!',
                    description=f'Морфа с ID {id_} больше не существует!',
                    color=0xff0000,
                    timestamp=datetime.now()
                ))
            else:
                await interaction.send(embed=disnake.Embed(
                    title='Ой',
                    description='Произошла ошибка на стороне базы данных!',
                    color=disnake.Color.dark_red()
                ))
            return
        else:
            await interaction.send(embed=disnake.Embed(
                title='Ой',
                description='У вас нет прав, чтобы сделать это!',
                color=0x580000
            ))
            return

    @commands.slash_command(name='get', description='Получить морф из базы данных')
    async def get_morph(self, interaction: disnake.AppCmdInter,
                  id_: str = commands.Param(description='morph id')):
        # Тут вы знаете
        data = get_(id_)
        if data['error'] is not None:
            await interaction.send(embed=disnake.Embed(
                title='Ошибка!',
                description='Морфа либо нет, либо ошибка на стороне базы данных!',
                color=disnake.Color.red()
            ))
            return

        embed = disnake.Embed(
            title=f'Морф с ID {id_}',
            color=disnake.Color.green()
        )
        embed.add_field(name='Морф', value=data['morph'], inline=False)
        embed.add_field(name='Чей?', value=f'<@{data['people']}>', inline=False)
        embed.add_field(name='Создан', value=f'<@{data['inspector']}>', inline=False)
        embed.add_field(name='Структура', value=data['structure'], inline=False)
        embed.add_field(name='Статус морфа', value=data['status'], inline=False)

        await interaction.send(embed=embed)
        return


def setup(bot):
    bot.add_cog(Morphs(bot))
