import streamlit as st
import os
import pandas as pd


class Table:
    def __init__(self):
        # self.placeholder = st.empty()
        self.df = None
        self.limit = 100

    def show_dataframe(self):
        # with self.placeholder.beta_container():
        text = "Choose the DataFrame (table) you want to display. The viewer is limited to 100 rows. "
        data_path = "src/data"
        options = os.listdir(data_path)
        table = st.selectbox(text, options)
        self.df = pd.read_csv(os.path.join(data_path, table)).head(self.limit)
        st.dataframe(self.df)

    # def _empty(self):
    #     self.placeholder.empty()
