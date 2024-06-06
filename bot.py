from os import getenv
from dotenv import load_dotenv

from utils import Interface_Bot


if __name__ == '__main__':
    load_dotenv()
    bot = Interface_Bot()
    bot.load_cog('cogs')
    bot.prefix = getenv('PREFIX')
    bot.run(getenv('TOKEN'))
