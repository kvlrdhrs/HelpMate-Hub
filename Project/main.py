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

    @staticmethod
    def search(table_name, city=None, keyword=None):
        conditions = []
        params = []
        
        if city is not None:
            conditions.append("city = %s")
            params.append(city)
        if keyword is not None:
            conditions.append("info ILIKE %s")
            params.append('%' + keyword + '%')
        
        query = "SELECT * FROM {} WHERE ".format(table_name) + " AND ".join(conditions)
        cursor.execute(query, tuple(params))
        result = cursor.fetchall()
        return result

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
    print('Please enter <2> to find for volunteers in Help_MatchMaker')
    print('Please enter <3> to go one level up in the menu')
    recruiter_choice = input('>>>: ')
    return recruiter_choice

def search_menu():
    while True:
        user_choice = input('''Would you like to search by:\n
        City    : enter <1>
        Keyword : enter <2>
        Both    : enter <3>
        Or go up: enter <4>
        >>>: ''')
        if user_choice in ['1', '2', '3', '4']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

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
    info = input('Please enter the tasks your seeking a volunteer for: ')
    new_volunteer = Menu(name, email, phone, city, age, info)
    new_volunteer.insert("lf_volunteers")
    print('You are added to a lf_volunteers list')


def main():
    while True:
        user_choice = show_welcome_menu()
        if user_choice in ['1', '2']:
            if user_choice == '1':
                choice = volunteer_menu()
            else:
                choice = LFV_menu()

            if choice == '1':
                add_new_volunteer() if user_choice == '1' else add_new_LF_volunteers()
            elif choice == '2':
                search_choice = search_menu()
                if search_choice == '1':
                    city = input("Enter city: ")
                    results = Menu.search("volunteers", city=city)  # Change here
                    print("Search results:")
                    for result in results:
                        print(result)
                elif search_choice == '2':
                    keyword = input("Enter keyword: ")
                    results = Menu.search("volunteers", keyword=keyword)  # Change here
                    print("Search results:")
                    for result in results:
                        print(result)
                elif search_choice == '3':
                    city = input("Enter city: ")
                    keyword = input("Enter keyword: ")
                    results = Menu.search("volunteers", city=city, keyword=keyword)  # Change here
                    print("Search results:")
                    for result in results:
                        print(result)
                elif search_choice == '4':
                    continue
            elif choice == '3':
                continue
            else:
                break
        elif user_choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()