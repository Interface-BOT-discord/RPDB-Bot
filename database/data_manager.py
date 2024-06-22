import sqlite3 as sq

from logs import info, error

PATH = 'database/data.db'
TABLE = 'servers'
MORPHS = 'morphs'

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


def add_morph(data: dict) -> bool:
    """
    Создает морф
    :param data:
    :return bool:
    """
    info('Add morph')
    try:
        with sq.connect(PATH) as conn:
            cur = conn.cursor()
            cur.execute(f"""INSERT INTO {MORPHS} VALUES ('{data['id']}', '{data['morph']}', '{data['people']}',
            '{data['inspector']}', '{data['structure']}', 'active')""")
    except Exception as e:
        error(f'{e} DATABASE')
        return False
    return True


def add_(data):
    return add_morph(data)


def del_morph(id_) -> bool:
    """
    Удаляет морф из БД
    :param id_:
    :return bool:
    """
    info('Delete morph')
    try:
        with sq.connect(PATH) as conn:
            cur = conn.cursor()
            cur.execute(f"DELETE FROM {MORPHS} WHERE id = '{id_}'")
    except Exception as e:
        error(f'{e} DATABASE')
        return False
    return True


def del_(id_):
    return del_morph(id_)


def get_morphs(id_: str) -> dict:
    """
    Get Morph
    :param id_:
    :return dict:
    """
    info('Get morphs')
    try:
        with sq.connect(PATH) as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {MORPHS} WHERE id = '{id_}'")
            morph = cur.fetchone()
    except Exception as e:
        error(f'{e} DATABASE')
        return {'error': e}
    if morph is not None:
        return {
            'error': None,
            'id': id_,
            'morph': morph[1],
            'people': morph[2],
            'inspector': morph[3],
            'structure': morph[4],
            'status': morph[5]
        }
    else:
        return {'error': 'Morph is exist'}


def get_(id_):
    return get_morphs(id_)

