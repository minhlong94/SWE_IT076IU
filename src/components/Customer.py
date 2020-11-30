class Customer:
    """Class Customer is where we manage and store info about who registering into our system.

    Args:
        customer_id (str): is used for identifying and differentiating customer.
        customer_name (str): is the name of the organization or individual who is the customer.

    Raises:
        TypeError: if customer_id or customer_name is empty or None.

    Attributes:
        customer_id: where we store customer_id.
        customer_name: where we store customer_name.
    """

    def __init__(self, customer_id, customer_name):
        if not customer_id:
            raise TypeError("Argument 'customer_id' is required!")
        if not customer_name:
            raise TypeError("Argument 'customer_name' is required!")

        self.customer_id = customer_id
        self.customer_name = customer_name
