import streamlit as st
from src.gui.main_page import MainPage
from src.gui.menu import Menu
import bcrypt
import time

def main():
    with open("src/encryption/hash_pw.txt", "rb") as f:
        hashed_password = f.read()
        f.close()

    main_page = MainPage()
    main_page.call()
    st.sidebar.title("Login section")
    input_password = st.sidebar.text_input("Input administrator password: ", type="password", value="")
    st.sidebar.write("Note: this is a collapsible sidebar.")

    while not bcrypt.checkpw(input_password.encode("utf8"), hashed_password):
        st.sidebar.warning("Wrong password!")
        st.stop()
    else:
        st.sidebar.success("Login successful")
        main_page.clear()
        menu = Menu()
        menu.display_option()


if __name__ == "__main__":
    main()
