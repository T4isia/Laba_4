# Подключение библиотек
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.types import BotCommand


# Уникальный токен бота
TOKEN = '8281293402:AAENBSRFr_R_rasXd0ifq2sHpnYFLNFMiHs'


# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()


# Команды в Telegram
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Показать все команды"),
    ]
    await bot.set_my_commands(commands)


# Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):

    # Создаем inline-клавиатуру
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='🌍 Фото Земли со спутников',
                callback_data='photo of the Earth'
            )
        ],
        [
            InlineKeyboardButton(
                text='🛰 Фото дня от NASA (APOD)',
                callback_data='photo of the day'
            )
        ],
        [
            InlineKeyboardButton(
                text='🪐 Справка о планетах',
                callback_data='planetary reference'
            )
        ],
        [
            InlineKeyboardButton(
                text='📰 Новости космоса',
                callback_data='news'
            )
        ],
        [
            InlineKeyboardButton(
                text='📍 Фото по координатам',
                callback_data='photo by coordinates'
            )
        ]
    ])

    await message.answer(
        f'Здравствуйте, {message.from_user.first_name}. 🚀 '
        f'Я — бот о космосе! '
        f'Чтобы Вы хотели узнать?',
        reply_markup=markup
    )


# Любые другие сообщения
@dp.message()
async def non_mes(message: types.Message):
    await message.answer('Команда не найдена')


# Обработка inline-кнопок
@dp.callback_query()
async def callback_message(callback: types.CallbackQuery):

    if callback.data in (
        'photo of the Earth',
        'photo of the day',
        'planetary reference',
        'news',
        'photo by coordinates'
    ):
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Ок',
                    callback_data='test'
                )
            ]
        ])

        await callback.message.edit_text(
            'Функция работает',
            reply_markup=markup
        )

        await callback.answer()


# Запуск бота
async def main():
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
