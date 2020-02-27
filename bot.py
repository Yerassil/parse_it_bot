import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

isRunning = 0


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    global isRunning
    if not isRunning:
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, 'How old are you?')
        bot.register_next_step_handler(msg, askAge)
        isRunning = True


def askAge(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Age must be a number. Please, try again.')
        bot.register_next_step_handler(msg, askAge)
        return
    msg = bot.send_message(chat_id, 'Thank you. Now I know that you are ' + text)


@bot.message_handler(content_types=["text"])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == 'hi':
        bot.send_message(chat_id, 'Hi there! I\'m a parser bot')
    elif text == 'how are you?':
        bot.send_message(chat_id, 'I\'m fine. How are you?')
    else:
        bot.send_message(chat_id, 'Sorry, didn\'t catch that')


bot.polling(none_stop=True)
