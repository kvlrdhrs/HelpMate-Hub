from typing import Final
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application
import psycopg2

TOKEN: Final = '7011755268:AAF7c9zDMwmAW1nN5ZDfkDktc9N8iweKFaM'
BOT_USERNAME: Final = '@HelpMatch_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for creating me, Kanan!')



if __name__== '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.run_polling(poll_interval=1)

