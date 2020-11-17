import streamlit as st

from src.gui.table import Table


class Menu:
    def __init__(self):
        self.select_box = st.empty()
        self.text = "Choose between viewing table or viewing profit plot: "
        self.options = ["View table", "View profit plot"]
        self.current_option = ""

    def display_option(self):
        self.current_option = self.select_box.selectbox(self.text, self.options)
        if self.current_option == "View table":
            self.display_table()
        elif self.current_option == "View profit plot":
            pass

    def display_table(self):
        table = Table()
        table.show_dataframe()
