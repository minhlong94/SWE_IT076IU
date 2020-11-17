import io
import os
import pandas_profiling as pp
import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report as spr


class Table:
    def __init__(self):
        self.show_df = None
        self.profile_df = None
        self.limit_rows = 200
        self.select_box = st.empty()
        self.dataframe = st.empty()
        self.text = "Choose the DataFrame (table) you want to display. " \
                    "The viewer is limited to {} rows.".format(self.limit_rows)
        self.data_path = "src/data"
        self.profile_report = None

    def show_dataframe(self):
        with st.beta_container():
            col1, col2 = st.beta_columns(2)
            with col1:
                options = os.listdir(self.data_path)
                table = st.selectbox(self.text, options)
                df = pd.read_csv(os.path.join(self.data_path, table))
                self.show_df = df.head(self.limit_rows)
                self.profile_df = df
                buffer = io.StringIO()
                df.info(buf=buffer)
                st.text(buffer.getvalue())
                st.dataframe(self.show_df)
            with col2:
                self.profile_report = self.profile_df.profile_report()
                spr(self.profile_report)
