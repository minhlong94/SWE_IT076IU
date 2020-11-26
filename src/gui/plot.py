import streamlit as st
import pandas as pd
import os
import datetime


class Plot:
    def __init__(self, sales_df = "sales_train.csv"):
        self.df = pd.read_csv(os.path.join("src/data/", sales_df))
        datetime_format = "%d.%m.%Y"
        self.min_date = datetime.datetime.strptime(self.df["date"].min(), datetime_format)
        self.max_date = datetime.datetime.strptime(self.df["date"].max(), datetime_format)

    def plot(self):
        st.write("Please choose the start date and end date. Notice that start day should be less than end date")
        start_date = st.date_input("Start date", value = self.min_date, min_value=self.min_date,
                                   max_value=self.max_date, key="start")
        end_date = st.date_input("Start date", value=self.max_date, min_value=self.min_date,
                                 max_value=self.max_date, key="end")
        assert start_date <= end_date, st.warning("Start day is after end date.")
        st.write(start_date, end_date)

