import sqlite3 as sq
import csv

db = sq.connect('./13_lab/data_base/toy_db.db')
cur = db.cursor()

columns = []

with open('./13_lab/large_toy_inventory.csv', 'r') as file:
    data = csv.DictReader(file)
    dict_from_csv = dict(list(data)[0])
    columns = list(dict_from_csv.keys())

cur.execute(f'CREATE TABLE toys ({columns})')

