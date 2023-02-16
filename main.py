import telebot
from config import *
from extensions import ConvercionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['menu'])
def main_menuu(message):
    bot.send_message(message.chat.id, main_menu)

@bot.message_handler(commands=['start'])
def startt(message):
    bot.send_message(message.chat.id, help + '\n /menu')

@bot.message_handler(commands=['help'])
def helpp(message):
    bot.send_message(message.chat.id, help + '\n /menu')

@bot.message_handler(commands=['values'])
def valuess(message):
    bot.send_message(message.chat.id, 'Список доступных для конвертации валют:')
    for i in values:
        bot.send_message(message.chat.id, i)
    bot.send_message(message.chat.id, '/menu')

@bot.message_handler(content_types=['text'])
def convert_result(message: telebot.types.Message):
    try:
        val = message.text.split(' ')

        if len(val) != 3:
            raise ConvercionException('Cлишком много или слишком мало параметров \n /help')

        base, quote, amount = val
        result = CryptoConverter.convert(base, quote, amount)
    except ConvercionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n {e}')
    else:
        text = f'{amount} {values[base]} ({base}) в {values[quote]} ({quote}) составит: {result}'
        bot.send_message(message.chat.id, text + '\n /menu')


bot.polling(none_stop=True)