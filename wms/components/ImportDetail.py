def insert(connection, import_id, item_id, import_amount):
    if not isinstance(import_amount, int) or import_amount < 0:
        raise TypeError("Argument 'import_id' must be a non-negative integer!")

    cur = connection.cursor()
    cur.execute('''INSERT INTO ImportDetail (importID, itemID, importAmount) VALUES (?,?,?)''',
                (import_id, item_id, import_amount))
    connection.commit()


def search_by_import_id(connection, import_id=None):
    cur = connection.cursor()
    if import_id is None:
        return cur.execute('''SELECT * FROM ImportDetail LIMIT 0''').fetchall()
    return cur.execute('''SELECT * FROM ImportDetail WHERE importID = ?''', (import_id,)).fetchall()


def columns_names(connection):
    cur = connection.cursor()
    cur.execute('''SELECT * FROM ImportDetail LIMIT 0''')
    columns = [i[0] for i in cur.description]
    return columns
