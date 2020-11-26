class Customer:
    """
    Class Customer is where we manage and store info about who registering into our system.

    Args:
        customer_id (str): is used for identifying and differentiating customer.
        customer_name (str): is the name of the organization or individual who is the customer.

    Attributes:
        _customer_id: where we store customer_id.
        _customer_name: where we store customer_name.
    """

    def __init__(self, customer_id, customer_name):
        if customer_id is None:
            raise TypeError("Argument 'customer_id' is required!")
        if customer_name is None:
            raise TypeError("Argument 'customer_name' is required!")

        self._customer_id = customer_id
        self._customer_name = customer_name
