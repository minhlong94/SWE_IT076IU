import sqlite3


def insert(connection, import_id, import_date, buyer_id, shop_id):
    """Add a new import to the database.

    Args:
        connection (sqlite3.Connection)
        import_id (str)
        import_date (datetime)
        buyer_id (str)
        shop_id (str)
    """

    if not import_id:
        raise TypeError("Argument 'import_id' is required!")
    if not import_date:
        raise TypeError("Argument 'import_date' is required!")
    if not buyer_id:
        raise TypeError("Argument 'buyer_id' is required!")
    if not shop_id:
        raise TypeError("Argument 'shop_id' is required!")

    cur = connection.cursor()
    cur.execute('''INSERT INTO Imports (importID, importDate, buyerID, shopID) VALUES (?,?,?,?)''',
                (import_id, import_date, buyer_id, shop_id))
    connection.commit()


def delete_by_id(connection, import_id):
    if not import_id:
        raise TypeError("Argument 'import_id' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Imports WHERE importID = ?''', (import_id,))
    connection.commit()


def search_by_id(connection, import_id):
    if not import_id:
        raise TypeError("Argument 'import_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Imports WHERE importID LIKE ?''', ('%' + import_id + '%',))


def search_by_date(connection, import_date):
    if not import_date:
        raise TypeError("Argument 'import_date' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Imports WHERE importDate LIKE ?''', ('%' + import_date + '%',))


def search_by_buyer_id(connection, buyer_id):
    if not buyer_id:
        raise TypeError("Argument 'buyer_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Imports WHERE buyerID LIKE ?''', ('%' + buyer_id + '%',))


def search_by_shop_id(connection, shop_id):
    if not shop_id:
        raise TypeError("Argument 'shop_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Imports WHERE shopID LIKE ?''', ('%' + shop_id + '%',))


def get_all(connection):
    return connection.cursor().execute('''SELECT * FROM Imports''')
