import streamlit as st
import bcrypt
import time


class MainPage:
    def __init__(self):
        # self.placeholder = st.empty()
        self.login_successful = False

    def call(self):
        # with self.placeholder.beta_container():
        self._welcome()
        self._login()

    def _welcome(self):
        st.title("Wholesale Management System")
        text = """
                   Welcome to the wholesale management system of company XXX.\n
                   **WARNING: AUTHORIZED ACCESS ONLY**\n
                   Input your administrator password, then click "Login" button to login.
                   """
        st.info(text)

    def _login(self):
        f = open("src/encryption/hash_pw.txt", "rb")
        hashed_password = f.read()
        f.close()
        input_password = st.text_input("Input administrator password: ", type="password")
        # button = st.button("Login")
        # if button:
        if not bcrypt.checkpw(input_password.encode("utf8"), hashed_password):
            st.warning("Wrong password.")
            st.stop()
        else:
            st.success("Login successful! Loading system viewer...")
            time.sleep(3)
            self.login_successful = True
            # self._empty()
    #
    # def _empty(self):
    #     self.placeholder.empty()

