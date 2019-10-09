# Tyler Huang
# SoftDev1 pd02
# K#17 -- No Trouble
# 2019-10-08

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE = "data.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

command = "CREATE TABLE courses (code TEXT,  mark INTEGER, id INTEGER);" # create table, test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement
with open('courses.csv', 'r') as csvfile: # open csv file
    reader = csv.DictReader(csvfile, delimiter = ",") #convert csv into dictionary with , as delimiter
    reader.__next__() #skip first line
    for line in reader:
        command = "INSERT INTO courses VALUES (\"" + line['code'] + "\"," + line['mark'] + "," + line['id'] + ");" # insert code,mark,id into table, test SQL stmt in sqlite3 shell, save as string
        c.execute(command) # run SQL statement
        #print(line['code'])

command = "CREATE TABLE students (name TEXT,  age INTEGER, id INTEGER);" # create table, test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement
with open('students.csv', 'r') as csvfile: # open csv file
    reader = csv.DictReader(csvfile, delimiter = ",") #convert csv into dictionary with , as delimiter
    reader.__next__() #skip first line
    for line in reader:
        command = "INSERT INTO students VALUES (\"" + line['name'] + "\"," + line['age'] + "," + line['id'] + ");" # insert name,age,id into table, test SQL stmt in sqlite3 shell, save as string
        c.execute(command) # run SQL statement

db.commit() #save changes
db.close()  #close database
