from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.default_keyboard import start_markup
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    """ Handel of command start """

    await message.answer(text='Я могу подсказать где находится ближайшее ваше заведение\n'
                              'Для этого укажите геолокацию', reply_markup=start_markup)
