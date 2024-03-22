import members
import psycopg2

db_params = {
    "host": 'localhost',
    "user": 'postgres',
    "password": 'xo4MK99!ds',
    "port": '5432',
    "dbname": 'helpmatch_makers'
}

connection = psycopg2.connect(**db_params)
cursor = connection.cursor()


def entrance_menu():
    print('****************************')
    print('Welcome to HelpMatch_Makers!')
    print('****************************\n')
    print('Please enter <V> to work as a volunteer')
    print('Please enter <L> to look for a volunteer')
    print('Please enter <X> to exit the program')
    entrance_choice = input('>>>: ')
    return entrance_choice


def volunteer_menu():
    print('\nPlease enter <A> to be added as a volunteer to our database')
    print('Please enter <S> to search for opportunities in our database')
    print('Please enter <U> to go one level up in the menu')
    volunteer_choice = input('>>>: ')
    return volunteer_choice

def volunteer_recruiter_menu():
    print('\nPlease enter <A> to be added as a volunteer recruiter to our database')
    print('Please enter <S> to search for volunteers in our database')
    print('Please enter <U> to go one level up in the menu')
    recruiter_choice = input('>>>: ')
    return recruiter_choice

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

def add_volunteer():
    print('Great that you want to be a volunteer!')




def help_match_makers():
    is_in_program = True
    while is_in_program:
        entrance_choice = entrance_menu().upper()
        if entrance_choice == 'V':
            volunteer_choice = ''
            while volunteer_choice != 'U':
                volunteer_choice = volunteer_menu().upper()
                if volunteer_choice == 'A':
                    pass
                elif volunteer_choice == 'S':
                    pass
                elif volunteer_choice != 'U':
                    print('\nYour input is invalid, please try again.')
        elif entrance_choice == 'L':
            recruiter_choice = ''
            while recruiter_choice != 'U':
                recruiter_choice = volunteer_recruiter_menu().upper()
                if recruiter_choice == 'A':
                    pass
                elif recruiter_choice == 'S':
                    pass
                elif recruiter_choice != 'U':
                    print('\nYour input is invalid, please try again.')
        elif entrance_choice == 'X':
            print('\nThank you for you interest! We hope to see you again in the future.')
            is_in_program = False
        else:
            print('\nYour input is invalid, please try again.\n')

if __name__ == '__main__':
    help_match_makers()
    if connection:
        cursor.close()
        connection.close()
