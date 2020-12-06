import streamlit as st
from src.gui.table import Table
from src.gui.plot import Plot


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
        self.select_box = st.empty()
        self.text = "Choose between viewing table or viewing profit plot: "
        self.options = ["View table", "View profit plot"]
        self.current_option = ""
        self.plot = Plot()
        self.table = Table()

    def display_option(self):
        """Display options as select box

        Display options as select box, either View table or View profit plot
        """
        self.current_option = self.select_box.selectbox(self.text, self.options)
        if self.current_option == "View table":
            self.table.show_dataframe()
        elif self.current_option == "View profit plot":
            self.plot.plot()

