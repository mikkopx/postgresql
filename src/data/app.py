import psycopg2
from config import config

def menu():
    print("DATABASEAPP")

def connect():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()

        while True:

            if valinta == 1:
                select_all(cursor)
                break

            if valinta == 2:
                column_names(cursor)
                break

            if valinta == 3:
                name = input("Name: ")
                age = int(input("Age: "))
                while True:
                    print("Student? ")
                    syote = input("[T]rue or [F]alse: ")
                    if syote == "T":
                        student = True
                        break
                    if syote == "F":
                        student = False
                        break
                insert(name, age, student, cursor)
                break

            if valinta == 4:
                syote = int(input("ID: "))
                deleteperson(syote, cursor)
                break

            if valinta == 5:
                break

        con.commit()
        cursor.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def select_all(cursor):
    SQL = 'SELECT * FROM person;'
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def column_names(cursor):
    SQL = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'person';" 
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def insert(name, age, student, cursor):
    SQL = "INSERT INTO person (name, age, student) VALUES (%s, %s, %s);"
    data = (f"{name}", age, student)
    cursor.execute(SQL, data)

def insertperson(name, age, student, cursor):
    SQL = "INSERT INTO person (name, age, student) VALUES (%s, %s, %s);"
    data = (f"{name}", age, student)
    cursor.execute(SQL, data)

def updateperson(age, id, cursor):
    SQL = "UPDATE person SET age = %s WHERE id = %s;"
    data = (age, id)
    cursor.execute(SQL, data)

def deleteperson(id, cursor):
    SQL = "DELETE FROM person WHERE id = %s;"
    data = (id,)
    cursor.execute(SQL, data)

valinta = 0
menu()

while True:
    valinta = int(input("1.SELECT ALL 2.COLUMN NAMES 3.INSERT 4.DELETE 5.QUIT "))
    if valinta == 5:
        print("Bye :)")
        break
    else:
        connect()