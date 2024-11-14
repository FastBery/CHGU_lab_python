import sqlite3 as sq
import pandas as pd

db = sq.connect('./13_lab/data_base/toy_inventory.db')
# cursor = db.cursor()
# cursor.execute("CREATE TABLE toys ()")

toy_data = pd.read_csv('./13_lab/large_toy_inventory.csv')

toy_data.to_sql('Toys', db, if_exists='replace', index=False)

cur = db.cursor()

n = 0

for i in cur.execute('SELECT * FROM Toys WHERE Manufacturer=\'Lego\''):
    n += 1
    print(i)
    if n == 10:
        break


db.close()