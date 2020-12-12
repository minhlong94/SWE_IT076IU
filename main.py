import base64
import hashlib

import bcrypt
import streamlit as st
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

from src.gui.main_page import MainPage
from src.gui.menu import Menu
from src.encryption import hash_password


@st.cache(show_spinner=False, max_entries=1, ttl=5)
def _get_session_id():
    # Hack to get the session object from Streamlit.

    ctx = get_report_ctx()

    this_session = None

    current_server = Server.get_current()
    if hasattr(current_server, '_session_infos'):
        # Streamlit < 0.56
        session_infos = Server.get_current()._session_infos.values()
    else:
        session_infos = Server.get_current()._session_info_by_id.values()

    for session_info in session_infos:
        s = session_info.session
        if (
                # Streamlit < 0.54.0
                (hasattr(s, '_main_dg') and s._main_dg == ctx.main_dg)
                or
                # Streamlit >= 0.54.0
                (not hasattr(s, '_main_dg') and s.enqueue == ctx.enqueue)
                or
                # Streamlit >= 0.65.2
                (not hasattr(s, '_main_dg') and s._uploaded_file_mgr == ctx.uploaded_file_mgr)
        ):
            this_session = s

    if this_session is None:
        raise RuntimeError(
            "Oh noes. Couldn't get your Streamlit Session object. "
            'Are you doing something fancy with threads?')

    return str(id(this_session))


def _login_section():
    st.sidebar.title("LOGIN SECTION")
    st.sidebar.write(""" 
        ## **WARNING: AUTHORIZED ACCESS ONLY**
        Input your administrator password on the left sidebar, then press "Enter" to login.
    """)
    input_password = st.sidebar.text_input("Input administrator password: ", type="password", value="")
    return input_password


def main():
    hash_password()
    current_session_id = _get_session_id()

    with open("src/encryption/check_session", "rb") as f:
        check_login = f.readline()
    with open("src/encryption/hash_pw", "rb") as f:
        hashed_password = f.read()

    st.set_page_config(page_title="Wholesale Management System", layout="wide")

    main_page = MainPage()
    main_page.call()

    if check_login != hashlib.sha1(current_session_id.encode()).digest():
        input_password = _login_section()
        if st.sidebar.button("Login") or input_password:
            if not bcrypt.checkpw(base64.b64encode(hashlib.sha256(input_password.encode()).digest()), hashed_password):
                st.sidebar.warning("Wrong password!")
                st.stop()
            else:
                with open("src/encryption/check_session", "wb") as f:
                    f.write(hashlib.sha1(current_session_id.encode()).digest())
                st.experimental_rerun()
    else:
        st.sidebar.title("Experimental App")
        if st.sidebar.button("Logout"):
            with open("src/encryption/check_session", "wb") as f:
                f.write(hashlib.sha1("IS_LOGGED_OUT".encode()).digest())
            st.experimental_rerun()
        menu = Menu()
        menu.display_option()
    st.sidebar.write("Note: this is a collapsible sidebar.")


if __name__ == "__main__":
    main()
