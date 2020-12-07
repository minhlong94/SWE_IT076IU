import sqlite3
import hashlib
from datetime import datetime
from uuid import uuid1, uuid4

import pandas as pd
import streamlit as st

from src import components


def _create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as err:
        print(err)
    return connection


class Database:
    def __init__(self, db_file):
        self.connection = _create_connection(db_file)
        self.tables = [table[0] for table in self.connection.cursor().execute(
            "SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
        self.current_option = ""

    def show_search(self):
        with st.beta_container():
            self.current_option = st.selectbox("Select table to add data", self.tables)

            if self.current_option == "Customer":
                customer_name = st.text_input("Input customer name: ", value="")
                if customer_name:
                    data = components.Customer.search_by_name(self.connection, customer_name)
                    df = pd.DataFrame(data.fetchall(), columns=['Customer ID', 'Customer name'])
                    st.write(df)

            elif self.current_option == "Category":
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
            self.current_option = st.selectbox("Select table to search data", self.tables)

            if self.current_option == "Customer":
                customer_name = st.text_input("Input customer name: ", value="")
                customer_id = "CUSTOMER-ID-" + hashlib.md5(customer_name.encode()).hexdigest() + "-" + str(uuid1())
                if st.button("Add customer"):
                    check = components.Customer.insert(self.connection, customer_id, customer_name)
                    if check is None:
                        st.error("Error!")
                    else:
                        st.success("Customer was added successfully!")

            elif self.current_option == "Category":
                category_name = st.text_input("Input category name: ", value="")
                category_id = "CATEGORY-ID-" + hashlib.md5(category_name.encode()).hexdigest()
                if st.button("Add category"):
                    check = components.Category.insert(self.connection, category_id, category_name)
                    if check is None:
                        st.error("Error!")
                    else:
                        st.success("Category was added successfully!")

            elif self.current_option == "Buyer":
                buyer_name = st.text_input("Input buyer name: ", value="")
                buyer_id = "BUYER-ID-" + hashlib.md5(buyer_name.encode()).hexdigest()
                if st.button("Add category"):
                    check = components.Category.insert(self.connection, buyer_id, buyer_name)
                    if check is None:
                        st.error("Error!")
                    else:
                        st.success("Buyer was added successfully!")

            elif self.current_option == "Shop":
                shop_name = st.text_input("Input shop name: ", value="")
                shop_id = "SHOP-ID-" + hashlib.md5(shop_name.encode()).hexdigest()
                if st.button("Add category"):
                    check = components.Category.insert(self.connection, shop_id, shop_name)
                    if check is None:
                        st.error("Error!")
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
            self.current_option = st.selectbox("Select table to search data", self.tables)

            if self.current_option == "Customer":
                input_value = st.text_input("Input customer id or name: ", value="")
                if st.button("Remove customer") and input != "":
                    components.Customer.delete_by_id(self.connection, input_value)
                    components.Customer.delete_by_name(self.connection, input_value)


            elif self.current_option == "Category":
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
