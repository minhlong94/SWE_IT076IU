def insert(connection, transaction_id, item_id, item_price, transaction_amount):
    if not isinstance(item_price, float) or item_price < 0:
        raise TypeError("Argument 'transaction_id' must be a non-negative integer!")
    if not isinstance(transaction_amount, int) or transaction_amount < 0:
        raise TypeError("Argument 'transaction_id' must be a non-negative integer!")

    cur = connection.cursor()
    cur.execute(
        '''INSERT INTO TransactionDetail (transactionID, itemID, itemPrice, transactionAmount) VALUES (?,?,?,?)''',
        (transaction_id, item_id, item_price, transaction_amount))
    connection.commit()


def search_by_transaction_id(connection, transaction_id=None):
    cur = connection.cursor()
    if transaction_id is None:
        return cur.execute('''SELECT * FROM TransactionDetail LIMIT 0''').fetchall()
    return cur.execute('''SELECT * FROM TransactionDetail WHERE transactionID = ?''', (transaction_id,)).fetchall()


def columns_names(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM TransactionDetail LIMIT 0''')
    columns = [i[0] for i in cur.description]
    return columns
