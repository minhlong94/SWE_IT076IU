"""All Imports API methods."""
import sqlite3


def insert(connection, import_id, import_date, shop_id):
    """Add a new import to the database.

    Args:
        connection (sqlite3.Connection)
        import_id (str)
        import_date (datetime)
        shop_id (str)
    """

    cur = connection.cursor()
    cur.execute('''INSERT INTO Imports (importID, importDate, shopID) VALUES (?,?,?)''',
                (import_id, import_date, shop_id))
    connection.commit()
    return cur.lastrowid


def delete_by_id(connection, import_id):
    cur = connection.cursor()
    removed = cur.execute('''SELECT * FROM Imports WHERE importID = ?''', (import_id,))
    cur.execute('''DELETE FROM Imports WHERE importID = ?''', (import_id,))
    connection.commit()
    return removed.fetchall()


def search_by_id(connection, import_id=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if import_id is None:
        return _get_all(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Imports WHERE importID = ?''', (import_id,)).fetchall()


def search_by_date(connection, import_date=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if import_date is None:
        return _get_none(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Imports WHERE importDate = ?''', (import_date,)).fetchall()


def search_by_shop_id(connection, shop_id=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if shop_id is None:
        return _get_none(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Imports WHERE shopID = ?''', (shop_id,)).fetchall()


def search_all(connection, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    cur.execute(f'''SELECT {columns} FROM Imports''')
    return cur.fetchall()


def get_min_max_date(connection):
    cur = connection.cursor()
    cur.execute('''SELECT MIN (importDate), MAX (importDate) FROM Imports''')
    min_date = max_date = None
    try:
        from datetime import datetime

        dates = cur.fetchone()
        min_date = datetime.strptime(dates[0], '%Y-%m-%d')
        max_date = datetime.strptime(dates[1], '%Y-%m-%d')
    except TypeError:
        pass
    return min_date, max_date


def max_id(connection):
    cur = connection.cursor()
    cur.execute('''SELECT MAX (importID) FROM Imports''')
    _id = None
    try:
        _id = cur.fetchone()[0]
    except TypeError:
        pass
    return _id


def columns_names(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Imports LIMIT 0''')
    columns = [i[0] for i in cur.description]
    return columns


def _get_none(connection, columns):
    cur = connection.cursor()
    cur.execute(f'''SELECT {columns} FROM Imports LIMIT 0''')
    return cur.fetchall()
