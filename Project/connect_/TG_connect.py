from typing import Final
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application
import asyncio
import psycopg2

TOKEN: Final = '7011755268:AAF7c9zDMwmAW1nN5ZDfkDktc9N8iweKFaM'
BOT_USERNAME: Final = '@HelpMatch_bot'


connection = psycopg2.connect(
    host = '127.0.0.1',
    port = '5432',
    user = 'postgres',
    password = '232323',
    dbname = 'help_mm'
)

cursor=connection.cursor()
connection.autocommit=True

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  reply_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
  reply_markup.add(['Volunteer', 'Volunteer Recruiter'])
  await update.message.reply_text('Welcome to Help_MatchMaker! Choose your role:', reply_markup=reply_markup)

async def main():
  async with Application.builder().token(TOKEN).build() as app:
    await app.initialize()  # Await initialization
    try:
      await app.run_polling()
    finally:
      await app.shutdown()  # Await shutdown


if __name__ == '__main__':
  asyncio.run(main())
