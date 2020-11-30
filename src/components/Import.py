import math
from datetime import datetime

from src.components.Item import Item


class Import:
    """Class Import is where we manage the imports from the Buyer.

    Args:
        import_id (str): is used for identifying this import.
        buyer_id (str): is used for identifying the buyer from whom we get supplies.
        inventory_id (str): is used for identifying where we are about to store the imports.
        imported_date (datetime): is used for specifying when we get the imports.

    Raises:
        TypeError: an error occurred when import_id, buyer_id or inventory_id is empty or None.

    Attributes:
        import_id: where we store import_id.
        buyer_id: where we store buyer_id.
        inventory_id: where we store inventory_id.
        imported_date: where we store imported_date.
    """

    def __init__(self, import_id, buyer_id, inventory_id, imported_date=datetime.today()):
        if not import_id:
            raise TypeError("Argument 'import_id' is required!")
        if not buyer_id:
            raise TypeError("Argument 'buyer_id' is required!")
        if not inventory_id:
            raise TypeError("Argument 'inventory_id' is required!")

        self.import_id = import_id
        self.buyer_id = buyer_id
        self.inventory_id = inventory_id
        self.imported_date = imported_date
        self.import_details = set()

    def add_import_detail(self, item, imported_amount):
        """Adds an import detail to the import.

        Args:
            item (Item)
            imported_amount (int)

        Raises:
            TypeError: an error occurred when
                item is not of Item type;
                imported_amount is not of int type;
                imported_amount is not a non-negative integer.
        """

        if not isinstance(item, Item):
            raise TypeError("Argument 'item' must be an instance of Item!")
        if not imported_amount:
            raise TypeError("Argument 'imported_amount' must be specified!")
        if not isinstance(imported_amount, int) or math.isnan(imported_amount):
            raise TypeError("Argument 'imported_amount' must be a non-negative integer!")
        if imported_amount <= 0:
            raise ValueError("Argument 'imported_amount' must be greater than 0!")

        self.import_details.add(_ImportDetail(self.import_id, item, imported_amount))

    def import_items(self):
        """Get a list of items in the import.

        Returns:
            dict: a dictionary mapping pairs of item id (key) and quantity (value).
        """

        items = dict()
        for element in self.import_details:
            items.update({element.item.item_id: element.quantity})
        return items

    def print_import_details(self):
        # Prints the import details.
        for element in self.import_details:
            print(element)


class _ImportDetail:
    def __init__(self, import_id, item, imported_amount):
        self._import_id = import_id
        self.item = item
        self.imported_amount = imported_amount

    def __str__(self):
        return f"Import ID: {self._import_id} - Item ID: {self.item.item_id} - Amount: {self.imported_amount}\n"
