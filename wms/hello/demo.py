import base64
import hashlib
import os

import bcrypt
import streamlit as st

import wms
from wms import SessionState
from wms import gui


@st.cache(allow_output_mutation=True, show_spinner=False, max_entries=1, ttl=300)
def _get_cached_id():
    return dict()


def run(**kwargs):
    session_state = SessionState.get(is_login=False, welcome=False)

    try:
        encryption_key = kwargs["encryption_file"]
        database_file = kwargs["database_file"]
    except KeyError:
        from wms import cli

        encryption_key = cli.ENCRYPTION_KEY
        database_file = cli.DATABASE_FILE

    with open(encryption_key, "rb") as f:
        hashed_password = f.read()

    st.set_page_config(page_title="Wholesale Management System", layout="wide")

    main_page = gui.MainPage()
    main_page.call()

    if not session_state.is_login:
        gui.intro()

        st.sidebar.header("LOGIN SECTION")
        st.sidebar.subheader("**WARNING: AUTHORIZED ACCESS ONLY**")
        st.sidebar.write("""
                        Input your privileged password on the left sidebar, then click **Sign in** or press **Enter** to login.
                    """)
        session_state.input_password = st.sidebar.text_input("Input privileged password: ", type="password",
                                                             value=session_state.input_password or "")

        if st.sidebar.button("Sign in") or session_state.input_password:
            if not bcrypt.checkpw(base64.b64encode(hashlib.sha512(session_state.input_password.encode()).digest()),
                                  hashed_password):
                st.sidebar.warning("Wrong password!")
                st.stop()
            else:
                session_state.is_login = True
                st.experimental_rerun()
    else:
        if not session_state.welcome:
            st.balloons()
            session_state.welcome = True

        menu = gui.Menu(db_file=database_file,
                        csv_zip=os.path.join(os.path.dirname(wms.__file__), "hello/dummy/dummy_data.zip"))

        menu.display_option()

        st.sidebar.markdown("---")
        st.sidebar.write(f"*Current session ID: {session_state.get_id()}*")
        if st.sidebar.button("Sign out"):
            session_state.clear()

        gui.info()

    session_state.sync()


if __name__ == "__main__":
    run()
