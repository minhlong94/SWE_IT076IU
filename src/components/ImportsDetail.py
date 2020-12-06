def insert(connection, import_id, item_id, import_amount):
    if not import_id:
        raise TypeError("Argument 'import_id' is required!")
    if not item_id:
        raise TypeError("Argument 'item_id' is required!")
    if not isinstance(import_amount, int) or import_amount < 0:
        raise TypeError("Argument 'import_id' must be a non-negative integer!")

    cur = connection.cursor()
    cur.execute('''INSERT INTO ImportsDetail (importID, itemID, importAmount) VALUES (?,?,?)''',
                (import_id, item_id, import_amount))
    connection.commit()


def search_by_import_id(connection, import_id):
    if not import_id:
        raise TypeError("Argument 'import_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM ImportsDetail WHERE importID LIKE ?''', ('%' + import_id + '%',))
