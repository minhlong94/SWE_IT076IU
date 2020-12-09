def create_database(db_file="src/database/database.db"):
    import os.path

    if not os.path.exists(db_file):
        with open(db_file, 'w+'):
            pass

        import sqlite3

        con = sqlite3.connect("database.db")
        cur = con.cursor()

        cur.execute('''DROP TABLE IF EXISTS Customer''')
        cur.execute('''CREATE TABLE Customer
        (
          customerID VARCHAR(50) NOT NULL,
          customerName VARCHAR(500) NOT NULL,
          PRIMARY KEY (customerID)
        )''')

        cur.execute('''DROP TABLE IF EXISTS ItemCategory''')
        cur.execute('''CREATE TABLE ItemCategory
        (
          categoryID VARCHAR(50) NOT NULL,
          categoryName VARCHAR(500) NOT NULL,
          PRIMARY KEY (categoryID)
        )''')

        # cur.execute('''DROP TABLE IF EXISTS Buyer''')
        # cur.execute('''CREATE TABLE Buyer
        # (
        #   buyerID VARCHAR(50) NOT NULL,
        #   buyerName VARCHAR(500) NOT NULL,
        #   PRIMARY KEY (buyerID)
        # )''')

        cur.execute('''DROP TABLE IF EXISTS Shop''')
        cur.execute('''CREATE TABLE Shop
        (
          shopID VARCHAR(50) NOT NULL,
          shopName VARCHAR(500) NOT NULL,
          PRIMARY KEY (shopID)
        )''')

        cur.execute('''DROP TABLE IF EXISTS Imports''')
        cur.execute('''CREATE TABLE Imports
        (
          importID VARCHAR(50) NOT NULL,
          importDate DATETIME NOT NULL,
          shopID VARCHAR(50) NOT NULL,
          PRIMARY KEY (importID),
          FOREIGN KEY (shopID) REFERENCES Shop(shopID)
        )''')

        cur.execute('''DROP TABLE IF EXISTS Transactions''')
        cur.execute('''CREATE TABLE Transactions
        (
          transactionID VARCHAR(50) NOT NULL,
          transactionDate DATETIME NOT NULL,
          transactionStatus VARCHAR(20) NOT NULL,
          customerID VARCHAR(50) NOT NULL,
          shopID VARCHAR(50) NOT NULL,
          PRIMARY KEY (transactionID),
          FOREIGN KEY (customerID) REFERENCES Customer(customerID),
          FOREIGN KEY (shopID) REFERENCES Shop(shopID)
        )''')

        cur.execute('''DROP TABLE IF EXISTS Item''')
        cur.execute('''CREATE TABLE Item
        (
          itemID VARCHAR(50) NOT NULL,
          itemName VARCHAR(500) NOT NULL,
          quantity INT NOT NULL,
          categoryID VARCHAR(50) NOT NULL,
          shopID VARCHAR(50) NOT NULL,
          PRIMARY KEY (itemID),
          FOREIGN KEY (categoryID) REFERENCES ItemCategory(categoryID),
          FOREIGN KEY (shopID) REFERENCES Shop(shopID)
        )''')

        cur.execute('''DROP TABLE IF EXISTS TransactionDetail''')
        cur.execute('''CREATE TABLE TransactionDetail
        (
          transactionID VARCHAR(50) NOT NULL,
          itemID VARCHAR(50) NOT NULL,
          transactionAmount INT NOT NULL,
          PRIMARY KEY (transactionID),
          FOREIGN KEY (transactionID) REFERENCES Transactions(transactionID),
          FOREIGN KEY (itemID) REFERENCES Item(itemID)
        )''')

        cur.execute('''DROP TABLE IF EXISTS ImportDetail''')
        cur.execute('''CREATE TABLE ImportDetail
        (
          importID VARCHAR(50) NOT NULL,
          itemID VARCHAR(50) NOT NULL,
          importAmount INT NOT NULL,
          PRIMARY KEY (itemID, importID),
          FOREIGN KEY (importID) REFERENCES Imports(importID),
          FOREIGN KEY (itemID) REFERENCES Item(itemID)
        )''')

        con.commit()

        tables = [table[0] for table in con.cursor().execute(
            "SELECT name FROM sqlite_master WHERE type='table';").fetchall()]

        import streamlit

        streamlit.write(f"database created with tables {tables}")

        con.close()
