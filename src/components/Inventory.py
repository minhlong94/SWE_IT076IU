class Inventory:
    """
    Inventory is where we store and manage every product we have imported, and supply items for the transactions

    Args:
        inventory_id (str): is used for identifying the inventory

    Attributes:
        _inventory_id: where we store inventory_id
    """

    def __init__(self, inventory_id):
        self._inventory_id = inventory_id
