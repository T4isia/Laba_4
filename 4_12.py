import telebot # Библиотека для работы с Telegram API
from telebot import types # Импорт библиотеки, которая содержит классы для создания элементов интерфейса


# Уникальный токен бота
token = '8281293402:AAENBSRFr_R_rasXd0ifq2sHpnYFLNFMiHs'

bot = telebot.TeleBot(token)


# Декоратор, который привязывает следующую функцию к обработке команды /start
@bot.message_handler(commands=['start'])
def start(message):

    # Создаем inline-клавиатуру
    markup = types.InlineKeyboardMarkup()

    # Создаем кнопки и добавляем
    but1 = types.InlineKeyboardButton(
        '🌍 Фото Земли со спутников',
        callback_data='photo of the Earth'
    )
    markup.add(but1)
    but2 = types.InlineKeyboardButton(
        '🛰 Фото дня от NASA (APOD)',
        callback_data='photo of the day'
    )
    markup.add(but2)
    but3 = types.InlineKeyboardButton(
        '🪐 Справка о планетах',
        callback_data='planetary reference'
    )
    markup.add(but3)
    but4 = types.InlineKeyboardButton(
        '📰 Новости космоса',
        callback_data='news'
    )
    markup.add(but4)
    but5 = types.InlineKeyboardButton(
        '📍 Фото по координатам',
        callback_data='photo by coordinates'
    )
    markup.add(but5)

    # Отправляем сообщение с клавиатурой
    bot.send_message(
        message.chat.id,
        f'Здравствуйте, {message.from_user.first_name}.'
        f' Чтобы Вы хотели узнать?',
        reply_markup=markup
    )


# Декоратор без параметров - будет обрабатывать любые сообщения
@bot.message_handler()
def non_mes(message):
    bot.send_message(message.chat.id, 'Команда не найдена')


# Декоратор для обработки нажатий на кнопки, которые под сообщением бота
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data in (
            'photo of the Earth',
            'photo of the day',
            'planetary reference',
            'news', 'photo by coordinates'
    ):
        # Создаем новую клавиатуру с одной кнопкой
        markup = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton(
            'Ок', callback_data='test'
        )
        markup.add(but1)

        # Редактируем существующее сообщение
        bot.edit_message_text(
            'Функция работает',
            callback.message.chat.id,
            callback.message.message_id,
            reply_markup=markup
        )


# Запуск бота
if __name__ == '__main__':
    bot.polling(non_stop=True)
