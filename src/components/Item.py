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


def delete_by_id(connection, item_id):
    if not item_id:
        raise TypeError("Argument 'item_id' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Item WHERE itemID = ?''', (item_id,))
    connection.commit()


def delete_by_name(connection, item_name):
    if not item_name:
        raise TypeError("Argument 'item_name' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Item WHERE itemName = ?''', (item_name,))
    connection.commit()


def search_by_id(connection, item_id):
    if not item_id:
        raise TypeError("Argument 'item_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Item WHERE itemID LIKE ?''', ('%' + item_id + '%',))


def search_by_name(connection, item_name):
    if not item_name:
        raise TypeError("Argument 'item_name' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Item WHERE itemName LIKE ?''', ('%' + item_name + '%',))


def search_by_category_id(connection, category_id):
    if not category_id:
        raise TypeError("Argument 'category_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Item WHERE categoryID LIKE ?''', ('%' + category_id + '%',))


def search_by_shop_id(connection, shop_id):
    if not shop_id:
        raise TypeError("Argument 'shop_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Item WHERE shopID LIKE ?''', ('%' + shop_id + '%',))


def get_all(connection):
    return connection.cursor().execute('''SELECT * FROM Item''')
