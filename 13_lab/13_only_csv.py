import sqlite3 as sq
import csv

db = sq.connect('./13_lab/data_base/toy_db.db')
cur = db.cursor()

columns = []

with open('./13_lab/large_toy_inventory.csv', 'r') as file:
    data = csv.DictReader(file)
    dict_from_csv = dict(list(data)[0])
    columns = list(dict_from_csv.keys())

cur.execute(f'CREATE TABLE IF NOT EXISTS toys (SKU,Toy_Name, Price, Quantity,Age_Range, Manufacturer)')

print(columns)

with open('./13_lab/large_toy_inventory.csv', 'r') as file:
    dr = csv.DictReader(file)
    to_db = [(i['SKU'], i['Toy_Name'], i['Price'],i['Quantity'], i['Age_Range'],i['Manufacturer']) for i in dr]

cur.executemany("INSERT INTO toys (SKU, Toy_Name, Price, Quantity,Age_Range, Manufacturer) VALUES (?, ?, ?, ?, ?, ?);", to_db)

n = 0
for i in cur.execute('SELECT * FROM toys WHERE Manufacturer=\'ToyLand\''):
    n += 1
    print(i)
    if n == 1000:
        break

db.commit()
db.close() 

# 'SKU', 'Toy Name', 'Price', 'Quantity', 'Age Range', 'Manufacturer'
