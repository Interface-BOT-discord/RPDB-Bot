import pkgutil

import disnake
from disnake.ext import commands


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
        owner = guild.owner
        emb = disnake.Embed(
            title=f'{guild.name} + RPDB = Автоматизированный проект',
            description=f'Привет, {owner.mention}! Вы пригласили меня, и это значит, что вы теперь '
                        f'Твоя задача - подать заявку на вступление в проект AHS. Напиши нам!',
            color=0x47eabc
        )
        emb.add_field(name='Discord: ', value='discord.com/invite/32p2BWqgJn', inline=True)

    def load_cog(self, path: str):
        for file in pkgutil.iter_modules([path]):
            try:
                self.load_extension(f'cogs.{file.name}')
                print(f'Loaded {file.name}')
            except Exception as e:
                print(f'Failed to load {file.name} ({type(e).__name__})')