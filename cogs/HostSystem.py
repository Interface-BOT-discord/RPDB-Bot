import disnake
from disnake.ext import commands
import aiohttp

from database import get_
from logs import info


class HostSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='out', description='Получить морф на хосте по ID')
    async def out(self, inter: disnake.AppCmdInter, id_: str):
        data = get_(id_)
        morph = {'morph': data['morph']}
        people = data['people']
        if people == inter.author.id:
            session = aiohttp.ClientSession()
            async with session.post(f'http://127.0.0.1:1314/morph/get', json=morph) as resp:
                info('Response to server.')

            if resp.status == 200:
                await session.close()
                await inter.send(embed=disnake.Embed(
                    title='Выдача!',
                    description='В скором времени, вы получите свой морф на хосте!',
                    color=disnake.Color.green()
                ))
            else:
                await inter.send(embed=disnake.Embed(
                    title='Ой',
                    description='В данный момент хост не запущен, или бот не находится на сервере',
                    color=disnake.Color.red()
                ))
        else:
            await inter.send(embed=disnake.Embed(
                title='Ой',
                description='Это не ваш морф',
                color=disnake.Color.red()
            ))


def setup(bot):
    bot.add_cog(HostSystem(bot))