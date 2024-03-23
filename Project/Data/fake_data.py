import psycopg2
from faker import Faker

# Establish a connection to the database
connection = psycopg2.connect(
    host='localhost',
    port='5432',
    user='postgres',
    password='232323',
    dbname='helpmatch_maker'
)

# Create a cursor object
cursor = connection.cursor()

# Set the connection to automatically commit transactions
connection.autocommit = True

# Create an instance of Faker
fake = Faker()

# Define the number of records we want to generate
num_records = 500

# Generate and insert data
for _ in range(num_records):
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    city = fake.city()
    age = fake.random_int(min=18, max=90)
    info = fake.text(max_nb_chars=200)
    
    cursor.execute(
        """
        INSERT INTO looking_for_volunteers (name, email, phone, city, age, info)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (name, email, phone, city, age, info)
    )

    cursor.execute(
        """
        INSERT INTO volunteers (name, email, phone, city, age, info)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (name, email, phone, city, age, info)
    )


# Close the connection
cursor.close()
connection.close()
