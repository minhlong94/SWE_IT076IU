"""Hack to add per-session state to Streamlit.

Works for Streamlit >= v0.65

Usage
-----

>>> from wms import SessionState
>>>
>>> session_state = SessionState.get(user_name='', favorite_color='black')
>>> session_state.user_name
''
>>> session_state.user_name = 'Mary'
>>> session_state.favorite_color
'black'

Since you set user_name above, next time your script runs this will be the
result:
>>> session_state = get(user_name='', favorite_color='black')
>>> session_state.user_name
'Mary'

"""

from streamlit.hashing import _CodeHasher
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server


class _SessionState:
    """SessionState: Add per-session state to Streamlit."""

    def __init__(self, session, hash_funcs, **kwargs):
        """Initialize SessionState instance."""
        self.__dict__["_state"] = {
            "data": {},
            "hash": None,
            "hasher": _CodeHasher(hash_funcs),
            "is_rerun": False,
            "session": session,
            "session_id": id(session),
        }
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __call__(self, **kwargs):
        """Initialize state data once."""
        for key, value in kwargs.items():
            if key not in self._state["data"]:
                self._state["data"][key] = value

    def __getitem__(self, key):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(key, None)

    def __getattr__(self, key):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(key, None)

    def __setitem__(self, key, value):
        """Set state value."""
        self._state["data"][key] = value

    def __setattr__(self, key, value):
        """Set state value."""
        self._state["data"][key] = value

    def get_id(self):
        return self._state["session_id"]

    def clear(self):
        """Clear session state and request a rerun."""
        self._state["data"].clear()
        self._state["session"].request_rerun()

    def sync(self):
        """Rerun the app with all state values up to date from the beginning to fix rollbacks."""

        # Ensure to rerun only once to avoid infinite loops
        # caused by a constantly changing state value at each run.
        #
        # Example: state.value += 1
        if self._state["is_rerun"]:
            self._state["is_rerun"] = False

        elif self._state["hash"] is not None:
            if self._state["hash"] != self._state["hasher"].to_bytes(self._state["data"], None):
                self._state["is_rerun"] = True
                self._state["session"].request_rerun()

        self._state["hash"] = self._state["hasher"].to_bytes(self._state["data"], None)


def _get_session():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError('Could not get Streamlit session object.')

    return session_info.session


def get(hash_funcs=None, **kwargs):
    """Gets a SessionState object for the current session.

    Example
    -------
    >>> session_state = get(user_name="", favorite_color="black")
    >>> session_state.user_name
    ''
    >>> session_state.user_name = "Mary"
    >>> session_state.favorite_color
    'black'

    Since you set user_name above, next time your script runs this will be the
    result:
    >>> session_state = get(user_name='', favorite_color="black")
    >>> session_state.user_name
    'Mary'

    """

    # Hack to get the session object from Streamlit.
    this_session = _get_session()

    # Got the session object! Now let's attach some state into it.
    if not hasattr(this_session, "_custom_session_state"):
        this_session._custom_session_state = _SessionState(this_session, hash_funcs, **kwargs)

    return this_session._custom_session_state
