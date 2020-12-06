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

cur.execute('''DROP TABLE IF EXISTS Category''')
cur.execute('''CREATE TABLE Category
(
  categoryID VARCHAR(50) NOT NULL,
  categoryName VARCHAR(500) NOT NULL,
  PRIMARY KEY (categoryID)
)''')

cur.execute('''DROP TABLE IF EXISTS Buyer''')
cur.execute('''CREATE TABLE Buyer
(
  buyerID VARCHAR(50) NOT NULL,
  buyerName VARCHAR(500) NOT NULL,
  PRIMARY KEY (buyerID)
)''')

cur.execute('''DROP TABLE IF EXISTS Inventory''')
cur.execute('''CREATE TABLE Inventory
(
  inventoryID VARCHAR(50) NOT NULL,
  inventoryName VARCHAR(500) NOT NULL,
  PRIMARY KEY (inventoryID)
)''')

cur.execute('''DROP TABLE IF EXISTS Imports''')
cur.execute('''CREATE TABLE Imports
(
  importDate DATE NOT NULL,
  importID VARCHAR(50) NOT NULL,
  inventoryID VARCHAR(50) NOT NULL,
  buyerID VARCHAR(50) NOT NULL,
  PRIMARY KEY (importID),
  FOREIGN KEY (inventoryID) REFERENCES Inventory(inventoryID),
  FOREIGN KEY (buyerID) REFERENCES Buyer(buyerID)
)''')

cur.execute('''DROP TABLE IF EXISTS Transactions''')
cur.execute('''CREATE TABLE Transactions
(
  transactionID VARCHAR(50) NOT NULL,
  createDate DATE NOT NULL,
  transactionStatus VARCHAR(20) NOT NULL,
  customerID VARCHAR(50) NOT NULL,
  inventoryID VARCHAR(50) NOT NULL,
  PRIMARY KEY (transactionID),
  FOREIGN KEY (customerID) REFERENCES Customer(customerID),
  FOREIGN KEY (inventoryID) REFERENCES Inventory(inventoryID)
)''')

cur.execute('''DROP TABLE IF EXISTS Item''')
cur.execute('''CREATE TABLE Item
(
  itemName VARCHAR(500) NOT NULL,
  itemID VARCHAR(50) NOT NULL,
  quantity INT NOT NULL,
  categoryID VARCHAR(50) NOT NULL,
  inventoryID VARCHAR(50) NOT NULL,
  PRIMARY KEY (itemID),
  FOREIGN KEY (categoryID) REFERENCES Category(categoryID),
  FOREIGN KEY (inventoryID) REFERENCES Inventory(inventoryID)
)''')

cur.execute('''DROP TABLE IF EXISTS TransactionsDetail''')
cur.execute('''CREATE TABLE TransactionsDetail
(
  transactionAmount INT NOT NULL,
  transactionID VARCHAR(50) NOT NULL,
  itemID VARCHAR(50) NOT NULL,
  PRIMARY KEY (transactionID),
  FOREIGN KEY (transactionID) REFERENCES Transactions(transactionID),
  FOREIGN KEY (itemID) REFERENCES Item(itemID)
)''')

cur.execute('''DROP TABLE IF EXISTS ImportsDetail''')
cur.execute('''CREATE TABLE ImportsDetail
(
  importAmount INT NOT NULL,
  itemID VARCHAR(50) NOT NULL,
  importID VARCHAR(50) NOT NULL,
  PRIMARY KEY (itemID, importID),
  FOREIGN KEY (itemID) REFERENCES Item(itemID),
  FOREIGN KEY (importID) REFERENCES Imports(importID)
)''')

con.commit()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())