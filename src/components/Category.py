import sqlite3


def insert(connection, category_id, category_name):
    """Add a new Category to the database.

    Args:
        connection (sqlite3.Connection)
        category_id (str)
        category_name (str)
    """

    if not category_id:
        raise TypeError("Argument 'category_id' is required!")
    if not category_name:
        raise TypeError("Argument 'category_name' is required!")

    cur = connection.cursor()
    cur.execute('''INSERT INTO Category (categoryID, categoryName) VALUES (?,?)''', (category_id, category_name))
    connection.commit()


def delete_by_id(connection, category_id):
    if not category_id:
        raise TypeError("Argument 'category_id' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Category WHERE categoryID = ?''', (category_id,))
    connection.commit()


def delete_by_name(connection, category_name):
    if not category_name:
        raise TypeError("Argument 'category_name' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Category WHERE categoryName = ?''', (category_name,))
    connection.commit()


def search_by_id(connection, category_id):
    if not category_id:
        raise TypeError("Argument 'category_id' is required!")

    cur = connection.cursor()
    cur.execute('''SELECT * FROM Category WHERE categoryID LIKE ?''', ('%' + category_id + '%',))


def search_by_name(connection, category_name):
    if not category_name:
        raise TypeError("Argument 'category_name' is required!")

    cur = connection.cursor()
    cur.execute('''SELECT * FROM Category WHERE categoryName LIKE ?''', ('%' + category_name + '%',))
