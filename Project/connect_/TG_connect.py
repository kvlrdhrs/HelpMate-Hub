from typing import Final
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application
import psycopg2
import asyncio

TOKEN: Final = '7011755268:AAF7c9zDMwmAW1nN5ZDfkDktc9N8iweKFaM'
BOT_USERNAME: Final = '@HelpMatch_bot'

class Menu():
    def __init__(self, name, email, phone, city, age, info):
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city
        self.age = age
        self.info = info

    async def insert(self, table_name):
        connection = psycopg2.connect(
            host = '127.0.0.1',
            port = '5432',
            user = 'postgres',
            password = '232323',
            dbname = 'helpmatch_maker'
        )
        cursor = connection.cursor()
        connection.autocommit = True

        try:
            cursor.execute(f"""
            INSERT INTO {table_name} (name, email, phone, city, age, info)
            VALUES (%s, %s, %s, %s, %s, %s)""",
            (self.name, self.email, self.phone, self.city, self.age, self.info)
            )
            connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            connection.close()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This is just an example. You need to collect the actual data from the user.
    menu = Menu('name', 'email', 'phone', 'city', 25, 'info')
    await menu.insert('volunteers')

    await update.message.reply_text('Data inserted successfully!')

if __name__== '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
