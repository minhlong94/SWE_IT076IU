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

    if not transaction_id:
        raise TypeError("Argument 'transaction_id' is required!")
    if not transaction_date:
        raise TypeError("Argument 'transaction_date' is required!")
    if transaction_status != "PENDING" and transaction_status != "COMPLETED":
        raise ValueError("Argument 'transaction_status' must be either 'PENDING' or 'COMPLETED'!")
    if not customer_id:
        raise TypeError("Argument 'customer_id' is required!")
    if not shop_id:
        raise TypeError("Argument 'shop_id' is required!")

    cur = connection.cursor()
    cur.execute(
        '''INSERT INTO "Transaction" (transactionID, transactionDate, transactionStatus, customerID, shopID) 
        VALUES (?,?,?,?,?)''',
        (transaction_id, transaction_date, transaction_status, customer_id, shop_id))
    connection.commit()


def delete_by_id(connection, transaction_id):
    if not transaction_id:
        raise TypeError("Argument 'transaction_id' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM "Transaction" WHERE transactionID = ?''', (transaction_id,))
    connection.commit()


def search_by_id(connection, transaction_id):
    if not transaction_id:
        raise TypeError("Argument 'transaction_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM "Transaction" WHERE transactionID LIKE ?''', ('%' + transaction_id + '%',))


def search_by_date(connection, transaction_date):
    if not transaction_date:
        raise TypeError("Argument 'transaction_date' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM "Transaction" WHERE transactionDate LIKE ?''', ('%' + transaction_date + '%',))


def search_by_status(connection, transaction_status):
    if not transaction_status:
        raise TypeError("Argument 'transaction_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM "Transaction" WHERE transactionStatus LIKE ?''', ('%' + transaction_status + '%',))


def search_by_customer_id(connection, customer_id):
    if not customer_id:
        raise TypeError("Argument 'customer_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM "Transaction" WHERE customerID LIKE ?''', ('%' + customer_id + '%',))


def search_by_shop_id(connection, shop_id):
    if not shop_id:
        raise TypeError("Argument 'shop_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM "Transaction" WHERE shopID LIKE ?''', ('%' + shop_id + '%',))


def get_all(connection):
    return connection.cursor().execute('''SELECT * FROM "Transaction"''')
