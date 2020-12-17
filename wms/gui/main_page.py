import streamlit as st

from wms import SessionState

session_state = SessionState.get()


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


def intro():
    st.markdown("""
        ---\n
        This is a wholesale management system project for Software Engineering course in 
        [International University - VNU-HCM](https://hcmiu.edu.vn/en/).\n
        The web application is built with [Streamlit](https://www.streamlit.io/).\n
        Source code is available at [GitHub](https://github.com/minhlong94/SWE_IT076IU).\n
    """)


def info():
    st.sidebar.markdown("""
        ---\n
        [International University - VNU-HCM](https://hcmiu.edu.vn/en/)\n
        [Streamlit](https://www.streamlit.io/)\n
        [GitHub](https://github.com/minhlong94/SWE_IT076IU)\n
    """)


def login_section():
    pass


def logout_section():
    pass
