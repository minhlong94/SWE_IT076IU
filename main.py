import base64
import hashlib

import bcrypt
import streamlit as st

from src import SessionState
from src.gui.main_page import MainPage
from src.gui.menu import Menu


@st.cache(allow_output_mutation=True, show_spinner=False, max_entries=1, ttl=300)
def get_cached_id():
    return dict()


def main():
    session_state = SessionState.get(welcome=False, input_password='', menu=None)

    cached_ids = get_cached_id()
    print(f"Session ID: {session_state.session_id}\t Cached ID: {cached_ids}\n")

    with open("src/encryption/hash_pw", "rb") as f:
        hashed_password = f.read()

    st.set_page_config(page_title="Wholesale Management System", layout="wide")

    MainPage().call()

    if session_state.session_id not in cached_ids.values():
        st.sidebar.header("LOGIN SECTION")
        st.sidebar.subheader("**WARNING: AUTHORIZED ACCESS ONLY**")
        st.sidebar.write("""
            Input your privileged password on the left sidebar, then click **Sign in** or press **Enter** to login.
        """)
        session_state.input_password = st.sidebar.text_input("Input privileged password: ", type="password",
                                                             value=session_state.input_password)

        if st.sidebar.button("Sign in") or session_state.input_password:
            if not bcrypt.checkpw(base64.b64encode(hashlib.sha256(session_state.input_password.encode()).digest()),
                                  hashed_password):
                st.sidebar.warning("Wrong password!")
                st.stop()
            else:
                cached_ids[session_state.session_id] = session_state.session_id
                st.experimental_rerun()
    else:
        if not session_state.welcome:
            st.balloons()
            session_state.welcome = True

        st.sidebar.header("APP OPTIONS")
        st.sidebar.warning("This application is still in development state.")
        st.sidebar.write(f"*Current session ID: {session_state.session_id}*")

        if st.sidebar.button("Sign out"):
            session_state.input_password = ''
            cached_ids.pop(session_state.session_id)
            session_state.welcome = False
            st.experimental_rerun()

        session_state.menu = Menu()
        session_state.menu.display_option()
    st.sidebar.write("Note: this is a collapsible sidebar.")


if __name__ == "__main__":
    main()
