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


def main_menu():
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

def add_new_volunteer():
    print('Great that you want to be a volunteer!')
    name = input('Please enter your full name: ')
    email = input('Please enter your email address: ')
    phone = input('Please enter your phone number: ')
    city = input('Please enter the city you live in: ')
    gender = input('Please enter the gender you identify as (Male, Female or Other): ')
    birth_year = input('Please enter your year of birth: ')
    info = input('Please specify the work you would like to do: ')
    new_volunteer = members.Volunteer(name, email, phone, city, gender, birth_year, info)
    new_volunteer.add()
    # check if addition was successful

def add_new_volunteer_seeker():
    print('Great that you want to offer a volunteering opportunity!')
    name = input('Please enter your name: ')
    email = input('Please enter your email address: ')
    phone = input('Please enter your phone number: ')
    city = input('Please enter your city: ')
    background_info = input('Please enter background info about you that might be relevant for the volunteer: ')
    tasks = input('Please enter the tasks your seeking a volunteer for: ')
    new_volunteer_seeker = members.VolunteerSeeker(name, email, phone, city, background_info, tasks)
    new_volunteer_seeker.add()

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
                    add_new_volunteer_seeker()
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
