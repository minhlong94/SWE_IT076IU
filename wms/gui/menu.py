import streamlit as st

from wms.gui._database import Database, create_connection
from wms.gui._plot import Plot
from wms.gui._table import Table


class Menu:
    """Menu

    Page that appears after successfully login. Includes a select box to ask user options.

    Example:
        >>> menu = Menu()
        >>> menu.display_option() # Display the select box

    Attributes:
        select_box: streamlit container. The select box.
        text: string. The instruction for admin to choose.
        options: list of string. Available options
        current_option: string, default "". Current selection of the select box
    """
    def __init__(self, db_file="database/database.db"):
        self.connection = create_connection(db_file)
        self.select_box = st.sidebar.empty()
        self.text = "Choose an option: "
        self.options = ["Search", "Add", "Remove", "View table", "View profit plot", "Export to csv"]
        self.current_option = ""
        self.database = Database(self.connection)
        self.plot = Plot(self.connection)
        self.table = Table(self.connection)

    def display_option(self):
        """Display options as select box

        Options:
            Search: go to search page.\n
            Add: go to add page.\n
            Remove: go to remove page.\n
            View table: here to view tables in the database.\n
            View profit plot: view the plot of profit in a specific amount of time.\n
            Export to csv: to export the data from the database to csv format.
        """
        
        self.current_option = self.select_box.selectbox(self.text, self.options)
        if self.current_option == "Search":
            self.database.show_search()
        elif self.current_option == "Add":
            self.database.show_add()
        elif self.current_option == "Remove":
            self.database.show_remove()
        elif self.current_option == "View table":
            self.table.show_dataframe()
        elif self.current_option == "View profit plot":
            self.plot.plot()
        elif self.current_option == "Export to csv":
            self.database.export_data()
