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
    print('\nPlease enter <1> to be added as a volunteer recruiter to Help_MatchMaker')
    print('Please enter <2> to find for volunteers in Help_MatchMaker')
    print('Please enter <3> to go one level up in the menu')
    recruiter_choice = input('>>>: ')
    return recruiter_choice

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
    print('Great that you want to be a volunteer!')
    name = input('Please enter your name: ')
    email = input('Please enter your email address: ')
    phone = input('Please enter your phone number: ')
    city = input('Please enter the city you live in: ')
    age = input('Please enter your age: ')
    info = input('Please specify the work you would like to do: ')
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
                pass
            elif volunteer_choice == '3':
                user_choise = show_welcome_menu()
            else:
                    break


        elif user_choise == '2':
            recruiter_choice = LFV_menu()
            if recruiter_choice == '1':
                pass
            elif recruiter_choice == '2':
                pass
            elif recruiter_choice == '3':
                user_choise = show_welcome_menu()
            else:
                pass


        elif user_choise == '3':
                break
        else:
            print("Invalid choice. Please try again.")



        # continue_program = input("Do you want to continue? (Y/N): ")
        # if continue_program.upper() != 'Y':
        #     break


if __name__ == '__main__':
    main()