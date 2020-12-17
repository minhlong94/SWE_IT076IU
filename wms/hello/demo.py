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
    session_state = SessionState.get(is_login=False, welcome=False, input_password="")

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
        gui.login_section()
        if st.sidebar.button("Sign in") or session_state.input_password:
            if not bcrypt.checkpw(base64.b64encode(hashlib.sha512(session_state.input_password.encode()).digest()),
                                  hashed_password):
                with st.sidebar.warning("Wrong password!"):
                    session_state.input_password = ""
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
        gui.logout_section()
        gui.info()

    session_state.sync()


if __name__ == "__main__":
    run()
