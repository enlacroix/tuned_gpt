import configparser
import threading
from answering import mainTask

config = configparser.ConfigParser()
config.read('config.ini')
token = config['passwords']['tgToken']

def start(update, context):
    user = update.effective_user
    context.bot.send_message(chat_id=user.id, text='Привет')


def message_handler(update, context):
    thread = threading.Thread(target=mainTask, args=(update, context))
    thread.start()