import base64
import hashlib

import bcrypt
import streamlit as st

from src.gui.main_page import MainPage
from src.gui.menu import Menu


def login_section():
    st.sidebar.title("LOGIN SECTION")
    st.sidebar.write(""" 
        ## **WARNING: AUTHORIZED ACCESS ONLY**
        Input your administrator password on the left sidebar, then press "Enter" to login.
    """)
    input_password = st.sidebar.text_input("Input administrator password: ", type="password", value="")
    return input_password


def main():
    with open("src/encryption/check_login", "rb+") as f:
        check_login = f.readline()
    with open("src/encryption/hash_pw", "rb") as f:
        hashed_password = f.read()

    st.set_page_config(page_title="Wholesale Management System", layout="wide")

    main_page = MainPage()
    main_page.call()

    if check_login != hashlib.md5("IS_LOGGED_IN".encode()).digest():
        input_password = login_section()
        if st.sidebar.button("Login"):
            if not bcrypt.checkpw(base64.b64encode(hashlib.sha256(input_password.encode()).digest()), hashed_password):
                st.sidebar.warning("Wrong password!")
                st.stop()
            else:
                with open("src/encryption/check_login", "wb") as f:
                    f.write(hashlib.md5("IS_LOGGED_IN".encode()).digest())
                st.experimental_rerun()
    else:
        st.sidebar.title("Experimental App")
        if st.sidebar.button("Logout"):
            with open("src/encryption/check_login", "wb") as f:
                f.write(hashlib.md5("IS_LOGGED_OUT".encode()).digest())
            st.experimental_rerun()
        menu = Menu()
        menu.display_option()
    st.sidebar.write("Note: this is a collapsible sidebar.")

    import atexit
    atexit.register(on_terminate)


def on_terminate():
    with open("src/encryption/check_login", "wb") as f:
        f.write(hashlib.md5("IS_LOGGED_OUT".encode()).digest())


if __name__ == "__main__":
    main()
