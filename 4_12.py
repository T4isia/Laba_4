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
        BotCommand(command="start",
                   description="Запустить бота"
        ),
        BotCommand(command="help",
                   description="Показать все команды"
        ),
        BotCommand(command="earth_photo",
                   description="🌍 Фото Земли со спутника"
        ),
        BotCommand(command="apod",
                   description="🛰 Фото дня от NASA (APOD)"
        ),
        BotCommand(command="planets",
                   description="🪐 Справка о планетах"
        ),
        BotCommand(command="news",
                   description="📰 Новости космоса"
        ),
    ]
    await bot.set_my_commands(commands)


# Функция меню
def get_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='1 или /earth_photo - 🌍 Фото Земли со спутника',
                callback_data='photo of the earth'
            )
        ],
        [
            InlineKeyboardButton(
                text='2 или /apod - 🛰 Фото дня от NASA (APOD)',
                callback_data='photo of the day'
            )
        ],
        [
            InlineKeyboardButton(
                text='3 или /planets - 🪐 Справка о планетах',
                callback_data='planetary reference'
            )
        ],
        [
            InlineKeyboardButton(
                text='4 или /news - 📰 Новости космоса',
                callback_data='news'
            )
        ],
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
    await message.answer_photo(
        photo="https://resizer.mail.ru/p/"
              "a5db777f-57b6-56e2-a846-d28cb6add0f6/"
              "AQAKteqhd-KlJvH2QU-3mpvdd3E7LxmwXM0D8EpkGCZneW5xzAc7o3VbjvJgZQ_EcTfXrE0-3nFfEEon70v5Bwaf5DM.jpg",
        caption="🌍 Это Земля из Космоса",
        reply_markup=get_menu()
    )

# Команда /apod
@dp.message(Command("apod"))
async def apod_cmd(message: types.Message):
    await message.answer_photo(
        photo="https://apod.nasa.gov/apod/image/"
              "2508/Crab_HubbleChandraSpitzer_3600.jpg",
        caption="🛰 Это фото дня от NASA",
        reply_markup = get_menu()
        )

# Команда /planets
@dp.message(Command("planets"))
async def planets_cmd(message: types.Message):
    await message.answer(
        "🪐 Это справка о планетах\n"
        "https://astrovert.ru/journal/solar_system/"
        "planety-solnechnoy-sistemy-opisanie-klassifikatsiya-i-pravila-nablyudeniya/",
        reply_markup = get_menu()
    )

# Команда /news
@dp.message(Command("news"))
async def news_cmd(message: types.Message):
    await message.answer(
        "📰 Это новости космоса\n"
        "https:// lenta.ru/rubrics/science/cosmos/",
        reply_markup = get_menu()
    )


# Обработка inline-кнопок
@dp.callback_query()
async def callback_message(callback: types.CallbackQuery):

    if callback.data == 'photo of the earth':
        await callback.message.answer_photo(
            photo="https://resizer.mail.ru/p/"
                  "a5db777f-57b6-56e2-a846-d28cb6add0f6/"
                  "AQAKteqhd-KlJvH2QU-3mpvdd3E7LxmwXM0D8EpkGCZneW5xzAc7o3VbjvJgZQ_EcTfXrE0-3nFfEEon70v5Bwaf5DM.jpg",
            caption="🌍 Это Земля из Космоса",
            reply_markup = get_menu()
        )

    elif callback.data == 'photo of the day':
        await callback.message.answer_photo(
            photo="https://apod.nasa.gov/"
                  "apod/image/2508/"
                  "Crab_HubbleChandraSpitzer_3600.jpg",
             caption="🛰 Это фото дня от NASA",
            reply_markup=get_menu()
        )

    elif callback.data == 'planetary reference':
        await callback.message.answer(
            "🪐 Это справка о планетах\n"
            "https://astrovert.ru/journal/solar_system/"
            "planety-solnechnoy-sistemy-opisanie-klassifikatsiya-i-pravila-nablyudeniya/",
            reply_markup = get_menu()
        )

    elif callback.data == 'news':
        await callback.message.answer(
            "📰 Это новости космоса\n"
            "https://lenta.ru/rubrics/science/cosmos/",
            reply_markup = get_menu()
        )

    await callback.answer()


# Пользовательский ввод и обработка исключений
@dp.message()
async def text_commands(message: types.Message):
    text = message.text.strip()

    if text == "1":
        await message.answer_photo(
            photo="https://resizer.mail.ru/p/"
                  "a5db777f-57b6-56e2-a846-d28cb6add0f6/"
                  "AQAKteqhd-KlJvH2QU-3mpvdd3E7LxmwXM0D8EpkGCZneW5xzAc7o3VbjvJgZQ_EcTfXrE0-3nFfEEon70v5Bwaf5DM.jpg",
            caption="🌍 Это Земля из Космоса",
            reply_markup=get_menu()
        )

    elif text == "2":
        await message.answer_photo(
            photo="https://apod.nasa.gov/"
                  "apod/image/2508/"
                  "Crab_HubbleChandraSpitzer_3600.jpg",
            caption="🛰 Это фото дня от NASA",
            reply_markup=get_menu()
        )

    elif text == "3":
        await message.answer(
            "🪐 Это справка о планетах\n"
            "https://astrovert.ru/journal/solar_system/"
            "planety-solnechnoy-sistemy-opisanie-klassifikatsiya-i-pravila-nablyudeniya/",
            reply_markup=get_menu()
        )

    elif text == "4":
        await message.answer(
            "📰 Это новости космоса\n"
            "https://lenta.ru/rubrics/science/cosmos/",
            reply_markup=get_menu()
        )

    else:
        await message.answer(
        'Команда не найдена',
        reply_markup=get_menu()
    )


# Запуск бота
async def main():
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
