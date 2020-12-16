"""All Item API methods."""
import sqlite3


def insert(connection, item_id, item_name, quantity, category_id, shop_id):
    """Add a new item to the database.

    Args:
        connection (sqlite3.Connection)
        item_id (str)
        item_name (str)
        quantity (int)
        category_id (str)
        shop_id (str)
    """

    cur = connection.cursor()
    cur.execute('''INSERT INTO Item (itemID, itemName, quantity, categoryID, shopID) VALUES (?,?,?,?,?)''',
                (item_id, item_name, quantity, category_id, shop_id))
    connection.commit()
    return cur.lastrowid


def delete_by_id(connection, item_id):
    cur = connection.cursor()
    removed = cur.execute('''SELECT * FROM Item WHERE itemID = ?''', (item_id,))
    cur.execute('''DELETE FROM Item WHERE itemID = ?''', (item_id,))
    connection.commit()
    return removed.fetchall()


def search_by_id(connection, item_id=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if item_id is None:
        return _get_none(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Item WHERE itemID = ?''', (item_id,)).fetchall()


def search_by_name(connection, item_name="", show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if item_name == "":
        return _get_none(connection, columns)
    if item_name == "*":
        return _get_all(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Item WHERE itemName LIKE ?''', ('%' + item_name + '%',)).fetchall()


def search_by_category_id(connection, category_id=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if category_id is None:
        return _get_none(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Item WHERE categoryID = ?''', (category_id,)).fetchall()


def search_by_shop_id(connection, shop_id=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if shop_id is None:
        return _get_all(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Item WHERE shopID = ?''', (shop_id,)).fetchall()


def max_id(connection):
    cur = connection.cursor()
    cur.execute('''SELECT MAX (itemID) FROM Item''')
    _id = None
    try:
        _id = cur.fetchone()[0]
    except TypeError:
        pass
    return _id


def columns_names(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Item LIMIT 0''')
    columns = [i[0] for i in cur.description]
    return columns


def _get_all(connection, columns):
    cur = connection.cursor()
    cur.execute(f'''SELECT {columns} FROM Item''')
    return cur.fetchall()


def _get_none(connection, columns):
    cur = connection.cursor()
    cur.execute(f'''SELECT {columns} FROM Item LIMIT 0''')
    return cur.fetchall()
