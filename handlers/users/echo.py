from aiogram import types

from loader import dp


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def echo(message: types.Message):
    """ Handler of all messages """

    await message.answer(text=f'Ты чтото ввел неправильно\nлови свое сообщение:\n{message.text}')
