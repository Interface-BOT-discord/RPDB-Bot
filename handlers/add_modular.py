from datetime import datetime

import disnake
from disnake import TextInputStyle

from database.data_manager import add_
from logs import info, error


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
                max_length=32
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
            "id": values["id"].lower(),
            "morph": values["morph"],
            "people": values["people"],
            "inspector": inter.author.id,
            "structure": values["structure"],
        }

        if add_(data):
            info(f'Morph {data["id"]} has been added')
            await inter.response.send_message(embed=disnake.Embed(
                title='Морф создан!',
                description=f'Ваш морф с ID {data["id"]} был создан!',
                color=disnake.Color.green(),
                timestamp=datetime.now()
            ))
        else:
            info(f'Morph {data["data"]} not added')
            await inter.response.send_message(embed=disnake.Embed(
                title='Морф не создан!',
                description=f'Ваш морф с ID {data["id"]} не был создан! Из за сбоя в базе данных',
                color=disnake.Color.green(),
                timestamp=datetime.now()
            ))
