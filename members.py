# import psycopg2

# db_params = {
#     "host": 'localhost',
#     "user": 'postgres',
#     "password": 'xo4MK99!ds',
#     "port": '5432',
#     "dbname": 'helpmatch_makers'
# }

# class Member:
#     def __init__(self, name, email, phone, city):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.city = city

#     def email_in_table(self, table):
#         try:
#             connection = psycopg2.connect(**db_params)
#             cursor = connection.cursor()
#             query = f"""SELECT COUNT(email) FROM {table} WHERE email = '{self.email}';"""
#             cursor.execute(query)
#             result = cursor.fetchall()  # Is a tuple with 1 element (the count), inside a list with 1 element (the tuple)
#         except (Exception, psycopg2.Error) as error:
#             print(f"Error connecting to the database: {error}")
#         finally:
#             if connection:
#                 cursor.close()
#                 connection.close()
#                 return result[0][0]

#     def add_and_check(self, table):
#         if self.email_in_table(table) == 0:
#             self.add()
#             if self.email_in_table(table) == 1:
#                 print('You have been added successfully.')
#         elif self.email_in_table(table) == 1:
#             print('Your email address already exists in the table!')


# class Volunteer(Member):
#     def __init__(self, name, email, phone, city, gender, birth_year, info):
#         super().__init__(name, email, phone, city)
#         self.gender = gender
#         self.birth_year = birth_year
#         self.info = info

#     def add(self):
#         try:
#             connection = psycopg2.connect(**db_params)
#             cursor = connection.cursor()
#             query = f"""INSERT INTO volunteers (name, email, phone, city, gender, birth_year, info)
#             VALUES ('{self.name}', '{self.email}', '{self.phone}', '{self.city}', '{self.gender}', {self.birth_year}, '{self.info}');
#             """
#             cursor.execute(query)
#             connection.commit()
#         except (Exception, psycopg2.Error) as error:
#             print(f"Error connecting to the database: {error}")
#         finally:
#             if connection:
#                 cursor.close()
#                 connection.close()


# class VolunteerSeeker(Member):
#     def __init__(self, name, email, phone, city, background_info, tasks):
#         super().__init__(name, email, phone, city)
#         self.background_info = background_info
#         self.tasks = tasks

#     def add(self):
#         try:
#             connection = psycopg2.connect(**db_params)
#             cursor = connection.cursor()
#             query = f"""INSERT INTO looking_for_volunteers (name, email, phone, city, background_info, tasks)
#             VALUES ('{self.name}', '{self.email}', '{self.phone}', '{self.city}', '{self.background_info}', '{self.tasks}');
#             """
#             cursor.execute(query)
#             connection.commit()
#         except (Exception, psycopg2.Error) as error:
#             print(f"Error connecting to the database: {error}")
#         finally:
#             if connection:
#                 cursor.close()
#                 connection.close()

# if __name__ == '__main__':
#     volunteer_1 = Volunteer('Manon', 'manonnie@aol.nl', '06-12345678', 'The Hague', 'Female', 1981, "I love to do crafts with children.")
#     volunteer_1.add_and_check('volunteers')

#     volunteer_seeker_1 = VolunteerSeeker('Kieke', 'info@mocschilderswijk', '+31 707371356', 'The Hague', 'A meeting place for people with different cultural backgrounds.', 'Teaching Dutch to migrants.')
#     volunteer_seeker_1.add_and_check('looking_for_volunteers')