import disnake
from disnake.ext import commands
import aiohttp

helper = disnake.ApplicationCommandInteraction


class Morphs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='add', description='Добавляет морф в базу данных')
    def add_morph(self):
        # Тут кароче надо сделать добавление морфа через диалоговое окошко
        pass

    @commands.slash_command(name='remove', description='Удаляет морф из базы данных')
    def remove_morph(self,
                     id_: int = commands.Param(description='morph id')):
        # Тут кароче надо сделать удаление морфа
        pass

    @commands.slash_command(name='get', description='Получить морф из базы данных')
    def get_morph(self,
                  id_: int = commands.Param(description='morph id')):
        # Тут вы знаете
        pass


def setup(bot):
    bot.add_cog(Morphs(bot))
