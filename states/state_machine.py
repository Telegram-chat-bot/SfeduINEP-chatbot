from aiogram.dispatcher.filters.state import State, StatesGroup


class PositionState(StatesGroup):
    set_pressed_btn = State()
    get_pressed_btn = State()


class User_State(StatesGroup):
    direction = State()

    get_info_for_question = State()
    user_question_dir = State()

    question = State()


class AdminState(StatesGroup):
    get_id = State()
    get_answer = State()
