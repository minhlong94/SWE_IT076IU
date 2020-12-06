import streamlit as st

from src.gui import Database

from src.gui.plot import Plot
from src.gui.table import Table


class Menu:
    """Menu

    Page that appears after successfully login. Includes a select box to ask user options.
    Attributes:
        select_box: streamlit container. The select box.
        text: string. The instruction for admin to choose.
        options: list of string. Available options
        current_option: string, default "". Current selection of the select box

    Example usage:
    menu = Menu()
    menu.display_option() => Display the select box
    menu.display_table() => Display the table (as DataFrame)
    """
    def __init__(self):
        self.connection = Database.create_connection("src/database/database.db")
        self.select_box = st.sidebar.empty()
        self.text = "Choose between viewing table or viewing profit plot: "
        self.options = ["Search", "Add", "Remove", "View table", "View profit plot"]
        self.current_option = ""
        self.database = Database.Database(self.connection)
        self.plot = Plot()
        self.table = Table()

    def display_option(self):
        """Display options as select box

        Display options as select box, either View table or View profit plot
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
