import sqlite3


def insert(connection, shop_id, shop_name):
    """Add a new shop to the database.

    Args:
        connection (sqlite3.Connection)
        shop_id (str)
        shop_name (str)
    """

    if not shop_id:
        raise TypeError("Argument 'shop_id' is required!")
    if not shop_name:
        raise TypeError("Argument 'shop_name' is required!")

    cur = connection.cursor()
    cur.execute('''INSERT INTO Shop (shopID, shopName) VALUES (?,?)''', (shop_id, shop_name))
    connection.commit()


def delete_by_id(connection, shop_id):
    if not shop_id:
        raise TypeError("Argument 'shop_id' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Shop WHERE shopID = ?''', (shop_id,))
    connection.commit()


def delete_by_name(connection, shop_name):
    if not shop_name:
        raise TypeError("Argument 'shop_name' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Shop WHERE shopName = ?''', (shop_name,))
    connection.commit()


def search_by_id(connection, shop_id):
    if not shop_id:
        raise TypeError("Argument 'shop_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Shop WHERE shopID LIKE ?''', ('%' + shop_id + '%',))


def search_by_name(connection, shop_name):
    if not shop_name:
        raise TypeError("Argument 'shop_name' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Shop WHERE shopName LIKE ?''', ('%' + shop_name + '%',))


def get_all(connection):
    return connection.cursor().execute('''SELECT * FROM Shop''')
