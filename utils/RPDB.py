import pkgutil

import disnake
from disnake.ext import commands

dev_guild = [1247566813500543099, 1227280685526552656]


class Interface_Bot(commands.InteractionBot):
    def __init__(self):
        super().__init__(
            intents=disnake.Intents.all(),
            test_guilds=dev_guild
        )

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    def load_cog(self, path: str):
        for file in pkgutil.iter_modules([path]):
            try:
                self.load_extension(f'cogs.{file.name}')
                print(f'Loaded {file.name}')
            except Exception as e:
                print(f'Failed to load {file.name} ({type(e).__name__})')