from aiogram.dispatcher.filters.state import State, StatesGroup

class User_State(StatesGroup):
    question = State()

class Admin_State(StatesGroup):
    edit_btn = State()
    get_password = State()
    edit_inf = State()