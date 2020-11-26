class Buyer:
    """
    Class Buyer is where we manage and store info about whom we get the supply from.

    Args:
        buyer_id (str): is used for identifying and differentiating buyer.
        buyer_name (str): is the name of the organization or individual who is the buyer.

    Attributes:
        _buyer_id: where we store buyer_id.
        _buyer_name: where we store buyer_name.
    """

    def __init__(self, buyer_id, buyer_name):
        if buyer_id is None:
            raise TypeError("Argument 'buyer_id' is required!")
        if buyer_id is None:
            raise TypeError("Argument 'buyer_name' is required!")

        self._buyer_id = buyer_id
        self._buyer_name = buyer_name
