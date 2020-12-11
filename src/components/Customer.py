import sqlite3


def insert(connection, customer_id, customer_name):
    """Add a new Customer to the database.

    Args:
        connection (sqlite3.Connection)
        customer_id (str)
        customer_name (str)
    """

    if not customer_id:
        raise TypeError("Argument 'customer_id' is required!")
    if not customer_name:
        raise TypeError("Argument 'customer_name' is required!")

    cur = connection.cursor()
    cur.execute('''INSERT INTO Customer (customerID, customerName) VALUES (?,?)''', (customer_id, customer_name))
    connection.commit()
    return cur.lastrowid


def delete_by_id(connection, customer_id):
    if not customer_id:
        raise TypeError("Argument 'customer_id' is required!")

    cur = connection.cursor()
    removed = cur.execute('''SELECT * FROM Customer WHERE customerID = ?''', (customer_id,))
    cur.execute('''DELETE FROM Customer WHERE customerID = ?''', (customer_id,))
    connection.commit()
    return removed


def search_by_id(connection, customer_id=0, show_columns=None):
    cur = connection.cursor()
    if not show_columns:
        return cur.execute('''SELECT * FROM Customer WHERE customerID = ?''', (customer_id,)).fetchall()
    columns = ", ".join(show_columns)
    return cur.execute(f'''SELECT {columns} FROM Customer WHERE customerID = ?''', (customer_id,)).fetchall()


def search_by_name(connection, customer_name="", show_columns=None):
    cur = connection.cursor()
    if not show_columns:
        return cur.execute('''SELECT * FROM Customer WHERE customerName LIKE ?''',
                           ('%' + customer_name + '%',)).fetchall()
    columns = ", ".join(show_columns)
    return cur.execute(f'''SELECT {columns} FROM Customer WHERE customerName LIKE ?''',
                       ('%' + customer_name + '%',)).fetchall()


def get_all(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Customer''')
    return cur.fetchall()


def max_id(connection):
    cur = connection.cursor()
    cur.execute('''SELECT MAX (customerID) FROM Customer''')
    return cur.fetchone()[0]


def columns_names(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Customer LIMIT 0''')
    names = [i[0] for i in cur.description]
    return names
