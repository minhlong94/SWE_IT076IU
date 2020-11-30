import streamlit as st


class MainPage:
    """Main Page of the Web App

    The main page displays the title, a short description, and instructions for admin

    Attributes:
        title: streamlit container. The title of the web.
        info_field: streamlit container. The short description of the web

    Example usage:
    main_page = MainPage()
    main_page.call() => display title and info_field
    main_page.clear() => clear info field
    """
    def __init__(self):
        self.title = st.empty()
        self.header = st.empty()
        self.info_field = st.empty()

    def call(self):
        self._welcome()

    def _welcome(self):
        self.title.title("Wholesale Management System")
        self.header.header("Welcome to the WMS of company That Boring Company.")
