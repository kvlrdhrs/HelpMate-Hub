import psycopg2

connection = psycopg2.connect(
    host = '127.0.0.1',
    port = '5432',
    user = 'postgres',
    password = '232323',
    dbname = 'help_mm'
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
        (self.name, self.email, self.phone, self.city, self.age, self.info))


    def delete(self, table_name, key):
        cursor.execute(f"""
        DELETE FROM {table_name} WHERE email = %s""", (key,))

    def update(self, table_name, key, column, new_value):
        cursor.execute(f"""
        UPDATE {table_name} SET {column} = %s WHERE email = %s""", (new_value, key))


def main_menu():
    print('****************************')
    print('Welcome to HelpMatch_Makers!')
    print('****************************\n')
    print('Please enter <1> to work as a volunteer')
    print('Please enter <2> to look for a volunteer')
    print('Please enter <3> to exit the program')
    user_choice = input('>>>: ')
    return user_choice


def volunteer_menu():
    print('\nPlease enter <A> to be added as a volunteer to our database')
    print('Please enter <S> to search for opportunities in our database')
    print('Please enter <U> to go one level up in the menu')
    volunteer_choice = input('>>>: ')
    return volunteer_choice


def LFV_menu():
    print('\nPlease enter <A> to be added as a volunteer recruiter to our database')
    print('Please enter <S> to search for volunteers in our database')
    print('Please enter <U> to go one level up in the menu')
    recruiter_choice = input('>>>: ')
    return recruiter_choice


def add_new_volunteer():
    print('Great that you want to be a volunteer!')
    name = input('Please enter your full name: ')
    email = input('Please enter your email address: ')
    phone = input('Please enter your phone number: ')
    city = input('Please enter the city you live in: ')
    age = input('Please enter your age: ')
    info = input('Please specify the work you would like to do: ')
    
    # Create Menu instance
    new_volunteer = Menu(name, email, phone, city, age, info)
    new_volunteer.insert('volunteers')


def delete_volunteer(email):
    Menu.delete('volunteers', email)


def update_volunteer(email, column, new_value):
    Menu.update('volunteers', email, column, new_value)


def help_match_makers():
    is_in_program = True
    while is_in_program:
        entrance_choice = main_menu().upper()
        if entrance_choice == 'V':
            volunteer_choice = ''
            while volunteer_choice != 'U':
                volunteer_choice = volunteer_menu().upper()
                if volunteer_choice == 'A':
                    add_new_volunteer()
                elif volunteer_choice == 'S':
                    pass
                elif volunteer_choice != 'U':
                    print('\nYour input is invalid, please try again.')
        elif entrance_choice == 'L':
            recruiter_choice = ''
            while recruiter_choice != 'U':
                recruiter_choice = volunteer_recruiter_menu().upper()
                if recruiter_choice == 'A':
                    pass  # Add function to add new volunteer seekers
                elif recruiter_choice == 'S':
                    pass
                elif recruiter_choice != 'U':
                    print('\nYour input is invalid, please try again.')
        elif entrance_choice == 'X':
            print('\nThank you for your interest! We hope to see you again in the future.')
            is_in_program = False
        else:
            print('\nYour input is invalid, please try again.\n')


if __name__ == '__main__':
    help_match_makers()
    if connection:
        cursor.close()
        connection.close()
