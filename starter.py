from os import getenv
import dotenv

from utils import Interface_Bot
from logs import debug, info


if __name__ == '__main__':
    debug('Load .env')
    dotenv.load_dotenv()

    bot = Interface_Bot()
    bot.load_cog('cogs')
    bot.prefix = getenv('PREFIX')
    info('Bot run')
    bot.run(getenv('TOKEN'))
