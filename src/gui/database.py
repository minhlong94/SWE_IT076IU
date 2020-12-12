import sqlite3

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
        self.tables = [table[0] for table in self.connection.cursor().execute(
            "SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
        try:
            self.tables.remove("ImportDetail")
            self.tables.remove("TransactionDetail")
        except ValueError:
            pass
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
                customer_name = ''
                choice = st.selectbox("Search by id/name: ", options=['id', 'name'])
                if choice == "id":
                    customer_id = st.number_input("Input customer id: ", min_value=0,
                                                  max_value=Customer.max_id(self.connection), value=0, step=1)
                elif choice == "name":
                    customer_name = st.text_input("Input customer name: ", value=customer_name)
                columns = st.multiselect("Select columns to show: ", self.customer_columns)
                if not columns:
                    columns = self.customer_columns
                if st.button("Search") or customer_name:
                    with st.beta_expander("Show customer with selected column(s)"):
                        if choice == "id":
                            data = Customer.search_by_id(self.connection, customer_id, columns)
                        elif choice == "name":
                            data = Customer.search_by_name(self.connection, customer_name, columns)
                        st.dataframe(pd.DataFrame.from_records(data, columns=columns)[:1000])

            elif self.current_option == "ItemCategory":
                st.info("""
                    Input name to search for category in the database.
                    If there is no input, all entries be shown.\n
                    *Limit to 1000 rows.*
                """)
                category_name = ''
                choice = st.selectbox("Search by id/name: ", options=['id', 'name'])
                if choice == "id":
                    category_id = st.number_input("Input category id: ", min_value=0,
                                                  max_value=ItemCategory.max_id(self.connection), value=0, step=1)
                elif choice == "name":
                    category_name = st.text_input("Input category name: ", value=category_name)
                columns = st.multiselect("Select columns to search: ", self.category_columns)
                if not columns:
                    columns = self.category_columns
                if st.button("Search") or category_name:
                    with st.beta_expander("Show category with selected column(s)"):
                        if choice == "id":
                            data = ItemCategory.search_by_id(self.connection, category_id, columns)
                        elif choice == "name":
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
                shop_name = ''
                choice = st.selectbox("Search by id/name: ", options=['id', 'name'])
                if choice == "id":
                    shop_id = st.number_input("Input shop id: ", min_value=0,
                                              max_value=Shop.max_id(self.connection), value=0, step=1)
                elif choice == "name":
                    shop_name = st.text_input("Input shop name: ", value=shop_name)
                columns = st.multiselect("Select columns to show: ", self.shop_columns)
                if not columns:
                    columns = self.shop_columns
                if st.button("Search") or shop_name:
                    with st.beta_expander("Show shop with selected column(s)"):
                        if choice == "id":
                            data = Shop.search_by_id(self.connection, shop_id, columns)
                        elif choice == "name":
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
                item_name = ''
                choice = st.selectbox("Search by id/name: ", options=['id', 'name', 'category', 'shop'])
                if choice == "id":
                    item_id = st.number_input("Input category id: ", min_value=0,
                                              max_value=Item.max_id(self.connection), value=0, step=1)
                elif choice == "name":
                    item_name = st.text_input("Input item name: ", value=item_name)
                elif choice == "category":
                    category_id = st.number_input("Input category id: ", min_value=0,
                                                  max_value=ItemCategory.max_id(self.connection), value=0, step=1)
                elif choice == "shop":
                    shop_id = st.number_input("Input shop id: ", min_value=0,
                                              max_value=Shop.max_id(self.connection), value=0, step=1)
                columns = st.multiselect("Select columns to show: ", self.item_columns)
                if not columns:
                    columns = self.item_columns
                if st.button("Search") or item_name:
                    with st.beta_expander("Show item with selected column(s)"):
                        if choice == "id":
                            data = Item.search_by_id(self.connection, item_id, columns)
                        elif choice == "name":
                            data = Item.search_by_name(self.connection, item_name, columns)
                        elif choice == "category":
                            data = Item.search_by_category_id(self.connection, category_id, columns)
                        elif choice == "shop":
                            data = Item.search_by_shop_id(self.connection, shop_id, columns)
                        st.dataframe(pd.DataFrame.from_records(data, columns=columns)[:1000])

    def show_add(self):
        with st.beta_container():
            self.current_option = st.selectbox("Select table to add: ", self.tables)

            if self.current_option == "Customer":
                customer_name = st.text_input("Input customer name: ", value="")
                customer_id = Customer.max_id(self.connection) + 1
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
                category_id = ItemCategory.max_id(self.connection) + 1
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
                shop_id = Shop.max_id(self.connection)
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
                item_id = Item.max_id(self.connection)
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
                st.info("""
                    Input id or name to search for customer to remove from the database.
                    If there is no input, all entries be shown.
                    Limit to 1000 rows.
                """)
                choice = st.selectbox("Search by id/name: ", options=['id', 'name'])
                if choice == "id":
                    customer_id = st.number_input("Input customer id: ", min_value=0,
                                                  max_value=Customer.max_id(self.connection), value=0, step=1)
                    data = Customer.search_by_id(self.connection, customer_id)
                elif choice == "name":
                    customer_name = st.text_input("Input customer name: ", value="")
                    data = Customer.search_by_name(self.connection, customer_name)
                df = pd.DataFrame.from_records(data, columns=self.customer_columns)[:1000]
                with st.beta_expander("Show all customers"):
                    st.dataframe(df)
                with st.beta_expander("Remove customer(s)", expanded=True):
                    if choice == "id":
                        selected_ids = [customer_id]
                        data = Customer.search_by_id(self.connection, customer_id)
                        df = pd.DataFrame.from_records(data, columns=self.customer_columns).loc[
                            df["customerID"] == customer_id]
                    elif choice == "name":
                        selected_ids = st.multiselect("Select customer id(s): ", df["customerID"])
                        data = Customer.search_by_name(self.connection, customer_name)
                        try:
                            df = pd.concat([pd.DataFrame.from_records(data, columns=self.customer_columns).loc[
                                                df["customerID"] == i] for i in selected_ids], ignore_index=True)
                        except ValueError:
                            pass
                    st.dataframe(df)
                    if st.button("Remove customer"):
                        for Cid in selected_ids:
                            removed = Customer.delete_by_id(self.connection, Cid)
                            print(removed)
                            st.experimental_rerun()

            elif self.current_option == "ItemCategory":
                st.info("""
                    Input id or name to search for item category to remove from the database.
                    If there is no input, all entries be shown.
                    Limit to 1000 rows.
                """)
                choice = st.selectbox("Search by id/name: ", options=['id', 'name'])
                if choice == "id":
                    category_id = st.number_input("Input category id: ", min_value=0,
                                                  max_value=ItemCategory.max_id(self.connection), value=0, step=1)
                    data = ItemCategory.search_by_id(self.connection, category_id)
                elif choice == "name":
                    category_name = st.text_input("Input category name: ", value="")
                    data = ItemCategory.search_by_name(self.connection, category_name)
                df = pd.DataFrame.from_records(data, columns=self.category_columns)[:1000]
                with st.beta_expander("Show all item categories"):
                    st.dataframe(df)
                with st.beta_expander("Remove item category(s)", expanded=True):
                    if choice == "id":
                        data = ItemCategory.search_by_id(self.connection, category_id)
                        df = pd.DataFrame.from_records(data, columns=self.category_columns).loc[
                            df["categoryID"] == category_id]
                    elif choice == "name":
                        selected_ids = st.multiselect("Select category id(s): ", df["categoryID"])
                        data = ItemCategory.search_by_name(self.connection, category_name)
                        try:
                            df = pd.concat([pd.DataFrame.from_records(data, columns=self.category_columns).loc[
                                                df["categoryID"] == i] for i in selected_ids], ignore_index=True)
                        except ValueError:
                            pass
                    st.dataframe(df)
                    if st.button("Remove customer"):
                        for ICid in selected_ids:
                            removed = ItemCategory.delete_by_id(self.connection, ICid)
                            print(removed)
                            st.experimental_rerun()

            elif self.current_option == "Buyer":
                pass

            elif self.current_option == "Shop":
                st.info("""
                    Input id or name to search for shop to remove from the database.
                    If there is no input, all entries be shown.
                    Limit to 1000 rows.
                """)
                choice = st.selectbox("Search by id/name: ", options=['id', 'name'])
                if choice == "id":
                    shop_id = st.number_input("Input shop id: ", min_value=0,
                                              max_value=Shop.max_id(self.connection), value=0, step=1)
                    data = Shop.search_by_id(self.connection, shop_id)
                elif choice == "name":
                    shop_name = st.text_input("Input shop name: ", value="")
                    data = Shop.search_by_name(self.connection, shop_name)
                df = pd.DataFrame.from_records(data, columns=self.shop_columns)[:1000]
                with st.beta_expander("Show all shops"):
                    st.dataframe(df)
                with st.beta_expander("Remove shop(s)"):
                    if choice == "id":
                        data = Shop.search_by_id(self.connection, shop_id)
                        df = pd.DataFrame.from_records(data, columns=self.shop_columns).loc[
                            df["shopID"] == shop_id]
                    elif choice == "name":
                        selected_ids = st.multiselect("Select shop id(s): ", df["shopID"])
                        data = Shop.search_by_name(self.connection, shop_name)
                        try:
                            df = pd.concat([pd.DataFrame.from_records(data, columns=self.shop_columns).loc[
                                                df["shopID"] == i] for i in selected_ids], ignore_index=True)
                        except ValueError:
                            pass
                    st.dataframe(df)
                    if st.button("Remove customer"):
                        for Cid in selected_ids:
                            removed = Shop.delete_by_id(self.connection, Cid)
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
                    with st.spinner(f"Exporting table '{table}'..."):
                        cursor = self.connection.cursor()
                        cursor.execute(f"SELECT * FROM {table}")
                        with open(f"{export_path}/{table}.csv", "w+", encoding="utf-8", newline="") as csv_file:
                            csv_writer = csv.writer(csv_file, delimiter=",")
                            csv_writer.writerow([i[0] for i in cursor.description])
                            csv_writer.writerows(cursor)
                    st.success(f"Data exported Successfully into {export_path}/{table}.csv")

            except sqlite3.Error as err:
                print(err)
