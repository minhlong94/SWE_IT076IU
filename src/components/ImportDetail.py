from datetime import date


class ImportDetail:
    """
    Class ImportDetail is where we manage every product about to be import into the inventory

    Args:
        product_id (str): is used for identifying the imported product
        buyer_id (str): is used for identifying the buyer from whom we get supplies
        inventory_id (str): is used for identifying where we are about to store the imports
        imported_amount (int): is used for specifying the amount of product imported
        imported_date (date): is used for specifying the date when we get the imports

    Attributes:
        _product_id: where we store product_id
        _buyer_id: where we store buyer_id
        _inventory_id: where we store inventory_id
        _imported_amount: where we store imported_amount
        _imported_date: where we store imported_date
    """

    def __init__(self, product_id, buyer_id, inventory_id, imported_amount, imported_date=date.today()):
        self._product_id = product_id
        self._buyer_id = buyer_id
        self._inventory_id = inventory_id
        self._imported_amount = imported_amount
        self._imported_date = imported_date
