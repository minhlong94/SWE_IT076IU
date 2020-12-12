import base64
import hashlib

import bcrypt
import streamlit as st

import SessionState
from src.gui.main_page import MainPage
from src.gui.menu import Menu


def _login_section():
    st.sidebar.title("LOGIN SECTION")
    st.sidebar.write(""" 
        ## **WARNING: AUTHORIZED ACCESS ONLY**
        Input your administrator password on the left sidebar, then press "Enter" to login.
    """)
    input_password = st.sidebar.text_input("Input administrator password: ", type="password", value="")
    return input_password


def main():
    session_id = SessionState.get_session_id()
    cached_id = SessionState.get_cached_id()

    with open("src/encryption/hash_pw", "rb") as f:
        hashed_password = f.read()

    st.set_page_config(page_title="Wholesale Management System", layout="wide")

    main_page = MainPage()
    main_page.call()

    if session_id not in cached_id:
        input_password = _login_section()
        if st.sidebar.button("Login") or input_password:
            if not bcrypt.checkpw(base64.b64encode(hashlib.sha256(input_password.encode()).digest()), hashed_password):
                st.sidebar.warning("Wrong password!")
                st.stop()
            else:
                cached_id.clear()
                cached_id.append(session_id)
                st.experimental_rerun()
    else:
        st.sidebar.title("Experimental App")
        if st.sidebar.button("Logout"):
            cached_id.clear()
            st.experimental_rerun()
        menu = Menu()
        menu.display_option()
    st.sidebar.write("Note: this is a collapsible sidebar.")


if __name__ == "__main__":
    main()
