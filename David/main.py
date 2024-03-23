import psycopg2

connection = psycopg2.connect(
    host = '127.0.0.1',
    port = '5432',
    user = 'postgres',
    password = '232323',
    dbname = 'help_mm'
)

cursor = connection.cursor()
connection.autocommit = True

# creating funcionality to insert, delete and update data
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
        DELETE FROM {table_name} WHERE email = %s""",
        (self.email))

def search_by_city(table_name):
    city = input('Please enter the city you are interested in: ')
    cursor.execute(f"""SELECT * FROM {table_name} WHERE city = '{city}';""")
    result = cursor.fetchall()
    for hit in result:
        print(hit)


def search_by_keyword(table_name):
    keyword = input('Please enter a keyword you are interested in: ')
    cursor.execute(f"""SELECT * FROM {table_name} WHERE info ILIKE '%{keyword}%';""")
    result = cursor.fetchall()
    for hit in result:
        print(hit)


def search_by_city_and_keyword(table_name):
    city = input('Please enter the city you are interested in: ')
    keyword = input('Please enter a keyword you are interested in: ')
    cursor.execute(f"""SELECT * FROM {table_name} WHERE city = '{city}' AND info ILIKE '{keyword}';""")
    result = cursor.fetchall()
    for hit in result:
        print(hit)



#creating user_menu

def show_welcome_menu():
    print('\n****************************')
    print('Welcome to Help_MatchMaker!')
    print('****************************\n')
    print('Enter <1> to help as a volunteer')
    print('Enter <2> to look for a volunteer')
    print('Enter <3> to exit the program')
    user_choice = input('>>>: ')
    return user_choice
    
def volunteer_menu():
    print('\nEnter <1> to be added as a volunteer to Help_MatchMaker')
    print('Enter <2> to search for opportunities in Help_MatchMaker')
    print('Enter <3> to go one level up in the menu')
    volunteer_choice = input('>>>: ')
    return volunteer_choice

def LFV_menu():
    print('\nPlease enter <1> to be added as a volunteer recruiter')
    print('Please enter <2> to find volunteers in Help_MatchMaker')
    print('Please enter <3> to go one level up in the menu')
    recruiter_choice = input('>>>: ')
    return recruiter_choice

def search_menu():
    user_choice = input('''Would you like to search by:\n
    City    : enter <1>\n
    Keyword : enter <2>\n
    Both    : enter <3>\n
    Or go up: enter <4>\n
    >>>: ''')
    return user_choice

def add_new_volunteer():
    print('Great that you want to be a volunteer!')
    name = input('Please enter your name: ')
    email = input('Please enter your email address: ')
    phone = input('Please enter your phone number: ')
    city = input('Please enter the city you live in: ')
    age = input('Please enter your age: ')
    info = input('Please specify the work you would like to do: ')
    new_volunteer = Menu(name, email, phone, city, age, info)
    new_volunteer.insert("volunteers")
    print('You are added to a volunteer list')

def add_new_LF_volunteers():
    print('Great that you want to offer a volunteering opportunity!')
    name = input('Please enter your name: ')
    email = input('Please enter your email address: ')
    phone = input('Please enter your phone number: ')
    city = input('Please enter the city you live in: ')
    age = input('Please enter your age: ')
    info = input("Please enter the tasks you're seeking a volunteer for: ")
    new_volunteer = Menu(name, email, phone, city, age, info)
    new_volunteer.insert("lf_volunteers")
    print('You are added to a lf_volunteers list')


def main():
    while True:
        user_choise = show_welcome_menu()
        if user_choise == '1':
            volunteer_choice = volunteer_menu()
            if volunteer_choice == '1':
                add_new_volunteer()
            elif volunteer_choice == '2':
                search_mode = search_menu()
                while search_mode != '4':
                    if search_mode == '1':
                        search_by_city("lf_volunteers")
                    elif search_mode == '2':
                        search_by_keyword("lf_volunteers")
                    elif search_mode == '3':
                        search_by_city_and_keyword("lf_volunteers")
            elif volunteer_choice == '3':
                continue
            else:
                print("Invalid choice. Please try again.")

        elif user_choise == '2':
            recruiter_choice = LFV_menu()
            if recruiter_choice == '1':
                add_new_LF_volunteers()
            elif recruiter_choice == '2':
                search_mode = search_menu()
                while search_mode != '4':
                    if search_mode == '1':
                        search_by_city("volunteers")
                    elif search_mode == '2':
                        search_by_keyword("volunteers")
                    elif search_mode == '3':
                        search_by_city_and_keyword("volunteers")
            elif recruiter_choice == '3':
                continue
            else:
                print("Invalid choice. Please try again.")

        elif user_choise == '3':
                break
        else:
            print("Invalid choice. Please try again.")



        # continue_program = input("Do you want to continue? (Y/N): ")
        # if continue_program.upper() != 'Y':
        #     break


if __name__ == '__main__':
    # main()
    search_menu()