import sqlite3 as sq

from logs import info

PATH = './data.db'
TABLE = 'servers'

# Create DB
#
# conn = sq.connect(PATH)
# conn.close()

# Create Table
#
# conn = sq.connect(PATH)
# cur = conn.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS servers (id INTEGER NOT NULL , level TEXT NOT NULL )')
# conn.close()


def init_server(id_: int,
                level: str = 'guest'):
    """
    Добавляет сервер в базу данных
    :param id_:
    :param level:
    :return: None
    """

    level = level.lower()
    with sq.connect(PATH) as conn:
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {TABLE} (id, level) VALUES ({id_}, '{level}')")


def get_servers() -> dict:
    """
    Получаем все сервера базы данных, где возвращается словарь {id: тариф}
    :return: dict
    """
    info('Get all servers')
    with sq.connect(PATH) as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {TABLE}")
        servers = cur.fetchall()

    servers_ = {}
    for server in servers:
        servers_[server[0]] = server[1]
    return servers_


def update_level(id_: int, new_level: str):
    """
    Обновляет план
    :param id_:
    :param new_level:
    :return: None
    """
    info('Update server level')
    with sq.connect(PATH) as conn:
        cur = conn.cursor()
        cur.execute(f"UPDATE {TABLE} SET level = '{new_level}' WHERE id = {id_}")


def delete_server(id_: int):
    """
    Удаляет сервер из базы данных
    :param id_:
    :return: None
    """
    info('Delete server')
    with sq.connect(PATH) as conn:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {TABLE} WHERE id = {id_}")
