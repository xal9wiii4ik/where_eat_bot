from aiogram.dispatcher.filters.state import StatesGroup, State


class LocationState(StatesGroup):
    """ State of location """

    Location = State()
