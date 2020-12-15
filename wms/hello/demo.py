import base64
import errno
import hashlib
import os

import bcrypt
import streamlit as st

import wms
from wms import SessionState
from wms import encryption
from wms.gui.main_page import MainPage
from wms.gui.menu import Menu

OUTPUT_DIR = os.path.expanduser(os.path.join("~", ".wms"))
ENCRYPTION_KEY = os.path.join(OUTPUT_DIR, ".encryption")
DATABASE_DIR = os.path.join(OUTPUT_DIR, "database")
DATABASE_FILE = os.path.join(DATABASE_DIR, "WMS.db")


def create_output_dir():
    check = False

    if not os.path.exists(DATABASE_DIR):
        try:
            os.makedirs(DATABASE_DIR)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        else:
            check = True

    if not os.path.exists(ENCRYPTION_KEY):
        encryption.hash_password(encryption_file=ENCRYPTION_KEY)
        check = True

    return check


@st.cache(allow_output_mutation=True, show_spinner=False, max_entries=1, ttl=300)
def _get_cached_id():
    return dict()


def run(**kwargs):
    session_state = SessionState.get(welcome=False, input_password='', menu=None)

    cached_ids = _get_cached_id()
    print(f"Session ID: {session_state.session_id}\t Cached ID: {cached_ids}\n")

    with open(ENCRYPTION_KEY, "rb") as f:
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
            if not bcrypt.checkpw(base64.b64encode(hashlib.sha512(session_state.input_password.encode()).digest()),
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

        session_state.menu = Menu(db_file=DATABASE_FILE,
                                  csv_zip=os.path.join(os.path.dirname(wms.__file__), "data/dummy/dummy_data.zip"))
        session_state.menu.display_option()
    st.sidebar.write("Note: this is a collapsible sidebar.")


if __name__ == "__main__":
    run()
