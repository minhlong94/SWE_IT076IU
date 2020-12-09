import hashlib
import sqlite3
from uuid import uuid4

import pandas as pd
import streamlit as st

from src.components import *


def _create_connection(db_file):
    from src import database

    database.create_database(db_file)

    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as err:
        print(err)
    return connection


class Database:
    def __init__(self, db_file):
        self.connection = _create_connection(db_file)
        self.current_option = ""
        self.tables = [table[0] for table in self.connection.cursor().execute(
            "SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
        self.customer_columns = Customer.columns_names(self.connection)

    def show_search(self):
        with st.beta_container():
            self.current_option = st.selectbox("Select table to search :", self.tables)

            if self.current_option == "Customer":
                st.write("""
                    Input name to search for customer in the database.
                    If there is no input, all entries be shown.
                    Limit to 1000 rows.
                """)
                customer_name = st.text_input("Input customer name: ", value="")
                columns = st.multiselect("Select columns to search: ", self.customer_columns)
                if not columns:
                    columns = self.customer_columns
                if st.button("Search"):
                    with st.beta_expander("Show Customer with selected column(s)"):
                        data = Customer.search_by_name(self.connection, customer_name, columns)
                        st.write(pd.DataFrame.from_records(data.fetchall(), columns=columns)[:1000])

            elif self.current_option == "ItemCategory":
                pass

            elif self.current_option == "Buyer":
                pass

            elif self.current_option == "Shop":
                pass

            elif self.current_option == "Imports":
                pass

            elif self.current_option == "Transactions":
                pass

            elif self.current_option == "Item":
                pass

    def show_add(self):
        with st.beta_container():
            self.current_option = st.selectbox("Select table to add: ", self.tables)

            if self.current_option == "Customer":
                customer_name = st.text_input("Input customer name: ", value="")
                customer_id = "CUSTOMER-ID-" + hashlib.md5(customer_name.encode()).hexdigest() + "-" + str(uuid4())
                if st.button("Add customer"):
                    check = Customer.insert(self.connection, customer_id, customer_name)
                    with st.spinner("Adding customer..."):
                        if check is None:
                            st.error("Error when adding customer!")
                            st.stop()
                        else:
                            st.success("Customer was added successfully!")
                            data = Customer.search_by_id(self.connection, customer_id)
                            st.write(pd.DataFrame.from_records(data.fetchall(), columns=self.customer_columns))

            elif self.current_option == "ItemCategory":
                category_name = st.text_input("Input ItemCategory name: ", value="")
                category_id = "ItemCategory-ID-" + hashlib.md5(category_name.encode()).hexdigest()
                if st.button("Add ItemCategory"):
                    check = ItemCategory.insert(self.connection, category_id, category_name)
                    if check is None:
                        st.error("Error!")
                        st.stop()
                    else:
                        st.success("ItemCategory was added successfully!")

            elif self.current_option == "Buyer":
                buyer_name = st.text_input("Input buyer name: ", value="")
                buyer_id = "BUYER-ID-" + hashlib.md5(buyer_name.encode()).hexdigest()
                if st.button("Add ItemCategory"):
                    check = ItemCategory.insert(self.connection, buyer_id, buyer_name)
                    if check is None:
                        st.error("Error!")
                        st.stop()
                    else:
                        st.success("Buyer was added successfully!")

            elif self.current_option == "Shop":
                shop_name = st.text_input("Input shop name: ", value="")
                shop_id = "SHOP-ID-" + hashlib.md5(shop_name.encode()).hexdigest()
                if st.button("Add ItemCategory"):
                    check = ItemCategory.insert(self.connection, shop_id, shop_name)
                    if check is None:
                        st.error("Error!")
                        st.stop()
                    else:
                        st.success("shop was added successfully!")

            elif self.current_option == "Imports":
                pass

            elif self.current_option == "Transactions":
                pass

            elif self.current_option == "Item":
                pass

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
                df = pd.DataFrame.from_records(data.fetchall(), columns=self.customer_columns)[:1000]
                with st.beta_expander("Show Customer"):
                    st.dataframe(df)
                rows = st.multiselect("Select Customer: ", df.index)
                with st.beta_expander("Show selected customer(s)"):
                    data = Customer.search_by_name(self.connection, customer_name)
                    df = pd.DataFrame.from_records(data.fetchall(), columns=self.customer_columns).iloc[rows, :]
                    selected_ids = df.loc[:, "customerID"].tolist()
                    st.dataframe(df)
                    if st.button("Remove Customer"):
                        for cid in selected_ids:
                            removed = Customer.delete_by_id(self.connection, cid)
                            print(removed)
                            st.experimental_rerun()

            elif self.current_option == "ItemCategory":
                pass

            elif self.current_option == "Buyer":
                pass

            elif self.current_option == "Shop":
                pass

            elif self.current_option == "Imports":
                pass

            elif self.current_option == "Transactions":
                pass

            elif self.current_option == "Item":
                pass

    def export_data(self, export_path):
        import csv

        try:
            for table in self.tables:
                # Export data into CSV file
                st.info(f"Exporting table '{table}'...\n")
                cursor = self.connection.cursor()
                cursor.execute(f"SELECT * FROM {table}")
                with open(f"{export_path}/{table}.csv", "w+", encoding='utf-8') as csv_file:
                    csv_writer = csv.writer(csv_file, delimiter="\t")
                    csv_writer.writerow([i[0] for i in cursor.description])
                    csv_writer.writerows(cursor)
                st.success(f"Data exported Successfully into {export_path}/{table}.csv\n")

        except sqlite3.Error as err:
            print(err)
