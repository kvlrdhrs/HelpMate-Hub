import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    port = '5432',
    user = 'postgres',
    password = '232323',
)

cursor = connection.cursor()
connection.autocommit = True

cursor.execute("""DROP DATABASE if exists help_mm;""")
cursor.execute("""CREATE DATABASE help_mm;""")

cursor.close()
connection.close()