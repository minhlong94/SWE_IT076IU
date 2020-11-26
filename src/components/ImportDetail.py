from datetime import datetime


class ImportDetail:
    """
    Class ImportDetail is where we manage every product about to be import into the inventory.

    Args:
        product_id (str): is used for identifying the imported product.
        buyer_id (str): is used for identifying the buyer from whom we get supplies.
        inventory_id (str): is used for identifying where we are about to store the imports.
        imported_amount (int): is used for specifying the amount of product imported.
        imported_date (datetime): is used for specifying when we get the imports.

    Attributes:
        _product_id: where we store product_id.
        _buyer_id: where we store buyer_id.
        _inventory_id: where we store inventory_id.
        _imported_amount: where we store imported_amount.
        _imported_date: where we store imported_date.
    """

    def __init__(self, product_id, buyer_id, inventory_id, imported_amount, imported_date=datetime.today()):
        if product_id is None:
            raise TypeError("Argument 'product_id' is required!")
        if buyer_id is None:
            raise TypeError("Argument 'buyer_id' is required!")
        if inventory_id is None:
            raise TypeError("Argument 'inventory_id' is required!")
        if imported_amount is None:
            raise TypeError("Argument 'imported_amount' must be specified!")
        if not isinstance(imported_amount, int):
            raise TypeError("Argument 'imported_amount' must be an integer!")
        if imported_amount <= 0:
            raise ValueError("Argument 'imported_amount' must be greater than 0!")

        self._product_id = product_id
        self._buyer_id = buyer_id
        self._inventory_id = inventory_id
        self._imported_amount = imported_amount
        self._imported_date = imported_date
