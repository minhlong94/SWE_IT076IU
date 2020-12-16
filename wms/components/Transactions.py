"""All Transactions API methods."""
import sqlite3


def insert(connection, transaction_id, transaction_date, transaction_status, customer_id, shop_id):
    """Add a new transaction to the database.

    Args:
        connection (sqlite3.Connection)
        transaction_id (str)
        transaction_date (datetime)
        transaction_status (str)
        customer_id (str)
        shop_id (str)
    """

    if transaction_status != "PENDING" and transaction_status != "COMPLETED":
        raise ValueError("Argument 'transaction_status' must be either 'PENDING' or 'COMPLETED'!")

    cur = connection.cursor()
    cur.execute(
        '''INSERT INTO Transactions (transactionID, transactionDate, transactionStatus, customerID, shopID) 
        VALUES (?,?,?,?,?)''',
        (transaction_id, transaction_date, transaction_status, customer_id, shop_id))
    connection.commit()
    return cur.lastrowid


def delete_by_id(connection, transaction_id):
    cur = connection.cursor()
    removed = cur.execute('''SELECT * FROM Transactions WHERE transactionID = ?''', (transaction_id,))
    cur.execute('''DELETE FROM Transactions WHERE transactionID = ?''', (transaction_id,))
    connection.commit()
    return removed.fetchall()


def search_by_id(connection, transaction_id=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if transaction_id is None:
        return _get_none(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Transactions WHERE transactionID = ?''', (transaction_id,)).fetchall()


def search_by_date(connection, transaction_date=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if transaction_date is None:
        return _get_none(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Transactions WHERE transactionDate = ?''',
                       (transaction_date,)).fetchall()


def search_by_status(connection, transaction_status=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if transaction_status is None:
        return _get_none(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Transactions WHERE transactionStatus LIKE ?''',
                       ('%' + transaction_status + '%',)).fetchall()


def search_by_customer_id(connection, customer_id=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if customer_id is None:
        return _get_none(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Transactions WHERE customerID = ?''', (customer_id,)).fetchall()


def search_by_shop_id(connection, shop_id=None, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    if shop_id is None:
        return _get_none(connection, columns)
    return cur.execute(f'''SELECT {columns} FROM Transactions WHERE shopID = ?''', (shop_id,)).fetchall()


def search_all(connection, show_columns=None):
    cur = connection.cursor()
    columns = ", ".join(show_columns) if show_columns else "*"
    cur.execute(f'''SELECT {columns} FROM Transactions''')
    return cur.fetchall()


def get_min_max_date(connection):
    cur = connection.cursor()
    cur.execute('''SELECT MIN (transactionDate), MAX (transactionDate) FROM Transactions''')
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
    cur.execute('''SELECT MAX (transactionID) FROM Transactions''')
    _id = None
    try:
        _id = cur.fetchone()[0]
    except TypeError:
        pass
    return _id


def columns_names(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Transactions LIMIT 0''')
    columns = [i[0] for i in cur.description]
    return columns


def _get_none(connection, columns):
    cur = connection.cursor()
    cur.execute(f'''SELECT {columns} FROM Transactions LIMIT 0''')
    return cur.fetchall()
