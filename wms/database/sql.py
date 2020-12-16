import os
import sqlite3
import sys


def create_database(db_file, csv_zip=None):

    if not os.path.exists(db_file):
        with open(db_file, 'x'):
            pass

        con = None
        try:
            con = sqlite3.connect(db_file)
            cur = con.cursor()

            cur.execute('''DROP TABLE IF EXISTS Customer''')
            cur.execute('''CREATE TABLE Customer
                    (
                      customerID MEDIUMINT NOT NULL CHECK (customerID >= 0),
                      customerName VARCHAR(500) NOT NULL,
                      PRIMARY KEY (customerID)
                    )''')

            cur.execute('''DROP TABLE IF EXISTS ItemCategory''')
            cur.execute('''CREATE TABLE ItemCategory
                    (
                      categoryID MEDIUMINT NOT NULL CHECK (categoryID >= 0),
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
                      shopID MEDIUMINT NOT NULL CHECK (shopID >= 0),
                      shopName VARCHAR(500) NOT NULL,
                      PRIMARY KEY (shopID)
                    )''')

            cur.execute('''DROP TABLE IF EXISTS Imports''')
            cur.execute('''CREATE TABLE Imports
                    (
                      importID MEDIUMINT NOT NULL CHECK (importID >= 0),
                      importDate DATETIME NOT NULL,
                      shopID MEDIUMINT NOT NULL CHECK (shopID >= 0),
                      PRIMARY KEY (importID),
                      FOREIGN KEY (shopID) REFERENCES Shop(shopID)
                    )''')

            cur.execute('''DROP TABLE IF EXISTS Transactions''')
            cur.execute('''CREATE TABLE Transactions
                    (
                      transactionID MEDIUMINT NOT NULL CHECK (transactionID >= 0),
                      transactionDate DATETIME NOT NULL,
                      transactionStatus VARCHAR(20) NOT NULL,
                      customerID MEDIUMINT NOT NULL CHECK (customerID >= 0),
                      shopID MEDIUMINT NOT NULL CHECK (shopID >= 0),
                      PRIMARY KEY (transactionID),
                      FOREIGN KEY (customerID) REFERENCES Customer(customerID),
                      FOREIGN KEY (shopID) REFERENCES Shop(shopID)
                    )''')

            cur.execute('''DROP TABLE IF EXISTS Item''')
            cur.execute('''CREATE TABLE Item
                    (
                      itemID MEDIUMINT NOT NULL CHECK (itemID >= 0),
                      itemName VARCHAR(500) NOT NULL,
                      quantity INT NOT NULL DEFAULT 0 CHECK (quantity >= 0),
                      categoryID MEDIUMINT NOT NULL,
                      shopID MEDIUMINT NOT NULL CHECK (shopID >= 0),
                      PRIMARY KEY (itemID),
                      FOREIGN KEY (categoryID) REFERENCES ItemCategory(categoryID),
                      FOREIGN KEY (shopID) REFERENCES Shop(shopID)
                    )''')

            cur.execute('''DROP TABLE IF EXISTS TransactionDetail''')
            cur.execute('''CREATE TABLE TransactionDetail
                    (
                      transactionID MEDIUMINT NOT NULL CHECK (transactionID >= 0),
                      itemID MEDIUMINT NOT NULL CHECK (itemID >= 0),
                      itemPrice DOUBLE NOT NULL,
                      transactionAmount TINYINT NOT NULL CHECK (transactionAmount > 0),
                      PRIMARY KEY (transactionID),
                      FOREIGN KEY (transactionID) REFERENCES Transactions(transactionID),
                      FOREIGN KEY (itemID) REFERENCES Item(itemID)
                    )''')

            cur.execute('''DROP TABLE IF EXISTS ImportDetail''')
            cur.execute('''CREATE TABLE ImportDetail
                    (
                      importID MEDIUMINT NOT NULL CHECK (importID >= 0),
                      itemID MEDIUMINT NOT NULL CHECK (itemID >= 0),
                      importAmount SMALLINT NOT NULL CHECK (importAmount > 0),
                      PRIMARY KEY (itemID, importID),
                      FOREIGN KEY (importID) REFERENCES Imports(importID),
                      FOREIGN KEY (itemID) REFERENCES Item(itemID)
                    )''')

            con.commit()
            cur.close()

            if csv_zip:
                _import_from_csv(con, csv_zip)

        except sqlite3.Error as e:
            sys.exit(e)

        finally:
            con.close()


def _import_from_csv(connection, csv_zip_path):
    import pandas
    import zipfile

    try:
        with zipfile.ZipFile(csv_zip_path) as zf:
            csv_files = [f for f in zf.namelist()]

            for file in csv_files:
                table_name = os.path.splitext(file)[0]
                df = pandas.read_csv(zf.open(file), sep=",", skipinitialspace=True)
                df.to_sql(name=table_name, con=connection, if_exists="append", index=False)

    except ValueError as e:
        sys.exit(e)


def create_connection(db_file, csv_zip):
    create_database(db_file, csv_zip)

    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as err:
        print(err)
    return connection
