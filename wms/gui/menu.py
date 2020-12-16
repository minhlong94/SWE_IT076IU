import streamlit as st

from wms import SessionState
from wms.gui.management import Database, create_connection
from wms.gui.plot import Plot
from wms.gui.table import Table

session_state = SessionState.get()


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

    def __init__(self, db_file, csv_zip=None):
        self.connection = create_connection(db_file, csv_zip)
        self.container = st.sidebar.beta_container()
        self.options = ["Search", "Add", "Remove", "View table", "View profit plot"]
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

        self.container.header("NAVIGATION")

        current_option = self.container.radio("Go to: ", self.options)
        if current_option == "Search":
            self.database.show_search()
        elif current_option == "Add":
            self.database.show_add()
        elif current_option == "Remove":
            self.database.show_remove()
        elif current_option == "View table":
            self.table.show_dataframe()
        elif current_option == "View profit plot":
            self.plot.plot()
        return self.container
