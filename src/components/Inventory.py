from src.components.Item import Item


class Inventory:
    """Inventory is where we store and manage every product we have imported, and supply items for the transactions.

    Args:
        inventory_id (str): is used for identifying the inventory.

    Raises:
        TypeError: an error occurred when inventory_id is empty or None.

    Attributes:
        inventory_id: where we store inventory id.
        items: a dictionary mapping pairs of item id (key) and quantity (value).
    """

    def __init__(self, inventory_id):
        if not inventory_id:
            raise TypeError("Argument 'inventory_id' is required!")

        self.inventory_id = inventory_id
        self.items = dict()

    def add_item_to_inventory(self, item, quantity):
        """Adds an item to the inventory.

        Args:
            item (Item)
            quantity (int)
        """

        self.items.update({item.item_id: quantity})

    def remove_item_from_inventory(self, item):
        """Removes an item from the inventory.

        Args:
            item (Item)
        """

        self.items.pop(item.item_id, None)

    def add_quantity(self, item, quantity):
        pass

    def remove_quantity(self, item, quantity):
        pass
