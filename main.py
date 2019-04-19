import telegram
from telegram.ext import Updater, CommandHandler, ConversationHandler, RegexHandler
import logging
import random

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

ACTION = range(2)


def start(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    keyboard = [['Register']]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=False, resize_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id, text="Hi! I am the Automated Attendance Monitoring bot.\n"
                                                          "For future work with the system I need some your information.\n"
                                                          "Press the button 'Register', when you will be ready.",
                     reply_markup=reply_markup)
    return ACTION


def action(bot, update):
    if (update.message.text == 'Register'):
        # TODO здесь
        num = random.randint(0, 1000);
        # reply_markup = telegram.ReplyKeyboardMarkup(["Number"], one_time_keyboard=False)
        bot.send_message(chat_id=update.message.chat_id, text=num)
        return ACTION


def cancel(bot, update):
    return ConversationHandler.END


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


if __name__ == '__main__':
    bot = Updater(token='888461394:AAGRoUa61Q-ZjtKlmJeju5HPsjmRZaUUKww')

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            ACTION: [RegexHandler('^(Register)$', action)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    bot.dispatcher.add_handler(conv_handler)

    bot.dispatcher.add_error_handler(error)

    bot.start_polling()
    bot.idle()
