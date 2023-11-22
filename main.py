import telegram
from telegram.ext import MessageHandler, CommandHandler, Filters, Updater
from bot import start, message_handler, token

bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start, filters=Filters.chat_type.private))
dispatcher.add_handler(MessageHandler(~Filters.command & Filters.text, message_handler))

updater.start_polling()
