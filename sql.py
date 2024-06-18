import sqlite3

## Connect to sqlite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table and retrieve
cursor = connection.cursor()

## Create a table
table_info ="""
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), 
SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

## Insert Some More records

cursor.execute('''Insert into STUDENT values ('Krishan', 'Data Science', 'A', 90)''')
cursor.execute('''Insert into STUDENT values ('Arun', 'Data Science', 'B', 70)''')
cursor.execute('''Insert into STUDENT values ('Dhadi', 'Data Science', 'A', 100)''')
cursor.execute('''Insert into STUDENT values ('Manoj', 'DEVOPS', 'A', 75)''')
cursor.execute('''Insert into STUDENT values ('Giri', 'DEVOPS', 'B', 40)''')

## Display all the records
print("The Inserted Records are")

data = cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)

## Close the connection

connection.commit()
connection.close()