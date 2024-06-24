import disnake
from disnake.ext import commands
import aiohttp

from database import get_


class HostSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='out', description='Получить морф на хосте')
    async def out(self, ctx: disnake.AppCmdInter,
                  id_: str):
        data = get_(id_)
        if data['error'] == 'morph is not exist':

            await ctx.send(embed=disnake.Embed(
                title='Ой',
                description='Такого морфа не существует!',
                colour=disnake.Color.red()
            ))

        elif data['error'] is not None:

            await ctx.send(embed=disnake.Embed(
                title='Ой',
                description=f'Произошла ошибка! [{data["error"]}]',
                colour=disnake.Color.red()
            ))

        else:
            if str(data['people']) == str(ctx.author.id):
                try:
                    session = aiohttp.ClientSession()
                    async with session.post('http://127.0.0.1:1314/morph/get',
                                            json = {'morph': data['morph']}) as resp:
                        response = resp
                    await session.close()

                    if response.status == 200:
                        await ctx.send(embed=disnake.Embed(
                            title='Ура!',
                            description='Ждите ваш морф на хосте!',
                            colour=disnake.Color.green()
                        ))
                    else:
                        await ctx.send(embed=disnake.Embed(
                            title='Ой',
                            description=f'Ошибка на стороне API! Код ошибки: {response.status}',
                            colour=disnake.Color.red()
                        ))

                except Exception as e:

                    await ctx.send(embed=disnake.Embed(
                        title='Ой',
                        description=f'Мы не смогли отправить запрос на сервер! [{e.__class__.__name__}]',
                        colour=disnake.Color.red()
                    ))

            else:

                await ctx.send(embed=disnake.Embed(
                    title='Ой',
                    description='Этот морф вам не принадлежит!',
                    colour=disnake.Color.red()
                ))


def setup(bot):
    bot.add_cog(HostSystem(bot))