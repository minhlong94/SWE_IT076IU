import streamlit as st
from src.gui.main_page import MainPage
from src.gui.table import Table
import datetime
import os
import pandas as pd

placeholder = st.empty()
with placeholder.beta_container():
    main_page = MainPage()
    main_page.call()
    if main_page.login_successful:
        # placeholder.empty()
        # with placeholder.beta_container():
        text = "Choose between viewing table or viewing profit plot: "
        options = ["View table", "View profit plot"]
        # with placeholder.beta_container():
        option = st.selectbox(text, options)
        if option == "View table":
            table = Table()
            table.show_dataframe()
        elif option == "View profit plot":
            shop_id = st.text_input("Shop ID?")
            start_date = st.date_input("Start date: ", datetime.date.today())
            end_date = st.date_input("End date: ", datetime.date.today())
            # data_path = "src/data/sales_train.csv"
            # df = pd.read_csv(data_path)
            # datetime_format = "%Y.%m.%d"
            # df_shopid_date = df[(df["shop_id"] == shop_id)
            #              & (datetime.datetime.strftime(df["date"], datetime_format) ]
            # shop_profit = ((df_shopid_date["item_price"] * df_shopid_date["item_cnt_day"]))
