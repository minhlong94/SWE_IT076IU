class Item:
    """Class Item is where we define product's info in our system.

    Args:
        item_id (str): is used for identifying item.
        item_name (str): is the name of the item.
        category_id (str): is used for specifying the category of the item.

    Raises:
        TypeError: if item_id, item_name or category_id is empty or None.

    Attributes:
        item_id: where we store item_id.
        item_name: where we store item_name.
        category_id: where we store category_id.
    """

    def __init__(self, item_id, item_name, category_id):
        if not item_id:
            raise TypeError("Argument 'item_id' is required!")
        if not item_name:
            raise TypeError("Argument 'item_name' is required!")
        if not category_id:
            raise TypeError("Argument 'category_id' is required!")

        self.item_id = item_id
        self.item_name = item_name
        self.category_id = category_id
