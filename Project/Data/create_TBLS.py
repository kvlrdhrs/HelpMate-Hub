import psycopg2
import faker

connection = psycopg2.connect(
    host='localhost',
    port='5432',
    user='postgres',
    password='232323',
    dbname='helpmatch_maker'
)

cursor = connection.cursor()
connection.autocommit = True

cursor.execute("""DROP TABLE if exists looking_for_volunteers""")
create_table = """
    CREATE TABLE looking_for_volunteers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    age SMALLINT,
    info TEXT
    )
"""
cursor.execute(create_table)

cursor.execute("""DROP TABLE if exists volunteers""")
create_table2 = """
    CREATE TABLE volunteers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    age SMALLINT,
    info TEXT
    )
"""
cursor.execute(create_table2)

cursor.close()
connection.close()