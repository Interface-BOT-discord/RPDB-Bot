from os import getenv
import dotenv

from utils import RPDBBot
from logs import debug, info


if __name__ == '__main__':
    debug('Load .env')
    dotenv.load_dotenv()

    bot = RPDBBot()
    bot.load_cog('cogs')
    bot.prefix = getenv('PREFIX')
    info('Bot run')
    bot.run(getenv('TOKEN'))
