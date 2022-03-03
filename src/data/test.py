import psycopg2

con = psycopg2.connect(**config())

print ("Opened database successfully")