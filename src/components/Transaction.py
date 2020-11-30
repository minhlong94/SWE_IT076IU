import math
from datetime import datetime

from src.components.Item import Item


class Transaction:
    """Class Transaction is where we manage the transactions which the customers have made.

    Args:
        transaction_id (str): is used for identifying the transaction.
        customer_id (str): is used for specifying the customer who made the transaction.
        transaction_status (str): must be either PENDING or COMPLETED.
        created_date (datetime): is used for specifying when the transaction is created.

    Raises:
        TypeError: an error occurred when transaction_id, customer_id or transaction_status is empty or None.
        ValueError: an error occurred when argument transaction_status is invalid.

    Attributes:
        transaction_id: where we store transaction id
        transaction_status: where we store transaction status
        created_date: where we store created date
        transaction_details: list of transaction detail
    """

    STATUSES = {"PENDING", "COMPLETED"}

    def __init__(self, transaction_id, customer_id, transaction_status, created_date=datetime.today()):
        if not transaction_id:
            raise TypeError("Argument 'transaction_id' is required!")
        if not customer_id:
            raise TypeError("Argument 'customer_id' is required!")
        if not transaction_status:
            raise TypeError("Argument 'status' is required!")
        if transaction_status not in self.STATUSES:
            raise ValueError("Argument 'status' must be one of {}!".format(self.STATUSES))

        self.transaction_id = transaction_id
        self._customer_id = customer_id
        self.transaction_status = transaction_status
        self.created_date = created_date
        self.transaction_details = set()

    def add_transaction_detail(self, item, quantity):
        """Adds a new transaction detail to this transaction.

        Args:
            item (Item)
            quantity (int)

        Raises:
            TypeError: an error occurred when
                item is not of Item type;
                quantity is not of int type;
                quantity is not a non-negative integer.
        """

        if not isinstance(item, Item):
            raise TypeError("Argument 'item' must be an instance of Item!")
        if not quantity:
            raise TypeError("Argument 'imported_amount' must be specified!")
        if not isinstance(quantity, int) or math.isnan(quantity):
            raise TypeError("Argument 'imported_amount' must be a non-negative integer!")
        if quantity <= 0:
            raise ValueError("Argument 'imported_amount' must be greater than 0!")

        self.transaction_details.add(_TransactionDetail(self.transaction_id, item, quantity))

    def transaction_items(self):
        """Get a list of items in the transaction.

        Returns:
            dict: a dictionary mapping pairs of item id (key) and quantity (value).
        """

        items = dict()
        for element in self.transaction_details:
            items.update({element.item.item_id: element.quantity})
        return items

    def print_transaction_details(self):
        # Prints the transaction details.
        for element in self.transaction_details:
            print(element)


class _TransactionDetail:
    def __init__(self, transaction_id, item, quantity):
        self._transaction_id = transaction_id
        self.item = item
        self.quantity = quantity

    def __str__(self):
        return f"Transaction ID: {self._transaction_id} - Item ID: {self.item.item_id} - Quantity: {self.quantity}\n"
