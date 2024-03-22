from faker import Faker
import random
import psycopg2

connection = psycopg2.connect(
    host='localhost',
    port='5432',
    user='postgres',
    password='xo4MK99!ds',
    dbname='helpmatch_makers'
)

cursor = connection.cursor()

def insert_into_volunteers_table(name, email, phone, city, gender, birth_year):
    query = f"""INSERT INTO volunteers(name, email, phone, city, gender, birth_year)
    VALUES ('{name}', '{email}', '{phone}', '{city}', '{gender}', {birth_year});"""
    cursor.execute(query)
    connection.commit()

def insert_into_looking_for_volunteers(name, email, phone, city):
    query = f"""INSERT INTO looking_for_volunteers(name, email, phone, city)
    VALUES ('{name}', '{email}', '{phone}', '{city}');"""
    cursor.execute(query)
    connection.commit()

def insert_fake_volunteers(quantity):
    fake = Faker('en_GB')
    gender_list = ['Male', 'Female', 'Other']
    for number in range(quantity):
        gender = random.choices(gender_list, [9, 9, 2], k=1)[0]
        if gender == 'Male':
            first_name = fake.first_name_male()
        elif gender == 'Female':
            first_name = fake.first_name_female()
        else:
            first_name = fake.first_name()
        last_name = fake.last_name()
        name = f'{first_name} {last_name}'
        email = fake.email()
        phone = fake.phone_number()
        city = fake.city()
        birth_year = random.randint(1944,2008)
        insert_into_volunteers_table(name, email, phone, city, gender, birth_year)

def insert_fake_volunteer_recruiters(quantity):
    fake = Faker('en_GB')
    for number in range(quantity):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        city = fake.city()
        insert_into_looking_for_volunteers(name, email, phone, city)

# insert_fake_volunteer_recruiters(100)
# insert_fake_volunteers(100)


# info
# background info
# tasks
