import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# 🔑 ВСТАВЬТЕ СЮДА СВОЙ ТОКЕН
TOKEN = "8353313016:AAGGAQ6w4rRXRmo5JzsaEFN0SsDmlsfuoEw"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главное меню
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💰 Цены")],
        [KeyboardButton(text="🕒 Время тренировок")],
        [KeyboardButton(text="📋 Требования к аттестации")],
        [KeyboardButton(text="📖 Кодекс вида спорта")],
        [KeyboardButton(text="🔗 Полезные ссылки")],
    ],
    resize_keyboard=True
)

# Команда /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать!\nВыберите интересующий вас раздел:",
        reply_markup=main_keyboard
    )

# Обработчики кнопок

@dp.message(lambda message: message.text == "💰 Цены")
async def prices_handler(message: types.Message):
    await message.answer(
        "💰 *Цены на тренировки:*\n\n"
        "• Разовая тренировка — 600 руб.\n"
        "• Абонемент (12 занятий) — 4000 руб.\n"
        "• Индивидуальная тренировка — 1500 руб.",
        parse_mode="Markdown"
    )

@dp.message(lambda message: message.text == "🕒 Время тренировок")
async def schedule_handler(message: types.Message):
    await message.answer(
        "🕒 *Расписание тренировок:*\n\n"
        "Понедельник, среда, пятница\n"
        "младшая — 18:00\n"
        "средняя — 19:00\n"
        "старшая — 20:30\n"
        "Все тренировки - полтора часа\n",
        parse_mode="Markdown"
    )

@dp.message(lambda message: message.text == "📋 Требования к аттестации")
async def certification_handler(message: types.Message):
    await message.answer(
        "📋 *Требования к аттестации:*\n\n"
        "• Регулярное посещение тренировок\n"
        "• Знание базовой техники\n"
        "• Сдача нормативов\n"
        "• Участие в соревнованиях (по желанию)\n"
        "• Доблестное следование пути война\n"
        "• Уважение традиций и философии спорта\n",
        parse_mode="Markdown"
    )

@dp.message(lambda message: message.text == "📖 Кодекс вида спорта")
async def rules_handler(message: types.Message):
    await message.answer(
        "📖 *Кодекс карате киокушинкай:*\n\n"
        "1. Мы будем тренировать наши сердца и тела для достижения твердого, непоколебимого духа.\n"
        "2. Мы будем следовать истинному смыслу пути боевого искусства, чтобы наши чувства все время были наготове.\n"
        "3. С истинным упорством мы будем стремиться к преодолению своего эгоизма.\n"
        "4. Мы будем соблюдать правила этикета, уважения к старшим и воздерживаться от насилия.\n"
        "5. Мы будем следовать высшим идеалам и никогда не забудем истинную добродетель скромности.\n"
        "6. Мы будем стремиться к мудрости и силе, не ведая других желаний.\n"
        "7. Всю нашу жизнь, через изучение каратэ, мы будем стремиться выполнить истинное предназначение пути киокушинкай!\n",
        parse_mode="Markdown"
    )

@dp.message(lambda message: message.text == "🔗 Полезные ссылки")
async def links_handler(message: types.Message):
    await message.answer(
        "🔗 *Полезные ресурсы:*\n\n"
        "Устав федерации: http://www.kyokushinkarate.ru/ustav/\n"
        "Терминология спорта: https://sibkarate.ru/blog/terminologiya-kiokushinkay-karate/?ysclid=mlji02mgoz958624272\n"
        "Ссылка на заказ формы: https://docs.google.com/spreadsheets/d/1WlPu_2S7yJTk8VFkEkD-QzVQpVAzdWcHfRVL3bf-7os/edit?usp=sharing\n",
        disable_web_page_preview=True
    )

# Запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())