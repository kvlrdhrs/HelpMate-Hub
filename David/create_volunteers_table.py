import psycopg2

connection = psycopg2.connect(
    host='localhost',
    port='5432',
    user='postgres',
    password='xo4MK99!ds',
    dbname='helpmatch_makers'
)

cursor = connection.cursor()
connection.autocommit = True

cursor.execute("""DROP TABLE if exists volunteers""")
create_table = """
    CREATE TABLE volunteers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    city VARCHAR(100) NOT NULL,
    gender VARCHAR(20),
    birth_year SMALLINT,
    info TEXT
    )
"""
cursor.execute(create_table)

cursor.close()
connection.close()