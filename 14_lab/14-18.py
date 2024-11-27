import sqlite3 as sq
import csv
from tkinter import *


#functions for data base
def insert_to_db(table_name, y, z, a = None):
    db = sq.connect('./14_lab/data_base/14.db')
    cur = db.cursor()
    if table_name != 'Tasks':
        if table_name == 'Projects':
            cur.execute(f'INSERT OR IGNORE INTO {table_name} (name, status) VALUES (?, ?)', (y, z)) 
        elif table_name == 'Employees':
            cur.execute(f'INSERT OR IGNORE INTO {table_name} (name, last_name) VALUES (?, ?)', (y, z))
    else:
        cur.execute(f'INSERT OR IGNORE INTO {table_name} (project_id, employee_id, description) VALUES (?, ?, ?)', (y, z, a))
    db.commit()
    db.close()

def search_tasks_for_employees(name, last_name):
    db = sq.connect('./14_lab/data_base/14.db')
    cur = db.cursor()
    cur.execute(f''' SELECT Tasks.id, Tasks.description, Projects.name
    FROM Tasks
    INNER JOIN Employees ON Tasks.employee_id = Employees.id
    INNER JOIN Projects ON Tasks.project_id = Projects.id
    WHERE Employees.name = (?) AND Employees.last_name = (?) ''', (name, last_name))
    result = list(cur.fetchall())
    db.close()
    return result

def tasks_amount_for_project():
    db = sq.connect('./14_lab/data_base/14.db')
    cur = db.cursor()
    cur.execute(''' SELECT Projects.name, COUNT(Tasks.id) AS number_of_tasks
    FROM Tasks
    INNER JOIN Projects ON Tasks.project_id = Projects.id
    GROUP BY Projects.name ''')
    result = list(cur.fetchall())
    db.close()
    return result

def get_project_list():
    db = sq.connect('./14_lab/data_base/14.db')
    cur = db.cursor()
    cur.execute(''' SELECT name, status
    FROM Projects''')
    result = list(cur.fetchall())
    return result


def insert_tkinter():
    x = ent_id_1.get()
    y = ent_id_2.get()
    z = ent_id_3.get()
    insert_to_db(x, y, z)
    ent_id_1.delete(0, END)
    ent_id_2.delete(0, END)
    ent_id_3.delete(0, END)


#data base begin
db = sq.connect('./14_lab/data_base/14.db')
cur = db.cursor()
cur.execute("PRAGMA foreign_keys=ON;") #making foreign_keys=on


#creating tables if not exist
cur.execute('''CREATE TABLE IF NOT EXISTS Projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            status TEXT NOT NULL,
            UNIQUE(name, status)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            UNIQUE(name, last_name)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            employee_id INTEGER NOT NULL,
            description TEXT NULL,
            FOREIGN KEY (project_id) REFERENCES Projects (id) ON DELETE CASCADE,
            FOREIGN KEY (employee_id) REFERENCES Employees (id) ON DELETE CASCADE,
            UNIQUE(project_id, employee_id)
            )''')

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


#Making window
root = Tk()
root.title('12 lab (18)')

#Configuring window size
window_width = 400
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(True, True)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# def insert_tkinter():
#     x = ent_id_1.get()
#     y = ent_id_2.get()
#     z = ent_id_3.get()
#     insert_to_db(x, y, z)

Label(root, text='Table').grid(row=0)
Label(root, text='Name:').grid(row=1)
Label(root, text='Status:').grid(row=2)

ent_id_1 = Entry(root)
ent_id_1.grid(row=0, column=1)

ent_id_2 = Entry(root)
ent_id_2.grid(row=1, column=1)

ent_id_3 = Entry(root)
ent_id_3.grid(row=2, column=1)

Button(root, text='insert to db', command=insert_tkinter).grid(row=1, column=2)

for i in get_project_list():
    print(i)

root.mainloop()
db.close()