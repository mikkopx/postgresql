import psycopg2
from config import config

def connect():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        select_all(cursor)
        #column_names(cursor)
        #add_certificate(cursor, "AZ-105")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def select_all(cursor):
    SQL = 'SELECT * FROM certificates;'
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

def add_certificate(cursor, cert_name):
    SQL = "INSERT INTO certificates (name) VALUES ('{cert_name}');"
    cursor.execute(SQL)
    print ("Records created successfully");

if __name__ == '__main__':
    connect()