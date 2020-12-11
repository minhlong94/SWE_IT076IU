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
    cur.execute('''INSERT INTO ItemCategory (categoryID, categoryName) VALUES (?,?)''', (category_id, category_name))
    connection.commit()
    return cur.lastrowid


def delete_by_id(connection, category_id):
    if not category_id:
        raise TypeError("Argument 'category_id' is required!")

    cur = connection.cursor()
    removed = cur.execute('''SELECT * FROM ItemCategory WHERE categoryID = ?''', (category_id,))
    cur.execute('''DELETE FROM ItemCategory WHERE categoryID = ?''', (category_id,))
    connection.commit()
    return removed


def delete_by_name(connection, category_name):
    if not category_name:
        raise TypeError("Argument 'category_name' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM ItemCategory WHERE categoryName = ?''', (category_name,))
    connection.commit()


def search_by_id(connection, category_id=None, show_columns=None):
    cur = connection.cursor()
    if category_id is None:
        return cur.execute('''SELECT * FROM ItemCategory LIMIT 0''').fetchall()
    if not show_columns:
        return cur.execute('''SELECT * FROM ItemCategory WHERE categoryID = ?''', (category_id,)).fetchall()
    columns = ", ".join(show_columns)
    return cur.execute(f'''SELECT {columns} FROM ItemCategory WHERE categoryID = ?''', (category_id,)).fetchall()


def search_by_name(connection, category_name="", show_columns=None):
    cur = connection.cursor()
    if not show_columns:
        return cur.execute('''SELECT * FROM ItemCategory WHERE categoryName LIKE ?''',
                           ('%' + category_name + '%',)).fetchall()
    columns = ", ".join(show_columns)
    return cur.execute(f'''SELECT {columns} FROM ItemCategory WHERE categoryName LIKE ?''',
                       ('%' + category_name + '%',)).fetchall()


def get_all(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM ItemCategory''')
    return cur.fetchall()


def max_id(connection):
    cur = connection.cursor()
    cur.execute('''SELECT MAX (categoryID) FROM Category''')
    return cur.fetchone()[0]


def columns_names(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM ItemCategory LIMIT 0''')
    names = [i[0] for i in cur.description]
    return names
