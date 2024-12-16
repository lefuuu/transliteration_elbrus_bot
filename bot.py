import logging
import os
from email.policy import default

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(filename="mylog.log", level=logging.INFO)


@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}.\n Отправь мне ФИО на кириллице для транслитерации.'
    logging.info(f'{user_id} : {user_name} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def transliteration (message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_id} : {user_name} отправил {text}')

    translit_table = {
        "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ё": "E",
        "Ж": "ZH", "З": "Z", "И": "I", "Й": "I", "К": "K", "Л": "L", "М": "M",
        "Н": "N", "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T", "У": "U",
        "Ф": "F", "Х": "KH", "Ц": "TS", "Ч": "CH", "Ш": "SH", "Щ": "SHCH", "Ъ": "IE",
        "Ы": "Y", "Ь": "IE", "Э": "E", "Ю": "IU", "Я": "IA",
    }
    text1 = text.upper()
    result_text = ''
    for char in text1:
        result_text += ''.join(translit_table.get(char, char))
    await message.answer(text=f'Ваша ФИО на латинице : {result_text}')
    logging.info(f'{user_id} ввел {text} и получил {result_text}')

if __name__ == '__main__':
    dp.run_polling(bot)
