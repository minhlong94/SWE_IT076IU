import hashlib
import sqlite3
from uuid import uuid4

import pandas as pd
import streamlit as st

from src.components import *


def create_connection(db_file):
    from src import database

    database.create_database(db_file)

    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as err:
        print(err)
    return connection


class Database:
    def __init__(self, connection):
        self.connection = connection
        self.current_option = ""
        self.tables = [table[0] for table in
                       self.connection.cursor().execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
                       if table[0] != "ImportDetail" or table[0] != "TransactionDetail"]
        self.customer_columns = Customer.columns_names(self.connection)
        self.shop_columns = Shop.columns_names(self.connection)
        self.category_columns = ItemCategory.columns_names(self.connection)
        self.item_columns = Item.columns_names(self.connection)

    def show_search(self):
        with st.beta_container():
            self.current_option = st.selectbox("Select table to search :", self.tables)

            if self.current_option == "Customer":
                st.info("""
                    Input name to search for customer in the database.
                    If there is no input, all entries be shown.\n
                    *Limit to 1000 rows.*
                """)
                customer_name = st.text_input("Input customer name: ", value="")
                columns = st.multiselect("Select columns to search: ", self.customer_columns)
                if not columns:
                    columns = self.customer_columns
                if st.button("Search"):
                    with st.beta_expander("Show customer with selected column(s)"):
                        data = Customer.search_by_name(self.connection, customer_name, columns)
                        st.dataframe(pd.DataFrame.from_records(data, columns=columns)[:1000])

            elif self.current_option == "ItemCategory":
                st.info("""
                    Input name to search for category in the database.
                    If there is no input, all entries be shown.\n
                    *Limit to 1000 rows.*
                """)
                category_name = st.text_input("Input category name: ", value="")
                columns = st.multiselect("Select columns to search: ", self.category_columns)
                if not columns:
                    columns = self.category_columns
                if st.button("Search"):
                    with st.beta_expander("Show category with selected column(s)"):
                        data = ItemCategory.search_by_name(self.connection, category_name, columns)
                        st.dataframe(pd.DataFrame.from_records(data, columns=columns)[:1000])

            elif self.current_option == "Buyer":
                pass

            elif self.current_option == "Shop":
                st.info("""
                    Input name to search for shop in the database.
                    If there is no input, all entries be shown.\n
                    *Limit to 1000 rows.*
                """)
                shop_name = st.text_input("Input shop name: ", value="")
                columns = st.multiselect("Select columns to search: ", self.shop_columns)
                if not columns:
                    columns = self.shop_columns
                if st.button("Search"):
                    with st.beta_expander("Show shop with selected column(s)"):
                        data = Shop.search_by_name(self.connection, shop_name, columns)
                        st.dataframe(pd.DataFrame.from_records(data, columns=columns)[:1000])

            elif self.current_option == "Imports":
                st.warning("Not yet implemented.")
                st.stop()

            elif self.current_option == "Transactions":
                st.warning("Not yet implemented.")
                st.stop()

            elif self.current_option == "Item":
                st.info("""
                    Input name to search for category in the database.
                    If there is no input, all entries be shown.\n
                    *Limit to 1000 rows.*
                """)
                item_name = st.text_input("Input item name: ", value="")
                category_name = st.text_input("Input category name: ", value="")
                shop_name = st.text_input("Input shop name: ", value="")
                columns = st.multiselect("Select columns to search: ", self.item_columns)
                if not columns:
                    columns = self.item_columns
                if st.button("Search by item name"):
                    with st.beta_expander("Show item with selected column(s)"):
                        data = Item.search_by_name(self.connection, item_name, columns)
                        st.dataframe(pd.DataFrame.from_records(data, columns=columns)[:1000])
                if st.button("Search by category name"):
                    with st.beta_expander("Show item with selected column(s)"):
                        data = Item.search_by_category_name(self.connection, category_name, columns)
                        st.dataframe(pd.DataFrame.from_records(data, columns=columns)[:1000])
                if st.button("Search by shop name"):
                    with st.beta_expander("Show item with selected column(s)"):
                        data = Item.search_by_shop_name(self.connection, shop_name, columns)
                        st.dataframe(pd.DataFrame.from_records(data, columns=columns)[:1000])

    def show_add(self):
        with st.beta_container():
            self.current_option = st.selectbox("Select table to add: ", self.tables)

            if self.current_option == "Customer":
                customer_name = st.text_input("Input customer name: ", value="")
                customer_id = "CUSTOMER-ID-" + str(uuid4())
                if st.button("Add customer"):
                    check = Customer.insert(self.connection, customer_id, customer_name)
                    with st.spinner("Adding customer..."):
                        if check is None:
                            st.exception("Error when adding customer!")
                            st.stop()
                        else:
                            st.success("Customer was added successfully!")
                            data = Customer.search_by_id(self.connection, customer_id)
                            st.dataframe(pd.DataFrame.from_records(data, columns=self.customer_columns))

            elif self.current_option == "ItemCategory":
                category_name = st.text_input("Input ItemCategory name: ", value="")
                category_id = "ItemCategory-ID-" + hashlib.md5(category_name.encode()).hexdigest()
                if st.button("Add item category"):
                    check = ItemCategory.insert(self.connection, category_id, category_name)
                    if check is None:
                        st.exception("Error when adding category!")
                        st.stop()
                    else:
                        st.success("Item category was added successfully!")
                        data = ItemCategory.search_by_id(self.connection, category_id)
                        st.dataframe(pd.DataFrame.from_records(data, columns=self.category_columns))

            elif self.current_option == "Buyer":
                pass

            elif self.current_option == "Shop":
                shop_name = st.text_input("Input shop name: ", value="")
                shop_id = "SHOP-ID-" + hashlib.md5(shop_name.encode()).hexdigest()
                if st.button("Add shop"):
                    check = Shop.insert(self.connection, shop_id, shop_name)
                    if check is None:
                        st.exception("Error when adding shop!")
                        st.stop()
                    else:
                        st.success("shop was added successfully!")
                        data = Shop.search_by_id(self.connection, shop_id)
                        st.dataframe(pd.DataFrame.from_records(data, columns=self.shop_columns))

            elif self.current_option == "Imports":
                st.warning("Not yet implemented.")
                st.stop()

            elif self.current_option == "Transactions":
                st.warning("Not yet implemented.")
                st.stop()

            elif self.current_option == "Item":
                item_name = st.text_input("Input item name: ", value="")
                item_id = "ITEM-ID-" + hashlib.md5(item_name.encode()).hexdigest()
                quantity = st.number_input("Input item quantity: ", min_value=0, value=0, step=1)
                categories = {}
                for category in ItemCategory.get_all(self.connection):
                    categories[category[0]] = category[1]
                category_name = st.selectbox("Input item category: ", list(categories.values()))
                category_id = None
                for key, value in categories.items():
                    if value == category_name:
                        category_id = key
                st.write(f"Category ID currently: {category_id}")
                shops = {}
                for shop in Shop.get_all(self.connection):
                    shops[shop[0]] = shop[1]
                shop_name = st.selectbox("Input shop name: ", list(shops.values()))
                shop_id = None
                for key, value in shops.items():
                    if value == shop_name:
                        shop_id = key
                st.write(f"Shop ID currently: {shop_id}")
                if st.button("Add item"):
                    check = Item.insert(self.connection, item_id, item_name, quantity, category_id, shop_id)
                    if check is None:
                        st.exception("Error when adding item!")
                        st.stop()
                    else:
                        st.success("shop was added successfully!")
                        data = Item.search_by_id(self.connection, item_id)
                        st.dataframe(pd.DataFrame.from_records(data, columns=self.item_columns))

    def show_remove(self):
        with st.beta_container():
            self.current_option = st.selectbox("Select table to remove: ", self.tables)

            if self.current_option == "Customer":
                st.write("""
                    Input name to search for customer in the database.
                    If there is no input, all entries be shown.
                    Limit to 1000 rows.
                """)
                customer_name = st.text_input("Input customer name: ", value="")
                data = Customer.search_by_name(self.connection, customer_name)
                df = pd.DataFrame.from_records(data, columns=self.customer_columns)[:1000]
                with st.beta_expander("Show customer"):
                    st.dataframe(df)
                rows = st.multiselect("Select customer: ", df.index)
                with st.beta_expander("Show selected customer(s)"):
                    data = Customer.search_by_name(self.connection, customer_name)
                    df = pd.DataFrame.from_records(data, columns=self.customer_columns).iloc[rows, :]
                    selected_ids = df.loc[:, "customerID"].tolist()
                    st.dataframe(df)
                    if st.button("Remove customer"):
                        for Cid in selected_ids:
                            removed = Customer.delete_by_id(self.connection, Cid)
                            print(removed)
                            st.experimental_rerun()

            elif self.current_option == "ItemCategory":
                st.write("""
                    Input name to search for category in the database.
                    If there is no input, all entries be shown.
                    Limit to 1000 rows.
                """)
                category_name = st.text_input("Input category name: ", value="")
                data = ItemCategory.search_by_name(self.connection, category_name)
                df = pd.DataFrame.from_records(data, columns=self.category_columns)[:1000]
                with st.beta_expander("Show item category"):
                    st.dataframe(df)
                rows = st.multiselect("Select item category: ", df.index)
                with st.beta_expander("Show selected category(s)"):
                    data = ItemCategory.search_by_name(self.connection, category_name)
                    df = pd.DataFrame.from_records(data, columns=self.category_columns).iloc[rows, :]
                    selected_ids = df.loc[:, "categoryID"].tolist()
                    st.dataframe(df)
                    if st.button("Remove item category"):
                        for ICid in selected_ids:
                            removed = ItemCategory.delete_by_id(self.connection, ICid)
                            print(removed)
                            st.experimental_rerun()

            elif self.current_option == "Buyer":
                pass

            elif self.current_option == "Shop":
                st.write("""
                    Input name to search for shop in the database.
                    If there is no input, all entries be shown.
                    Limit to 1000 rows.
                """)
                shop_name = st.text_input("Input shop name: ", value="")
                data = Shop.search_by_name(self.connection, shop_name)
                df = pd.DataFrame.from_records(data, columns=self.shop_columns)[:1000]
                with st.beta_expander("Show shop"):
                    st.dataframe(df)
                rows = st.multiselect("Select shop: ", df.index)
                with st.beta_expander("Show selected shop(s)"):
                    data = Shop.search_by_name(self.connection, shop_name)
                    df = pd.DataFrame.from_records(data, columns=self.shop_columns).iloc[rows, :]
                    selected_ids = df.loc[:, "shopID"].tolist()
                    st.dataframe(df)
                    if st.button("Remove shop"):
                        for Sid in selected_ids:
                            removed = Shop.delete_by_id(self.connection, Sid)
                            print(removed)
                            st.experimental_rerun()

            elif self.current_option == "Imports":
                st.warning("Not yet implemented.")
                st.stop()

            elif self.current_option == "Transactions":
                st.warning("Not yet implemented.")
                st.stop()

            elif self.current_option == "Item":
                st.warning("Not yet implemented.")
                st.stop()

    def export_data(self, export_path="src/data/dummy"):
        import csv

        if st.button("Start exporting data"):
            try:
                for table in self.tables:
                    # Export data into CSV file
                    with st.spinner(f"Exporting table '{table}'...\n"):
                        cursor = self.connection.cursor()
                        cursor.execute(f"SELECT * FROM {table}")
                        with open(f"{export_path}/{table}.csv", "w+", encoding="utf-8", newline="") as csv_file:
                            csv_writer = csv.writer(csv_file, delimiter=",")
                            csv_writer.writerow([i[0] for i in cursor.description])
                            csv_writer.writerows(cursor)
                        st.success(f"Data exported Successfully into {export_path}/{table}.csv\n")

            except sqlite3.Error as err:
                print(err)
