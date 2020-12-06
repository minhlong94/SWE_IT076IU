import sqlite3


def insert(connection, transaction_id, transaction_date, transaction_status, customer_id, inventory_id):
    """Add a new transaction to the database.

    Args:
        connection (sqlite3.Connection)
        transaction_id (str)
        transaction_date (datetime)
        transaction_status (str)
        customer_id (str)
        inventory_id (str)
    """

    if not transaction_id:
        raise TypeError("Argument 'transaction_id' is required!")
    if not transaction_date:
        raise TypeError("Argument 'transaction_date' is required!")
    if transaction_status != "PENDING" and transaction_status != "COMPLETED":
        raise ValueError("Argument 'transaction_status' must be either 'PENDING' or 'COMPLETED'!")
    if not customer_id:
        raise TypeError("Argument 'customer_id' is required!")
    if not inventory_id:
        raise TypeError("Argument 'inventory_id' is required!")

    cur = connection.cursor()
    cur.execute(
        '''INSERT INTO Transactions (transactionID, transactionDate, transactionStatus, customerID, inventoryID) 
        VALUES (?,?,?,?,?)''',
        (transaction_id, transaction_date, transaction_status, customer_id, inventory_id))
    connection.commit()


def delete_by_id(connection, transaction_id):
    if not transaction_id:
        raise TypeError("Argument 'transaction_id' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Transactions WHERE transactionID = ?''', (transaction_id,))
    connection.commit()


def search_by_id(connection, transaction_id):
    if not transaction_id:
        raise TypeError("Argument 'transaction_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Transactions WHERE transactionID LIKE ?''', ('%' + transaction_id + '%',))


def search_by_date(connection, transaction_date):
    if not transaction_date:
        raise TypeError("Argument 'transaction_date' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Transactions WHERE transactionDate LIKE ?''', ('%' + transaction_date + '%',))


def search_by_status(connection, transaction_status):
    if not transaction_status:
        raise TypeError("Argument 'transaction_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Transactions WHERE transactionStatus LIKE ?''', ('%' + transaction_status + '%',))


def search_by_customer_id(connection, customer_id):
    if not customer_id:
        raise TypeError("Argument 'customer_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Transactions WHERE customerID LIKE ?''', ('%' + customer_id + '%',))


def search_by_inventory_id(connection, inventory_id):
    if not inventory_id:
        raise TypeError("Argument 'inventory_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Transactions WHERE inventoryID LIKE ?''', ('%' + inventory_id + '%',))
