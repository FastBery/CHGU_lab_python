import sqlite3 as sq
import csv
from tkinter import *

def insert_to_db(table_name, x, y, z, a = None):
    db = sq.connect('./14_lab/data_base/14.db')
    if table_name != 'Tasks':
        cursor = db.cursor()
        if table_name == 'Projects':
            cur.execute(f'INSERT INTO {table_name} (id, name, status) VALUES (?, ?, ?)', (x, y, z)) 
        elif table_name == 'Employees':
            cur.execute(f'INSERT INTO {table_name} (id, name, last_name) VALUES (?, ?, ?)', (x, y, z))
    else:
        cur.execute(f'INSERT INTO {table_name} (id, project_id, employee_id, description) VALUES (?, ?, ?, ?)', (x, y, z, a))
    db.commit()


db = sq.connect('./14_lab/data_base/14.db')
cur = db.cursor()

cur.execute("PRAGMA foreign_keys=ON;") #making foreign_keys=on

#creating tables if not exist
cur.execute('''CREATE TABLE IF NOT EXISTS Projects (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            status TEXT NOT NULL
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Tasks (
            id INTEGER PRIMARY KEY,
            project_id INTEGER NOT NULL,
            employee_id INTEGER NOT NULL,
            description TEXT NULL,
            FOREIGN KEY (project_id) REFERENCES Projects (id) ON DELETE CASCADE,
            FOREIGN KEY (employee_id) REFERENCES Employees (id) ON DELETE CASCADE
            )''')

# cur.execute("PRAGMA foreign_keys=ON;") #making foreign_keys=on

db.commit()

#importing data from files

datafile = open('./14_lab/projects.csv', encoding="utf8")
projects = list(csv.DictReader(datafile, delimiter=','))

datafile = open('./14_lab/employees.csv', encoding="utf8")
employees = list(csv.DictReader(datafile, delimiter=','))

datafile = open('./14_lab/tasks.csv', encoding="utf8")
tasks = list(csv.DictReader(datafile, delimiter=','))

#making tuples from data and then inserting them into tables

projects_tuples = [ (tuple(i.values())) for i in projects]
try:
    # print(projects_tuples)
    cur.executemany('INSERT INTO Projects (id, name, status) VALUES (?, ?, ?)', projects_tuples)
except sq.IntegrityError:
    pass

employees_tuples = [ (tuple(i.values())) for i in employees]
try:
    # print(employees_tuples)
    cur.executemany('INSERT INTO Employees (id, name, last_name) VALUES (?, ?, ?)', employees_tuples)
except sq.IntegrityError:
    pass


tasks_tuples = [ (tuple(i.values())) for i in tasks]
try:
    # print(tasks_tuples)
    cur.executemany('INSERT INTO Tasks (id, project_id, employee_id, description) VALUES (?, ?, ?, ?)', tasks_tuples)
except sq.IntegrityError:
    pass

db.commit()

#checking if everything works

cur.execute('SELECT * FROM Projects')
for i in cur.fetchall():
    print(i)
print('--------------')

cur.execute('SELECT * FROM Employees')
for i in cur.fetchall():
    print(i)
print('--------------')

cur.execute('SELECT * FROM Tasks')
for i in cur.fetchall():
    print(i)
print('--------------')

#Tasks for lab
print("tasks")

cur.execute(''' SELECT Tasks.id, Tasks.description, Projects.name
FROM Tasks
INNER JOIN Employees ON Tasks.employee_id = Employees.id
INNER JOIN Projects ON Tasks.project_id = Projects.id
WHERE Employees.name = 'Olga' AND Employees.last_name = 'Smirnova' ''')
for i in cur.fetchall():
    print(i)
print('--------------')

cur.execute(''' SELECT Projects.name, COUNT(Tasks.id) AS number_of_tasks
FROM Tasks
INNER JOIN Projects ON Tasks.project_id = Projects.id
GROUP BY Projects.name ''')
for i in cur.fetchall():
    print(i)
print('--------------')

#checking delete function

# cur.execute('DELETE FROM Projects WHERE status=\'Completed\'')
# db.commit()

# cur.execute('SELECT * FROM Projects')
# print(cur.fetchall())
# print('--------------')

# cur.execute('SELECT * FROM Employees')
# print(cur.fetchall())
# print('--------------')

# cur.execute('SELECT * FROM Tasks')
# print(cur.fetchall())
# print('--------------')

insert_to_db('Projects', 11, 'Armagedon', 'process')

cur.execute('SELECT * FROM Projects')
for i in cur.fetchall():
    print(i)
print('--------------')

insert_to_db('Employees', 11, 'Kura', 'Kur')
cur.execute('SELECT * FROM Employees')
for i in cur.fetchall():
    print(i)
print('--------------')

insert_to_db('Tasks', 11, 11, 11, 'WTF')
cur.execute('SELECT * FROM Tasks')
for i in cur.fetchall():
    print(i)
print('--------------')

db.close()

# #Making window
# root = Tk()
# root.title('12 lab (18)')

# #Configuring window size
# window_width = 400
# window_height = 500

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# center_x = int(screen_width/2 - window_width / 2)
# center_y = int(screen_height/2 - window_height / 2)

# root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# root.resizable(True, True)

# root.mainloop()
