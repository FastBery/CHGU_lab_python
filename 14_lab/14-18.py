import sqlite3 as sq
import csv


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


db.close()