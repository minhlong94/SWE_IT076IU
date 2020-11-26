import streamlit as st
import pandas as pd
import os
import datetime
import plotly.express as px


class Plot:
    def __init__(self, sales_df="sales.csv"):
        self.df = pd.read_csv(os.path.join("src/data/", sales_df))
        self.datetime_format = "%d-%m-%Y"
        self.min_date = datetime.datetime.strptime(self.df["date"].min(), self.datetime_format)
        self.max_date = datetime.datetime.strptime(self.df["date"].max(), self.datetime_format)
        self.shop_ids = self.df["shop_id"].unique()
        self.num_days_to_plot_week = 90

    def plot(self):
        with st.beta_container():
            st.write("Please choose the start date and end date. Notice that start day should be less than end date")
            start_date = st.date_input("Start date", value=self.min_date, min_value=self.min_date,
                                       max_value=self.max_date, key="start").strftime(self.datetime_format)
            end_date = st.date_input("Start date", value=self.max_date, min_value=self.min_date,
                                     max_value=self.max_date, key="end").strftime(self.datetime_format)
            shop_id = st.selectbox("Select the SHOP ID: ", self.shop_ids)
            assert start_date <= end_date, st.warning("Start day is after end date.")
            st.write(start_date, end_date)
            days_in_between = datetime.datetime.strptime(end_date, self.datetime_format) \
                              - datetime.datetime.strptime(start_date, self.datetime_format)
            plot_df = self.df[(self.df["date"] >= start_date)
                              & (self.df["date"] <= end_date)
                              & (self.df["shop_id"] == shop_id)]
            if days_in_between.days < self.num_days_to_plot_week:
                st.write("Plotting profit by week")
                plot_df["date"] = pd.to_datetime(plot_df["date"]) - pd.to_datetime(7, unit="d")
                plot_df["revenue"] = plot_df["item_price"] * plot_df["item_cnt_day"]
                profit_df = plot_df.groupby([pd.Grouper(key="date", freq="W-MON"), plot_df["shop_id"]]) \
                    ["revenue"].sum() \
                    .reset_index() \
                    .sort_values("date")
                # plot_df["date"] = plot_df["date"].strptime(self.datetime_format)
                st.write(plot_df)
                fig = px.line(profit_df, x="date", y="revenue", title="Weelky profit of shop {}".format(shop_id))
                st.plotly_chart(fig)
            else:
                st.write("Plotting profit by month")
            group_df = (plot_df["item_price"] * plot_df["item_cnt_day"]) \
                .groupby([plot_df["date"], plot_df["shop_id"]]) \
                .sum() \
                .reset_index(name="revenue")
