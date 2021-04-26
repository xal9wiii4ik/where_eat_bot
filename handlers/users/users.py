from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.users.services import get_location, get_address
from keyboards.inline.start_inline_keyboards import restaurant_murk_up
from loader import dp
from states.location import LocationState

URL = {
    'bk': 'https://burger-king.by/',
    'mak': 'https://mcdonalds.by/',
    'dodo': 'https://dodopizza.by/',
}


@dp.message_handler(state="*", content_types=types.ContentTypes.LOCATION)
async def location_button(message: types.Message, state: FSMContext):
    """ Handler of default button get location """

    await state.reset_state()
    latitude = message.location.latitude
    longitude = message.location.longitude
    await LocationState.Location.set()
    await state.update_data(
        longitude=longitude,
        latitude=latitude
    )
    address = await get_address(longitude=longitude, latitude=latitude)
    await message.answer(text=f'Ты в городе {address[1]}', reply_markup=restaurant_murk_up)


@dp.callback_query_handler(text='mak', state=LocationState.Location)
async def mak_callback(call: CallbackQuery, state: FSMContext):
    """ Handel of callback mak """

    data = await state.get_data()
    location = await get_location(longitude=data['longitude'], latitude=data['latitude'], name='Макдональдс')
    if location:
        await dp.bot.send_message(chat_id=call.from_user.id, text=URL['mak'])
        await dp.bot.send_location(chat_id=call.from_user.id, longitude=location[0], latitude=location[1])
    else:
        await dp.bot.send_message(chat_id=call.from_user.id, text='В вашем регионе нет макдональдсов(')


@dp.callback_query_handler(text='bk', state=LocationState.Location)
async def bk_callback(call: CallbackQuery, state: FSMContext):
    """ Handel of callback bk """

    data = await state.get_data()
    location = await get_location(longitude=data['longitude'], latitude=data['latitude'], name='Бургер Кинг')
    if location:
        await dp.bot.send_message(chat_id=call.from_user.id, text=URL['bk'])
        await dp.bot.send_location(chat_id=call.from_user.id, longitude=location[0], latitude=location[1])
    else:
        await dp.bot.send_message(chat_id=call.from_user.id, text='В вашем регионе нет Бургер Кинга(')


@dp.callback_query_handler(text='dodo', state=LocationState.Location)
async def dodo_callback(call: CallbackQuery, state: FSMContext):
    """ Handel of callback dodo """

    data = await state.get_data()
    location = await get_location(longitude=data['longitude'], latitude=data['latitude'], name='Додо Пицца')
    if location:
        await dp.bot.send_message(chat_id=call.from_user.id, text=URL['dodo'])
        await dp.bot.send_location(chat_id=call.from_user.id, longitude=location[0], latitude=location[1])
    else:
        await dp.bot.send_message(chat_id=call.from_user.id, text='В вашем регионе нет Додо Пиццы(')
