import disnake
from disnake.ext import commands
from datetime import datetime

from handlers import add_modular as mod
from config import lists as devs

helper = disnake.ApplicationCommandInteraction


class Morphs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='add', description='Добавляет морф в базу данных')
    async def add_morph(self, interaction: disnake.AppCmdInter):
        if interaction.author.has_permissions(manage_server=True) or interaction.author.id in devs.devs:
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
                     id_: int = commands.Param(description='morph id')):
        # Тут кароче надо сделать удаление морфа
        pass

    @commands.slash_command(name='get', description='Получить морф из базы данных')
    async def get_morph(self, interaction: disnake.AppCmdInter,
                  id_: int = commands.Param(description='morph id')):
        # Тут вы знаете
        pass


def setup(bot):
    bot.add_cog(Morphs(bot))
