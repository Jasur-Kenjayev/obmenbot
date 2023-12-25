from aiogram.dispatcher.filters.state import StatesGroup, State


class NewPost(StatesGroup):
    phone = State()
    Confirm = State()
