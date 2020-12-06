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
    cur.execute('''DELETE FROM Customer WHERE customerID = ?''', (customer_id,))
    connection.commit()


def delete_by_name(connection, customer_name):
    if not customer_name:
        raise TypeError("Argument 'customer_name' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Customer WHERE customerName = ?''', (customer_name,))
    connection.commit()


def search_by_id(connection, customer_id):
    if not customer_id:
        raise TypeError("Argument 'customer_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Customer WHERE customerID LIKE ?''', ('%' + customer_id + '%',))


def search_by_name(connection, customer_name):
    if not customer_name:
        raise TypeError("Argument 'customer_name' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Customer WHERE customerName LIKE ?''', ('%' + customer_name + '%',))
