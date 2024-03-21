import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    port = '5432',
    user = 'postgres',
    password = 'xo4MK99!ds',
)

cursor = connection.cursor()
connection.autocommit = True

cursor.execute("""DROP DATABASE if exists HelpMatch_Makers;""")
cursor.execute("""CREATE DATABASE HelpMatch_Makers;""")

cursor.close()
connection.close()