import sqlite3


def insert(connection, inventory_id, inventory_name):
    """Add a new inventory to the database.

    Args:
        connection (sqlite3.Connection)
        inventory_id (str)
        inventory_name (str)
    """

    if not inventory_id:
        raise TypeError("Argument 'inventory_id' is required!")
    if not inventory_name:
        raise TypeError("Argument 'inventory_name' is required!")

    cur = connection.cursor()
    cur.execute('''INSERT INTO Inventory (inventoryID, inventoryName) VALUES (?,?)''', (inventory_id, inventory_name))
    connection.commit()


def delete_by_id(connection, inventory_id):
    if not inventory_id:
        raise TypeError("Argument 'inventory_id' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Inventory WHERE inventoryID = ?''', (inventory_id,))
    connection.commit()


def delete_by_name(connection, inventory_name):
    if not inventory_name:
        raise TypeError("Argument 'inventory_name' is required!")

    cur = connection.cursor()
    cur.execute('''DELETE FROM Inventory WHERE inventoryName = ?''', (inventory_name,))
    connection.commit()


def search_by_id(connection, inventory_id):
    if not inventory_id:
        raise TypeError("Argument 'inventory_id' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Inventory WHERE inventoryID LIKE ?''', ('%' + inventory_id + '%',))


def search_by_name(connection, inventory_name):
    if not inventory_name:
        raise TypeError("Argument 'inventory_name' is required!")

    cur = connection.cursor()
    return cur.execute('''SELECT * FROM Inventory WHERE inventoryName LIKE ?''', ('%' + inventory_name + '%',))
