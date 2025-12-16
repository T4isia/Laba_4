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
        BotCommand(command="earth_photo", description="🌍 Фото Земли со спутников"),
        BotCommand(command="apod", description="🛰 Фото дня от NASA (APOD)"),
        BotCommand(command="planets", description="🪐 Справка о планетах"),
        BotCommand(command="news", description="📰 Новости космоса"),
        BotCommand(command="coords", description="📍 Фото по координатам"),
    ]
    await bot.set_my_commands(commands)


# Функция меню
def get_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='/earth_photo - 🌍 Фото Земли со спутников',
                callback_data='photo of the earth'
            )
        ],
        [
            InlineKeyboardButton(
                text='/apod - 🛰 Фото дня от NASA (APOD)',
                callback_data='photo of the day'
            )
        ],
        [
            InlineKeyboardButton(
                text='/planets - 🪐 Справка о планетах',
                callback_data='planetary reference'
            )
        ],
        [
            InlineKeyboardButton(
                text='/news - 📰 Новости космоса',
                callback_data='news'
            )
        ],
        [
            InlineKeyboardButton(
                text='/coords - 📍 Фото по координатам',
                callback_data='photo by coordinates'
            )
        ]
    ])

# Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        f'Здравствуйте, {message.from_user.first_name}. 🚀 '
        f'Я — бот о космосе! '
        f'Чтобы Вы хотели узнать?',
        reply_markup=get_menu()
    )

# Команда /help
@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer("Команды:",
                         reply_markup = get_menu()
                         )

# Команда /earth_photo
@dp.message(Command("earth_photo"))
async def earth_photo_cmd(message: types.Message):
    await message.answer("🌍 Здесь будет фото Земли со спутников",
                         reply_markup = get_menu()
                         )

# Команда /apod
@dp.message(Command("apod"))
async def apod_cmd(message: types.Message):
    await message.answer("🛰 Здесь будет фото дня от NASA",
                         reply_markup = get_menu()
                         )

# Команда /planets
@dp.message(Command("planets"))
async def planets_cmd(message: types.Message):
    await message.answer("🪐 Здесь будет справка о планетах",
                         reply_markup = get_menu()
                         )

# Команда /news
@dp.message(Command("news"))
async def news_cmd(message: types.Message):
    await message.answer("📰 Здесь будут новости космоса",
                         reply_markup = get_menu()
                         )

# Команда /coords
@dp.message(Command("coords"))
async def coords_cmd(message: types.Message):
    await message.answer("📍 Здесь будет фото по координатам",
                         reply_markup = get_menu()
                         )


# Обработка inline-кнопок
@dp.callback_query()
async def callback_message(callback: types.CallbackQuery):

    if callback.data == 'photo of the earth':
        await callback.message.answer(
            "🌍 Здесь будет фото Земли со спутников",
            reply_markup = get_menu()
            )

    elif callback.data == 'photo of the day':
        await callback.message.answer(
            "🛰 Здесь будет фото дня от NASA",
            reply_markup=get_menu()
        )

    elif callback.data == 'planetary reference':
        await callback.message.answer(
            "🪐 Здесь будет справка о планетах",
            reply_markup = get_menu()
            )

    elif callback.data == 'news':
        await callback.message.answer(
            "📰 Здесь будут новости космоса",
            reply_markup = get_menu()
            )

    elif callback.data == 'photo by coordinates':
        await callback.message.answer(
            "📍 Здесь будет фото по координатам",
            reply_markup = get_menu()
            )

    await callback.answer()


# Любые другие сообщения
@dp.message()
async def non_mes(message: types.Message):
    await message.answer('Команда не найдена')


# Запуск бота
async def main():
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
