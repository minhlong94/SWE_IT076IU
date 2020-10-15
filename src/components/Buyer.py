class Buyer:
    """
    Class Buyer is where we manage and store info about whom we get the supply from

    Args:
        buyer_id (str): is used for identifying and differentiating buyer
        buyer_name (str): is the name of the organization or individual who is the buyer

    Attributes:
        _buyer_id: where we store buyer_id
        _buyer_name: where we store buyer_name
    """

    def __init__(self, buyer_id, buyer_name):
        _buyer_id = buyer_id
        _buyer_name = buyer_name
