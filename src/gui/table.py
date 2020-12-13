import io
import sqlite3

import hiplot as hip
import pandas as pd
import pandas_profiling as pp
import streamlit as st
import streamlit.components.v1 as components


class Table:
    """Table displayer

    Display the top few rows of the table (DataFrame), its information and the Pandas Profiling HTML.

    Attributes:
        show_df: pandas DataFrame. DataFrame that will be displayed. Limit to 200 rows.
        profile_df: pandas DataFrame. DataFrame that will be calculated using Pandas Profiling. \
            This DF is usually the full DataFrame.
        limit_rows: int, default 200. Number of rows to be displayed as sample
        select_box: streamlit container. A select box to ask admin which DataFrame to display.
        dataframe: streamlit container. A container to display the DataFrame.
        text: string. The instruction for admin.
        data_path: string (as path). The relative path to the data directory.
        profile_report: Pandas Profiling ProfileReport. The Pandas Profiling ProfileReport \
            that will be displayed as HTML.

    Example usage:
    table = Table()
    table.show_dataframe() => Show options and the selected DataFrame.

    """

    def __init__(self, connection):
        self.connection = connection
        self.show_df = None
        self.profile_df = None
        self.limit_rows = 100000
        self.select_box = st.empty()
        self.dataframe = st.empty()
        self.text = "Choose the DataFrame (table) you want to display. " \
                    "The viewer is limited to {} rows.".format(self.limit_rows)
        self.data_path = "src/data/dummy"
        self.profile_report = None

    def show_dataframe(self, minimal=True):
        with st.beta_container():
            # Options
            options = [table[0] for table in self.connection.cursor().execute(
                "SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
            table = st.selectbox(self.text, options, index=3)
            st.info(f"Note: due to limited output size, the displayed DataFrame is limited to the first "
                    f"{self.limit_rows} rows only.\n\nHowever, the Pandas Profiling Report "
                    f"calculates on the full DataFrame.")

            col1, col2 = st.beta_columns(2)
            with col1:
                df = _load_df(table, self.connection)
                self.show_df = df.head(self.limit_rows)  # Only shows limited rows
                self.profile_df = df

                # Show DataFrame's info
                buffer = io.StringIO()
                df.info(buf=buffer)
                st.text(buffer.getvalue())

                # Show HiPlot
                xp = hip.Experiment.from_dataframe(self.show_df)
                xp.display_st(key="hip")
            with col2:
                # Show Pandas Profile Report
                self.profile_report = pp.ProfileReport(self.profile_df, minimal=minimal, progress_bar=False)
                with st.spinner("Generating profile report..."):
                    components.html(self.profile_report.to_html(), height=1500, scrolling=True)


@st.cache(persist=True, show_spinner=False, max_entries=10, hash_funcs={sqlite3.Connection: id}, ttl=300)
def _load_df(table, connection):
    return pd.read_sql(f'''SELECT * FROM {table}''', connection)
