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

    if not item_id:
        raise TypeError("Argument 'item_id' is required!")
    if not item_name:
        raise TypeError("Argument 'item_name' is required!")

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


def search_by_id(connection, item_id):
    if not item_id:
        raise TypeError("Argument 'item_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Item WHERE itemID LIKE ?''', ('%' + item_id + '%',)).fetchall()


def search_by_name(connection, item_name="", show_columns=None):
    cur = connection.cursor()
    if not show_columns:
        return cur.execute('''SELECT * FROM Item WHERE itemName LIKE ?''', ('%' + item_name + '%',)).fetchall()
    columns = ", ".join(show_columns)
    return cur.execute(f'''SELECT {columns} FROM Item WHERE itemName LIKE ?''', ('%' + item_name + '%',)).fetchall()


def search_by_category_name(connection, category_name="", show_columns=None):
    cur = connection.cursor()
    category_ids = [ids for ids in cur.execute('''SELECT categoryID FROM ItemCategory WHERE categoryName LIKE ?''',
                                               ('%' + category_name + '%',)).fetchall()]
    items = []
    if not show_columns:
        for category_id in category_ids:
            cur.execute('''SELECT * FROM Item WHERE categoryID = ?''', category_id)
            items.extend(cur.fetchall())
    else:
        columns = ", ".join(show_columns)
        for category_id in category_ids:
            cur.execute(f'''SELECT {columns} FROM Item WHERE categoryID = ?''', category_id)
            items.extend(cur.fetchall())
    return items


def search_by_shop_name(connection, shop_name="", show_columns=None):
    cur = connection.cursor()
    shop_ids = [Sid for Sid in
                cur.execute('''SELECT shopID FROM Shop WHERE shopName LIKE ?''', ('%' + shop_name + '%',)).fetchall()]
    items = []
    if not show_columns:
        for shop_id in shop_ids:
            cur.execute('''SELECT * FROM Item WHERE shopID = ?''', shop_id)
            items.extend(cur.fetchall())
    else:
        columns = ", ".join(show_columns)
        for shop_id in shop_ids:
            cur.execute(f'''SELECT {columns} FROM Item WHERE shopID = ?''', shop_id)
            items.extend(cur.fetchall())
    return items


def get_all(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Item''')
    return cur.fetchall()


def max_id(connection):
    cur = connection.cursor()
    cur.execute('''SELECT MAX (itemID) FROM Item''')
    return cur.fetchone()[0]


def columns_names(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Item LIMIT 0''')
    names = [i[0] for i in cur.description]
    return names
