import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Hi there!')


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
