import streamlit as st
import pandas as pd
import os
import datetime
import plotly.express as px


class Plot:
    """Plot the profit

    Attributes:
        self.df: pandas DataFrame. The sales DF.
        self.shop_id: pandas DataFrame. The mapping from shop_id to shop_name
        self.min_date = datetime.datetime. The min date in the sales df
        self.max_date: datetime.datetime. The max date in the sales df
        self.shop_ids: list of int. List of shop ids
        self.num_days_to_plot_week: int, default 90. If days between start_date and end_date <90, do weekly plot, else
            monthly plot
        self.template: string, default "ggplot2". Plotly.express template.
    """

    def __init__(self, sales_df="sales.csv", shop_df="shops.csv"):
        df = pd.read_csv(os.path.join("src/data/", sales_df))
        df["date"] = pd.to_datetime(df["date"])
        shops = pd.read_csv(os.path.join("src/data/", shop_df))
        self.df = df
        self.shop_df = shops
        self.datetime_format = "%d-%m-%Y"
        self.min_date = self.df["date"].min()
        self.max_date = self.df["date"].max()
        self.shop_ids = shops["shop_id"].unique()
        self.num_days_to_plot_week = 90
        self.template = "ggplot2"

    def plot(self):
        """Plot the profit
        Get user's inputs: start_date, end_date and shop_id
        Check if end_date >= start_day, raises AssertionError if False
        Select in the DF that is between start_day and end_date and only contains shop_id
        Group the selected DF by week or month depends on the condition, then use plotly.express to plot the line chart

        Raises:
            AssertionError, if end_date < start_date
        Return:
            None
        """
        with st.beta_container():
            st.write("Please choose the start date and end date. Notice that start day should be less than end date")
            start_date = datetime.datetime.fromordinal(st.date_input("Start date", value=self.min_date,
                                                                     min_value=self.min_date,
                                                                     max_value=self.max_date, key="start").toordinal())
            end_date = datetime.datetime.fromordinal(st.date_input("Start date", value=self.max_date,
                                                                   min_value=self.min_date,
                                                                   max_value=self.max_date, key="end").toordinal())
            shop_id = st.selectbox("Select the SHOP ID: ", self.shop_ids)

            st.write(self.shop_df)

            try:
                assert start_date <= end_date
            except AssertionError:
                st.warning("Start day is after end date.")
                st.stop()
            days_in_between = end_date - start_date

            selected_df = self.df[(self.df["date"].between(start_date, end_date))
                                  & (self.df["shop_id"] == shop_id)]
            selected_df["profit"] = selected_df["item_price"] * selected_df["item_cnt_day"]
            plot_title = " profit of shop {} from {} to {}".format(shop_id, start_date.date(), end_date.date())

            if days_in_between.days <= self.num_days_to_plot_week:
                st.info("Plotting profit by week")
                selected_df["date"] = pd.to_datetime(selected_df["date"]) - pd.to_timedelta(7, unit="d")
                profit_df = selected_df.groupby([pd.Grouper(key="date", freq="W-MON")])["profit"].sum() \
                    .reset_index() \
                    .sort_values("date")  # Group by week
                fig = px.line(profit_df, x="date", y="profit",
                              title="Weekly" + plot_title, template=self.template)
                st.plotly_chart(fig)
            else:
                st.info("Plotting profit by month")
                profit_df = selected_df.groupby([pd.Grouper(key="date", freq="M")])["profit"].sum() \
                    .reset_index() \
                    .sort_values("date")  # Group by month
                fig = px.line(profit_df, x="date", y="profit",
                              title="Monthly" + plot_title, template=self.template)
                st.plotly_chart(fig)
