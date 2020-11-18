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
        self.info_field = st.empty()

    def call(self):
        self._welcome()

    def _welcome(self):
        self.title.title("Wholesale Management System")
        text = """
               Wholesale management system of company That Boring Company.  
               ## **WARNING: AUTHORIZED ACCESS ONLY**
               Input your administrator password on the left sidebar, then press "Enter" to login.
               """
        self.info_field.markdown(text)

    def clear(self):
        self.info_field.empty()
