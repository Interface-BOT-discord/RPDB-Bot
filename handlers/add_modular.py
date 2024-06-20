from datetime import datetime

import disnake
from disnake import TextInputStyle

from requests import add


class MyModal(disnake.ui.Modal):
    """
    Создает модульное окно для занесения морфа в азу данных DBFM
    """
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="ID",
                placeholder="Enter morph ID.",
                custom_id="id",
                style=TextInputStyle.short,
                max_length=16,
            ),
            disnake.ui.TextInput(
                label="morph",
                placeholder="Enter formatted morph.",
                custom_id="morph",
                style=TextInputStyle.long,
                max_length=4000
            ),
            disnake.ui.TextInput(
                label="people",
                placeholder="Enter member ID.",
                custom_id="people",
                style=TextInputStyle.short,
                max_length=16
            ),
            disnake.ui.TextInput(
                label="structure",
                placeholder="Enter structure name.",
                custom_id="structure",
                style=TextInputStyle.short,
                max_length=16
            )
        ]
        super().__init__(
            title="Create morph",
            custom_id="add_morph",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        values = inter.text_values
        data = {
            "id": values["id"],
            "morph": values["morph"],
            "people": values["people"],
            "inspector": inter.author.id,
            "structure": values["structure"],
        }



    async def on_error(self, interaction: disnake.MessageInteraction, error):
        embed = disnake.Embed(
            title="Ошибка взаимодействия!"
        )
        embed.add_field(name='Error:', value=str(error))
        interaction.response.send_message(embed=embed)
