import pkgutil

import disnake
from disnake.ext import commands

from database import init_server

from logs import info

guilds = [1247566813500543099, 1227280685526552656]


class Interface_Bot(commands.InteractionBot):
    def __init__(self):
        super().__init__(
            intents=disnake.Intents.all(),
            test_guilds=guilds
        )

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        print(disnake.__version__)

    async def on_guild_join(self, guild: disnake.Guild):
        info(f'Join guild {guild.name}({guild.id})')
        owner = guild.owner
        emb = disnake.Embed(
            title=f'{guild.name} + RPDB = Автоматизированный проект',
            description=f'Привет, {owner.mention}! Вы пригласили меня, и это значит, что вы теперь '
                        f'Твоя задача - подать заявку на вступление в проект AHS. Напиши нам!',
            color=0x47eabc
        )
        emb.add_field(name='Discord: ', value='discord.com/invite/32p2BWqgJn', inline=True)
        await owner.send(embed=emb)

        await owner.send('Initialization to the database is underway')
        init_server(guild.id)
        await owner.send('Initialization complete')

    async def on_guild_remove(self, guild: disnake.Guild):
        info(f'Remove guild {guild.name}({guild.id})')
        owner = guild.owner
        emb = disnake.Embed(
            title='Пока!',
            description='К сожалению, кто то или вы кикнули меня с вашего сервера, если вы отказались от нас, '
                        'напишите нам в нашем дискорд сервере! Очень жаль(',
            color=0xff0000,
        )
        emb.add_field(name='Discord: ', value='discord.com/invite/32p2BWqgJn', inline=True)
        await owner.send(embed=emb)

    def load_cog(self, path: str):
        info('Cog loading started')
        for file in pkgutil.iter_modules([path]):
            try:
                self.load_extension(f'cogs.{file.name}')
                print(f'Loaded {file.name}')
            except Exception as e:
                with open('log.txt', 'w') as f:
                    f.write(f'{str(e)}\n')
                print(f'Failed to load {file.name} ({type(e).__name__} (FULL IN log.txt))')

