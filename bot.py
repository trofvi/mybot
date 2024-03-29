import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def greet_user(update, context):
    logger.info('Вызван /start')
    update.message.reply_text('Привет, пользователь, у тебя наконец-то получилось! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text 
    logger.info(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()