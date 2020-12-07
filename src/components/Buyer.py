import sqlite3


def insert(connection, buyer_id, buyer_name):
    """Add a new buyer to the database.

    Args:
        connection (sqlite3.Connection)
        buyer_id (str)
        buyer_name (str)
    """

    if not buyer_id:
        raise TypeError("Argument 'buyer_id' is required!")
    if not buyer_name:
        raise TypeError("Argument 'buyer_name' is required!")

    cur = connection.cursor()
    cur.execute('''INSERT INTO Buyer (buyerID, buyerName) VALUES (?,?)''', (buyer_id, buyer_name))
    connection.commit()


def delete_by_id(connection, buyer_id):
    if not buyer_id:
        raise TypeError("Argument 'buyer_id' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Buyer WHERE buyerID = ?''', (buyer_id,))
    connection.commit()


def delete_by_name(connection, buyer_name):
    if not buyer_name:
        raise TypeError("Argument 'buyer_name' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Buyer WHERE buyerName = ?''', (buyer_name,))
    connection.commit()


def search_by_id(connection, buyer_id):
    if not buyer_id:
        raise TypeError("Argument 'buyer_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Buyer WHERE buyerID LIKE ?''', ('%' + buyer_id + '%',))


def search_by_name(connection, buyer_name):
    if not buyer_name:
        raise TypeError("Argument 'buyer_name' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Buyer WHERE buyerName LIKE ?''', ('%' + buyer_name + '%',))


def get_all(connection):
    return connection.cursor().execute('''SELECT * FROM Buyer''')
