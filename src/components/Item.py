class Item:
    """
    Class Item is where we define product's info in our system

    Args:
        item_id (str): is used for identifying item
        item_name (str): name of the item
        category_id (str): define the category of the item

    Attributes:
        _item_id: where we store item_id
        _item_name: where we store item_name
        _category_id: where we store category_id
    """

    def __init__(self, item_id, item_name, category_id):
        _item_id = item_id
        _item_name = item_name
        _category_id = category_id
