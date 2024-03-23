import psycopg2
import telebot

connection = psycopg2.connect(
    host='127.0.0.1',
    port='5432',
    user='postgres',
    password='232323',
    dbname='help_mm'
)

cursor = connection.cursor()
connection.autocommit = True

bot = telebot.TeleBot("7011755268:AAF7c9zDMwmAW1nN5ZDfkDktc9N8iweKFaM")

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

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('1. Help as a volunteer')
    itembtn2 = telebot.types.KeyboardButton('2. Look for a volunteer')
    itembtn3 = telebot.types.KeyboardButton('3. Exit')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Welcome to Help_MatchMaker!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '1. Help as a volunteer')
def volunteer_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('1. Add as a volunteer')
    itembtn2 = telebot.types.KeyboardButton('2. Search for opportunities')
    itembtn3 = telebot.types.KeyboardButton('3. Go back')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "What would you like to do?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '2. Look for a volunteer')
def recruiter_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('1. Add as a recruiter')
    itembtn2 = telebot.types.KeyboardButton('2. Find volunteers')
    itembtn3 = telebot.types.KeyboardButton('3. Go back')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "What would you like to do?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '3. Exit')
def exit_program(message):
    bot.send_message(message.chat.id, "Goodbye!")
    bot.stop_polling()

@bot.message_handler(func=lambda message: message.text == '3. Go back')
def go_back(message):
    start(message)

@bot.message_handler(func=lambda message: message.text == '1. Add as a volunteer')
def add_new_volunteer(message):
    bot.send_message(message.chat.id, 'Great that you want to be a volunteer!')
    bot.send_message(message.chat.id, 'Please enter your name:')
    bot.register_next_step_handler(message, ask_email)

def ask_email(message):
    bot.send_message(message.chat.id, 'Please enter your email address:')
    bot.register_next_step_handler(message, ask_phone)

def ask_phone(message):
    bot.send_message(message.chat.id, 'Please enter your phone number:')
    bot.register_next_step_handler(message, ask_city)

def ask_city(message):
    bot.send_message(message.chat.id, 'Please enter the city you live in:')
    bot.register_next_step_handler(message, ask_age)

def ask_age(message):
    bot.send_message(message.chat.id, 'Please enter your age:')
    bot.register_next_step_handler(message, ask_info)

def ask_info(message):
    bot.send_message(message.chat.id, 'Please specify the work you would like to do:')
    bot.register_next_step_handler(message, save_volunteer_info)

def save_volunteer_info(message):
  new_volunteer = Menu(
      message.text,  # Name
      message.text,  # Email
      message.text,  # Phone
      message.text,  # City
      message.text,  # Age
      message.text   # Info
  )
  new_volunteer.insert("volunteers")
  bot.send_message(message.chat.id, 'You are added to the volunteer list')


bot.polling()
