import sqlite3 as sq
import csv
from tkinter import *
from tkinter import ttk


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

def select_for_table(table_name):
    db = sq.connect('./14_lab/data_base/14.db')
    cur = db.cursor()
    cur.execute(f'SELECT * FROM {table_name}')
    result = cur.fetchall()
    db.close()
    return result


#insert function for tkinter GUI
def insert_tkinter():
    x = table_choose_insert.get()
    if x == '':
        error = Label(frame_insert, text="Choose table")
        error.grid(row=2, column=2)
        root.after(1500, lambda: error.destroy())
        return
    y = ent_id_1.get()
    z = ent_id_2.get()
    if y == '' or z == '':
        error = Label(frame_insert, text="Fill all fields!")
        error.grid(row=2, column=2)
        root.after(1500, lambda: error.destroy())
        return
    insert_to_db(x, y, z)
    table_choose_insert.delete(0, END)
    ent_id_1.delete(0, END)
    ent_id_2.delete(0, END)
    done = Label(frame_insert, text="Done")
    done.grid(row=2, column=2)
    root.after(1500, lambda: done.destroy())


#get data from table
def get_data_from_table():
    table_name = table_choose_select.get()
    table_choose_select.delete(0, END)
    if table_name == '':
        error = Label(frame_group_tasks, text="Choose table")
        error.grid(row=1, column=2)
        root.after(1500, lambda: error.destroy())
        return
    with open(f'./14_lab/data_from_table_{table_name}', 'w') as file:
        data = select_for_table(table_name)
        file.writelines(str(i) + '\n' for i in data)
        done = Label(frame_group_tasks, text="Done")
        done.grid(row=2, column=2)
        root.after(1500, lambda: done.destroy())
    

#get employee's tasks
def employee_tasks():
    name = ent_name.get()
    last_name = ent_last_name.get()
    data = search_tasks_for_employees(name, last_name)
    if len(data) == 0:
        error = Label(frame_employee, text="Employee doesn't exist")
        error.grid(row=2, column=2)
        root.after(1500, lambda: error.destroy())
        return
    else:
        with open(f'./14_lab/{last_name}_{name}_tasks', 'w') as file:
            file.writelines(str(i) + '\n' for i in data)
            done = Label(frame_employee, text="Done")
            done.grid(row=2, column=2)
            root.after(1500, lambda: done.destroy())
    ent_name.delete(0, END)
    ent_last_name.delete(0, END)


def delete_project():
    parameter = table_choose_delete.get()
    x = ent_status.get()
    db = sq.connect('./14_lab/data_base/14.db')
    cur = db.cursor()
    if parameter == '':
        done = Label(frame_delete, text="Choose parameter")
        done.grid(row=3, column=1)
        root.after(1500, lambda: done.destroy())
        return
    if parameter == 'Status':
        cur.execute(f'DELETE FROM Projects WHERE status=\'{x}\'')
    else:
        cur.execute(f'DELETE FROM Projects WHERE name=\'{x}\'')
    db.commit()
    db.close()
    done = Label(frame_delete, text="Done")
    done.grid(row=3, column=1)
    root.after(1500, lambda: done.destroy())


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
root.title('14 lab (18)')


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


#Insert 
frame_insert = Frame(root)
frame_insert.pack(padx=20, pady=20)

Label(frame_insert, text='Table').grid(row=0)
Label(frame_insert, text='Name:').grid(row=1)
Label(frame_insert, text='Status/\nLast name:').grid(row=2)

#selector for insert
insert_n = StringVar()
table_choose_insert = ttk.Combobox(frame_insert, textvariable = insert_n)
table_choose_insert['values'] = ('Projects', 'Employees', 'Tasks')
table_choose_insert.current()
table_choose_insert.grid(row=0, column=1)

ent_id_1 = Entry(frame_insert)
ent_id_1.grid(row=1, column=1)

ent_id_2 = Entry(frame_insert)
ent_id_2.grid(row=2, column=1)

Button(frame_insert, text='insert to db', command=insert_tkinter).grid(row=1, column=2)


#get data from tables                             Dedokov loshara
frame_group_tasks = Frame(root)
frame_group_tasks.pack(padx=20, pady=20)

Label(frame_group_tasks, text='Table').grid(row=0)


#selecter
table_n = StringVar()
table_choose_select = ttk.Combobox(frame_group_tasks, textvariable = table_n)
table_choose_select['values'] = ('Projects', 'Employees', 'Tasks')
table_choose_select.current()
table_choose_select.grid(row=0, column=1, padx=10)

Button(frame_group_tasks, text="Get table data", command=get_data_from_table).grid(row=0, column=2)


#Select employee by name and last name
frame_employee = Frame(root)
frame_employee.pack(padx=20, pady=20)

Label(frame_employee, text='Name:').grid(row=0)
Label(frame_employee, text='Last name:').grid(row=1)

ent_name = Entry(frame_employee)
ent_name.grid(row=0, column=1)

ent_last_name = Entry(frame_employee)
ent_last_name.grid(row=1, column=1)

Button(frame_employee, text="Find employee's tasks", command=employee_tasks).grid(row=0, column=2, rowspan=2)


#delete project
frame_delete = Frame(root)
frame_delete.pack(padx=20, pady=20)

Label(frame_delete, text='Delete project:').grid(row=0, columnspan=2)

delete_n = StringVar()

table_choose_delete = ttk.Combobox(frame_delete, textvariable = delete_n)
table_choose_delete['values'] = ('Status', 'Project name')
table_choose_delete.current()
table_choose_delete.grid(row=1, columnspan=2, column=0)

ent_status = Entry(frame_delete)
ent_status.grid(row=2, column=0)

Button(frame_delete, text="Delete project", command=delete_project).grid(row=2, column=1)


cur.execute('SELECT * FROM Projects')
for i in cur.fetchall():
    print(i)
print('--------------')

root.mainloop()
db.close()