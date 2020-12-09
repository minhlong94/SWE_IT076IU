import datetime

import pandas as pd
import plotly.express as px
import streamlit as st


def _group_by(df, freq):
    """Group DF by freq

    Arguments:
        df: pandas DataFrame. The DF that needs to group by column "date"
        freq: string. Either "W-MON" (weekly group) or "M" (monthly group)

    Returns:
         profit_df: pandas DataFrame. The grouped DF by freq, with profit calculated.
    """
    df["transactionDate"] = pd.to_datetime(df["transactionDate"]) - pd.to_timedelta(7, unit="d")
    profit_df = df.groupby([pd.Grouper(key="transactionDate", freq=freq), "shopID"])["profit"].sum() \
        .reset_index() \
        .sort_values("transactionDate")  # Group by week
    return profit_df


def _select_df_in_between(df, start_date, end_date, shop_ids):
    """Get subset of DF that is between given dates

    Arguments:
         df: pandas DataFrame.
         start_date (datetime.datetime): The start date to select
         end_date (datetime.datetime): The end date to select. Start_date <= end_date
         shop_ids (int): The shop_id to select
    Returns:
        selected_df: pandas DataFrame. Subset of the DF with the given condition
    """

    selected_df = df[(df["transactionDate"].between(start_date, end_date))
                     & (df["shopID"].isin(shop_ids))]
    selected_df["profit"] = selected_df["itemPrice"] * selected_df["transactionAmount"]
    return selected_df


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

    Arguments:
        sales_df: string, default "sales.csv". Path to the sales csv file under src/data/...
        shop_df: string, default "shops.csv". Path to the shops csv file under src/data/...

    Sample usage:
        plot = Plot()
        plot.plot()
    """

    def __init__(self, connection, sales_df="sales.csv"):
        self.connection = connection
        # self.df = pd.read_csv(os.path.join("src/data/", sales_df))
        self.df = pd.read_sql('''
            SELECT t.transactionDate, t.shopID, td.itemID, td.itemPrice, td.transactionAmount 
            FROM Transactions t, TransactionDetail td 
            WHERE t.transactionID = td.transactionID 
        ''', self.connection)
        self.df["transactionDate"] = pd.to_datetime(self.df["transactionDate"])
        self.shop_df = pd.read_sql("SELECT * FROM Shop", self.connection)
        self.datetime_format = "%d-%m-%Y"
        self.min_date = self.df["transactionDate"].min()
        self.max_date = self.df["transactionDate"].max()
        self.shop_ids = self.shop_df["shopID"].unique()
        self.num_days_to_plot_week = 90
        self.template = "plotly"

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
            # Options
            st.info("Please choose the start date and end date. Notice that start day should be less than end date")
            start_date = datetime.datetime.fromordinal(st.date_input("Start date", value=self.min_date,
                                                                     min_value=self.min_date,
                                                                     max_value=self.max_date, key="start").toordinal())
            end_date = datetime.datetime.fromordinal(st.date_input("End date", value=self.max_date,
                                                                   min_value=self.min_date,
                                                                   max_value=self.max_date, key="end").toordinal())
            shop_ids = st.multiselect("Select the SHOP ID: ", self.shop_ids)
            with st.beta_expander("Show shop"):
                st.dataframe(self.shop_df)  # Show the sample DF

            # While multiselect is None
            while not shop_ids:
                st.stop()

            # Sanity check start_date and end_date
            try:
                assert start_date <= end_date
            except AssertionError:
                st.exception("Start day is after end date.")
                st.stop()

            days_in_between = end_date - start_date  # Get days in between

            selected_df = _select_df_in_between(self.df, start_date, end_date, shop_ids)
            plot_title = " profit of shop {} from {} to {}".format(shop_ids, start_date.date(), end_date.date())

            if days_in_between.days <= self.num_days_to_plot_week:
                st.info("Plotting profit by week")
                profit_df = _group_by(selected_df, "W-MON")
                st.dataframe(profit_df)
                fig = px.line(profit_df, x="transactionDate", y="profit",
                              title="Weekly" + plot_title, template=self.template)  # Plotly line chart
                st.plotly_chart(fig)
            else:
                st.info("Plotting profit by month")
                profit_df = _group_by(selected_df, "M")
                fig = px.line(profit_df, x="transactionDate", y="profit", title="Monthly" + plot_title,
                              template=self.template, color="shopID")  # Plotly
                st.plotly_chart(fig)
