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
    if not item_id:
        raise TypeError("Argument 'item_id' is required!")

    cur = connection.cursor()
    removed = cur.execute('''SELECT * FROM Item WHERE itemID = ?''', (item_id,))
    cur.execute('''DELETE FROM Item WHERE itemID = ?''', (item_id,))
    connection.commit()
    return removed


def search_by_id(connection, item_id=None, show_columns=None):
    cur = connection.cursor()
    if item_id is None:
        return cur.execute('''SELECT * FROM Item LIMIT 0''').fetchall()
    if not show_columns:
        return cur.execute('''SELECT * FROM Item WHERE itemID = ?''', (item_id,)).fetchall()
    columns = ", ".join(show_columns)
    return cur.execute(f'''SELECT {columns} FROM Item WHERE itemID = ?''', (item_id,)).fetchall()


def search_by_name(connection, item_name="", show_columns=None):
    cur = connection.cursor()
    if not show_columns:
        return cur.execute('''SELECT * FROM Item WHERE itemName LIKE ?''', ('%' + item_name + '%',)).fetchall()
    columns = ", ".join(show_columns)
    return cur.execute(f'''SELECT {columns} FROM Item WHERE itemName LIKE ?''', ('%' + item_name + '%',)).fetchall()


def search_by_category_id(connection, category_id=None, show_columns=None):
    cur = connection.cursor()
    if category_id is None:
        return cur.execute('''SELECT * FROM Item LIMIT 0''').fetchall()
    if not show_columns:
        return cur.execute('''SELECT * FROM Item WHERE categoryID = ?''', (category_id,)).fetchall()
    columns = ", ".join(show_columns)
    return cur.execute(f'''SELECT {columns} FROM Item WHERE categoryID = ?''', (category_id,)).fetchall()


def search_by_shop_id(connection, shop_id=None, show_columns=None):
    cur = connection.cursor()
    if shop_id is None:
        return cur.execute('''SELECT * FROM Item LIMIT 0''').fetchall()
    if not show_columns:
        return cur.execute('''SELECT * FROM Item WHERE shopID = ?''', (shop_id,)).fetchall()
    columns = ", ".join(show_columns)
    return cur.execute(f'''SELECT {columns} FROM Item WHERE shopID = ?''', (shop_id,)).fetchall()


def get_all(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Item''')
    return cur.fetchall()


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
    names = [i[0] for i in cur.description]
    return names
