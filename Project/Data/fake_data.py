import psycopg2
from faker import Faker

# Establish a connection to the database
conn = psycopg2.connect(
    host = '127.0.0.1',
    port = '5432',
    user = 'postgres',
    password = '232323',
    dbname = 'helpmatch_maker'
)

# Create a cursor object
cursor = conn.cursor()

# Set the connection to automatically commit transactions
conn.autocommit = True

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
    gender = fake.random_element(elements=('Male', 'Female', 'Other'))
    age = fake.random_int(min=18, max=90)
    info = fake.text(max_nb_chars=200)
    background_info = fake.text(max_nb_chars=200)
    tasks = fake.text(max_nb_chars=200)
    
    cursor.execute(
        """
        INSERT INTO looking_for_volunteers (name, email, phone, city, tasks)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (name, email, phone, city, tasks)
    )

    cursor.execute(
        """
        INSERT INTO volunteers (name, email, phone, city, gender, age, info)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (name, email, phone, city, gender, age, info)
    )


# Close the connection
cursor.close()
conn.close()
