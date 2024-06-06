import sqlite3
from dotenv import load_dotenv
from os import getenv

load_dotenv()
DATA = {
    'PATH': getenv('PATH'),
    'TABLE': getenv('TABLE_SERVERS')
}

