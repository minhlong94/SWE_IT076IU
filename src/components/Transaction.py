from datetime import datetime


def pending():
    return "pending"


class Transaction:
    """
    Class Transaction is where we manage the transactions which the customers have made.

    Args:
        transaction_id (str): is used for identifying the transaction.
        customer_id (str): is used for specifying the customer who made the transaction.
        status (str): is used for specifying the status of the transaction.
        created_date (datetime): is used for specifying when the transaction is created.

    Attributes:
        _transaction_id: where we store transaction_id
        _customer_id: where we store customer_id
        _status: where we store status
        _created_date: where we store created_date
    """

    def __init__(self, transaction_id, customer_id, status, created_date=datetime.today()):
        self._transaction_id = transaction_id
        self._customer_id = customer_id
        self._status = status
        self._created_date = created_date
