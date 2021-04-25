from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Set Location', request_location=True)
        ]
    ],
    resize_keyboard=True
)
