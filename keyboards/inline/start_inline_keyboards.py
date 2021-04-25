from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# inline конпки для категорий
restaurant_murk_up = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='mak', callback_data='mak')
    ],
    [
        InlineKeyboardButton(text='BurgerKing', callback_data='bk')
    ],
    [
        InlineKeyboardButton(text='DodoPizza', callback_data='dodo')
    ]
])
