import psycopg2

connection = psycopg2.connect(
    host = '127.0.0.1',
    port = '5432',
    user = 'postgres',
    password = '232323',
    dbname = 'helpmatch_maker'
)

cursor=connection.cursor()
connection.autocommit=True

# creating menu to insert, delete, update
class Menu():
    def __init__(self, name, email, phone, city, age, info):
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city
        self.age = age
        self.info = info

    def insert(self, table_name):
        cursor.execute(f"""
        INSERT INTO {table_name} (name, email, phone, city, age, info)
        VALUES (%s, %s, %s, %s, %s, %s)""",
        (self.name, self.email, self.phone, self.city, self.age, self.info)
        )




cursor.close()
connection.close()