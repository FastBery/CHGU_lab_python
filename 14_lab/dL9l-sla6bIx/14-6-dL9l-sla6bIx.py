import sqlite3 as sq
import csv

#data base begin
db = sq.connect('./lab_14/data_base/14.db')
cur = db.cursor()
cur.execute("PRAGMA foreign_keys=ON;") #making foreign_keys=on


#creating tables if not exist
cur.execute('''CREATE TABLE IF NOT EXISTS Candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Vacancies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vacancy_id INTEGER NOT NULL,
            candidate_id INTEGER NOT NULL,
            FOREIGN KEY (candidate_id) REFERENCES Candidates (id) ON DELETE CASCADE,
            FOREIGN KEY (vacancy_id) REFERENCES Vacancies (id) ON DELETE CASCADE
            )''')

db.commit()


#importing data from files
datafile = open('./lab_14/applications.csv', encoding="utf8")
applications = list(csv.DictReader(datafile, delimiter=','))
print(applications)

datafile = open('./lab_14/candidates.csv', encoding="utf8")
candidates = list(csv.DictReader(datafile, delimiter=','))

datafile = open('./lab_14/vacancies.csv', encoding="utf8")
vacancies = list(csv.DictReader(datafile, delimiter=','))
# print(vacancies)


#making tuples from data and then inserting them into tables

# candidates_tuples = [ (tuple(i.values())) for i in candidates]
# cur.executemany('INSERT INTO Candidates (id, name, surname) VALUES (?, ?, ?)', candidates_tuples)


# vacancies_tuples = [ (tuple(i.values())) for i in vacancies]
# cur.executemany('INSERT INTO Vacancies (id, name) VALUES (?, ?)', vacancies_tuples)

# applications_tuples = [ (tuple(i.values())) for i in applications]
# cur.executemany('INSERT INTO  Applications (id, vacancy_id, candidate_id) VALUES (?, ?, ?)', applications_tuples)


query_1 = """
SELECT 
    Candidates.name,
    Candidates.surname,
    Vacancies.name AS vacancy
FROM 
    Applications
JOIN
    Candidates ON Applications.candidate_id = Candidates.id
JOIN 
    Vacancies ON Applications.vacancy_id = Vacancies.id ;
"""
cur.execute(query_1)
result_1 = cur.fetchall()
print("List of candidates and applications submitted by them:")
for row in result_1:
    print(row)


candidate_id = 1
query_2 = """
SELECT 
    Vacancies.name AS vacancy
FROM 
    Applications
JOIN 
    Vacancies ON Applications.vacancy_id = Vacancies.id
WHERE 
    Applications.candidate_id = (?)
"""
cur.execute(query_2, (candidate_id,))
result_2 = cur.fetchall()
print(f"\Vacancies submitted by candidate with ID {candidate_id}:")
for row in result_2:
    print(row)


query_3 = """
SELECT 
    Vacancies.name AS vacancy, 
    COUNT(Applications.id) AS num
FROM 
    Vacancies
LEFT JOIN 
    Applications ON Vacancies.id = Applications.vacancy_id
GROUP BY 
    Vacancies.id;
"""
cur.execute(query_3)
result_3 = cur.fetchall()
print("Number of applications for each vacancy:")
for row in result_3:
    print(row)


db.commit()

db.close()
