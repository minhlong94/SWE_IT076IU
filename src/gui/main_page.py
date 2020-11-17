import streamlit as st


class MainPage:
    def __init__(self):
        self.login_successful = True
        self.title = st.empty()
        self.info_field = st.empty()
        self.success = st.empty()

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
