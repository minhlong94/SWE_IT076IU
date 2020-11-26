from src.components.Item import Item


class Category:
    """Class Category is where we categorize our products.

    Args:
        category_id (str): is used for identifying category.
        category_name (str): is the name of the category.

    Raises:
        TypeError: if category_id or category_name is empty or None.

    Attributes:
        category_id: where we store category id.
        category_name: where we store category name.
        items: a list of items belonging to the category.
    """

    def __init__(self, category_id, category_name):
        if not category_id:
            raise TypeError("Argument 'category_id' is required!")
        if not category_name:
            raise TypeError("Argument 'category_name' is required!")

        self.category_id = category_id
        self.category_name = category_name
        self.items = set()

    def add_item_to_category(self, item):
        """Adds an item to the category.

        Args:
            item (Item)
        """

        self.items.add(item)

    def print_items(self):
        # Prints the list of items in the category.
        print(self.items)
