"""All Item category API methods."""
import sqlite3


def insert(connection, category_id, category_name):
    """Add a new Category to the database.

    Args:
        connection (sqlite3.Connection)
        category_id (str)
        category_name (str)
    """

    cur = connection.cursor()
    cur.execute('''INSERT INTO ItemCategory (categoryID, categoryName) VALUES (?,?)''', (category_id, category_name))
    connection.commit()
    return cur.lastrowid


def delete_by_id(connection, category_id):
    cur = connection.cursor()
    removed = cur.execute('''SELECT * FROM ItemCategory WHERE categoryID = ?''', (category_id,))
    cur.execute('''DELETE FROM ItemCategory WHERE categoryID = ?''', (category_id,))
    connection.commit()
    return removed.fetchall()


def search_by_id(connection, category_id=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if category_id is None:
        return _get_none(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM ItemCategory WHERE categoryID = ?''', (category_id,)).fetchall()


def search_by_name(connection, category_name="", show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if category_name == "":
        return _get_none(connection, columns)
    if category_name == "*":
        return _get_all(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM ItemCategory WHERE categoryName LIKE ?''',
                       ('%' + category_name + '%',)).fetchall()


def max_id(connection):
    cur = connection.cursor()
    cur.execute('''SELECT MAX (categoryID) FROM ItemCategory''')
    _id = None
    try:
        _id = cur.fetchone()[0]
    except TypeError:
        pass
    return _id


def columns_names(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM ItemCategory LIMIT 0''')
    columns = [i[0] for i in cur.description]
    return columns


def _get_all(connection, columns):
    cur = connection.cursor()
    cur.execute(f'''SELECT {columns} FROM ItemCategory''')
    return cur.fetchall()


def _get_none(connection, columns):
    cur = connection.cursor()
    cur.execute(f'''SELECT {columns} FROM ItemCategory LIMIT 0''')
    return cur.fetchall()
