def insert(connection, transaction_id, item_id, transaction_amount):
    if not transaction_id:
        raise TypeError("Argument 'transaction_id' is required!")
    if not item_id:
        raise TypeError("Argument 'item_id' is required!")
    if not isinstance(transaction_amount, int) or transaction_amount < 0:
        raise TypeError("Argument 'transaction_id' must be a non-negative integer!")

    cur = connection.cursor()
    cur.execute('''INSERT INTO TransactionsDetail (transactionID, itemID, transactionAmount) VALUES (?,?,?)''',
                (transaction_id, item_id, transaction_amount))
    connection.commit()


def search_by_transaction_id(connection, transaction_id):
    if not transaction_id:
        raise TypeError("Argument 'transaction_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM TransactionsDetail WHERE transactionID LIKE ?''', ('%' + transaction_id + '%',))


def get_all(connection):
    return connection.cursor().execute('''SELECT * FROM TransactionsDetail''')
